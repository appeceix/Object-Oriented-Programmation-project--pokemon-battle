import time
import numpy as np
import sys

def imprimir_con_retraso(s):
    '''Imprime una letra cada vez'''
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__ (self, nombre, tipos, movimientos, EVs, salud='===================='):
        # Guardamos las variables como atributos
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.salud = salud
        self.ataque = EVs['Ataque']
        self.defensa = EVs['Defensa']
        self.barras = 20 # Cantidad de barras de salud


    def print_de_batalla(self, Pokemon2):
        '''Imprime información de la pelea
        '''
        print("----BATALLA DE POKEMON----")
        print(f"\n{self.nombre}")
        print("TIPO/", self.tipos)
        print("ATAQUE/", self.ataque)
        print("DEFENSA/", self.defensa)
        print("NIVEL/", 3*(1+np.mean([self.ataque,self.defensa]))) # Forma en la que se calcula el nivel
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("TIPO/", Pokemon2.tipos)
        print("ATAQUE/", Pokemon2.ataque)
        print("DEFENSA/", Pokemon2.defensa)
        print("NIVEL/", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))
        time.sleep(2)

        version = ['fuego', 'agua', 'planta']
        for i, k in enumerate(version):

            if self.tipos == k:

                # Si son del mismo tipo, no es un ataque efectivo
                if Pokemon2.tipos == k:
                    string_1_attack = '\nNo es muy efectivo...'
                    string_2_attack = '\nNo es muy efectivo...'

                # Si Pokemon2 es fuerte contra nuestro pokemon
                if Pokemon2.tipos == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    string_1_attack = '\nNo es muy efectivo...'
                    string_2_attack = '\nEs muy efectivo!'

                # Si Pokemon2 es débil contra nuestro pokemon
                if Pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    string_1_attack = '\nEs muy efectivo!'
                    string_2_attack = '\nNo es muy efectivo...'    


        while (self.barras > 0) and (Pokemon2.barras > 0):

            # Imprime la salud de cada pokemon
            print(f"\n{self.nombre}\t\tPS\t{self.salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.salud}\n")

            # Turno Pokemon 1
            print(f"¡Vamos, {self.nombre}!")
            for i, x in enumerate(self.movimientos): # Obtenemos el índice y nombre del movimiento
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(string_1_attack)

            # Determinamos el daño a Pokemon2
            Pokemon2.barras -= self.ataque
            Pokemon2.salud = ""

            # Agregar barras adicionales a la salud cuando haya mejora de defensa
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.salud += "="
            
            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.salud}\n")
            time.sleep(.5)

            # Revisamos si Pokemon2 se debilitó
            if Pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + Pokemon2.nombre + ' se debilitó.')
                break


            # Turno Pokemon 2
            print(f"¡Vamos, {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"{Pokemon2.nombre} usó {Pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(string_2_attack)

            # Determinamos el daño a Pokemon1
            self.barras -= Pokemon2.ataque
            self.salud = ""

            # Agregar barras adicionales a la salud cuando haya mejora de defensa
            for j in range(int(self.barras+.1*self.defensa)):
                self.salud += "="

            time.sleep(1)
            print(f"{self.nombre}\t\tPS\t{self.salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.salud}\n")
            time.sleep(.5)

            # Revisamos si Pokemon1 se debilitó
            if self.barras <= 0:
                imprimir_con_retraso("\n..." + self.nombre + ' se debilitó.')
                break

            # Castigo por perder
            money = np.random.choice(5000)
            imprimir_con_retraso(f"\nPerdiste, pagas ${money}.\n")





if __name__ == '__main__':
    # Creación de pokemons fuera de la clase
    Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Garra Dragón', 'Giro Fuego', 'Anillo Ígneo'], {'Ataque':12, 'Defensa':8})
    Blastoise = Pokemon('Blastoise', 'agua', ['Hidrobomba', 'Pistola Agua', 'Hidropulso', 'Acua Cola'], {'Ataque':10, 'Defensa':10})
    Venusaur = Pokemon('Venusaur', 'planta', ['Rayo Solar', 'Hoja Afilada', 'Latigazo', 'Lluevehojas'], {'Ataque':8, 'Defensa':12})

    Charmander = Pokemon('Charmander', 'fuego', ['Ascuas', 'Giro Fuego'], {'Ataque':4, 'Defensa':2})
    Squirtle = Pokemon('Squirtle', 'agua', ['Pistola Agua', 'Burbuja'], {'Ataque':3, 'Defensa':3})
    Bulbasaur = Pokemon('Bulbasaur', 'planta', ['Látigo Cepa', 'Hoja Afilada'], {'Ataque':2, 'Defensa':4})

    Charmeleon = Pokemon('Charmeleon', 'fuego', ['Lanzallamas', 'Garra Dragón', 'Giro Fuego'], {'Ataque':8, 'Defensa':6})
    Wartortle = Pokemon('Wartortle', 'agua', ['Hidrobomba', 'Pistola Agua', 'Hidropulso'], {'Ataque':6, 'Defensa':6})
    Ivysaur = Pokemon('Ivysaur', 'planta', ['Rayo Solar', 'Hoja Afilada', 'Latigazo'], {'Ataque':4, 'Defensa':8})

    Charizard.print_de_batalla(Blastoise) # Inicia la pelea entre estos dos pokemon
    
