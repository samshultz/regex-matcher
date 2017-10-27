from django import forms


class RegexForm(forms.Form):
    """A Python Regular Expression (RegEx) form.
    
    This form is displayed to the user to get the regex pattern, and search the
    provided text for a match applying the giving methods and/or flags.
    
    Extends:
        forms.Form
    
    Variables:
        FLAG_LIST {list} -- A list of regex flags
        METHOD_LIST {list} -- A list of regex method
        pattern {[str]} -- A regex pattern
        flags {[checkbox]} -- Checkboxes of regex flags
        text {[stri]} -- Text to search
        methods {[radio button]} -- Radio Button of Regex flags
    """
    FLAG_LIST = [
        ('re.ascii', 're.ASCII'),
        ('re.ignorecase', 're.IGNORECASE'),
        ('re.multiline', 're.MULTILINE'),
        ('re.dotall', 're.DOTALL'),
        ('re.verbose', 're.VERBOSE')
    ]
    METHOD_LIST = [
        ('re.search', 're.search'),
        ('re.match', 're.match'),
        ('re.fullmatch', 're.fullmatch'),
        ('re.findall', 're.findall'),
        ('re.finditer', 're.finditer')
    ]
    pattern = forms.CharField()
    flags = forms.MultipleChoiceField(choices=FLAG_LIST,
        widget=forms.CheckboxSelectMultiple, required=False)
    text = forms.CharField(widget=forms.Textarea)
    method = forms.ChoiceField(choices=METHOD_LIST, widget=forms.RadioSelect,
        required=False)
