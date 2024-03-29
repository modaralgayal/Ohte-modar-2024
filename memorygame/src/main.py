import PySimpleGUI as sg
from create_packs import create_pack_layout
from display_packs import display_packs_layout
from services import HandlePacks


def memory_game_layout(cards):
    sg.theme("DarkGrey5")

    layout = [
        [sg.Text("Memory Game", font=("Helvetica", 20))],
        [sg.Text("Click on a card to reveal its definition.", font=("Helvetica", 12))],
        [
            sg.Button("◄", size=(3, 1), font=("Helvetica", 12), key="-PREV-"),
            sg.Text(
                "",
                size=(30, 1),
                font=("Helvetica", 12),
                justification="center",
                key="-CARD-",
            ),
            sg.Button("►", size=(3, 1), font=("Helvetica", 12), key="-NEXT-"),
        ],
        [
            sg.Text(
                "",
                font=("Helvetica", 12),
                size=(40, 1),
                justification="center",
                key="-DEFINITION-",
            )
        ],
        [sg.Button("Back To Menu", size=(15, 1), font=("Helvetica", 12), key="-BACK-")],
    ]

    return layout


def main():
    # Initial layout
    layout, _ = display_packs_layout()

    window = sg.Window("Memory Game", layout, size=(600, 500))

    current_layout = "display_packs"
    pack = HandlePacks()
    cards = []

    while True:
        event, values = window.read()

        if event in (None, "Exit"):
            break

        if current_layout == "create_pack":
            if event == "Back To Menu":
                window.close()
                layout, Cardpacks = display_packs_layout()
                window = sg.Window("Memory Game", layout, size=(600, 500))
                current_layout = "display_packs"

            elif event == "Add Card":
                name = values["-NAME-"]
                definition = values["-DEFINITION-"]
                if name and definition:
                    cards.append({"name": name, "definition": definition})
                    window["-NAME-"].update("")
                    window["-DEFINITION-"].update("")
                    window["-CARD_LIST-"].update(
                        values=[
                            f"{card['name']}: {card['definition']}" for card in cards
                        ]
                    )
                    print(cards)
            elif event == "Create Pack":
                # Show pack name input
                window["-PACK_NAME-"].update(visible=True)
                window["Confirm Pack Name"].update(visible=True)

            elif event == "Confirm Pack Name":
                pack_name = values["-PACK_NAME-"]
                pack.add_pack(pack_name, cards)
                sg.popup("Card pack created successfully!")
                cards = []
                window.close()
                layout, Cardpacks = display_packs_layout()
                window = sg.Window("Memory Game", layout, size=(600, 500))
                current_layout = "display_packs"

        elif current_layout == "display_packs":
            if event == "-TREE-":
                selected_item = values["-TREE-"]
                if selected_item:
                    window["Delete Pack"].update(disabled=False)
                else:
                    window["Delete Pack"].update(disabled=True)

            elif event == "Delete Pack":
                selected_item = values["-TREE-"][0]
                Cardpacks.delete_pack(selected_item)
                window.close()
                layout, _ = create_pack_layout()
                window = sg.Window("Memory Game", layout, size=(800, 500))
                current_layout = "create_pack"
            elif event == "Create Pack":
                window.close()
                layout, Cardpacks = create_pack_layout()
                window = sg.Window("Memory Game", layout, size=(800, 500))
                current_layout = "create_pack"
            else:
                pass  # Handle events specific to display packs layout

        window.refresh()

    window.close()


if __name__ == "__main__":
    main()
