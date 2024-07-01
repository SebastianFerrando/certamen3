import os

menu = '''
1.Registrar pedido
2.Listar todos los pedidos
3.Imprimir lista de pedidos
4.Salir\n'''

marca = ['toyota', 'ford', 'chevrolet']

reg_orden = []

orden = '''
                                                            RESUMEN DE PEDIDOS                  
______________________________________________________________________________________________________________________________________________
|MARCA              | AÑO DE FABRICACION             | KILOMETRAJE            | COSTO DE REPARACION   | IMPUESTO DE SERVICIO(8%)    | TOTAL  |
______________________________________________________________________________________________________________________________________________
'''

def pedidos():
    while (True):
        try:
            print("Servicio para toyota, ford y chevrolet: \n") 
            mar = input("Ingrese marca del vehiculo: ")
            fab = int(input("Ingrese año de fabricacion: "))
            kil = int(input("Ingrese kilometraje: "))
            cost = int(input("Ingrese costo: "))
            imp = round(cost*0.08)
            total = cost+imp
            reg_orden.append([mar, fab, kil, cost, imp, total])
            input("El pedido a sido registrado correctamente!")
            print(reg_orden)
            break
        except:
            input("Excepscion al registrar")

def listar():
    print(orden)
    agr=orden
    for i in reg_orden:
        agr += f"{i[0]:15s}"
        agr += f"{i[1]:30d}"
        agr += f"{i[2]:15d}"
        agr += f"{i[3]:15d}"
        agr += f"{i[4]:10d}"
        agr += f"{i[5]:10d}"
        agr += "\n"
    return agr

def imprimir():
    s = input(f"Todos/{marca}: ").strip().lower()
    if s == "todos":
        with open ("Todos.txt","w") as archivo:
            archivo.write(listar())
    elif s in marca:
        with open ("Todos.txt","w") as archivo:
            archivo.write(listar(s))
    input("Archivo creado con exito")


while (True):    
        os.system("cls")
        op = input(menu)
        if op == "1":
            pedidos()
        elif op == "2":
            print(listar())
            input("")
        elif op == "3":
            imprimir()
        elif op == "4":
            break
        else:
            input("Ingrese opcion valida!")
