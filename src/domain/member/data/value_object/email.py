from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EmailVo:
    email: str

    local_part = None
    domain_part = None
    host = None
    domain = None

    def __post_init__(self):
        self._split_part(email=self.email)
        self._split_domain()

        if self.host not in ["naver", "daum", "gmail"]:
            raise Exception("Not Allowed Email Host")

    def _split_part(self, email):
        local_part, domain_part = email.split("@")
        self.local_part = local_part
        self.domain_part = domain_part

    def _split_domain(self):
        host, domain = self.domain_part.split(".")
        self.host = host
        self.domain = domain
