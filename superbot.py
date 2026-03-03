# Importamos lo que vamos a necesitar para el bot
import funciones_superbot

# Comienza el programa
print("¡Hola! Soy Superbot, el mejor bot de todos.")
command = input("Dime qué hacer (comandos: juegos, calculadora, contador, chiste) (Puedes decir 'off' para finalizar el chat): ").lower()

while command != "off":
    if command == "juegos":
        juego = input("¿Qué jugaremos hoy? (piedra papel o tijeras, ahorcado, tirar los dados o adivina el numero): ").lower()
        if juego == "piedra papel o tijeras":
            command = funciones_superbot.rpsgame()
        elif juego == "tirar los dados":
            command = funciones_superbot.dado()
        elif juego == "ahorcado":
            command = funciones_superbot.ahorcado()
        elif juego == "adivina el numero":
            command = funciones_superbot.adivinar_numero()
        else:
            print("No entendí qué juego quieres jugar.")
            command = funciones_superbot.pregunta()
    elif command == "calculadora":
        command = funciones_superbot.calculadora()
    elif command == "contador":
        command = funciones_superbot.contador()
    elif command == "chiste":
        command = funciones_superbot.chistes()
    else:
        print("Parece que escribiste un comando equivocado, vuelve a intentarlo.")
        command = funciones_superbot.pregunta()

print("¡Hasta luego! Superbot se despide.")
#fin del programa