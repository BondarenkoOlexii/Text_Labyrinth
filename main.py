# Абстрактна фабріка, сінглентон, проксі

import json
import os

Labyrinth = [
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
    ["S", ".", ".", "|", ".", ".", ".", "|", ".", ".", ".", ".", ".", "|", ".", "|"],
    ["|", "|", ".", "|", ".", "|", "|", "|", ".", ".", "|", ".", ".", "|", ".", "|"],
    ["|", ".", ".", "|", ".", ".", "|", ".", ".", ".", "|", "|", ".", ".", ".", "|"],
    ["|", ".", "|", "|", "|", ".", "|", ".", "|", ".", "|", ".", ".", ".", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", ".", "|", ".", "|", "|", "|", "|", ".", "|"],
    ["|", "|", "|", ".", "|", "|", "|", ".", "|", ".", ".", ".", ".", ".", ".", "|"],
    ["|", ".", "|", ".", "|", ".", ".", ".", "|", "|", "|", "|", "|", "|", "|", "|"],
    ["|", ".", ".", ".", "|", ".", "|", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
    ["|", "|", "|", "|", "|", ".", "|", "|", ".", ".", "|", "|", "|", "|", ".", "|"],
    ["|", ".", ".", ".", ".", ".", "|", "|", "|", ".", ".", "|", ".", ".", ".", "|"],
    ["|", ".", "|", "|", "|", "|", "|", ".", ".", ".", ".", "|", ".", "|", "|", "|"],
    ["|", ".", "|", ".", ".", ".", "|", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
    ["|", ".", "|", ".", "|", "|", "|", "|", "|", ".", "|", "|", ".", "|", ".", "|"],
    ["|", ".", "|", ".", "|", ".", ".", "|", "|", "|", "|", ".", ".", "|", ".", "|"],
    ["|", ".", "|", ".", "|", ".", ".", "|", "|", ".", "|", ".", "|", "|", ".", "|"],
    ["|", ".", "|", ".", ".", "|", ".", "|", "|", ".", ".", ".", ".", "|", ".", "|"],
    ["|", ".", "|", "|", ".", "|", ".", "|", "|", "|", "|", "|", ".", "|", "|", "|"],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", "E"],
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
]


def clear_console():
    print('\n' * 50)  # Імітація очищення


class JSON:
    def __init__(self, json_file):
        self.json = json_file

    def write_info(self, key, value):
        data = {}
        if os.path.exists(self.json):
            with open(self.json, 'r') as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {}

        data[key] = value

        with open('walk_info.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def read_info(self):
        default_value = (1, 1)
        default_next_key = 0
        with open('walk_info.json', 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                return default_value, default_next_key
            if not data:
                return default_value, default_next_key

            last_key = list(data.keys())[-1]
            last_value = data[last_key]
            next_key = int(last_key) + 1
        return last_value, next_key  # отримуємо значення і наступний ключ для пробігу по позиціям

    def clear(self):
        with open('walk_info.json', 'w') as json_file:
            json.dump({}, json_file)


class Mase:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])

    def is_wall(self, x, y):
        return self.matrix[y][x] == "|"


class ShowMase:
    def __init__(self, matrix, current_player_pos):
        self.matrix = matrix
        self.player = current_player_pos

    def show_labirinth(self):
        for y in range(len(self.matrix)):

            row = ""

            for x in range(len(self.matrix[y])):
                if (x, y) == (0, 1):
                    row += "S  "

                elif (x, y) == (15, 18):
                    row += "E  "

                elif (x, y) == (self.player.x, self.player.y):
                    row += "P  "

                elif self.matrix[y][x] == "|":
                    row += "|  "

                else:
                    row += ".  "

            print(row)


class Player:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def move(self, direction):
        match direction:
            case "w":
                self.y -= 1
            case "s":
                self.y += 1
            case "a":
                self.x -= 1
            case "d":
                self.x += 1

    def position(self):
        return self.x, self.y


class Game:
    def __init__(self, maze, player):
        self.maze = maze
        self.player = player
        self.current_step = 0
        self.prev_all_position = []

    def move(self, directory):
        self.prev_all_position.append(self.player.position())
        json_file.write_info(key_for_json, self.prev_all_position[-1])
        self.player.move(directory)
        new_pos = self.player.position()

        if new_pos in self.prev_all_position:
            print("Шарік злякався і втік, гра завершена")
            return False
        elif maze.is_wall(new_pos[0], new_pos[1]):
            print("Шарік вдарився об стіну, гра завершена")
            return False
        print("Шарік знайшов правильний шлях")
        return True


maze = Mase(Labyrinth)

optimal_path = [[1, 1], [2, 1], [2, 2], [2, 3], [1, 3], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5],
                [7, 6], [7, 7], [7, 8],
                [8, 8], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [14, 9], [14, 10], [13, 10], [12, 10],
                [12, 11], [12, 12], [12, 13],
                [12, 14], [11, 14], [11, 15], [11, 16], [12, 16], [12, 17], [12, 18], [13, 18], [14, 18], [15, 18]]

player = None

json_file = JSON("walk_info.json")

start_x, start_y = 1, 1

key_for_json = 0

check_move = 0

game_on = True

exit_x = 14
exit_y = 18

start_input = input("Ти хочеш продовжити з моменту де закінчив чи почати усе з початку? Y/N").strip().lower()

if start_input == "y":
    start_position, next_index = json_file.read_info()
    next_index -= 1
    if start_position != (1, 1) or next_index > 0:
        start_x, start_y = start_position
        key_for_json = next_index
        check_move = next_index
    else:
        json_file.clear()
else:
    json_file.clear()

player = Player(start_x, start_y)
game = Game(maze, player)

while game_on:
    clear_console()
    maze_view = ShowMase(Labyrinth, player)
    maze_view.show_labirinth()

    direction = input("Введи напрямок").strip().lower()

    if direction in ["w", "s", "a", "d"]:
        current_x, current_y = player.position()

        if current_x == exit_x and current_y == exit_y:
            print("Вітаємо з перемогою")
            json_file.clear()
            break

        game_on = game.move(direction)

        last_move, _ = json_file.read_info()
        if last_move == optimal_path[check_move]:
            key_for_json += 1
            check_move += 1
        else:
            print("Ти пішов не по оптимальному маршруту")
            print(last_move)
            game_on = False

    else:
        print("Ви не вмієте ходити")
