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

def test_printing_out_item_prints_in_nice_format():
    """
Given I print out an Item
It prints in a nice format

"""
item = Item(1, "Bike", "sports equipment")
assert str(item) == "Item(1, Bike, sports equipment)"