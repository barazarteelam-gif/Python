print("     !!!BATALLA DE HECHICEROS!!!      ")
hechicero_p1=input("Hechicero 1, Escoja su Nombre")
print(f'Hechicero 1, te declaro como el gran {hechicero_p1}')
tipo_hechicero_p1=int(input(f'{hechicero_p1}, escoja que tipo de hechizos requiere para este duelo, 1.Tierra, 2.Fuego, 3.Hielo, 4.Aire, 5.Agua, 6.Electricidad'))

if tipo_hechicero_p1==1:
    hechizo_p1,poder_p1,vida_p1="Tierra",10,130
    print(f'El gran {hechicero_p1}, será un hechicero de Tierra')
elif tipo_hechicero_p1==2:
    hechizo_p1,poder_p1,vida_p1="Fuego",25,90
    print(f'El gran {hechicero_p1}, será un hechicero de Fuego')
elif tipo_hechicero_p1==3:
    hechizo_p1,poder_p1,vida_p1="Hielo",15,110
    print(f'El gran {hechicero_p1}, será un hechicero de Hielo')
elif tipo_hechicero_p1==4:
    hechizo_p1,poder_p1,vida_p1="Aire",20,95
    print(f'El gran {hechicero_p1} será un hechicero de Aire')
elif tipo_hechicero_p1==5:
    hechizo_p1,poder_p1,vida_p1="Agua",30,80
    print(f'El gran {hechicero_p1} será un hechicero de Agua')
elif tipo_hechicero_p1==6:
    hechizo_p1,poder_p1,vida_p1="Electricidad",22,93
    print(f'El gran {hechicero_p1} será un hechicero Eléctrico')
else:
    hechizo_p1,poder_p1,vida_p1="Energia Pura",18,100
    print(f'El gran {hechicero_p1} será un hechicero de Energia Pura')


hechicero_p2=input("Hechicero 2, Escoja su nombre")
print(f'Hechicero 2, te declaro como el gran {hechicero_p2}')
tipo_hechicero_p2=int(input(f'{hechicero_p2}, escoja que tipo de hechizos requiere para este duelo, 1.Tierra, 2.Fuego, 3.Hielo, 4.Aire, 5.Agua, 6.Electricidad'))
if tipo_hechicero_p2==1:
    hechizo_p2,poder_p2,vida_p2="Tierra",10,130
    print(f'El gran {hechicero_p2}, será un hechicero de Tierra')
elif tipo_hechicero_p2==2:
    hechizo_p2,poder_p2,vida_p2="Fuego",25,90
    print(f'El gran {hechicero_p2}, será un hechicero de Fuego')
elif tipo_hechicero_p2==3:
    hechizo_p2,poder_p2,vida_p2="Hielo",15,110
    print(f'El gran {hechicero_p2}, será un hechicero de Hielo')
elif tipo_hechicero_p2==4:
    hechizo_p2,poder_p2,vida_p2="Aire",20,95
    print(f'El gran {hechicero_p2} será un hechicero de Aire')
elif tipo_hechicero_p2==5:
    hechizo_p2,poder_p2,vida_p2="Agua",30,80
    print(f'El gran {hechicero_p2} será un hechicero de Agua')
elif tipo_hechicero_p2==6:
    hechizo_p2,poder_p2,vida_p2="Electricidad",22,93
    print(f'El gran {hechicero_p2} será un hechicero Eléctrico')
else:
    hechizo_p2,poder_p2,vida_p2="Energia Pura",18,100
    print(f'El gran {hechicero_p2} será un hechicero de Energia Pura')




ataque_defensa1=int(input(f'El gran {hechicero_p1} escogerá una acción, cual será esa acción?, 1.Atacar 2.Defender'))
ataque_defensa2=int(input(f'El gran {hechicero_p2} escogerá una acción, cual será esa acción?, 1.Ataque 2.Defender'))
multi_p1=1
multi_p2=1



if ataque_defensa1==1 and (hechizo_p1=="Fuego" and hechizo_p2=="Hielo") or (hechizo_p1=="Tierra" and hechizo_p2=="Fuego") or (hechizo_p1=="Hielo" and hechizo_p2=="Tierra") or (hechizo_p1=="Agua" and hechizo_p2=="Hielo") or (hechizo_p1=="Electricidad" and hechizo_p2=="Agua") or (hechizo_p1=="Aire" and hechizo_p2=="Electricidad") or (hechizo_p1=="Tierra" or hechizo_p2=="Aire"):
        multi_p1=multi_p1*1.5
elif ataque_defensa1==1 and (hechizo_p1=="Fuego" and hechizo_p2=="Tierra") or (hechizo_p1=="Tierra" and hechizo_p2=="Hielo") or (hechizo_p1=="Hielo" and hechizo_p2=="Fuego") or (hechizo_p1=="Hielo" and hechizo_p2=="Agua") or (hechizo_p1=="Agua" and hechizo_p2=="Electricidad") or (hechizo_p1=="Tierra" and hechizo_p2=="Aire") or (hechizo_p1=="Electricidad" and hechizo_p2=="Aire"):
        multi_p1=multi_p1*0.7

if ataque_defensa2==1 and (hechizo_p2=="Fuego" and hechizo_p1=="Hielo") or (hechizo_p2=="Tierra" and hechizo_p1=="Fuego") or (hechizo_p2=="Hielo" and hechizo_p1=="Tierra") or (hechizo_p2=="Agua" and hechizo_p1=="Hielo") or (hechizo_p2=="Electricidad" and hechizo_p1=="Agua") or (hechizo_p2=="Aire" and hechizo_p1=="Electricidad") or (hechizo_p2=="Tierra" or hechizo_p1=="Aire"):
        multi_p1=multi_p1*1.5
elif ataque_defensa2==1 and (hechizo_p2=="Fuego" and hechizo_p1=="Tierra") or (hechizo_p2=="Tierra" and hechizo_p1=="Hielo") or (hechizo_p2=="Hielo" and hechizo_p1=="Fuego") or (hechizo_p2=="Hielo" and hechizo_p1=="Agua") or (hechizo_p2=="Agua" and hechizo_p1=="Electricidad") or (hechizo_p2=="Tierra" and hechizo_p1=="Aire") or (hechizo_p2=="Electricidad" and hechizo_p1=="Aire"):
        multi_p1=multi_p1*0.7
elif (ataque_defensa1==2 and ataque_defensa2==1)or(ataque_defensa1==1 and ataque_defensa2==2):
            multi_p1=multi_p2*0.5
            multi_p2=multi_p1*0.5



    

daño_hechicero2=multi_p1*poder_p1
daño_hechicero1=multi_p2*poder_p2
vida_p1_final=vida_p1-daño_hechicero2
vida_p2_final=vida_p2-daño_hechicero1


print(f'El Gran {hechicero_p1} Recibió {daño_hechicero1} de daño')   
print(f'El Gran {hechicero_p1} quedó con {vida_p1_final} de vida')   
print(f'El Gran {hechicero_p2} Recibió {daño_hechicero2} de daño')    
print(f'El Gran {hechicero_p2} quedó con {vida_p2_final} de vida')   
      

if vida_p1_final>vida_p2_final:
            print(f'El Gran {hechicero_p1} HA SIDO EL GANADOR DE ESTE DUELO!!!')
elif vida_p2_final>vida_p1_final:
            print(f'El gran {hechicero_p2} HA SIDO EL GANADOR DE ESTE DUELO!!!')
else:
            print(f'Empate mágico entre los dos grandes {hechicero_p1} y {hechicero_p2}. Los dos nos han deleitado con un gran duelo de hechiceria, Felicitaciones a ambos')