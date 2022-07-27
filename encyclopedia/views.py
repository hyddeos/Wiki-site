from cgi import test
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms
from . import util
import markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, subject):
# Handels request such as url/X 

# If subject exists, get that. Otherwise render errormassage.

    if util.get_entry(subject):
        return render(request, "encyclopedia/wikisubject.html", {
        "subjecttitel": subject,
        "subject": markdown.markdown(util.get_entry(subject))
        })
    else:
        return render(request, "encyclopedia/wikisubject.html",)




def search(request):
# When you use the search bar 

    q = request.GET.get("q")

    if not util.get_entry(q):
    # Filter and get search results for q. Passed the results to searchword.html
        results = []   
        for subject in util.list_entries():
            if q in subject:
                results.append(subject)       

        if request.method == "GET":
            return render(request, 'encyclopedia/searchword.html', {
                'results': results, 
                'q':q.capitalize()
            })
    else:
    # Else there is a 100% and you get redirected to that wiki
        return render(request, "encyclopedia/wikisubject.html", {
            "subject": markdown.markdown(util.get_entry(q))
        })


def newpage(request):
    # Makes a new entry

    if request.method == 'POST': 

        title = request.POST["title"]
        text = request.POST["text"]

        if util.get_entry(title):
            # This entry already exists
            return render(request, "encyclopedia/newpage.html", {
            "form": forms.EntryForm(),
            "error": util.get_entry(title)
        })          
        else:
            # Save the file            
            util.save_entry(title, text)
            # After save takes user to that new entry          
            return redirect("/" + title)

    # Runs this is request is Get
    return render(request, "encyclopedia/newpage.html", {
        "form": forms.EntryForm()
    })

def editpage(request):
# Edits the page

    edit = request.GET.get("edit")
    # Removes "/" Before the edit term
    edit = edit[1::]
    # Load data from md file
    data_file = open(f'entries/{ edit }.md', 'r')       
    text = data_file.read()

    if request.method == 'POST':
        
        text = request.POST["updated"]
        util.save_entry(edit, text)

        return redirect("/" + edit)


    # Runs this is request is Get
    return render(request, "encyclopedia/editpage.html", {
        "edit": edit,
        "text": text
    })

def random_entry(request):
    # Sends user to random wiki
    return redirect("/" + random.choice(util.list_entries()))


       
  

  
