from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Path: {path}</p>
    <p>User-agent: {user_agent}</p>
    """)

def error(request):
    return HttpResponse("К сожалению произошла ошибка:(", status=400, reason='error')

def user(request, login='qwerty', folder="qwerty", post="0"):
    return HttpResponse(f"<h2>Login: {login} Folder: {folder} Post: {post}")
