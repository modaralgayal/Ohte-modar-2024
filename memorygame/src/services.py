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
            (pack_name.lower(), card_list),
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

        retrieved_cards_lists = []
        for row in cards_json_rows:
            pack_name = row[0]
            card_pack = json.loads(row[1])
            retrieved_cards_lists.append([pack_name, card_pack])
        
        print(retrieved_cards_lists)

        return retrieved_cards_lists

    def delete_pack(self, name):
        (self.cursor.execute(
            """
            DELETE FROM card_lists WHERE pack_name = ?
            """
            ,
            (name,)
        ))

        self.connection.commit()


if __name__ == "__main__":
    p = HandlePacks().get_packs()
    for row in p:
        print(row)
        print()
