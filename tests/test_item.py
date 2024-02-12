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