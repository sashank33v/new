from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role(self):
        pass


class Student(User):

    def role(self):
        return "Student"


class Admin(User):

    def role(self):
        return "Admin"
