import json
import sqlite3

import PySimpleGUI as sg


class CreatePack:
    def __init__(self):
        self.connection = sqlite3.connect("mydata.db")

    def create_card_pack(self, pack_name, cards):
        pack_data = json.dumps(cards)

        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO card_lists (pack_name, card_pack)
            VALUES (?, ?)
        """,
            (pack_name, pack_data),
        )
        self.connection.commit()
        self.connection.close()

pack = CreatePack()

def main():
    layout = [
        [sg.Text("Enter pack name:")],
        [sg.InputText(key="-PACK_NAME-")],
        [sg.Text("Enter card information (or type 'done' to finish):")],
        [
            sg.Text("Name:"),
            sg.InputText(key="-NAME-"),
            sg.Text("Definition:"),
            sg.InputText(key="-DEFINITION-"),
        ],
        [sg.Button("Add Card"), sg.Button("Create Pack")],
    ]

    window = sg.Window("Create Card Pack", layout)

    pack_name = ""
    cards = []

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Add Card":
            if values["-NAME-"] and values["-DEFINITION-"]:
                cards.append(
                    {"name": values["-NAME-"], "definition": values["-DEFINITION-"]}
                )

                window["-NAME-"].update("")
                window["-DEFINITION-"].update("")
        elif event == "Create Pack":
            pack_name = values["-PACK_NAME-"]
            pack.create_card_pack(pack_name, cards)
            sg.popup("Card pack created successfully!")
            break

    window.close()


if __name__ == "__main__":
    main()
