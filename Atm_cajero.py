"""Es un ejercicio basico en python
Aautor:pitt"""
import time
from tqdm import tqdm
print("\n              -------------------------------------------------------------INGRESANDO AL SISTEMA DE ATM-------------------------------------------------------------\n")
for i in tqdm(range(100)):
    time.sleep(0.1)

saldo=1000.0
ciclo=True
aux=1
contra="123456789"
reporte=[]
reporte_soles=[]
while ciclo:
    while aux==1:
        try:
            print("\n********************MENU********************")
            print("1 ---> Depositar en la cuenta")
            print("2 ---> Retirar dinero de la cuenta")
            print("3 ---> Visualizar dinero disponible")
            print("4 ---> Cambiar la contraseña")
            print("5 ---> Reporte de la cuenta")
            print("6 ---> Salir")
            opcion=int(input("Digite la opcion a realizar\n>"))
            aux=0
        except ValueError:
            print("\n---------------------------------")
            print("            OPCION")
            print("           INVALIDA")
            print("        (SOLO NUMEROS)")
            print("---------------------------------")
    aux=1
    if opcion==1:
        while aux==1:
            try:
                print("OPCION 1:-----------------------------------")
                dinner_extra=float(input("Digite el dinero a depositar\nS/."))
                if dinner_extra>0:
                    saldo+=dinner_extra
                    reporte.append("Deposito")
                    reporte_soles.append(dinner_extra)
                    print("       ----------------    ")
                    print("         Deposito de    ")
                    print("         S/.",dinner_extra)
                    print("          EXITOSO    ")
                    print("       ----------------    ")
                    aux=0
                else:
                    print("\n---------------------------------")
                    print("            INGRESO")
                    print("            INVALIDO")
                    print(" (El monto debe ser mayor que 0)")
                    print("---------------------------------") 
            except ValueError:
                print("\n---------------------------------")
                print("            OPCION")
                print("           INVALIDA")
                print("        (SOLO NUMEROS)")
                print("---------------------------------")
        aux=1
    elif opcion==2:
        print("OPCION 2:-----------------------------------")
        while aux==1:
            aux_contra=input("Digite la 'CONTRASEÑA' para retirar\n>")

            if aux_contra== contra:
                aux=0
            else:
                print("       -------------------------    ")
                print("         Contraseña incorrecta         ")
                print("       -------------------------    ")
        aux=1
        print("\n              -------------------------------------------------------------INGRESANDO A LA CUENTA-------------------------------------------------------------\n")
        for i in tqdm(range(100)):
            time.sleep(0.05)

        print("               --------------------------------------------------------------------------------------------------------------------------------------------------\n")
        while aux==1:
            try:
                monto_retiro=float(input("Digite el monto a retirar\nS/."))
                if monto_retiro>0:
                    if monto_retiro>saldo:
                        print("       ------------------------------    ")
                        print("         No tienes saldo suficiente")
                        print("           para retirar ese monto.")
                        print("       ------------------------------    ")
                    else:
                        saldo=saldo-monto_retiro
                        reporte.append("Retiro")
                        reporte_soles.append(monto_retiro)
                        print("       ----------------    ")
                        print("         Retiro de    ")
                        print("         S/.",monto_retiro)
                        print("          EXITOSO    ")
                        print("       ----------------    ")
                    aux=0
                else:
                    print("\n---------------------------------")
                    print("            INGRESO")
                    print("            INVALIDO")
                    print(" (El monto debe ser mayor que 0)")
                    print("---------------------------------")
            except ValueError:
                print("\n---------------------------------")
                print("            OPCION")
                print("           INVALIDA")
                print("        (SOLO NUMEROS)")
                print("---------------------------------")
        aux=1
    elif opcion==3:
        print("OPCION 3:-----------------------------------")
        print("     ---------------------------")
        print("         Tienes un saldo de")
        print("           S/.",saldo)
        print("            DISPONIBLE")
        print("     ---------------------------")
    elif opcion==4:
        print("OPCION 4:-----------------------------------")
        while aux==1:
            contra_nueva=input("Digite la contraseña nueva\n>")
            if contra_nueva==contra:
                print("         --------------------")
                print("            La contraseña")
                print("             es la misma")
                print("           que la anterior")
                print("         --------------------")
            elif contra_nueva != contra:
                contra=contra_nueva
                print("         -----------------    ")
                print("         Operacion exitoso.")
                print("         -----------------    ")
                aux=0
        aux=1
    elif opcion==5:
        print("OPCION 5:-----------------------------------")
        cant=len(reporte_soles)
        for i in range (0,cant):
            print("S/.",reporte_soles[i],"------------------>",reporte[i])
        print("--------------------------------------------")
        print("SALDO TOTAL:           S/.",saldo)
    elif opcion==6:
        print("--------------------------------------------")
        print("         GRACIAS POR SU PREFERENCIA")
        print("              VUELVE PRONTO")
        print("--------------------------------------------")
        ciclo=False
    else:
        print("\n---------------------------------")
        print("            OPCION")
        print("           INVALIDA")
        print("             [1-6]")
        print("---------------------------------")
    



        

    

