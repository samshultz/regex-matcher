import re

def regex_methods():
    return {
    're.search': re.search,
    're.match': re.match,
    're.fullmatch': re.fullmatch,
    're.findall': re.findall,
    're.finditer': re.finditer,
    }

def process_regex_form_data(pattern, flags, text, methods, method):
    """Process data returned by the regex form view.
    Takes the pattern returned from the regex form, the text
    to be matched as provided by the form, the methods returned
    from the reges_methods function, and the method returned from
    the regex form as parameters.

    It matches this pattern against the given text given the regex
    method provided.

    Variables:
        pattern {str} -- str of a regExp pattern
        flags {list} -- A list of regExp flags
        text {[str]} -- A text to match the regExp pattern against
        methods {[dict]} -- dictionary of regExp methods where the keys are
        str of regExp methods and the values are the literal regExp methods e.g
        >>> {'re.finditer': re.finditer, ... }
        method {[str]} -- A regExp method
    """
    multi_match = ''
    single_match = ''
    flags = "|".join(flags)
    regex = eval('re.compile(r"{}", {})'.format(pattern, flags))
    # if the user fails to select a method it defaults to the re.match method
    if not method:
        match = regex.match(text)
        # else convert the selected method from a string to a regex object by
        # searching regex_method returned by the regex_methods function.
    else:
        match = methods[method](regex, text)
        # if a match is found ...
        if match is not None:
            # check if the method used is the "re.findall" or "re.finditer"
            # method as these do not support the match.group() method
            if method == 're.findall':
                multi_match = match
            elif method == 're.finditer':
                multi_match = [i.group() for i in match]
            else:
                single_match = match.group()
    return single_match, multi_match