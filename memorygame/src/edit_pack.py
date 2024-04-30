import PySimpleGUI as sg
from services.services import HandlePacks
import json

def edit_pack_layout(selected_pack):
    """UI Display function for editing a pack"""
    sg.theme("DarkGrey5")
    handler = HandlePacks()
    pack_name, card_pack_json = handler.get_pack(selected_pack)[0]
    card_pack = json.loads(card_pack_json)
    card_names = [f"{card['name']}: {card['definition']} " for card in card_pack]
    print("This is the card_pack", card_pack)
    custom_font = ("Arial", 12)

    treedata = sg.TreeData()
    for card in card_pack:
        card_name = card["name"]
        treedata.insert("", str(card_name), str(card_name), [], icon=None)

    layout = [
        [sg.Text(f"Editing Pack: {selected_pack}", font=("Calibri", 24))],
        [sg.Text("Cards in Pack:", font=("Calibri", 16))],
        [
            sg.Listbox(
                values=card_names,
                size=(50, 10),
                font=custom_font,
                key="-CARDS-",
                enable_events=True,
            )
        ],
        [
            sg.Button("Edit Card", disabled=True),
            sg.Button("Delete Card", disabled=True),
            sg.Button("New Card", key="-NEW_CARD-"),
            sg.Button("Back"),
        ],
        [
            sg.Text(
                "Name:", font=custom_font, visible=False, key="-NAME_LABEL-"
            ),  # Add key to the name label
            sg.InputText(key="-NAME-", size=(30, 1), font=custom_font, visible=False),
            sg.Text(
                "Definition:", font=custom_font, visible=False, key="-DEFINITION_LABEL-"
            ),  # Add key to the definition label
            sg.InputText(
                key="-DEFINITION-", size=(30, 1), font=custom_font, visible=False
            ),
        ],
        [sg.Button("Add Card", key="-ADD_CARD-", visible=False)],
    ]

    return layout, handler
