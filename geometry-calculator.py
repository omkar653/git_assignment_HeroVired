import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):

        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):

        return length * width

if __name__ == "__main__":

    calculator = GeometryCalculator()

radius = 5

print(f"The area of the circle with radius {radius} =v{calculator.calculate_circle_area(radius)}")