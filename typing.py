#Tipos de variables en python
entero:int=0
#el infiere y deduce que tipo de variable se pone, por lo tanto, no hay necesidad de especificar el tipo de variable
decimal:float=0.001
cadena:str="Cadena de texto simple" #input siempre es string, input es una funcion que espera que se ingrese algo por teclado y una vez que se presiona enter, el valor ingresado se guarda en la variable
booleano:bool= True or False 
print(booleano)#print imprime mensaje en la terminal, convierte str 
entrada=int(input("msg"))#int convierte en numero la variable que se va a ingresar en el input
v:str="Sexo"
m:str="Verga"
print(f'Que quiere el pueblo? {v}, Y que quieren los hombres {m}')#f string es con comillas, y las llaves son para concatenar texto con las variables
