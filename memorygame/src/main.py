import PySimpleGUI as sg
from create_packs import create_pack_layout
from display_packs import display_packs_layout
from memoryGame import memory_game_layout
from services import HandlePacks


def main():
    layout, _ = display_packs_layout()

    window = sg.Window("Memory Game", layout, size=(600, 500))

    current_layout = "display_packs"
    pack = HandlePacks()
    Cardpacks = HandlePacks()
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
                    window["Play"].update(disabled=False)
                else:
                    window["Delete Pack"].update(disabled=True)
                    window["Play"].update(disabled=True)

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
            elif event == "Play":
                selected_item = values["-TREE-"]
                window.close()
                layout, _ = memory_game_layout(selected_item)
                window = sg.Window("Memory Game", layout, size=(600, 500))
                current_layout == "Play the Game"
        elif current_layout == "Play the Game":
            if event == "Back To Menu":
                window.close()
                layout, Cardpacks = display_packs_layout()
                window = sg.Window("Memory Game", layout, size=(600, 500))
                current_layout = "display_packs"

        else:
            pass  # Handle events specific to display packs layout

        window.refresh()

    window.close()


if __name__ == "__main__":
    main()
