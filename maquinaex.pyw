from tkinter import Tk, Label, Button, Entry, PhotoImage
import random
import os

maquina = Tk()
maquina.title("Maquina_Expendedora")
maquina.geometry("600x700+0+0")
maquina.config(bg="gray")

class Producto:
    def Pro():
        codigos = codigo.get()
        if codigos.strip(): 
            co = int(codigos)
            if co == 1701:
                precio = 12
            elif co == 1010:
                precio = 15
            elif co==1245:
                precio=17
            elif co==7654:
                precio=14
            elif co==8765:
                precio=16
            elif co==4532:
                precio=15
            elif co==8547:
                precio=18
            else:
                print("Código de producto no reconocido")
                precio = None
        else:
            precio = None
        return precio




class contenedor:
    def obtener_existencia():
        codi = codigo.get()
        if codi and codi.isdigit():
            cod = int(codi)
            if cod == 1701:
                try:
                    with open("existencia.txt", "r") as file:
                        exis = int(file.read())
                    print(exis)
                    return exis
                except FileNotFoundError:
                    print("")
                    with open("existencia.txt", "w") as file:
                        exis = random.randint(0,20)
                        file.write(str(exis))
                    return exis
            if cod == 1010:
                try:
                    with open("existencia_sabritas.txt", "r") as file:
                        exis_2 = int(file.read())
                    print(exis_2)
                    return exis_2
                except FileNotFoundError:
                    print("")
                    with open("existencia_sabritas.txt", "w") as file:
                        exis_2 = random.randint(0,20)
                        file.write(str(exis_2))
                    return exis_2
            if cod == 1245:
                try:
                    with open("existencia_gansito.txt", "r") as file:
                        exis_3 = int(file.read())
                    print(exis_3)
                    return exis_3
                except FileNotFoundError:
                    print("")
                    with open("existencia_gansito.txt", "w") as file:
                        exis_3 = random.randint(0,20)
                        file.write(str(exis_3))
                    return exis_3
            if cod == 7654:
                try:
                    with open("existencia_donas.txt", "r") as file:
                        exis_4 = int(file.read())
                    print(exis_4)
                    return exis_4
                except FileNotFoundError:
                    print("")
                    with open("existencia_donas.txt", "w") as file:
                        exis_4 = random.randint(0,20)
                        file.write(str(exis_4))
                    return exis_4
            if cod == 8765:
                try:
                    with open("existencia_doritos.txt", "r") as file:
                        exis_5 = int(file.read())
                    print(exis_5)
                    return exis_5
                except FileNotFoundError:
                    print("")
                    with open("existencia_doritos.txt", "w") as file:
                        exis_5 = random.randint(0,20)
                        file.write(str(exis_5))
                    return exis_5
            if cod == 4532:
                try:
                    with open("existencia_nito.txt", "r") as file:
                        exis_6 = int(file.read())
                    print(exis_6)
                    return exis_6
                except FileNotFoundError:
                    print("")
                    with open("existencia_nito.txt", "w") as file:
                        exis_6 = random.randint(0,20)
                        file.write(str(exis_6))
                    return exis_6
            if cod == 8547:
                try:
                    with open("existencia_takis.txt", "r") as file:
                        exis_7 = int(file.read())
                    print(exis_7)
                    return exis_7
                except FileNotFoundError:
                    print("")
                    with open("existencia_takis.txt", "w") as file:
                        exis_7 = random.randint(0,20)
                        file.write(str(exis_7))
                    return exis_7
            else:
                print("Código inválido o no ingresado")
                tex1.config(text="CODIGO")
                tex1.after(4000, lambda: tex1.config(text=""))
                tex3.config(text="NO")
                tex3.after(4000, lambda: tex3.config(text="BIENVENIDO"))
                tex4.config(text="VALIDO")
                tex4.after(4000, lambda: tex4.config(text=""))
    
    def obtener_producto():
        entrycred = credito.get()
        pre = Producto.Pro()
        pagado = 0
        if pre is not None:
            try:
                credi2 = int(entrycred)
                if credi2 >= pre:
                    print("Vendiendo")
                    pagado = 1
                else:
                    print("Crédito insuficiente")
                    tex1.config(text="CREDITO")
                    tex1.after(4000, lambda: tex1.config(text=""))
                    tex3.config(text="INSUFICIENTE")
                    tex3.after(4000, lambda: tex3.config(text="BIENVENIDO"))
                    pagado = 2
            except ValueError:
                print("El crédito ingresado no es válido")
        else:
            print("Código de producto no reconocido")
        return pagado
    
    def entrega_producto(b,e):
        compraexitosa=0
        if b ==1:
            if e>=1:
                print("Entregando Producto")
                tex3.config(text="Vendiendo")
                tex3.after(4000, lambda: tex3.config(text="BIENVENIDO"))
                compraexitosa=1
            else:
                print("Producto agotado")
                tex1.config(text="PRODUCTO")
                tex1.after(4000, lambda: tex1.config(text=""))
                tex3.config(text="AGOTADO")
                tex3.after(4000, lambda: tex3.config(text="BIENVENIDO"))
        return compraexitosa

    def actualizar_existencia(a, e):
        cod_2 = codigo.get()
        if cod_2.strip():
            try:
                codigo_2 = int(cod_2)
                if a == 1:
                    if codigo_2 == 1701:
                        e -= 1
                        with open("existencia.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de cocacola actualizada:", e)
                        producto_img.config(image=coca)
                    elif codigo_2 == 1010:
                        e -= 1
                        with open("existencia_sabritas.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de Sabritas actualizada:", e)
                        producto_img.config(image=sabritas)
                    elif codigo_2==1245:
                        e -= 1
                        with open("existencia_gansito.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de gansitos actualizada:", e)
                        producto_img.config(image=gansito)
                    elif codigo_2==7654:
                        e -= 1
                        with open("existencia_donas.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de donas actualizada:", e)
                        producto_img.config(image=donas)
                    elif codigo_2==8765:
                        e -= 1
                        with open("existencia_doritos.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de doritos actualizada:", e)
                        producto_img.config(image=doritos)
                    elif codigo_2==4532:
                        e -= 1
                        with open("existencia_nito.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de nito actualizada:", e)
                        producto_img.config(image=nito)
                    elif codigo_2==8547:
                        e -= 1
                        with open("existencia_takis.txt", "w") as file:
                            file.write(str(e))
                        print("Cantidad de takis actualizada:", e)
                        producto_img.config(image=takis)
                return e
            except ValueError:
                print("")
        else:
            print("")
        
