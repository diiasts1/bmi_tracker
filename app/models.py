from abc import ABC, abstractmethod

# Advanced OOP: Inheritance and Polymorphism
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_info(self):
        pass

# Core OOP: Encapsulation (using __height)
class User(Person):
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height  # Private attribute
        self.history = []       # List collection to store weight record

    @property
    def height(self):
        return self.__height

    def add_new_weight(self, weight):
        # Formula: BMI = weight / (height * height)
        bmi_value = weight / (self.__height ** 2)
        # Dictionary collection
        new_record = {"weight": weight, "bmi": round(bmi_value, 2)}
        self.history.append(new_record)

    def show_info(self): # Polymorphism
        return f"Student/User: {self.name}, Height: {self.__height}m"