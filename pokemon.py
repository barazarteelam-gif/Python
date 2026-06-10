entrenador1=input("Cual es tu nombre entrenador1?")
eleccion1=input(f'Cual sera tu pokemon? {entrenador1}')
if eleccion1==1:
    tipo_p1,vida_p1,poder_p1="Hierba",100,15
    print(f'Tu pokemon Sera Bulbasaur {entrenador1}')
elif eleccion1==2:
    tipo_p1,vida_p1,poder_p1="Fuego",80,20
    print(f'Tu pokemon Sera Charmander {entrenador1}')
elif eleccion1==3:
    tipo_p1,vida_p1,poder_p1="Agua",90,18
    print(f'Tu pokemon Sera Squirtle {entrenador1}')
else:
    print(f'Tu pokemon Sera Pikachu {entrenador1}')
    tipo_p1,vida_p1,poder_p1="Electrico",70,22
entrenador2=input("Cual es tu nombre entrenador2?")
eleccion2=input(f'Cual sera tu pokemon? {entrenador2}')
if eleccion2==1:
    tipo_p2,vida_p2,poder_p2="Hierba",100,15
    print(f'Tu pokemon sera Bulbasaur {entrenador2}')
elif eleccion1==2:
    tipo_p2,vida_p2,poder_p2="Fuego",80,20
    print(f'Tu pokemon sera Charmander {entrenador2}')
elif eleccion1==3:
    tipo_p2,vida_p2,poder_p2="Agua",90,18
    print(f'Tu pokemon sera Squirtle {entrenador2}')
else:
    tipo_p2,vida_p2,poder_p2="Electrico",70,22
    print(f'Tu pokemon sera Pikachu {entrenador2}')
    #Fase de Combate
    ataque1=input(f'1.Ataque Especial o 2.Ataque Normal {entrenador1}')
    ataque2=input(f'1.Ataque Especial o 2.Ataque Normal {entrenador2}')
    multi_p1=1
    multi_p2=1
    if ataque1==1:
        if(tipo_p1=="Fuego" and tipo_p2=="Hierba") or (tipo_p1=="Hierba" and tipo_p2=="Agua") or (tipo_p1=="Agua" and tipo_p2=="Fuego") or (tipo_p1=="Electrico" or tipo_p2=="Agua"):
            multi_p1=multi_p1*2
        elif(tipo_p1=="Fuego" and tipo_p2=="Agua") or (tipo_p1=="Agua" and tipo_p2=="Hierba") or (tipo_p1=="Hierba" and tipo_p2=="Fuego") or (tipo_p1=="Electrico" or tipo_p2=="Hierba"):
            multi_p1=multi_p1*0.5
    if ataque1==2:
        if(tipo_p1=="Fuego" and tipo_p2=="Hierba") or (tipo_p1=="Hierba" and tipo_p2=="Agua") or (tipo_p1=="Agua" and tipo_p2=="Fuego") or (tipo_p1=="Electrico" or tipo_p2=="Agua"):
            multi_p1=multi_p1*2
        elif(tipo_p1=="Fuego" and tipo_p2=="Agua") or (tipo_p1=="Agua" and tipo_p2=="Hierba") or (tipo_p1=="Hierba" and tipo_p2=="Fuego") or (tipo_p1=="Electrico" or tipo_p2=="Hierba"):
            multi_p1=multi_p1*0.5
    
    daño_p2=multi_p1*poder_p1
    daño_p1=multi_p2*poder_p2
    hp_p1_final=vida_p1-daño_p1
    hp_p2_final=vida_p2-daño_p2

    print(f'{entrenador1} recibio {daño_p1}. Vida Restante {hp_p1_final}')
    print(f'{entrenador2} recibio {daño_p2}. Vida Restante {hp_p2_final}')

    if hp_p1_final>hp_p2_final:
        print(f'{entrenador1} con {eleccion1} HAN GANADO LA BATALLA POKEMON!!!')
    elif hp_p2_final>hp_p1_final:
        print(f'{entrenador2} y {eleccion2} HAN GANADO LA BATALLA POKEMON!!!')
    else:
        print("Es un empate")

