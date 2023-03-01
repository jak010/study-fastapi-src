from dataclasses import dataclass


@dataclass
class EmailVo:
    email: str
    local_part: str = ""
    domain_part: str = ""
    host: str = ""
    domain: str = ""

    def __post_init__(self):
        self._split_part()
        self._split_domain()

        if self.host not in ["naver", "daum", "gmail"]:
            raise ValueError("Not Allowed Email Host")

    def _split_part(self):
        self.local_part, self.domain_part = self.email.split("@")

    def _split_domain(self):
        self.host, self.domain = self.domain_part.split(".")
