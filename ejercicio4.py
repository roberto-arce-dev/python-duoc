#1 cuota → 0 % de recargo.
#2 a 3 cuotas → 3 %.
#4 a 6 cuotas → 8 %.
#7 a 9 cuotas → 14 %.
#10 a 12 cuotas → 22 %
from random import randint
valid_monto=True
recargo= 0
monto_total=0
valor_cuota = 0
while valid_monto:
    try:
        monto = int(input("Ingresa un monto: "))
        valid_monto=False
    except ValueError:
        print("el monto ingresado no es valido")
        continue
num_cuotas= randint(1,12)
if num_cuotas == 1 :
    valor_cuota = monto
    monto_total = monto
    print(f"el numero de cuotas es: {num_cuotas}")
elif 2 <= num_cuotas <= 3:
    print(f"el numero de cuotas es: {num_cuotas}")
    recargo = monto * 0.03
elif 4 <= num_cuotas <= 6 :
    recargo = monto * 0.08
    print(f"entre entre la cuota 4 y 6")
elif 7 <= num_cuotas <= 9:
    recargo = monto * 0.14
    print(f"el numero de cuotas es: {num_cuotas}")
elif 10 <= num_cuotas <= 12:
    recargo = monto * 0.22
    print(f"el numero de cuotas es: {num_cuotas}")

monto_total = monto + recargo
valor_cuota = monto_total / num_cuotas 
print(f"tu monto de la cuota es: {valor_cuota} lo debes pagar en {num_cuotas} cuotas y el monto total a pagar es : {monto_total}")