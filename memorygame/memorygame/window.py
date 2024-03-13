import PySimpleGUI as sg
import random
import sqlite3

DB_FILE = "mydata.db"

def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS games
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, term TEXT, explanation TEXT)''')
    conn.commit()
    conn.close()

def save_game_to_database(game_data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO games (term, explanation) VALUES (?, ?)", game_data)
    conn.commit()
    conn.close()

def load_game_from_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT term, explanation FROM games")
    games = cursor.fetchall()
    conn.close()
    return games

def run_memory_game(game_data):
    random.shuffle(game_data)
    revealed = [False] * len(game_data)
    matched = set()
    tries = 0

    game_layout = [[sg.Button(" ", size=(20, 2), key=(i, j)) for j in range(2)] for i in range(len(game_data))]
    game_window = sg.Window("Memory Game", game_layout)

    while True:
        event, values = game_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Exit":
            game_window.close()
            return

        row, col = event

        if (row, col) in matched or revealed[row]:
            continue

        game_window[event].update(game_data[row][col])
        revealed[row] = True

        if len(matched) < len(game_data) // 2:
            if len(matched) == 0 or game_data[row][0] not in [x[0] for x in game_data[list(matched)]]:
                matched.add(row)
            else:
                for r in matched:
                    game_window[(r, 0)].update(" ")
                    game_window[(r, 1)].update(" ")
                matched.remove(row)
                tries += 1

        game_window["-OUTPUT-"].update(f"Tries: {tries}")

    game_window.close()

def main():
    create_database()

    layout = [
        [sg.Text("Enter term:"), sg.Input(key="-TERM-")],
        [sg.Text("Enter explanation:"), sg.Input(key="-EXPLANATION-")],
        [sg.Text("Number of cards:"), sg.Input(key="-NUM_CARDS-")],
        [sg.Button("Add Card"), sg.Button("Start Game"), sg.Button("Exit")]
    ]

    window = sg.Window("Memory Game", layout)

    game_data = []

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Add Card":
            term = values["-TERM-"]
            explanation = values["-EXPLANATION-"]
            if term and explanation:
                game_data.append((term, explanation))
                window["-TERM-"].update("")
                window["-EXPLANATION-"].update("")
                window["-NUM_CARDS-"].update(len(game_data))

        if event == "Start Game":
            num_cards = int(values["-NUM_CARDS-"])
            if num_cards > 0:
                run_memory_game(game_data[:num_cards])

    save_game_to_database(game_data)
    window.close()

if __name__ == "__main__":
    main()
