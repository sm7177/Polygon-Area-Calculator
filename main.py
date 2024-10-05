class Polygon:
    def __init__(self, sides_length):
        self.sides_length = sides_length

    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Square(Polygon):
    def __init__(self, side_length):
        super().__init__(side_length)

    def area(self):
        return self.sides_length ** 2


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__((length, width))

    def area(self):
        return self.sides_length[0] * self.sides_length[1]


class RegularPolygon(Polygon):
    def __init__(self, side_length, num_sides):
        super().__init__(side_length)
        self.num_sides = num_sides

    def area(self):
        if self.num_sides == 5:
            multiplier = 1.72048  
        elif self.num_sides == 6:
            multiplier = 2.59808  
        elif self.num_sides == 7:
            multiplier = 3.63391  
        elif self.num_sides == 8:
            multiplier = 4.82843  
        else:
            raise ValueError("Unsupported number of sides")

        return (self.num_sides * self.sides_length ** 2) / (4 * multiplier)


class Pentagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 5)


class Hexagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 6)


class Heptagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 7)


class Octagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 8)


def main():
    while True:
        print("Choose the polygon to calculate area:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Pentagon")
        print("4. Hexagon")
        print("5. Heptagon")
        print("6. Octagon")
        print("7. Exit")

        choice = int(input("Please enter your choice: "))

        if choice == 1:
            side = float(input("Enter the side length of the square: "))
            square = Square(side)
            print(f"The area of the square is: {square.area()}")

        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangle = Rectangle(length, width)
            print(f"The area of the rectangle is: {rectangle.area()}")

        elif choice == 3:
            side = float(input("Enter the side length of the pentagon: "))
            pentagon = Pentagon(side)
            print(f"The area of the pentagon is: {pentagon.area()}")

        elif choice == 4:
            side = float(input("Enter the side length of the hexagon: "))
            hexagon = Hexagon(side)
            print(f"The area of the hexagon is: {hexagon.area()}")

        elif choice == 5:
            side = float(input("Enter the side length of the heptagon: "))
            heptagon = Heptagon(side)
            print(f"The area of the heptagon is: {heptagon.area()}")

        elif choice == 6:
            side = float(input("Enter the side length of the octagon: "))
            octagon = Octagon(side)
            print(f"The area of the octagon is: {octagon.area()}")

        elif choice == 7:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
