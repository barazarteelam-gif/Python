nota=int(input("Ingresa tu nota"))
if nota<0 or nota>100:
    print("Nota invalida")
elif nota>=99 or nota>=90:
    print("Sacaste A, Felicidades")
elif nota>=89 or nota>=80:
    print("Sacaste B")
elif nota>=79 or nota>=70:
    print("Sacaste C")
elif nota>=69 or nota>=60:
    print("Sacaste D")
elif nota>=59 or nota>=0:
    print("Sacaste F, Reprobaste")