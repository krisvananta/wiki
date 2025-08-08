from django.shortcuts import render
from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title,):
    return render(request, "encyclopedia/read.html", {
        "entry": util.get_entry(title)
    })

def add(request):
    return