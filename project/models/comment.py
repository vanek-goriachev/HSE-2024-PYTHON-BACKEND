import uuid
from datetime import datetime as Datetime



class Comment:
    author_id: uuid.UUID
    text: str
    create_date: Datetime
    update_date: Datetime
    like_count: int

    def __init__(self, author_id: uuid.UUID, text: str) -> None:
        self.author_id = author_id
        self.text = text
        self.create_date = Datetime.now()
        self.update_date = self.create_date
        self.like_count = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_date = Datetime.now()

    def like(self) -> None:
        self.like_count += 1

    def dislike(self) -> None:
        self.like_count -= 1

    def __repr__(self) -> str:
        return f"<Comment from {self.author_id} at {self.create_date.strftime('%d-%m-%Y %H:%M:%s')}"

