# {{Item}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
```
As a User
So that I can store my Items
I want to be able to CRUD Items
```

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Item:
    def __init__(self, id, name, type):
        # Parameters:
        #   id: string
        #   name: string
        #   type: string
        # Side effects:
        #   Sets the id, name and type property of the self object
        pass # No code here yet

    def __eq__(self, other):
        # Parameters:
        #   other: instance of object
        # Returns:
        #   bool
        # Side-effects
        #   none
        pass # No code here yet

    def __repr__(self):
        # Returns:
        #   A string printing out the Item in a nice format.
        # Side-effects:
        #   none
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a Item is instantiated
It has an id, name and type
"""
item = Item(1, "Phone", "electric")
assert item.id == 1
assert item.name == "Phone"
assert item.type == "electric"

"""
Given two Items have identical parameters
They are equal
"""
item1 = Item(1, "Tennis shorts", "sportswear")
item2 = Item(1, "Tennis shorts", "sportswear")

assert item1 == item2

"""
Given I print out an Item
It prints in a nice format

"""
item1 = Item(1, "Bike", "sports equipment")
assert str(item) == "Item(1, Bike, sports equipment)"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
