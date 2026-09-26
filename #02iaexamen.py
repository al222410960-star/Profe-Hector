import random

# ==========================================================
# DATOS DEL USUARIO

print("=" * 55)
print("       SISTEMA DE DIAGNÓSTICO TÉCNICO - BIENVENIDA")
print("=" * 55)

nombre = input("Ingrese su nombre completo: ")
direccion = input("Ingrese su dirección: ")

print("\nSeleccione el tipo de equipo:")
print("1. PC")
print("2. Laptop")
print("3. Servidor")
print("4. Tablet")

opcion = input("Opción (1-4): ")
tipos_equipo = {"1": "PC", "2": "Laptop", "3": "Servidor", "4": "Tablet"}
tipo_equipo = tipos_equipo.get(opcion, "Equipo Desconocido")


numero_reporte = f"REP-{random.randint(10000, 99999)}"

# ==========================================================
# DIAGNÓSTICO BÁSICO DEL EQUIPO

print("\n--- CUESTIONARIO DE DIAGNÓSTICO ---")
electricidad = input("¿Tiene electricidad? (s/n): ").strip().lower() == "s"
enciende = input("¿Enciende? (s/n): ").strip().lower() == "s"
imagen = input("¿Muestra imagen? (s/n): ").strip().lower() == "s"
sistema = input("¿Carga el sistema operativo? (s/n): ").strip().lower() == "s"
sonido = input("¿Tiene sonido? (s/n): ").strip().lower() == "s"
internet = input("¿Tiene internet? (s/n): ").strip().lower() == "s"

# ==========================================================
# IMPRESIÓN DEL REPORTE FINAL

print("\n" + "=" * 55)
print("             REPORTE DE DIAGNÓSTICO")
print("=" * 55)
print(f"Bienvenido(a), {nombre}!")
print(f"Número de Reporte : {numero_reporte}")
print(f"Dirección         : {direccion}")
print(f"Tipo de Equipo    : {tipo_equipo}")
print("-" * 55)

if not electricidad:
    print("Diagnóstico: revisar alimentación.")
elif not enciende:
    print("Diagnóstico: revisar fuente de poder.")
elif not imagen:
    print("Diagnóstico: revisar monitor.")
elif not sistema:
    print("Diagnóstico: revisar disco duro.")
elif not internet:
    print("Diagnóstico: revisar conexión red.")
else:
    print("Diagnóstico: funcionamiento básico correcto.")

print("=" * 55) 

