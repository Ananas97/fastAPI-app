import uvicorn
import secrets
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse

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


uvicorn.run(app, host="127.0.0.1", port=8000)
