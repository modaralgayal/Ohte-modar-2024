"""
These are the services responsible for communicating with the database
"""

import json
import sqlite3


class HandlePacks:
    """This class handles all the sql databse operations"""

    def __init__(self):
        self.connection = sqlite3.connect("mydata.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS card_lists (
                id INTEGER PRIMARY KEY,
                pack_name TEXT,
                card_pack TEXT NOT NULL
            )
            """
        )

    def add_pack(self, pack_name, cardpack):
        print(pack_name, cardpack)
        """Adds a pack of cards to the databse, which the user creates and can play later"""
        print("initially passed")
        print(cardpack)
        card_list = json.dumps(cardpack)

        self.cursor.execute(
            """
            INSERT INTO card_lists (pack_name, card_pack) VALUES (?, ?)
            """,
            (pack_name, card_list),
        )
        self.connection.commit()

    def get_packs(self):
        """The other functions call this to display all the user's games"""
        self.cursor.execute(
            """
            SELECT pack_name, card_pack
            FROM card_lists
            """
        )
        cards_json_rows = self.cursor.fetchall()

        retrieved_cards_lists = []
        for row in cards_json_rows:
            pack_name = row[0]
            card_pack = json.loads(row[1])
            retrieved_cards_lists.append([pack_name, card_pack])

        return retrieved_cards_lists

    def get_pack(self, name):
        """Called by other functions to get one specific pack"""
        print(name)
        self.cursor.execute(
            """
            SELECT pack_name, card_pack
            FROM card_lists
            WHERE pack_name == ?
            """,
            (name,),
        )

        card_pack = self.cursor.fetchall()
        retrieved_cards_list = []
        for row in card_pack:
            pack_name = row[0]
            print("This is the row", row[1])
            card_pack = row[1]
            retrieved_cards_list.append([pack_name, card_pack])

        return retrieved_cards_list

    def delete_pack(self, name):
        """Delete a pack"""
        self.cursor.execute(
            """
                DELETE FROM card_lists WHERE pack_name = ?
                """,
            (name,),
        )
        self.connection.commit()

    def delete_card_from_pack(self, pack_name, card_name):
        """Delete a specific card from a pack"""
        pack = self.get_pack(pack_name)
        print("Card to be deleted", card_name)
        if not pack:
            return False

        pack_contents = pack[0][1]  # Extract pack contents

        print("Contents of the pack", pack_contents)

        for card in pack_contents:
            if card["name"] == card_name:
                pack_contents.remove(card)
                self.cursor.execute(
                    """
                    UPDATE card_lists
                    SET card_pack = ?
                    WHERE pack_name = ?
                    """,
                    (json.dumps(pack_contents), pack_name),
                )
                self.connection.commit()
                return True
        # Checking if deletetion is successful
        pack = self.get_pack(pack_name)
        print("This is the new pack:", pack)
        return False

    def add_card_to_existing_pack(self, pack_name, card):

        pack = self.get_pack(pack_name)
        if not pack:
            print("Pack not found, something went wrong")
            return False

        pack_contents = pack[0][1]

        pack_contents.append(card)

        print("Contents of the new pack: ", pack_contents)

        # Update the pack in the database
        self.cursor.execute(
            """
            UPDATE card_lists
            SET card_pack = ?
            WHERE pack_name = ?
            """,
            (str(pack_contents), str(pack_name)),
        )
        self.connection.commit()  # Commit the transaction

        return True


if __name__ == "__main__":
    pack1 = "Animals", [
        {"name": "Dog", "definition": "A domesticated carnivorous mammal."},
        {"name": "Cat", "definition": "A small domesticated carnivorous mammal."},
        {
            "name": "Elephant",
            "definition": "A large herbivorous mammal with a long trunk.",
        },
    ]

    pack2 = "Fruits", [
        {
            "name": "Apple",
            "definition": "A round fruit with red or green skin and a whitish flesh.",
        },
        {"name": "Banana", "definition": "A long curved fruit with a yellow skin."},
        {
            "name": "Orange",
            "definition": "A round citrus fruit with a tough bright orange skin.",
        },
    ]

    pack3 = "countries", [
        {"name": "United States", "definition": "A country in North America."},
        {"name": "United Kingdom", "definition": "A country in Europe."},
        {"name": "Australia", "definition": "A country in Oceania."},
    ]

    handler = HandlePacks()
    handler.add_pack(pack1[0], pack1[1])
    handler.add_pack(pack2[0], pack2[1])
    handler.add_pack(pack3[0], pack3[1])
