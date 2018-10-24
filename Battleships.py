import string


class Ship:
    def __init__(self, size, name):
        self.size = size
        self.lives = size
        self.position = []
        self.name = name

    @staticmethod
    def __find_x(position):
        alpha = list(string.ascii_lowercase)
        return alpha.index(position[0])

    @staticmethod
    def __find_y(position):
        posy = int(position[-1])
        return posy if posy > 0 else 10

    def set_position(self, position):
        pos_x = Ship.__find_x(position)
        pos_y = Ship.__find_y(position)
        while True:
            orientation = input("Vertical or horizontal: v/h?")
            if orientation == "v":
                for i in range(self.size):
                    self.position.append([pos_x, pos_y + i])
                break
            elif orientation == "h":
                for i in range(self.size):
                    self.position.append([pos_x + i, pos_y])
                break

    def is_hit(self, position):
        hit_pos = [self.__find_x(position), self.__find_y(position)]
        if hit_pos in self.position:
            self.hit(hit_pos)
            return True
        else:
            return False

    def hit(self, position):
        self.lives -= 1
        self.position.remove(position)


class Destroyer(Ship):
    def __init__(self):
        Ship.__init__(self, 2, "Destroyer")


class Cruiser(Ship):
    def __init__(self):
        Ship.__init__(self, 3, "Cruiser")


class Submarine(Ship):
    def __init__(self):
        Ship.__init__(self, 3, "Submarine")


class Battleship(Ship):
    def __init__(self):
        Ship.__init__(self, 4, "Battleship")


class Carrier(Ship):
    def __init__(self):
        Ship.__init__(self, 5, "Carrier")


class BattleShips:
    def __init__(self):
        self.p1_ships = [Destroyer(), Submarine(), Cruiser(), Battleship(), Carrier()]
        self.p2_ships = [Destroyer(), Submarine(), Cruiser(), Battleship(), Carrier()]
        self.p1_history = []
        self.p2_history = []
        self.grid = []
        for i in range(1, 11):
            for a in string.ascii_lowercase:
                self.grid.append(a + str(i))
                if a == "j":
                    break

    def __set_positions(self, ships):
        for ship in ships:
            pos_valid = False
            while pos_valid == False:
                pos = ""
                while pos not in self.grid:
                    pos = input("Please enter the position for your " + str(ship.name) + " (Top-Left point): ")
                ship.set_position(pos)
                if self.check_ships(ships):
                    pos_valid = True
                else:
                    print("Ship position is not unique!!!")

    @staticmethod
    def check_ships(ships):
        positions = []
        for ship in ships:
            for pos in ship.position:
                if pos in positions:
                    return False
                positions.append(pos)
        return True

    def shoot(self, player):
        position = input("Please choose a position between A1 and J10: ").lower().strip()
        if player == "p1":
            while position in self.p1_history:
                print("You've already shot there!")
                position = input("Please choose a position between A1 and J10: ").lower().strip()
            self.p1_history.append(position)
            for ship in self.p1_ships:
                if ship.is_hit(position):
                    if ship.lives == 0:
                        self.p1_ships.remove(ship)
                        print("You sunk my", ship.name + "!")
                    return True
            return False
        else:
            while position in self.p2_history:
                print("You've already shot there!")
                position = input("Please choose a position between A1 and J10: ").lower().strip()
            self.p2_history.append(position)
            for ship in self.p2_ships:
                if ship.is_hit(position):
                    if ship.lives == 0:
                        self.p2_ships.remove(ship)
                        print("You sunk my", ship.name + "!")
                    return True
            return False

    def play(self):
        self.__set_positions(self.p1_ships)
        self.__set_positions(self.p2_ships)
        while len(self.p1_ships) > 0 and len(self.p2_ships) > 0:
            if self.shoot("p1"):
                print("Hit!")
            else:
                print("Miss!")
            if self.shoot("p2"):
                print("Hit!")
            else:
                print("Miss!")
        if len(self.p1_ships) == 0:
            print("Player 2 wins!!!")
        else:
            print("Player 1 wins!!!")


game = BattleShips()
game.play()
