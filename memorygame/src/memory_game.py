import PySimpleGUI as sg
from services import HandlePacks

Cardpacks = HandlePacks()

card_packs = Cardpacks.get_packs()

treedata = sg.TreeData()

for pack_name, card_pack in card_packs:
    treedata.Insert("", pack_name, pack_name, "")
    for card in card_pack:
        card_name = card["name"]
        treedata.Insert(pack_name, card_name, card_name, "")

sg.theme("LightGrey1")

tree = sg.Tree(
    treedata,
    num_rows=10,
    font=("Helvetica", 16),
    col0_width=30,
    enable_events=True,
    show_expanded=False,
    key="-TREE-",
)

delete_button = sg.Button("Delete Pack", disabled=True)  # Initially disabled
test_button = sg.Button("test")

layout = [
    [sg.Text("All your Packs:", font=("Calibri", 24))],
    [tree],
    [delete_button],
]

window = sg.Window("Memory Game", layout, size=(600, 500))

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break

    if event == "-TREE-":
        selected_item = values["-TREE-"]
        if selected_item:
            delete_button.update(disabled=False)
        else:
            delete_button.update(disabled=True)

    elif event == "Delete Pack":
        selected_item = values["-TREE-"][0]
        pack_name = selected_item if selected_item else None
        if pack_name:
            Cardpacks.delete_pack(pack_name)
            treedata.Delete(selected_item)

    window.refresh()


window.close()
