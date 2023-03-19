from __future__ import annotations

import json
from src.seedwork.entity import AbstractEntity


class MemberEntity(AbstractEntity):

    def __init__(self, email: str, name: str, age: int):
        self.email = email
        self.name = name
        self.age = age

    def to_json(self):
        return json.dumps({
            "reference_id": self.reference_id
        })

    def to_dict(self):
        return {
            "reference_id": self.reference_id,
            "email": self.email,
            "name": self.name,
            "age": self.age
        }

    def __str__(self):
        return f"Member(\n" \
               f" reference_id={self.reference_id},\n" \
               f" email={self.email},\n" \
               f" name={self.name},\n" \
               f" age={self.age}\n" \
               f")"
