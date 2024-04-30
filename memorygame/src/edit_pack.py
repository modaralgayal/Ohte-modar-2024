import PySimpleGUI as sg
from services.services import HandlePacks


def edit_pack_layout(selected_pack):
    """UI Display function for editing a pack"""
    sg.theme("DarkGrey5")
    handler = HandlePacks()
    pack_name, card_pack = handler.get_pack(selected_pack)[0]
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
            sg.Button("Add Card"),
            sg.Button("Back"),
        ],
    ]

    return layout, handler
