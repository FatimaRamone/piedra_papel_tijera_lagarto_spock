
# importo random y creo una lista para las posibilidades del valor del JugadorMaquina
import random
lista=["piedra" , "papel" , "tijera" , "lagarto" , "spock"]


#creo una superclase
class Jugador():
    def __init__(self , nombre , score = 0): #tengo un default para score , por eso no tengo que definirlo en el objeto
        self.nombre= nombre
        self.score= score
    #ESTO ES UNA DEFINICIÓN

    def jugar(self):
        pass
 

class JugadorHumano(Jugador):
    def __init__(self , nombre ,score = 0):
        super().__init__(nombre , score)
    #ESTO NO ES UNA DEFINICIÓN , ES UNA LLAMADA

#llama a la función init de la superclase para evitar repetición de las definiciones

    def jugar(self):
     while True:
        valor1 = input("Introduce un valor: ")
        if valor1 not in lista:
            print("Ese valor no es válido. Introduce un valor de nuevo.")
        else:
            return valor1

    
    #creo una función específica para Jugador Humano , que requiere un input del usuario
        

class JugadorMaquina(Jugador):

    def __init__(self , nombre = "Maquina" ,score = 0):    # JugadorMaquina tiene nombre por default
        super().__init__(nombre , score)
       # print(self.nombre , self.score)

 #ESTO NO ES UNA DEFINICIÓN , ES UNA LLAMADA

#llama a la función init de la superclase para evitar repetición de las definiciones

    

    def jugar(self):
        
         #importa contenido de la lista usando la funcion de python "random"
             
        return random.choice(lista)   #selecciono un valor random de la lista
    
   