from django.shortcuts import render, redirect


def index(request):
    return redirect("posts:feeds")
    # if request.user.is_authenticated:
    #     return redirect("posts:feeds")
    # else:
    #     return redirect("users:login")
