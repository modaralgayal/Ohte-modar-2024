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
        [sg.InputText(key="-PACK_NAME-", size=(30, 1))],
        [sg.Text("Enter card information")],
        [
            sg.Text("Name:"),
            sg.InputText(key="-NAME-", size=(20, 1), expand_x=True),
            sg.Text("Definition:"),
            sg.InputText(key="-DEFINITION-", size=(20, 1), expand_y=True),
        ],
        [sg.Button("Add Card"), sg.Button("Create Pack")],
        [sg.Text("Cards in Pack:")],
        [sg.Listbox(values=[], size=(45, 6), key="-CARD_LIST-")],
        [sg.Button("Remove Selected Card")],
    ]

    window = sg.Window("Create Card Pack", layout, size=(600, 350))

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
                window["-CARD_LIST-"].update(
                    values=[f"{card['name']}: {card['definition']}" for card in cards]
                )
        elif event == "Create Pack":
            pack_name = values["-PACK_NAME-"]
            pack.create_card_pack(pack_name, cards)
            sg.popup("Card pack created successfully!")
            break
        elif event == "Remove Selected Card":
            pass

    window.close()


if __name__ == "__main__":
    main()
