import sqlite3

# Connect to the database
connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()

# Create the cards table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY,
        card_name TEXT NOT NULL,
        card_definition TEXT NOT NULL
    )
""")

cards_data = [
    ("Ace of Spades", "The highest card in a standard deck of playing cards."),
    ("King of Hearts", "A face card in a standard deck of playing cards, typically depicted with a crown."),
    ("Queen of Diamonds", "A face card in a standard deck of playing cards, typically depicted with a crown and holding a scepter."),
]

# Insert the cards into the cards table
cursor.executemany("""
    INSERT INTO cards (card_name, card_definition)
    VALUES (?, ?)
""", cards_data)

cursor.execute("""
    SELECT card_name, card_definition
    FROM cards
""")

cards = cursor.fetchall()

for card in cards:
    print("Card:", card[0])
    print("Definition:", card[1])
    print()


# Create the games table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        game_name TEXT NOT NULL,
        card_pack_id INTEGER,
        FOREIGN KEY (card_pack_id) REFERENCES cards(id)
    )
""")

# Commit changes and close connection
connection.commit()
connection.close()
