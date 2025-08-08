import os

ruta_archivo = "C:/Users/saul.frias/PycharmProjects/SeleniumProject/introduccion/imagen/pega.png"

if os.path.isfile(ruta_archivo):
    print("✅ El archivo existe")
else:
    print("❌ Archivo NO encontrado")