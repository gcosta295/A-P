Harina=float(input("Cuantas tazas de harina quiere usar?"))
print(Harina, "tazas de harina")

Agua=float(input("Cuantas tazas de agua?"))
print(Agua, "tazas de agua")

Sal=float(input("Cuantas cucharadas de sal quiere usar?"))
Sal=Sal/3/16
print(Sal, "tazas de sal")

Aceite=float(input("Cuantas cucharadas de aceite quiere usar?"))
Aceite=Aceite/3
print(Aceite, "tazas de aceite")

total=Aceite+Agua+Sal+Harina

print("Despues de ser cocinadas tienes", total, "tazas de arepas")
