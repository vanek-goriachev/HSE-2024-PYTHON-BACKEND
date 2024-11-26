from datetime import datetime as Datetime


class Comment:
    def __init__(self, author_id, text):
        self.author_id = author_id
        self.text = text
        self.create_data = Datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text):
        self.text = new_text
        self.update_data = Datetime.now()

    def like(self):
        self.like_count += 1

    def dislike(self):
        self.like_count -= 1

    def __repr__(self):
        return f"<Comment from {self.author_id} at {self.create_data.strftime('%d-%m-%Y %H:%M:%s')}"