class Cajon:
    def Credit(a,b):
        credi = credito.get()
        print("credito entregado", credi)
        cambio=0
        if a==1:
            cambio=int (credi)-b
            print("cambio",cambio)
        return cambio

def funciones(event):
    global cant1
    global a
    global b
    global c
    global e
    tex1.config(text="")
    tex3.config(text="")
    tex4.config(text="")
    prodctos = Producto.Pro()
    existencia = contenedor.obtener_existencia()
    resultado_obtener_producto = contenedor.obtener_producto()
    cantidad_entregada = contenedor.entrega_producto(resultado_obtener_producto,existencia)
    e = contenedor.actualizar_existencia(cantidad_entregada, existencia)
    cred = Cajon.Credit(cantidad_entregada,prodctos)
    tex2.config(text=cred)
    tex2.after(4000, lambda: tex2.config(text="CAMBIO"))
    producto_img.after(4000,lambda: producto_img.config(image=""))
    credito.delete(0)

def devolver():
    cre_3=credito.get()
    cre_4=int(cre_3)
    tex2.config(text=cre_4)
    credito.delete(0)
    tex2.after(4000, lambda: tex2.config(text="CAMBIO"))


if os.path.exists("existencia.txt"):
    os.remove("existencia.txt")
if os.path.exists("existencia_sabritas.txt"):
    os.remove("existencia_sabritas.txt")
if os.path.exists("existencia_gansito.txt"):
    os.remove("existencia_gansito.txt")
if os.path.exists("existencia_donas.txt"):
    os.remove("existencia_donas.txt")
if os.path.exists("existencia_doritos.txt"):
    os.remove("existencia_doritos.txt")
if os.path.exists("existencia_nito.txt"):
    os.remove("existencia_nito.txt")
if os.path.exists("existencia_takis.txt"):
    os.remove("existencia_takis.txt")  
hola = PhotoImage(file="maquina.gif")
imagen = Label(maquina, image=hola).place(x=0, y=0, height=700, width=600)
coca=PhotoImage(file="alely.png")
sabritas=PhotoImage(file="sabritas.png")
gansito=PhotoImage(file="gansito.png")
donas=PhotoImage(file="donas.png")
doritos=PhotoImage(file="doritos.png")
nito=PhotoImage(file="nito.png")
takis=PhotoImage(file="takis.png")


codigo = Entry(maquina, bg="white")
codigo.place(x=473, y=145, height=55, width=62)
credito = Entry(maquina, bg="gray")
credito.place(x=472, y=258, height=60, width=70)

Label(maquina, text="INGRESA CREDITO", bg="blue", fg="white", font="consolas 6 bold").place(x=472, y=238, height=20, width=70)

Label(maquina, text="1701-ALELY-$99999", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=380, height=20, width=84)
Label(maquina, text="1010-SABRITAS-$15", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=400, height=20, width=84)
Label(maquina, text="1245-GANSITO-$17", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=420, height=20, width=84)
Label(maquina, text="7654-DONAS-$14", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=440, height=20, width=84)
Label(maquina, text="8765-DORITOS-$16", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=460, height=20, width=84)
Label(maquina, text="4532-NITO-$15", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=480, height=20, width=84)
Label(maquina, text="8547-TAKIS-$18", bg="white", fg="black", font="consolas 7 bold").place(x=465, y=500, height=20, width=84)

Label(maquina, text="SOLO ADMITE BILLETES DE 20", bg="RED", fg="WHITE", font="consolas 10 bold").place(x=150, y=520, height=40, width=250)
a = Producto.Pro()
e = contenedor.obtener_existencia()
b = contenedor.obtener_producto()
c = contenedor.entrega_producto(b,e)
d = contenedor.actualizar_existencia(c, e)
f = Cajon.Credit(c,a)

tex1 = Label(maquina, text="")
tex1.place(x=473, y=65, height=20, width=62)
tex3 = Label(maquina, text="Bienvenido")
tex3.place(x=473, y=85, height=20, width=62)
tex4 = Label(maquina, text="")
tex4.place(x=473, y=105, height=20, width=62)

tex2 = Label(maquina, text="Cambio", font= "consolas 9 bold")
tex2.place(x=480, y=330, height=35, width=50)

producto_img=Label(maquina)
producto_img.place(x=120, y=590, height=80, width= 270)

bt1 = Button(maquina, text="COMPRAR", bg="white", fg="black", command=funciones)
bt1.place(x=473, y=200, height=25, width=62)

bt2 = Button(maquina, text="DEVOLVER", bg="blue", fg="black", command=devolver)
bt2.place(x=473, y=360, height=20, width=62)

credito.bind("<Up>",funciones)
codigo.bind("<Return>",funciones)
maquina.mainloop()