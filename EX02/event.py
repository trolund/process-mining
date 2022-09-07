import datetime


class Event:
    name: str
    case_id: str
    time: datetime
    user_id: str

    def __init__(self, name, case_id, user_id, date):
        self.time = date
        self.name = name
        self.case_id = case_id
        self.user_id = user_id

    def __lt__(self, other):
        return self.name < other.name