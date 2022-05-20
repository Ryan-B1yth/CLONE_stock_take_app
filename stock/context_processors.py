"""
Imports
"""


def base(request):
    """
    Base context
    """
    default_user = request.user
    return ({
        'default_user': default_user
        })
