""" Main page where the pack titles are displayed along with their titles """

import PySimpleGUI as sg
from services.services import HandlePacks


def display_packs_layout():
    """UI Display function"""
    cardpacks = HandlePacks()
    card_packs = cardpacks.get_packs()
    sg.theme("DarkGrey5")

    treedata = sg.TreeData()
    for pack_name, card_pack in card_packs:
        treedata.insert("", str(pack_name), str(pack_name), [], icon=None)
        for card in card_pack:
            card_name = card["name"]
            treedata.insert(
                str(pack_name), str(card_name), str(card_name), [], icon=None
            )

    layout = [
        [sg.Text("All your Packs:", font=("Calibri", 24))],
        [
            sg.Tree(
                treedata,
                font=("Helvetica", 16),
                col0_width=30,
                enable_events=True,
                show_expanded=False,
                key="-TREE-",
            )
        ],
        [
            sg.Button("Delete Pack", disabled=True),
            sg.Button("Create Pack"),
            sg.Button("Play", disabled=True),
            sg.Button("Edit Pack", disabled=True),
        ],
    ]

    return layout, cardpacks
