class Card:
    def __init__(self, color, value, weight):
        self.color = color
        self.value = value
        self.weight = weight

    def __eq__(self, other):
        return self.color == other.color and self.value == other.value

    def to_tuples(self):
        return self.color, self.value

    def __str__(self):
        return self.color + ' ' + self.value
