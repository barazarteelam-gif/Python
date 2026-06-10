
    
piso = [(1,1),(1,2),(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),(5,1),(5,2)]
habitacion_piso = int(input("Bienvenido al hotel de Don Ramon, elija el piso en el que se desea quedar"))
habitacion_puerta = int(input("En que puerta desea quedarse? Puerta 1 o Puerta 2"))
nombre = input("A nombre de quien está la habitación")
eleccion = (habitacion_piso,habitacion_puerta)
if eleccion not in piso:
       print("ERROR:PISO NO VALIDO")
else:
    print(f"Habitacion Asignada:{habitacion_piso}0{habitacion_puerta}")
    print(f"Huesped: {nombre}")
    salir = input("Desea salir del hotel? Si/No").lower()
    if salir == "si":
            eleccion= None
            print(f"{nombre} ha salido del hotel")
            print(f"Habitacion Vaciada : {habitacion_piso}0{habitacion_puerta}")
    elif salir == "no":
                print("Disfrute su estancia, el programa terminara, y para salir tendra que volver a iniciarlo")


  
  

            
                    

        




    

