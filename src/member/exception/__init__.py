from fastapi.exceptions import HTTPException


class MemberNotFound(HTTPException):

    def __init__(self):
        super().__init__(status_code=404, detail="Member not found")
