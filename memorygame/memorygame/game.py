import PySimpleGUI as sg

tree_data = {'Root': ['Node 1', 'Node 2', 'Node 3'],
             'Node 1': ['Subnode 1', 'Subnode 2'],
             'Node 2': ['Subnode 3'],
             'Node 3': []}

treedata = sg.TreeData()

layout = [[sg.Text(text="Memory Game")],
          [sg.Tree(treedata ,num_rows=3)]]

window = sg.Window("Hello World", layout, size=(500,250))


while True: 
    event, values = window.read()
    print(event,values)
    if event in (None, "Exit"):
        break
window.close()