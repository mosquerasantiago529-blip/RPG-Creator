
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from personaje import generar_personaje, ganar_experiencia

app = FastAPI(title="RPG Creator")

app.add_middleware(
    SessionMiddleware,
    secret_key="rpg_creator_clave_secreta_2026"
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def inicio(request: Request):
    personaje = request.session.get("personaje")

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "personaje": personaje
        }
    )


@app.post("/generar")
def crear_personaje(
    request: Request,
    nombre: str = Form(...),
    raza: str = Form(...),
    clase_personaje: str = Form(...)
):
    personaje = generar_personaje(nombre, raza, clase_personaje)

    request.session["personaje"] = personaje

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "personaje": personaje
        }
    )


@app.post("/ganar-experiencia")
def subir_experiencia(request: Request):
    personaje = request.session.get("personaje")

    if personaje:
        personaje = ganar_experiencia(personaje, 25)
        request.session["personaje"] = personaje

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "personaje": personaje
        }
    )
