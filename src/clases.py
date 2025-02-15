# Importando módulo os para manipular el archivo.txt (agregar y eliminar películas)
import os

# Superclase Película con atributo nombre (privado), director, año y género (públicos)
class Película:
    def __init__(self, nombre, director, año, género):
        self.__nombre = nombre.title()
        self.director = director.title()
        self.año = int(año)
        self.género = género.title()
        
    def nombre_película(self):
        return self.__nombre
    
    def __str__(self):
        return f'Título: "{self.nombre_película()}"\nDirector: {self.director}\nAño de lanzamiento: {self.año}\nGenéro: {self.género}\n'
     
# Superclase CatálogoPelícula con atributo público catálogo, ruta de archivo con equivalencia a un archivo.txt con el nombre del catálogo y una lista vacía de películas
class CatálogoPelícula:
    def __init__(self, nombre_catálogo):
        self.nombre_catálogo = nombre_catálogo
        self.ruta_archivo = f'{nombre_catálogo}.txt'
        self.películas = []
    
# Método agregar_película() con atributo película que agrega películas al .txt de ruta_archivo
    def agregar_película(self, película):
        self.películas.append(película)
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'Título: "{película.nombre_película()}", Director: {película.director}, Año de lanzamiento: {película.año}, Género: {película.género}\n')
    
# Método listar_películas() que lee el contenido del archivo.txt y lo imprime por consola. En el caso de no existir el archivo, imprime un mensaje
    def listar_películas(self):
        if not os.path.exists(self.ruta_archivo):
            print('\nActualmente, no hay películas en el catálogo 😢\n')
        else:
            print('\nEstas son las películas que se encuentran actualmente en el catálogo:\n')
            with open(f'{self.ruta_archivo}', 'r') as archivo:
                print(archivo.read())
    
# Método eliminar_catálogo() que elimina el catálogo en caso de existir. Si el género (nombre_catálogo) no coincide con el dato ingresado, no se borrará el archivo. Si el archivo no existe, se imprime un mensaje
    def eliminar_películas(self):
        print('\n¿Qué película(s) deseas eliminar?\n')
        
        print(f'{self.nombre_catálogo}\n')
        eliminando_catálogo = input('Ingrese el género de la(s) película(s) que deseas eliminar: ').title()
            
        if os.path.exists(self.ruta_archivo) and eliminando_catálogo == self.nombre_catálogo:
            os.remove(self.ruta_archivo)
            print(f'\n¡La(s) película(s) del género "{self.nombre_catálogo}" ha(n) sido eliminada(s) con éxito!\n')
        elif eliminando_catálogo != self.nombre_catálogo:
            print('\nEl valor ingresado es inválido. Por favor, intente nuevamente.\n')
        else:
            print('\nEste género de película no existe.\n')
                