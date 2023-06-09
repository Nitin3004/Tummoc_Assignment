from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import timedelta, datetime
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["users"]
users_collection = db["users"]

security = HTTPBasic()


def authenticate_user(username: str, password: str):
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        return True
    else:
        return False


def get_current_time():
    return datetime.now()


def get_expiration_time():
    return datetime.now() + timedelta(minutes=5)


@app.post("/create-user")
async def create_user(username: str, password: str):
    user = {"username": username, "password": password}
    users_collection.insert_one(user)
    return {"message": "User created successfully"}


@app.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    if not authenticate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    return {"message": "Login successful"}


@app.post("/login-with-authentication")
async def login_with_authentication(credentials: HTTPBasicCredentials = Depends(security)):
    if not authenticate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    current_time = get_current_time()
    expiration_time = get_expiration_time()
    return {"message": "Login successful", "current_time": current_time, "expiration_time": expiration_time}


@app.post("/login-with-session-timeout")
async def login_with_session_timeout(credentials: HTTPBasicCredentials = Depends(security)):
    if not authenticate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    current_time = get_current_time()
    expiration_time = get_expiration_time()

    if current_time >= expiration_time:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired")

    return {"message": "Login successful", "current_time": current_time, "expiration_time": expiration_time}
