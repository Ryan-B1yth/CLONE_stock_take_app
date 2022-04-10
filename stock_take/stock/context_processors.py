
def base(request):
    default_user = request.user
    return ({'default_user': default_user})
