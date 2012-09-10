from django.shortcuts import render

import forms

def index(request):

    data = {}

    form = forms.MyFirstForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data['is_valid_form'] = True


    data['form'] = form
    return render(request, "index.html", data)
