from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Sample FastAPI API", version="0.1.0")
templates = Jinja2Templates(directory="templates")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"error": None})


@app.post("/login", response_class=HTMLResponse)
def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    if username == "admin" and password == "admin":
        return templates.TemplateResponse(request, "welcome.html", {"username": username})

    return templates.TemplateResponse(
        request,
        "login.html",
        {"error": "Invalid username or password"},
        status_code=401,
    )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
