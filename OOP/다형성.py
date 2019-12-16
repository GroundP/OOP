from math import pi
from abc import ABC, abstractmethod

"""
다형성은 하나의 변수를 여러 인스턴스로 나타낼 수 있는 형태, 특징
그리고 추상 클래스란 '여러 클래스들의 공통점을 추상화해서 모아놓은 클래스'이며, 
다형성은 추상클래스를 통해 구현할 수 있다.

ABC는 Abstract Base Class로 추상클래스를 나타낸다
abstractclassmethod는 추상 메소드를 나타낸다
"""

class Figure(ABC):
    """도형 클래스(추상 클래스)"""

    @abstractmethod
    def area(self) -> float: # 추상 메소드는 type hinting을 해주는 것이 좋다
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass


class Rectangle(Figure):
    """직사각형 클래스"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이 리턴"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레 리턴"""
        return self.width * 2 + self.height * 2

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle(Figure):
    """원 클래스"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이 리턴"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레 리턴"""
        return pi * 2 * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class Cylinder(Figure):
    """원통 클래스"""

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        """원통의 넓이를 리턴"""
        return pi * self.radius * self.radius * self.height

    def perimeter(self):
        """원통의 둘레를 리턴"""
        return pi * 2 * self.radius * self.height

    def __str__(self):
        """원통의 정보를 문자여롤 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Figure):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])


cylinder = Cylinder(7, 4)
rectangle = Rectangle(3, 7)
circle = Circle(4)

paint_program = Paint()

paint_program.add_shape(cylinder)
paint_program.add_shape(circle)
paint_program.add_shape(rectangle)

print(paint_program.total_perimeter_of_shapes())  # 에러가 난다!
print(paint_program.total_area_of_shapes())
