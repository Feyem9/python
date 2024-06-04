from fastapi import Depends , FastAPI , HTTPException , status# type:ignore
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm #type:ignore
from pydantic import BaseModel #type:ignore
from datetime import datetime , timedelta
from jose import JWTError , jwt #type:ignore
from passlib.context import CryptContext #type:ignore


SECRET_KEY = '5578c6dc369e192791d436a4d6f991e008c48b94cf7e5a922d7deda89cf18538'
ALGORITHM = 'HS256'
ACCES_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

db = {
    'user':{
        'username':'christ',
        'name' :'tian',
        'email': 'christian@gmail.com',
        'hash_password':'',
        'disable':False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None#type:ignore



class User(BaseModel):
    username:str
    email:str or None = None#type:ignore
    full_name:str or None = None#type:ignore
    disable:str  or None = None#type:ignore


class UserInDb(User):
    hashed_password:str


pwd_context = CryptContext(schemes=['bscrypt'],deprecated=['auto'])    
oauth_2_scheme=OAuth2PasswordBearer(tokenUrl='token')

def verify_password(password , hash):
    return pwd_context.verify(password , hash)


def get_password_hash(password_hash):
    return pwd_context.hash(password_hash)


def get_user(db , username:str):
    if username in db:
        user_data = db[username]
        return UserInDb(**user_data)