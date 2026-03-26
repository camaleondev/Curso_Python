def recibir_empleados(lista_empleados):  # recibe un diccionario de empleados
    return lista_empleados


def empleados_con_sueldo_mayor(lista_empleados, sueldo_minimo):
    return [
        empleado for empleado in lista_empleados if empleado["salary"] >= sueldo_minimo
    ]


# Ejemplo de uso
empleados = recibir_empleados(
    [
        {"name": "Ana", "age": 28, "salary": 2500},
        {"name": "Luis", "age": 35, "salary": 3200},
        {"name": "Carlos", "age": 40, "salary": 1800},
        {"name": "Marta", "age": 30, "salary": 4000},
    ]
)

filtrados = empleados_con_sueldo_mayor(empleados, 2000)

print(filtrados)
