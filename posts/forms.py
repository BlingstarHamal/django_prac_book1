from django import forms
from posts.models import Comment, Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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

# 기존 포스트폼
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             "content",
#         ]
#         widgets = {
#             "content": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder" : "내용을 작성해 주세요",
#                 }
#             )
#         }
        

# 섬머노트 포스트 폼 

class NoticeWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {
            'title' : forms.TextInput(
                attrs={"class":"form-control mb-2",
                    "placeholder":"제목을 작성해 주세요",
                    }),
            'content' : SummernoteWidget(
                attrs={'summernote': {"placeholder" : "내용을 작성해 주세요",
                                        # 'width': '100%', 'height': '500px' ,
                                    },
                        "class": "summernote form-control",
                }),
        }