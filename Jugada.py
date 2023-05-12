
dict = {'tijera': ['papel', 'lagarto'], 'papel': ['piedra', 'spock'], 'piedra': ['lagarto', 'tijera'],
        'lagarto': ['spock', 'papel'], 'spock': ['tijera', 'piedra']}

# dict = {'self.valor1 :['self.valor2' ,self.valor2] , etc}

 
        
 #defino la clase
class Jugada():
    def __init__(self , valor , valor2):
        self.valor=valor        
        self.valor2=valor2
   

    #un objeto de una clase  se va a definir como jugada1= Jugada(atributos)

    # Clase : los valores de la clase Jugada , se van a llamar self.valor y self.valor2
    # Main : los valores de el objeto jugada1 , se van a llamar jugada1.valor y jugada1.valor2



    #segunda versión , más optimizada , usando un diccionario

    def func(self):
         #return False if self.valor in dict[self.valor2] else True  
         return self.valor2 in dict[self.valor]
    
    #return False if "tijera" en el dict ["papel" , "largarto"] , en otro caso True 






     #version numero uno:
    def primeraversion(self):
            
            if self.valor == "piedra" and self.valor2 == "tijera":
                 return True
            elif self.valor == "tijera" and self.valor2 == "papel":
                 return True
            elif self.valor == "papel" and self.valor2 == "piedra":
                 return True
            
            elif self.valor == "piedra" and self.valor2 == "lagarto":
                 return True
            elif self.valor == "lagarto" and self.valor2 == "spock":
                 return True
            elif self.valor == "spock" and self.valor2 == "tijera":
                 return True
            
            elif self.valor == "tijera" and self.valor2 == "lagarto":
                 return True
            elif self.valor == "lagarto" and self.valor2 == "papel":
                 return True
            elif self.valor == "papel" and self.valor2 == "spock":
                 return True
            elif self.valor == "spock" and self.valor2 == "piedra":
                 return True
            elif self.valor == "lagarto" and self.valor2 == "papel":
                 return True
            elif self.valor == "papel" and self.valor2 == "spock":
                 return True
            else:
                 return False
            
    
   