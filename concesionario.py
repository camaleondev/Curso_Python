from datetime import datetime


# =========================
# CLASE BASE: VEHICULO
# =========================
class Vehiculo:
    def __init__(self, codigo, marca, modelo, anio, precio):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Vendido"
        return f"[{self.codigo}] {self.marca} {self.modelo} ({self.anio}) - ${self.precio:,.2f} - {estado}"


# =========================
# HERENCIA: AUTO
# =========================
class Auto(Vehiculo):
    def __init__(self, codigo, marca, modelo, anio, precio, puertas):
        super().__init__(codigo, marca, modelo, anio, precio)
        self.puertas = puertas

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Tipo: Auto | Puertas: {self.puertas}"


# =========================
# HERENCIA: MOTO
# =========================
class Moto(Vehiculo):
    def __init__(self, codigo, marca, modelo, anio, precio, cilindrada):
        super().__init__(codigo, marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Tipo: Moto | Cilindrada: {self.cilindrada}cc"


# =========================
# CLASE CLIENTE
# =========================
class Cliente:
    def __init__(self, id_cliente, nombre, presupuesto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.vehiculos_comprados = []

    def ver_presupuesto(self):
        return (
            f"Cliente: {self.nombre} | Presupuesto disponible: ${self.presupuesto:,.2f}"
        )

    def comprar_vehiculo(self, vehiculo):
        if self.presupuesto >= vehiculo.precio:
            self.presupuesto -= vehiculo.precio
            self.vehiculos_comprados.append(vehiculo)
            return True
        return False

    def mostrar_compras(self):
        if not self.vehiculos_comprados:
            return f"{self.nombre} no ha comprado vehículos."

        compras = "\n".join([v.mostrar_info() for v in self.vehiculos_comprados])
        return f"Vehículos comprados por {self.nombre}:\n{compras}"


# =========================
# CLASE TRANSACCION
# =========================
class Transaccion:
    def __init__(self, tipo, vehiculo, cliente=None):
        self.tipo = tipo  # "COMPRA_STOCK" o "VENTA"
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.fecha = datetime.now()

    def mostrar_transaccion(self):
        if self.tipo == "COMPRA_STOCK":
            return f"{self.fecha} | COMPRA DE STOCK | {self.vehiculo.mostrar_info()}"
        elif self.tipo == "VENTA":
            return f"{self.fecha} | VENTA | Cliente: {self.cliente.nombre} | {self.vehiculo.mostrar_info()}"


# =========================
# CLASE PRINCIPAL: CONCESIONARIA
# =========================
class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.historial_transacciones = []

    def agregar_vehiculo(self, vehiculo):
        self.inventario.append(vehiculo)
        transaccion = Transaccion("COMPRA_STOCK", vehiculo)
        self.historial_transacciones.append(transaccion)
        print(f"Vehículo agregado al inventario: {vehiculo.mostrar_info()}")

    def mostrar_vehiculos_disponibles(self):
        disponibles = [v for v in self.inventario if v.disponible]
        if not disponibles:
            print("No hay vehículos disponibles en este momento.")
            return

        print(f"\nVehículos disponibles en {self.nombre}:")
        for vehiculo in disponibles:
            print(vehiculo.mostrar_info())

    def buscar_vehiculo_por_codigo(self, codigo):
        for vehiculo in self.inventario:
            if vehiculo.codigo == codigo and vehiculo.disponible:
                return vehiculo
        return None

    def vender_vehiculo(self, codigo, cliente):
        vehiculo = self.buscar_vehiculo_por_codigo(codigo)

        if not vehiculo:
            print("Vehículo no encontrado o ya fue vendido.")
            return

        if cliente.comprar_vehiculo(vehiculo):
            vehiculo.disponible = False
            transaccion = Transaccion("VENTA", vehiculo, cliente)
            self.historial_transacciones.append(transaccion)
            print("\n✅ Venta realizada con éxito.")
            print(f"{cliente.nombre} compró: {vehiculo.mostrar_info()}")
        else:
            print(
                f"\n❌ {cliente.nombre} no tiene presupuesto suficiente para comprar este vehículo."
            )

    def mostrar_historial(self):
        if not self.historial_transacciones:
            print("No hay transacciones registradas.")
            return

        print(f"\nHistorial de transacciones de {self.nombre}:")
        for t in self.historial_transacciones:
            print(t.mostrar_transaccion())


# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
    # Crear concesionaria
    concesionaria = Concesionaria("AutoMundo")

    # Agregar vehículos al inventario (compra de stock)
    auto1 = Auto("A001", "Toyota", "Corolla", 2022, 85000, 4)
    auto2 = Auto("A002", "Mazda", "CX-5", 2023, 120000, 4)
    moto1 = Moto("M001", "Yamaha", "MT-03", 2021, 32000, 321)

    concesionaria.agregar_vehiculo(auto1)
    concesionaria.agregar_vehiculo(auto2)
    concesionaria.agregar_vehiculo(moto1)

    # Crear cliente
    cliente1 = Cliente("C001", "Miguel", 130000)

    # Mostrar presupuesto del cliente
    print("\n" + cliente1.ver_presupuesto())

    # Mostrar vehículos disponibles
    concesionaria.mostrar_vehiculos_disponibles()

    # Cliente compra un vehículo
    concesionaria.vender_vehiculo("A001", cliente1)

    # Mostrar presupuesto actualizado
    print("\n" + cliente1.ver_presupuesto())

    # Mostrar compras del cliente
    print("\n" + cliente1.mostrar_compras())

    # Mostrar vehículos disponibles luego de la venta
    concesionaria.mostrar_vehiculos_disponibles()

    # Mostrar historial de transacciones
    concesionaria.mostrar_historial()
