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

tree = sg.Tree(
    treedata,
    num_rows=3,
    font=("Helvetica", 14),
    col0_width=20,
    row_height=50,
    enable_events=True,
)

layout = [[sg.Push(), sg.Text(text="Memory Game"), sg.Push()], [tree]]

window = sg.Window("Hello World", layout, size=(500, 350))

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    # Handle tree item clicks
    if event == "Tree":
        selected_item = values[event][0]  # Get the clicked item
        print("Clicked item:", selected_item)
window.close()
