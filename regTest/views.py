from django.shortcuts import render
from django.views.generic import View
from .forms import RegexForm
from .utils import regex_methods, process_regex_form_data


class Index(View):
    form_class = RegexForm
    template_name = "regTest/index.html"

    def get(self, request):
        regex_form = self.form_class(initial={'method': 're.match'})
        return render(request, self.template_name, {'regex_form': regex_form})

    def post(self, request):
        single_match, multi_match, error = '', '', ''
        
        methods = regex_methods()
        regex_form = self.form_class(request.POST)

        if regex_form.is_valid():
            cd = regex_form.cleaned_data
            pattern, flags, text= cd['pattern'], cd['flags'], cd['text']
            method = cd['method']
            try:
                single_match, multi_match = process_regex_form_data(pattern,
                    flags, text, methods, method)
            except:
                error = "Invalid RegEX. Try Again"
        return render(request, self.template_name, {'regex_form': regex_form,
            "multi_match": multi_match, "single_match": single_match,
            'error': error})
