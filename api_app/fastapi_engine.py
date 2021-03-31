import uvicorn
import secrets
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


def valid(credentials: HTTPBasicCredentials = Depends(security)):
    username = secrets.compare_digest(credentials.username, "user")
    password = secrets.compare_digest(credentials.password, "password")
    if not (username and password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True


@app.get("/", dependencies=[Depends(valid)])
async def get_root():
    return "Hello world!"


uvicorn.run(app, host="127.0.0.1", port=8000)
