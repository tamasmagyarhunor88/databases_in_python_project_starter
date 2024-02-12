from lib.item import *

def test_instantiates_with_id_name_type():
    """
    Given a Item is instantiated
    It has an id, name and type
    """
    item = Item(1, "Phone", "electric")
    assert item.id == 1
    assert item.name == "Phone"
    assert item.type == "electric"

def test_two_identical_properties_items_are_equal():
    """
    Given two Items have identical parameters
    They are equal
    """
    item1 = Item(1, "Tennis shorts", "sportswear")
    item2 = Item(1, "Tennis shorts", "sportswear")

    assert item1 == item2