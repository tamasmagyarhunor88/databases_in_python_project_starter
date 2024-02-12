class Item():
    def __init__(self, id, name, type) -> None:
        self.id = id
        self.name = name
        self.type = type

    def __eq__(self, other):
        return self.__dict__ == other.__dict__