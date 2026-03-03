import random
opciones_rps = ["piedra", "papel", "tijeras"]
palabras_ahorcado = ["python", "mundo", "programa", "superbot", "juego", "teclado"]
chistes_opciones = [
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "Había una vez una silla que decidió ser psicóloga. ¿Cuál era su especialidad? El 'sillencio terapéutico'.",
    "¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!"
]

# Definimos función para pedir nuevo comando
def pregunta():
    return input("Dime qué hacer ahora (comandos: juegos, calculadora, contador, chiste) (Puedes decir 'off' para finalizar el chat): ").lower()

# Calculadora
def calculadora():
    print("\nCalculadora activada.")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")

    operacion = input("¿Qué operación deseas hacer?: ").lower()
    if operacion not in ["suma", "resta", "multiplicacion", "division"]:
        print("Operación no válida.")
        return pregunta()

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor ingresa solo números.")
        return pregunta()

    if operacion == "suma":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif operacion == "resta":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif operacion == "multiplicacion":
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif operacion == "division":
        if num2 == 0:
            print("¡Error! No se puede dividir por cero.")
        else:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
    return pregunta()

# Juego de piedra papel o tijeras
def rpsgame():
    rps = input("Elige piedra, papel o tijeras: ").lower()
    bot_rps = random.choice(opciones_rps)
    print("Tú elegiste:", rps)
    print("Superbot eligió:", bot_rps)

    if rps == bot_rps:
        print("¡Empate!")
    elif (rps == "piedra" and bot_rps == "tijeras") or (rps == "papel" and bot_rps == "piedra") or (rps == "tijeras" and bot_rps == "papel"):
        print("¡Ganaste!")
    elif rps in opciones_rps:
        print("¡Perdiste!")
    else:
        print("Opción no válida.")
    return pregunta()

# Juego del dado
def dado():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 10)
    dado3 = random.randint(1, 100)
    choosedado = input("Elige un dado: dado1 = 6 lados, dado2 = 10 lados, dado3 = 100 lados: ").lower()
    if choosedado == "dado1":
        print("Superbot tiró el dado y salió:", dado1)
    elif choosedado == "dado2":
        print("Superbot tiró el dado y salió:", dado2)
    elif choosedado == "dado3":
        print("Superbot tiró el dado y salió:", dado3)
    else:
        print("No te pude comprender.")
    return pregunta()

# Juego del ahorcado
def ahorcado():
    palabra = random.choice(palabras_ahorcado)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("_ " * len(palabra))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien! La letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan", intentos , "intentos.")

        progreso = ""
        for l in palabra:
            if l in letras_adivinadas:
                progreso += l + " "
            else:
                progreso += "_ "
        print(progreso)

        if all(l in letras_adivinadas for l in palabra):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
            return pregunta()

    print(f"¡Oh no! Te quedaste sin intentos. La palabra era: {palabra}")
    return pregunta()

# Contador de caracteres
def contador():
    texto_contador = input("Escribe tu texto aquí: ")
    caracteres = len(texto_contador)
    print("La cantidad de caracteres en tu texto es de:", caracteres)
    return pregunta()

# Adivinar número
def adivinar_numero():
    print("Estoy pensando en un número entre el 1 al 100, ¿podrás adivinarlo?")
    numero_pensado = random.randint(1, 100)
    intentos_adivinador = 0

    while True:
        try:
            intento = int(input("Adivina el número: "))
            intentos_adivinador += 1
            if intento < numero_pensado:
                print("Demasiado bajo.")
            elif intento > numero_pensado:
                print("Demasiado alto.")
            else:
                print("¡Correcto! Adivinaste el número en", intentos_adivinador, "intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return pregunta()

# Chistes
def chistes():
    print(random.choice(chistes_opciones))
    return pregunta()
