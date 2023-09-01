from src.service_layer.unit_of_work import SqlalchemyUnitofWork


class MemberUseCase:

    def __init__(self):
        self.uow = SqlalchemyUnitofWork()

    def find_member(self):
        with self.uow as uow:
            print(uow.repository)
            print(type(uow.repository.member_repository))

            # print(dir(uow.repository.member_repository))
            # print(dir(uow.repository.member_repository()))

            # print(uow.repository.member_repository.find_member())
            # print(dir(uow.repository))
