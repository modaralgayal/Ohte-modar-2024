""" Memory Game """
from random import shuffle

import PySimpleGUI as sg
from services import HandlePacks


def extract_cards_and_definitions(pack):
    """organizes fetched pack"""
    cards = []
    definitions = []
    for item in pack:
        _, card_list = item
        shuffle(card_list)
        for card in card_list:
            cards.append(card["name"])
            definitions.append(card["definition"])
    return cards, definitions


def create_memory_game_layout():
    """Creates the memory game layout"""
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
    return layout


def run_memory_game(window, name):
    """Runs the memory game with provided layout and selected pack name"""
    handle = HandlePacks()
    pack = handle.get_pack(name[0])
    sg.theme("DarkGrey5")

    cards, definitions = extract_cards_and_definitions(pack)

    index = 0
    show_definition = False

    while True:
        event, _ = window.read()

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
        elif event == "Back To Menu":
            print("Going back to menu")
            window.close()

        if show_definition:
            window["-CARD-"].update(definitions[index])
        else:
            window["-CARD-"].update(cards[index])

    print("Going back to menu")

    window.close()

    return "Exit"
