from django.shortcuts import render


def index(request) -> None:
    return render(request, "editor/index.html")
