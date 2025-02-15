# Importando archivo clases.py con sus superclases
from clases import Película, CatálogoPelícula

# Variable que imprime un mensaje (para usar con errores y excepciones)
mensaje_error = 'Ha ocurrido algo inesperado ❗\n'

# Función que imprime el menú de opciones del catálogo
def menú_catálogo():
    print('A continuación, te ofrecemos las opciones disponibles:\n')
    print('1. Agregar película(s) ✨')
    print('2. Listar películas 📄')
    print('3. Eliminar catálogo de películas ❌')
    print('4. Salir 👋\n')
    
# Función que presenta un título principal y un condicional según la opción seleccionada del menú por el usuario
def corriendo_catálogo():
    print('\nBienvenido al catálogo de películas "Ada" 🌸 ¿Qué deseas hacer hoy?')
    
    while True:
        try:
            menú_catálogo()
            opción = int(input('Seleccione una opción [1-4]: '))

            # Si opción es igual a 1, se pide nombre, director, año de lanzamiento y género de la película
            if opción == 1:
                nombre_película = input('\nIngresa el nombre de la película: ').title()
                director_película = input(f'Ingresa el director(a) de la película: ').title()
                año_película = int(input(f'Ingresa el año de lanzamiento de la película: '))
                género_película = input(f'Ingresa el género de la película: ').title()
                
                # Se crea un catálogo (archivo.txt) con el género ingresado como nombre del catálogo y se ingresan la información de película dentro del mismo
                catálogo = CatálogoPelícula(género_película)
                película = Película(nombre_película, director_película, año_película, género_película)
                catálogo.agregar_película(película)
                
                print('\n¡Película agregada con éxito! 💖\n')
                continue
                
            # Si opción es igual a 2, activa el método listar_películas() de la superclase CatálogoPelícula
            elif opción == 2:
                catálogo.listar_películas()
                continue
            
            # Si opción es igual a 3, activa el método eliminar_películas() de la superclase CatálogoPelícula
            elif opción == 3:
                catálogo.eliminar_películas()
                continue
            
            # Si la opción es 4, imprime un mensaje de despedida y cierra el programa
            elif opción == 4:
                print('\nGracias por utilizar el catálogo de películas "Ada" 🌸 Te esperamos nuevamente. ¡Hasta la próxima! 👋\n')
                break
                
            # En el caso de que las opciones no sean [1, 2, 3, 4], imprimirá un mensaje de opción inválida y reiniciará el ciclo mostrando las opciones disponibles
            else:
                print('La opción ingresada no es válida. Por favor, intente nuevamente 😥')
            break
 
        # Dependiendo el tipo de excepción que pueda ocurrir durante el programa, esta sección imprime el mensaje correspondiente para el usuario
        except ValueError:
            print(f'\n{mensaje_error}La opción ingresada no es válida. Por favor, intente nuevamente 😥\n')
            continue
        except KeyboardInterrupt:
            print(f'\n{mensaje_error}Se ha utilizado el comando de cierre. Cerrando el programa... ¡Hasta luego! 👋\n')
            break
        except UnboundLocalError:
            print(f'\n{mensaje_error}No hay información en esta sección aún. Prueba agregando películas primero ✨\n')

# Corriendo el programa
corriendo_catálogo()
