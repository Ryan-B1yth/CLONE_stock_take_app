"""
Imports
"""
# Docstring only for PEP8 compliance


def base(request):
    """
    Base context
    """
    default_user = request.user
    return ({
        'default_user': default_user
        })
