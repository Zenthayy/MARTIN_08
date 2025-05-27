asignaturas = ["Matematicas", "Ffsica", "Quqmica", "Historia", "Lengua"]
repetir = []

for i in range(len(asignaturas)):
    nota = float(input(f"¿Qué nota has sacado en {asignaturas[i]}? "))
    if nota < 5:
        repetir.append(asignaturas[i])

print("\nTienes que repetir las siguientes asignaturas:")
for asignatura in repetir:
    print(asignatura)