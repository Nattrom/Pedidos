import os
import time

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def animacion(texto, velocidad=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()


def pausa():
    animacion("\nPresione una tecla para continuar...", 0.03)
    input()


def titulo():
    limpiar()
    print("=" * 40)
    animacion("  ====== MENÚ SISTEMA DE PEDIDOS ======", 0.02)
    print("=" * 40)


def mostrar_menu():
    opciones = [
        "1 ► Registrar cliente",
        "2 ► Registrar producto",
        "3 ► Crear pedido",
        "4 ► Ver pedidos",
        "5 ► Ver ingresos",
        "6 ► Reporte final",
        "7 ► Salir"
    ]

    for opcion in opciones:
        print(opcion)
        time.sleep(0.3)
