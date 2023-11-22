from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util
from django.urls import reverse
from markdown2 import Markdown
import random
from django import forms

class CreateNewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    title_body = forms.CharField(label="Content")

class EditPageForm(forms.Form):
    title = forms.CharField(label="Title")
    title_body = forms.CharField(label="Content")

    
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#def title(request, name):
#   return render(request, "encyclopedia/entries.html", {
#        "name": name.capitalize()
#        }) 

def CreateNewPage(request):
    if request.method == "POST":
        form = CreateNewPageForm(request.POST)
        if form.is_valid():

            titlex = form.cleaned_data["title"]
            content = form.cleaned_data["title_body"]

            util.save_entry(titlex, content)
            return title(request, titlex)
    
    else:
        return render(request, "encyclopedia/CreateNewPage.html", {
            "form": CreateNewPageForm()
    })

def RandomPage(request):

    return title(request, random.choice(util.list_entries()))
     
    
#(f"{name.capitalize()} \n\n Nothing here yet.")

def title(request, name):
    name_body = util.get_entry(name)
    markdowner = Markdown()
    return render(request, "encyclopedia/entries.html", {
        "name": name.capitalize(),
        "name_body": markdowner.convert(name_body)
       # "name_body": util.get_entry(name)
        })



def edit(request):
    if request.method == "POST":
        form = EditPageForm((request.POST))
        if form.is_valid():

            titlex = form.cleaned_data["title"]
            content = form.cleaned_data["title_body"]
            
            util.save_entry(titlex, content)
            return title(request, titlex)
    
    else:
        return render(request, "encyclopedia/edit.html", {
            "form": EditPageForm()
    })



