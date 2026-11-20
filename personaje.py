
import random


def generar_personaje(nombre, raza, clase_personaje):

    estadisticas = {
        "Fuerza": random.randint(5, 20),
        "Defensa": random.randint(5, 20),
        "Agilidad": random.randint(5, 20),
        "Inteligencia": random.randint(5, 20),
        "Vitalidad": random.randint(50, 100)
    }

    habilidades = {
        "Guerrero": ["Golpe poderoso", "Escudo de hierro", "Furia"],
        "Mago": ["Bola de fuego", "Teletransportación", "Rayo arcano"],
        "Arquero": ["Disparo preciso", "Lluvia de flechas", "Camuflaje"],
        "Asesino": ["Ataque sigiloso", "Veneno", "Sombra mortal"]
    }

    avatares = {
        "Guerrero": "guerrero.png",
        "Mago": "mago.png",
        "Arquero": "arquero.png",
        "Asesino": "asesino.png"
    }

    return {
        "nombre": nombre,
        "raza": raza,
        "clase": clase_personaje,
        "nivel": 1,
        "experiencia": 0,
        "xp_siguiente": 100,
        "estadisticas": estadisticas,
        "habilidades": habilidades.get(clase_personaje, []),
        "avatar": avatares.get(clase_personaje, "guerrero.png")
    }


def ganar_experiencia(personaje, cantidad=25):

    personaje["experiencia"] += cantidad

    while personaje["experiencia"] >= personaje["xp_siguiente"]:

        personaje["experiencia"] -= personaje["xp_siguiente"]
        personaje["nivel"] += 1
        personaje["xp_siguiente"] += 50

        personaje["estadisticas"]["Fuerza"] += 2
        personaje["estadisticas"]["Defensa"] += 2
        personaje["estadisticas"]["Agilidad"] += 2
        personaje["estadisticas"]["Inteligencia"] += 2
        personaje["estadisticas"]["Vitalidad"] += 10

    return personaje
