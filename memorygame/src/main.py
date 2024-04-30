""" Main component """

import json

import PySimpleGUI as sg
from create_packs import create_pack_layout
from display_packs import display_packs_layout
from edit_pack import edit_pack_layout
from memory_game import create_memory_game_layout, run_memory_game
from services.services import HandlePacks


def main():
    """Main function"""
    layout, _ = display_packs_layout()

    window = sg.Window("Memory Game", layout, size=(600, 500))

    current_layout = "display_packs"
    pack = HandlePacks()
    cards = []

    while True:
        event, values = window.read()

        if event in (None, "Exit"):
            break

        elif current_layout == "create_pack":
            if event == "Back To Menu":
                window.close()
                layout, cardpacks = display_packs_layout()
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
                window["-PACK_NAME-"].update(visible=True)
                window["Confirm Pack Name"].update(visible=True)

            elif event == "Confirm Pack Name":
                pack_name = values["-PACK_NAME-"]
                pack.add_pack(pack_name, cards)
                sg.popup("Card pack created successfully!")
                cards = []
                window.close()
                layout, cardpacks = display_packs_layout()
                window = sg.Window("Memory Game", layout, size=(600, 500))
                current_layout = "display_packs"

        elif current_layout == "display_packs":
            if event == "-TREE-":
                selected_item = values["-TREE-"]
                if selected_item:
                    window["Delete Pack"].update(disabled=False)
                    window["Play"].update(disabled=False)
                    window["Edit Pack"].update(disabled=False)
                else:
                    window["Delete Pack"].update(disabled=True)
                    window["Play"].update(disabled=True)
                    window["Edit Pack"].update(disabled=True)

            elif event == "Edit Pack":
                window.close()
                pack_being_edited = values["-TREE-"][0]
                layout, _ = edit_pack_layout(pack_being_edited)
                window = sg.Window("Edit Pack", layout, size=(800, 500))
                current_layout = "Edit Pack"

            elif event == "Delete Pack":
                selected_item = values["-TREE-"][0]
                pack.delete_pack(selected_item)
                window.close()
                layout, _ = create_pack_layout()
                window = sg.Window("Memory Game", layout, size=(800, 500))
                current_layout = "create_pack"

            elif event == "Create Pack":
                window.close()
                layout, cardpacks = create_pack_layout()
                window = sg.Window("Memory Game", layout, size=(800, 500))
                current_layout = "create_pack"
            elif event == "Play":
                selected_item = values["-TREE-"]
                current_layout == "Play the Game"
                window.close()
                layout = create_memory_game_layout()
                window = sg.Window("Memory Game", layout, size=(600, 500))
                done = run_memory_game(window, selected_item)
                if done == "Exit":
                    window.close()
                    layout, _ = display_packs_layout()
                    window = sg.Window("Memory Game", layout, size=(600, 500))
                    current_layout = "display_packs"

        elif current_layout == "Edit Pack":

            if values["-CARDS-"]:
                selected_card = values["-CARDS-"][0]
                window["Delete Card"].update(disabled=False)

            if event == "Edit Card":
                pass

            # Delete a card
            elif event == "Delete Card":
                selected_card = values["-CARDS-"][0] if values["-CARDS-"] else None
                if selected_card:

                    pack.delete_card_from_pack(
                        pack_being_edited, selected_card.split(":")[0]
                    )
                    card_pack = json.loads(pack.get_pack(pack_being_edited)[0][1])
                    card_names = [
                        f"{card['name']}: {card['definition']}" for card in card_pack
                    ]
                    window["-CARDS-"].update(values=card_names)

            # add card to existing pack
            elif event == "-NEW_CARD-":  # Check if the "Add Card" button is clicked
                # Make the non-visible elements visible
                window["-NAME_LABEL-"].update(visible=True)
                window["-NAME-"].update(visible=True)
                window["-DEFINITION_LABEL-"].update(visible=True)
                window["-DEFINITION-"].update(visible=True)
                window["-ADD_CARD-"].update(visible=True)

            elif event == "-ADD_CARD-":
                name = values["-NAME-"]
                definition = values["-DEFINITION-"]
                new_card = {"name": name, "definition": definition}
                window["-NAME-"].update("")
                window["-DEFINITION-"].update("")
                pack.add_card_to_existing_pack(pack_being_edited, new_card)
                print("Pack addition successful")
                card_pack_data = pack.get_pack(pack_being_edited)[0][1]
                card_pack = json.loads(card_pack_data)
                card_names = [
                    f"{card['name']}: {card['definition']}" for card in card_pack
                ]
                window["-CARDS-"].update(values=card_names)

            # go back to menu
            elif event == "Back To Menu":
                window.close()
                layout, cardpacks = display_packs_layout()
                window = sg.Window("Memory Game", layout, size=(600, 500))
                current_layout = "display_packs"

        else:
            pass

        window.refresh()

    window.close()


if __name__ == "__main__":
    main()
