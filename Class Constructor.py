"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    def __init__(self):
        self.firstname =  ""
        self.lastname =  ""
        self.age =  0
    """Represent person with firstname, lastname and age."""

    pass


class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    """Represent student with firstname, lastname and age."""

    pass


if __name__ == '__main__':
    # empty usage

    # 3 x person usage

    # 3 x student usage
    pass
