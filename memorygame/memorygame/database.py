import sqlite3
import json

cards_list_1 = [
    {"name": "Ace of Spades", "definition": "The highest card in a standard deck of playing cards."},
    {"name": "King of Hearts", "definition": "A face card in a standard deck of playing cards, typically depicted with a crown."},
    {"name": "Queen of Diamonds", "definition": "A face card in a standard deck of playing cards, typically depicted with a crown and holding a scepter."}
]

cards_list_2 = [
    {"name": "Jack of Clubs", "definition": "A face card in a standard deck of playing cards, typically depicted as a man holding a sword."},
    {"name": "10 of Spades", "definition": "A numeric card in a standard deck of playing cards with ten symbols representing the suit of spades."},
    {"name": "9 of Hearts", "definition": "A numeric card in a standard deck of playing cards with nine symbols representing the suit of hearts."}
]

cards_json_1 = json.dumps(cards_list_1)
cards_json_2 = json.dumps(cards_list_2)

connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS card_lists (
        id INTEGER PRIMARY KEY,
        cards TEXT NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO card_lists (cards) VALUES (?)
""", (cards_json_1,))

cursor.execute("""
    INSERT INTO card_lists (cards) VALUES (?)
""", (cards_json_2,))

connection.commit()

cursor.execute("""
    SELECT cards
    FROM card_lists
""")

cards_json_rows = cursor.fetchall()

retrieved_cards_lists = [json.loads(row[0]) for row in cards_json_rows]

connection.close()

print("Retrieved Lists of Cards:")
for index, cards_list in enumerate(retrieved_cards_lists, start=1):
    print(f"List {index}:")
    for card in cards_list:
        print("Name:", card["name"])
        print("Definition:", card["definition"])
        print()
    print()
