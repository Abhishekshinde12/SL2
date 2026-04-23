from fastapi import APIRouter, Depends, status, HTTPException, Request, Response
from src.models.user import User
from src.schemas.user import UserCreate, UserRead, UserUpdate, UserLogin
from src.dependencies import AuthDep, SessionDep
from sqlmodel import select 
from src.core.security import hash_password, verify_password, create_access_token, create_refresh_token, decode_token
from fastapi.security import OAuth2PasswordRequestForm
from src.core.config import settings 


router = APIRouter(prefix="/auth", tags=["Auth"])

COOKIE_SETTINGS = {
    'httponly': True, # JS cant access this
    'secure': False, # True = HTTPS, False = Http
    'samesite': 'lax' # Prevents CSRF
}

# register
@router.post("/signup", response_model=UserRead)
def registerUser(
    data: UserCreate,
    session: SessionDep
):
    existing = session.exec(select(User).where(User.email == data.email)).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already registered/')
    
    user = User(
        name=data.name, email=data.email, 
        hashed_password = hash_password(data.password), 
        role=data.role, institution_id=data.institution_id)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# login 
@router.post("/login")
def loginUser(
    response: Response,
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = session.exec(select(User).where(User.email == form_data.username)).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    access_token = create_access_token(str(user.id), user.role)
    refresh_token = create_refresh_token(str(user.id), user.role)

    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRY_TIME * 60,
        **COOKIE_SETTINGS
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRY_TIME*24*60*60,
        path="/auth/refresh", # only sent to this endpoint
        **COOKIE_SETTINGS
    )

    return {"message": "Logged in"}


@router.post("/refresh")
def refresh_token(
    request: Request,
    response: Response,
    session: SessionDep
):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="No refresh token")

    try:
        payload = decode_token(refresh_token, "refresh")
        user_id = str(payload["sub"])
        role = payload["role"]

        # Optional but recommended: check user still exists
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        access_token = create_access_token(user_id, role)
        new_refresh_token = create_refresh_token(user_id, role)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRY_TIME * 60,
        **COOKIE_SETTINGS
    )

    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRY_TIME * 24 * 60 * 60,
        path="/auth/refresh",
        **COOKIE_SETTINGS
    )

    return {"message": "Token refreshed"}


# update
@router.put("/update", response_model=UserRead)
def updateUser(
    data: UserUpdate,
    session: SessionDep,
    current_user: AuthDep
):
    user = session.get(User, current_user.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.name:
        user.name = data.name

    if data.password:
        user.hashed_password = hash_password(data.password)

    if data.institution_id:
        user.institution_id = data.institution_id

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


# logout
@router.post("/logout")
def logout(
    response: Response,
    current_user: AuthDep
):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token", path="/auth/refresh")

    return {"message": "Logged out"}