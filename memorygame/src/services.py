import json
import sqlite3


class HandlePacks:

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
        card_list = json.dumps(cardpack)

        self.cursor.execute(
            """
            INSERT INTO card_lists (pack_name, card_pack) VALUES (?, ?)
            """,
            (pack_name, card_list),
        )
        self.connection.commit()

    def get_packs(self):

        self.cursor.execute(
            """ 
            SELECT pack_name, card_pack
            FROM card_lists
            """
        )
        cards_json_rows = self.cursor.fetchall()

        retrieved_cards_lists = [(row[0], json.loads(row[1])) for row in cards_json_rows]
        self.connection.commit()
        self.connection.close()
        return retrieved_cards_lists
