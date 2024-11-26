from models.comment import Comment


def get_ordered_comments_by_likes(comments: list[Comment], order="desc"):
    return sorted(
        comments,
        key=lambda comment: comment.like_count,
        reverse=(order.lower() == 'desc'),
    )
