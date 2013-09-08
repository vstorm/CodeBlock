from django import forms
from django.contrib.comments.forms import CommentForm
from my_comment_app.models import CommentWithReply

class CommentFormWithReply(CommentForm):
    rName = forms.CharField(widget=forms.HiddenInput,required=False)
    rContent = forms.CharField(widget=forms.HiddenInput,required=False)
    
    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return CommentWithReply

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the title field
        data = super(CommentFormWithReply,self).get_comment_create_data()
        data['rName'] = self.cleaned_data['rName']
        data['rContent'] = self.cleaned_data['rContent']
        return data
    