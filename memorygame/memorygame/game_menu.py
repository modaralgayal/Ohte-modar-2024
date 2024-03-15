import PySimpleGUI as sg

data = {'Root': ['Node 1', 'Node 2', 'Node 3'],
        'Node 1': ['Subnode 1', 'Subnode 2'],
        'Node 2': ['Subnode 3'],
        'Node 3': []}

treedata = sg.TreeData()

# Insert data into the tree
for key, value in data.items():
    treedata.Insert("", key, key, value)

tree = sg.Tree(treedata, num_rows=3, font=('Helvetica', 14), col0_width=20,row_height= 50, enable_events=True)

layout = [[sg.Push(), sg.Text(text="Memory Game"), sg.Push()],
          [tree]]

window = sg.Window("Hello World", layout, size=(500, 350))

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    # Handle tree item clicks
    if event == 'Tree':
        selected_item = values[event][0]  # Get the clicked item
        print("Clicked item:", selected_item)
window.close()
