#Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

NumTotalPagar = 0
descuento = 0

while True:
    monto = float(input("Digite el monto de la factura (Digite 0 para finalizar): "))
    
    if monto == 0:
        break

    NumTotalPagar += monto

if NumTotalPagar > 1000:
    descuento = NumTotalPagar * 0.1
    NumTotalPagar -= descuento

print(f"Monto total a pagar: $ {NumTotalPagar}")
print(f"Total de descuento aplicado: $ {descuento}")