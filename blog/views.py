from django.http import HttpResponse

def post_list(request):
    return HttpResponse("Привет! это мой первый блог на Django :)")
