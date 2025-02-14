class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield the length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(10, 5)

# Iterating over the rectangle instance
for dimension in rectangle:
    print(dimension)