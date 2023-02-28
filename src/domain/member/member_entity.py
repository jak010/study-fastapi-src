from __future__ import annotations


class Member:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Member(\n" \
               f" name={self.name},\n" \
               f" age={self.age}\n" \
               f")"
