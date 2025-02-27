game_board = [['-'for _ in range(3)]for _ in range (3)]#Создание игрового поля
def print_gameboard():#Вывод игрового поля в консоль
  columns="  A B C"
  print (columns)
  for i ,row in enumerate(game_board,start=1):
      print(i,' '.join(row))

print_gameboard()

game_board = [['-' for _ in range(3)] for _ in range(3)]  # Создание игрового поля


def print_gameboard():  # Вывод игрового поля в консоль
    columns = "  A B C"
    print(columns)
    for i, row in enumerate(game_board, start=1):
        print(i, ' '.join(row))


def winner():  # Проверка на победителя
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != "-":
            return game_board[0][i]
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != "-":
            return game_board[i][0]

    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "-":
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "-":
        return game_board[0][2]

    return None


# Выбор знаков
player1 = input("Игрок 1, выберите знак X или O: ").upper()
if player1 not in ['X', 'O']:
    print("Ошибка! Запустите игру заново!")
    exit()

player2 = "O" if player1 == "X" else "X"
print(f'Игрок 2, ваш знак: {player2}')
print("Начинает Игрок 1:")

columns = {"A": 0, "B": 1, "C": 2}  # Соответствие букв столбцов к индексам


def make_move(player):  # Ход игрока и проверки введенных данных
    while True:
        cord = input(f"Игрок {player}, введите координаты (например, A3): ")

        if len(cord) != 2 or cord[0] not in columns or not cord[1].isdigit():
            print("Ошибка! Введите корректные координаты!")
            continue

        row = int(cord[1]) - 1
        col = columns[cord[0]]

        if game_board[row][col] == '-':  # Проверяем, пустая ли клетка
            game_board[row][col] = player
            break  # Выходим из цикла после успешного хода
        else:
            print("Клетка уже занята! Пожалуйста, выберите другую.")


def game():
    current_player = player1
    while True:
        make_move(current_player)  # Игрок делает ход
        print_gameboard()  # Выводим поле

        winner_symbol = winner()  # Проверяем победителя
        if winner_symbol:
            print(f"Победитель — {winner_symbol}!")
            break

        if all(cell != '-' for row in game_board for cell in row):  # Проверка на ничью
            print("Ничья!")
            break

        current_player = player1 if current_player == player2 else player2  # Смена игрока


# Запуск игры
print_gameboard()
game()

player1= input("Игрок 1,Выбирете знак X или O: ").upper()#Инициализация игрока и выбор знака
if player1 not in ['X','O']:
    print("Ошибка! Запустите игру заново!")
    exit()
player2= "O" if player1 == "X" else "X"
print(f'Игрок 2,Ваш знак:  {player2}')
print("Начинает Игрок 1:")
columns = {"A": 0, "B": 1, "C": 2}
def make_move(player):#Ход игрока и проверки введенных данных
    while True:
        cord = input(f"Игрок {player}, Введите координаты (например,A3): ")  # Запрос на получения координат для расположеня знака на игровом поле

        if len(cord)!=2 or cord[0] not in columns or not cord[1].isdigit():#Проверяем введены ли верные координаты
            print("Ошибка!Введите корректные координаты!")
            continue
        row = int(cord[1]) - 1
        col = columns[cord[0]]

        if game_board[row][col] == '-':  # Проверка действительно ли введные координаты пустые
            game_board[row][col] = player
        else:
            print("Клетка уже занята! Пожалуйста выберите другую.")
def game():
    current_player=player1
    while True:
        make_move(current_player)
        print_gameboard()
        winner_symbol=winner()
        if winner_symbol:
            print(f"Победитель-{winner_symbol}!")
            break
        if all(cell !='-' for row in game_board for cell in row):
            print("Ничья!")
            break
        current_player = player1 if current_player == player2 else player2
print_gameboard()#Запуск игры
game()



