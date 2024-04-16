""" UI component for creating pack """
import PySimpleGUI as sg
from .services import HandlePacks


def create_pack_layout():
    """ UI of the pack creation """
    pack = HandlePacks()

    sg.theme("DarkGrey5")
    custom_font = ("Arial", 12)

    layout = [
        [sg.Text("Enter card(s) to study:", font=custom_font)],
        [
            sg.Text("Name:", font=custom_font),
            sg.InputText(key="-NAME-", size=(30, 1), font=custom_font),
            sg.Text("Definition:", font=custom_font),
            sg.InputText(key="-DEFINITION-", size=(30, 1), font=custom_font),
        ],
        [
            sg.Button("Add Card", size=(10, 1), font=custom_font),
            sg.Button("Create Pack", size=(10, 1), font=custom_font),
            sg.Button("Back To Menu", size=(10, 1), font=custom_font),
        ],
        [sg.Text("Cards in Pack:", font=custom_font)],
        [sg.Listbox(values=[], size=(60, 6), key="-CARD_LIST-", font=custom_font)],
        [
            sg.Text(
                "Enter pack name:", font=custom_font, visible=False
            ),  # Initially hidden
            sg.InputText(
                key="-PACK_NAME-", size=(40, 1), font=custom_font, visible=False
            ),  # Initially hidden
            sg.Button(
                "Confirm Pack Name", size=(15, 1), font=custom_font, visible=False
            ),
        ],  # Initially hidden
    ]

    return layout, pack
