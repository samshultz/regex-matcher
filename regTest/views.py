from django.shortcuts import render
from .forms import RegexForm
from .utils import regex_methods, process_regex_form_data


def index(request):
    regex_form = ''
    single_match = ''
    multi_match = ''
    error = ''
    methods = regex_methods()
    if request.method == "POST":
        regex_form = RegexForm(request.POST)
        if regex_form.is_valid():
            cd = regex_form.cleaned_data
            pattern, flags, text= cd['pattern'], cd['flags'], cd['text']
            method = cd['method']
            try:
                single_match, multi_match = process_regex_form_data(pattern, text,
                    methods, method)
            except:
                error = "Invalid RegEX. Try Again"
            
    else:
        regex_form = RegexForm()
    return render(request, 'regTest/index.html', {'regex_form': regex_form,
        "multi_match": multi_match, "single_match": single_match,
        'error': error})
