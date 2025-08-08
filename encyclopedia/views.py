from django.shortcuts import render
from django import forms
from markdown2 import markdown
from django.http import HttpResponseRedirect
from . import util

class NewArticleForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):
    content = util.get_entry(title)
    if content:
        content = markdown(content)
    else:
        content = markdown(f"## Article Not Found. \n \n Article {title} does not exist. \n You can create a new article by clicking on the 'Create New Article' button.")
    return render(request, "encyclopedia/read.html", {
        "title": title,
        "entry": content
    })

def add(request):
    if request.method == "POST":
        form = NewArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            md_content = f"# {title} \n\n {content}"

            util.save_entry(title, md_content)
            return HttpResponseRedirect(f"/wiki/{title}")
        else:
            return render(request, "encyclopedia/write.html", {
                "form": form
                })
        
    return render(request, 'encyclopedia/write.html', {
        "form" : NewArticleForm()
    })