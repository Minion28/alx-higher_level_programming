#!/usr/bin/python3
"""Student to JSON with filter
"""


class Student:
    """A class representation of a student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
