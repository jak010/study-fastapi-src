from __future__ import annotations

import json

from src.seedwork.entity import AbstractEntity


class _EmailVerification:
    def __init__(self, email: str):
        self._email = email

        self.local_part, self.domain_part = email.split("@")
        self.host, self.domain = self.domain_part.split(".")

        if self.host not in ["naver", "daum", "gmail"]:
            raise Exception("Not Allowed Email Host")

    def clean_email(self):
        return self._email


class MemberEntity(AbstractEntity):

    def __init__(self, email: str, name: str, age: int):
        # Notes: Classical Mapping 에서는 @propert를 사용할 경우 db에 저장이 안된다.
        self.email = _EmailVerification(email).clean_email()
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
