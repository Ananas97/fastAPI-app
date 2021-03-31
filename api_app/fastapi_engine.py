import uvicorn
import secrets
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse
from cipher_methods.methods import CaesarCipher as Cipher

app = FastAPI()
security = HTTPBasic()

'''Method with BasicAuth for user authorization'''


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


'''Root routing  with basic info on methods'''


@app.get("/", dependencies=[Depends(valid)])
async def get_root():
    html_content = "<html>" \
                   "<body>" \
                   "<h1>FASTAPI APP</h1>" \
                   "<div>" \
                   "Route for decode: <a href='/decode'>/decode/</a>" \
                   "</div>" \
                   "<div>" \
                   "Route for encode: <a href='/encode'>/encode/</a>" \
                   "</div>" \
                   "</body>" \
                   "</html>"

    return HTMLResponse(content=html_content, status_code=200)


'''Root routing for decode method'''


@app.get("/decode/{shift}/{message}", dependencies=[Depends(valid)])
async def decode(message: str, shift: int):
    cipher = Cipher(shift, message)
    return {"decoded": cipher.decrypt()}


'''Root routing for encode method'''


@app.get("/encode/{shift}/{message}", dependencies=[Depends(valid)])
async def encode(message: str, shift: int):
    cipher = Cipher(shift, message)
    return {"encrypted": cipher.encrypt()}


uvicorn.run(app, host="127.0.0.1", port=8000)
