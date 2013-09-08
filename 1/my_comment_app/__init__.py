from my_comment_app.models import CommentWithReply
from my_comment_app.forms import CommentFormWithReply

def get_model():
    return CommentWithReply

def get_form():
    return CommentFormWithReply