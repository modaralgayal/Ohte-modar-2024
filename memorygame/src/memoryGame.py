import PySimpleGUI as sg
from random import shuffle

def extract_cards_and_definitions(pack):
    cards = []
    definitions = []
    for item in pack:
        pack_name, card_list = item
        shuffle(card_list)
        for card in card_list:
            cards.append(card['name'])
            definitions.append(card['definition'])
    return cards, definitions

def memory_game_layout(pack):
    sg.theme("DarkGrey5")

    cards, definitions = extract_cards_and_definitions(pack)

    layout = [
        [sg.Text("Memory Game", font=("Helvetica", 20))],
        [sg.Text("Click on a card to reveal its definition.", font=("Helvetica", 12))],
        [
            sg.Button("◄", size=(3, 1), font=("Helvetica", 12), key="-PREV-"),
            sg.Button("", size=(30, 3), font=("Helvetica", 12), key="-CARD-"),
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

    window = sg.Window("Memory Game", layout, size=(600, 500))

    index = 0  # Index of current card
    show_definition = False

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-BACK-"):
            break
        elif event == "-PREV-":
            index = (index - 1) % len(cards)
            show_definition = False 
        elif event == "-NEXT-":
            index = (index + 1) % len(cards)
            show_definition = False 
        elif event == "-CARD-":
            show_definition = not show_definition

        # Update button text based on current state
        if show_definition:
            window["-CARD-"].update(definitions[index])
        else:
            window["-CARD-"].update(cards[index])

    window.close()

if __name__ == "__main__":
    pack = ['champions league', [{'name': 'Real Madrid ', 'definition': 'Best team'}, 
                                  {'name': 'Man City', 'definition': 'bruh too good'}, 
                                  {'name': 'Arsenal', 'definition': 'Lol Aint winning'}]], 
    memory_game_layout(pack)
