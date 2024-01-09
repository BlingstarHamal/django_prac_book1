from django import forms
from posts.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            # "user", 유저는 db에서 입력되어야함
            "post",
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "1",
                    "placeholder": "댓글달기...",
                    "style":"resize:none; border:none;"
                }
            )
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            )
        }
