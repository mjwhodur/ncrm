from django.shortcuts import render

# Create your views here.
def landing(request):
    if request.user.is_aunthenticated():
        return render(request, template_name='home/panel.html')
    else:
        return render(request, template_name='home/landing.html')

def login(request): # TODO Comment
    """

    :param request:
    :return:
    """
    pass

def logout(request): # TODO COMMENT
    """

    :param request:
    :return:
    """
    pass

def change_password(request): #TODO COMMENT
    """

    :param request:
    :return:
    """
    pass

