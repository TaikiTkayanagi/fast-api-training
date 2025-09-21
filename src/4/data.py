class User:
    def __init__(self, id:int, name: str):
        self.id = id
        self.name = name


user: list[User] = [
    User(id=1, name="Alice"),
    User(id=2, name="Bob"),
    User(id=3, name="Charlie"),
    User(id=4, name="Charlie"),
]

def get_user_by_id(user_id: int) -> User | None:
    for u in user:
        if u.id == user_id:
            return u
    return None