from ..services import HandlePacks


def test_add_pack():
    handler = HandlePacks()
    length_1 = len(handler.get_packs())
    handler.add_pack(
        "Gadgets",
        [
            {"name": "tv", "definition": "Big screen"},
            {"name": "Computer", "definition": "small screen and keyboard with mouse"},
        ],
    )
    length_2 = len(handler.get_packs())
    assert length_1 != length_2


def test_get_pack():
    handler = HandlePacks()
    pack = handler.get_pack("Gadgets")

    assert pack[0][0] == "Gadgets"
    assert pack[0][1] == [
        {"name": "tv", "definition": "Big screen"},
        {"name": "Computer", "definition": "small screen and keyboard with mouse"},
    ]


def test_delete_pack():
    handler = HandlePacks()

    handler.delete_pack("Gadgets")
    pack = handler.get_pack("Gadgets")
    assert pack == []
