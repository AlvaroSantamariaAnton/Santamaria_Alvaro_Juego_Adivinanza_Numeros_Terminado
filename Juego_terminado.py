import random   # Importamos la librería random para generar números aleatorios

# Muestra el título del juego
titulo = "Bienvenido al Juego de Adivinanza de Números"
print("\n" + titulo + "\n" + "-" * len(titulo))


def get_difficulty():
    # Función para obtener la dificultad del jugador

    while True:
        dificultad = input("\nElige la dificultad (fácil, normal, difícil o extrema): ").lower()
        if dificultad in ["fácil", "normal", "difícil", "extrema"]:
            
            # Mostrar la dificultad, su respectivo rango y sus respectivos intentos
            if dificultad == "fácil":
                print("\nHas seleccionado la dificultad: Fácil (Rango: 1-10) Tienes 5 intentos.")
            elif dificultad == "normal":
                print("\nHas seleccionado la dificultad: Normal (Rango: 1-50) Tienes 10 intentos.")
            elif dificultad == "difícil":
                print("\nHas seleccionado la dificultad: Difícil (Rango: 1-100) Tienes 15 intentos.")
            elif dificultad == "extrema":
                print("\nHas seleccionado la dificultad: Extrema (Rango: 1-1000) Tienes 25 intentos.")
            return dificultad
        else:
            print("\nPor favor, elige una dificultad válida (Ten en cuenta las tíldes).")



def generate_random_number(dificultad):
    # Genera un número aleatorio dentro de un rango dependiendo de la dificultad

    if dificultad == "fácil":
        return random.randint(1, 10)
    elif dificultad == "normal":
        return random.randint(1, 50)
    elif dificultad == "difícil":
        return random.randint(1, 100)
    elif dificultad == "extrema":
        return random.randint(1, 1000)



def get_max_attempts(dificultad):
    # Función para obtener el número máximo de intentos según la dificultad

    if dificultad == "fácil":
        return 8
    elif dificultad == "normal":
        return 20
    elif dificultad == "difícil":
        return 40
    elif dificultad == "extrema":
        return 60



def play_guessing_game():
    # Función principal para jugar la adivinanza

    # Obtener la dificultad del jugador
    dificultad = get_difficulty()
    
    # Generar un número aleatorio
    numero_a_adivinar = generate_random_number(dificultad)

    intentos = 0

    max_intentos = get_max_attempts(dificultad)

    while True:
        try:
            # Obtener la suposición del jugador
            suposicion = int(input("\nIntroduce tu suposición: "))
            
            # Incrementar el número de intentos
            intentos += 1

            # Verificar si la suposición es correcta
            if suposicion == numero_a_adivinar:

                # Mensaje personalizado según la cantidad de intentos
                if intentos == 1:
                    print(f"¡Increíble, adivinaste el número en {intentos} intento!")
                else:
                    print(f"¡Felicidades, adivinaste el número en {intentos} intentos!")
                break
    
            # Si el jugador no adivina en el número máximo de intentos, mostrar un mensaje y terminar el juego
            elif intentos == max_intentos:
                print(f"\nLo siento, has agotado tus {max_intentos} intentos. El número correcto era el {numero_a_adivinar}.") 
                break    
            elif suposicion < numero_a_adivinar:
                print("El número es mayor, intenta de nuevo.")
                print(f"Intentos: {intentos}")
            elif suposicion > numero_a_adivinar:
                print("El número es menor, intenta de nuevo.")
                print(f"Intentos: {intentos}")
            else:
                print("\nPor favor, introduce un número válido (Ten en cuenta el rango).")

        except ValueError:
            print("\nPor favor, introduce un número válido (Ten en cuenta el rango).")


# Juego principal
while True:
    play_guessing_game()
    
    # Solicitar al usuario que responda con "sí" o "no"
    while True:
        volver_a_jugar = input("\n¿Quieres volver a jugar? (sí/no): ").lower()
        if volver_a_jugar in ["sí", "no"]:
            break
        else:
            print("\nPor favor, responde con sí o no (Ten en cuenta las tíldes).")

    if volver_a_jugar == "no":
        print("\n¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        continue


# Bloque que se ejecuta solo si el script se ejecuta directamente (no se importa como módulo)
if __name__ == "__main__":
    pass