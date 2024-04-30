""" Tests for app """

import json

from ..services.services import HandlePacks


def test_add_pack():
    """Test pack addition"""
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
    """Test pack retrieval"""
    handler = HandlePacks()
    pack = handler.get_pack("Gadgets")

    assert pack[0][0] == "Gadgets"
    assert json.loads(pack[0][1]) == [
        {"name": "tv", "definition": "Big screen"},
        {"name": "Computer", "definition": "small screen and keyboard with mouse"},
    ]


def test_deleting_one_card():
    """Test deleting one card"""
    handler = HandlePacks()
    handler.delete_card_from_pack(
        "Gadgets",
        "tv",
    )

    pack = handler.get_pack("Gadgets")
    assert json.loads(pack[0][1]) == [
        {"name": "Computer", "definition": "small screen and keyboard with mouse"},
    ]


def test_adding_to_existing_pack():
    """Test adding existing pack"""
    handler = HandlePacks()

    handler.add_card_to_existing_pack(
        "Gadgets", {"name": "tv", "definition": "Big screen"}
    )
    pack = handler.get_pack("Gadgets")
    assert json.loads(pack[0][1]) == [
        {"name": "Computer", "definition": "small screen and keyboard with mouse"},        
        {"name": "tv", "definition": "Big screen"}
    ]


def test_delete_pack():
    """Test pack deletion"""
    handler = HandlePacks()

    handler.delete_pack("Gadgets")
    pack = handler.get_pack("Gadgets")
    assert pack == []
