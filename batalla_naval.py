import os


# =========================
# PASO 1: Clase Ship
# =========================
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []  # Lista de posiciones ocupadas por el barco
        self.hits = 0  # Cantidad de impactos recibidos

    def place_ship(self, board, start_row, start_col, direction):
        temp_positions = []

        # Verificar si cabe en el tablero
        if direction == "H":
            if start_col + self.size > 10:
                return False
            for i in range(self.size):
                if board[start_row][start_col + i] != " ":
                    return False
                temp_positions.append((start_row, start_col + i))

        elif direction == "V":
            if start_row + self.size > 10:
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != " ":
                    return False
                temp_positions.append((start_row + i, start_col))

        else:
            return False

        # Colocar el barco en el tablero
        for row, col in temp_positions:
            board[row][col] = self.name[0]  # Primera letra del nombre
        self.positions = temp_positions
        return True

    def hit(self):
        self.hits += 1
        return self.hits == self.size  # True si el barco fue hundido


# =========================
# PASO 2: Subclases de Ship
# =========================
class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destructor", 2)


class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarino", 3)


class Battleship(Ship):
    def __init__(self):
        super().__init__("Acorazado", 4)


# =========================
# PASO 3: Clase Player
# =========================
class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]  # Tablero propio
        self.ships = []  # Lista de barcos
        self.hits = [[" " for _ in range(10)] for _ in range(10)]  # Tablero de ataques

    def print_board(self, board_to_print, hide_ships=False):
        print("   " + " ".join(str(i) for i in range(10)))
        print("  +" + "--" * 10 + "+")

        for i, row in enumerate(board_to_print):
            display_row = []
            for cell in row:
                if hide_ships and cell not in ["X", "O", " "]:
                    display_row.append(" ")
                else:
                    display_row.append(cell)
            print(f"{i} |" + " ".join(display_row) + "|")

        print("  +" + "--" * 10 + "+")

    def place_ships(self):
        print(f"\n{self.name}, coloca tus barcos en el tablero.")
        ships_to_place = [Destroyer(), Submarine(), Battleship()]

        for ship in ships_to_place:
            placed = False
            while not placed:
                print(f"\nColocando {ship.name} (tamaño {ship.size})")
                self.print_board(self.board)

                try:
                    row = int(input("Ingresa la fila inicial (0-9): "))
                    col = int(input("Ingresa la columna inicial (0-9): "))
                    direction = input(
                        "Ingresa dirección (H para horizontal, V para vertical): "
                    ).upper()

                    if not (0 <= row < 10 and 0 <= col < 10):
                        print("❌ Posición fuera del tablero. Intenta de nuevo.")
                        continue

                    if ship.place_ship(self.board, row, col, direction):
                        self.ships.append(ship)
                        placed = True
                        print(f"✅ {ship.name} colocado correctamente.")
                    else:
                        print("❌ No se puede colocar ahí. Intenta de nuevo.")
                except ValueError:
                    print(
                        "❌ Entrada inválida. Debes ingresar números para fila y columna."
                    )

    def attack(self, opponent):
        print(f"\n{self.name}, es tu turno de atacar.")
        print("\nTu tablero de ataques:")
        self.print_board(self.hits)

        while True:
            try:
                row = int(input("Ingresa la fila a atacar (0-9): "))
                col = int(input("Ingresa la columna a atacar (0-9): "))

                if not (0 <= row < 10 and 0 <= col < 10):
                    print("❌ Posición fuera del tablero. Intenta de nuevo.")
                    continue

                # Ya atacó esa posición
                if self.hits[row][col] in ["X", "O"]:
                    print("❌ Ya atacaste esa posición. Elige otra.")
                    continue

                # Verificar si hay un barco
                if opponent.board[row][col] != " " and opponent.board[row][col] != "X":
                    print("💥 ¡Impacto!")
                    self.hits[row][col] = "X"
                    ship_symbol = opponent.board[row][col]
                    opponent.board[row][col] = "X"

                    # Buscar qué barco fue impactado
                    for ship in opponent.ships:
                        if (row, col) in ship.positions:
                            sunk = ship.hit()
                            if sunk:
                                print(f"🚢 ¡Has hundido el {ship.name}!")
                            break
                    break
                else:
                    print("🌊 Agua.")
                    self.hits[row][col] = "O"
                    if opponent.board[row][col] == " ":
                        opponent.board[row][col] = "O"
                    break

            except ValueError:
                print("❌ Entrada inválida. Debes ingresar números.")

    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships)


# =========================
# PASO 4: Clase BattleshipGame
# =========================
class BattleshipGame:
    def __init__(self):
        player1_name = input("Nombre del Jugador 1: ")
        player2_name = input("Nombre del Jugador 2: ")

        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def play(self):
        # Colocación de barcos
        self.clear_screen()
        self.player1.place_ships()
        input("\nPresiona Enter para continuar y ocultar el tablero...")
        self.clear_screen()

        self.player2.place_ships()
        input("\nPresiona Enter para comenzar la batalla...")
        self.clear_screen()

        # Turnos de juego
        current_player = self.player1
        opponent = self.player2

        while True:
            print("\n==============================")
            print(f"Turno de {current_player.name}")
            print("==============================")

            current_player.attack(opponent)

            # Verificar victoria
            if opponent.all_ships_sunk():
                print(f"\n🏆 ¡{current_player.name} ha ganado la partida!")
                print(f"\nTablero final de {opponent.name}:")
                opponent.print_board(opponent.board)
                break

            input("\nPresiona Enter para pasar el turno...")
            self.clear_screen()

            # Intercambiar jugadores
            current_player, opponent = opponent, current_player


# =========================
# PASO 5: Ejecutar el juego
# =========================
game = BattleshipGame()
game.play()
