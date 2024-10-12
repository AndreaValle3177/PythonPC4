path = "/workspaces/PythonPC4/temperaturas.txt"
with open(path, mode='r') as file:
    lineas = file.readlines()
print (lineas)

temperaturas = []
for linea in lineas:

    _, temperatura= linea.strip().split(',')
   
    temperatura = float(temperatura)

   
    temperaturas.append(temperatura)
print (temperaturas)

temperatura_max = max(temperaturas)
temperatura_min = min(temperaturas)
temperatura_promedio = sum(temperaturas)/len(temperaturas)

print(f'Temperatura máxima: {temperatura_max}')
print(f'Temperatura mínima: {temperatura_min}')
print(f'Temperatura promedio: {temperatura_promedio:.2f}')

with open('resumen_temperaturas.txt', mode='w') as file:
    file.write(f'Temperatura máxima: {temperatura_max}\n')
    file.write(f'Temperatura mínima: {temperatura_min}\n')
    file.write(f'Temperatura promedio: {temperatura_promedio:.2f}\n')
