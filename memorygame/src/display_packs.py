import PySimpleGUI as sg
from services import HandlePacks

def display_packs_layout():
    Cardpacks = HandlePacks()
    card_packs = Cardpacks.get_packs()
    sg.theme('DarkGrey5')

    treeData = sg.TreeData()
    for pack_name, card_pack in card_packs:
        treeData.insert("", str(pack_name), str(pack_name), [], icon=None)
        for card in card_pack:
            card_name = card["name"]
            treeData.insert(str(pack_name), str(card_name), str(card_name), [], icon=None)

    layout = [
        [sg.Text("All your Packs:", font=("Calibri", 24))],
        [sg.Tree(
            treeData,
            font=("Helvetica", 16),
            col0_width=30,
            enable_events=True,
            show_expanded=False,
            key="-TREE-",
        )],
        [sg.Button("Delete Pack", disabled=True),
         sg.Button("Create Pack")],
    ]

    return layout, Cardpacks
