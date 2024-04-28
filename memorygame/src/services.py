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
        print("This is the cardpack", card_pack)
        retrieved_cards_list = []
        for row in card_pack:
            pack_name = row[0]
            card_pack = json.loads(row[1])
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
