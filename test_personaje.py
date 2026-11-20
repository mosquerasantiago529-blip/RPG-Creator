
from fastapi.testclient import TestClient
from main import app
from personaje import generar_personaje

client = TestClient(app)


# PRUEBA 1: Generar personaje correctamente
def test_generar_personaje():
    personaje = generar_personaje("Davxx", "Humano", "Guerrero")

    assert personaje["nombre"] == "Davxx"
    assert personaje["raza"] == "Humano"
    assert personaje["clase"] == "Guerrero"


# PRUEBA 2: Verificar nivel inicial
def test_nivel_inicial():
    personaje = generar_personaje("Thor", "Orco", "Mago")

    assert personaje["nivel"] == 1


# PRUEBA 3: Verificar estadísticas
def test_estadisticas_validas():
    personaje = generar_personaje("Loki", "Elfo", "Arquero")

    for valor in personaje["estadisticas"].values():
        assert isinstance(valor, int)
        assert valor >= 5


# PRUEBA 4: Verificar habilidades
def test_habilidades_segun_clase():
    personaje = generar_personaje("Shadow", "Humano", "Asesino")

    assert "Ataque sigiloso" in personaje["habilidades"]


# PRUEBA 5: Verificar ruta principal
def test_ruta_principal():
    respuesta = client.get("/")

    assert respuesta.status_code == 200
    assert "RPG Creator" in respuesta.text


# PRUEBA 6: Verificar generación desde el formulario
def test_generar_desde_formulario():
    respuesta = client.post(
        "/generar",
        data={
            "nombre": "Davxx",
            "raza": "Humano",
            "clase_personaje": "Guerrero"
        }
    )

    assert respuesta.status_code == 200
    assert "Davxx" in respuesta.text
    assert "Golpe poderoso" in respuesta.text


# PRUEBA 7: Verificar datos incompletos
def test_datos_incompletos():
    respuesta = client.post("/generar", data={})

    assert respuesta.status_code == 422

