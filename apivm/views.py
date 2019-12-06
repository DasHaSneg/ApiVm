from django.shortcuts import render

# Create your views here.
def messages_list (request):
    return render(request, 'apivm/messages_list.html', {})