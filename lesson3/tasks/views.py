from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

tasks = ["foo", "bar", "baz"]


# Create your views here.


def index(request):
    return render(request, "tasks/index.html", {
        "tasks_html": tasks
    })


# 'NewTaskForm' is just the name of the class we just set for the HTML
# forms.Form is an inheritance and make it easier for us to use by Django
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


def add(request):

    # check if method is Post
    if request.method == "POST":

        # take in the data that the user submitted and save it as form if you leave empty the parenthesis,
        # the form is blank if you populate it with some data, its going to do is contains all of the data that the
        # user submitted when they submitted the form
        form = NewTaskForm(request.POST)

        # Check if form data is valid(server-side)
        # if the user is at the old page or not updated page, and the server
        # just updated, django will validate it and display some errors
        if form.is_valid():

            # isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # add the new task to our list of tasks
            tasks.append(task)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))

        else:

            # if the form is invalid, re-render the page with existing information
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })



