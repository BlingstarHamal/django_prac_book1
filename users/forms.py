from django import forms
from django.core.exceptions import ValidationError
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"class":"form-control",
                    "placeholder": "사용자명 (3자리 이상)",
                    'autocomplete': 'off',
                    })
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"class":"form-control",
                    "placeholder": "비밀번호 (4자리 이상)", 
                    'autocomplete': 'asdadasdasd',
                    })
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"class":"form-control",
                    "placeholder": "사용자명 (3자리 이상)",
                    'autocomplete': 'off',
                    })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control",
                    "placeholder": "비밀번호 (4자리 이상)", 
                    'autocomplete': 'asdadasdasd',
                    }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control",
                    "placeholder": "비밀번호 (4자리 이상)", 
                    'autocomplete': 'asdadasdasd',
                    }))
    profile_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class":"form-control"}
        )
    )
    short_description = forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control",
                    "placeholder": "간단 소개",
                    'autocomplete': 'off',
                    })
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다.")
        return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password2", "비밀번호가 일치하지 않습니다.")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]
        user = User.objects.create_user(
            username=username,
            password=password1,
            profile_image=profile_image,
            short_description=short_description,
        )
        return user
