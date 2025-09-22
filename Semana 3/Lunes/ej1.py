notas = [10,16,20,16,6,7,8,3,4,6,2,10,16,20,16,6,7,8,3,4,6,2,10,16,20,16,6,7,8,3,4,6,2,10,16,20,16,6,7,8,3,4,6,2,10,16,20,16,6,7,8,3,4,6,2]
avg = 0
total = 0
cont_aprobados = 0
cont_reprobados = 0
for estudiante in notas:
    total += estudiante
    if estudiante >= 10:
        cont_aprobados += 1
    else:
        cont_reprobados += 1
if len(notas) > 0:
    avg = total / len(notas)

print("************* RESULTADOS *************")
print(f"Promedio: {avg}")
print(f"Aprobados: {cont_aprobados}")
print(f"Reprobados: {cont_reprobados}")