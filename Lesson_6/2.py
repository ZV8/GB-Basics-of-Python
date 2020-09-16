class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return self._length * self._width * 25 * 5 / 1000


new_road = Road(100, 10)
print(f"Масса асфальта = {new_road.mass()} тонн")
