from django.shortcuts import render
# from django.views.generic import ListView

from support.models import Faq

# Create your views here.
def index(request):
    return render(request, 'index.html')

def faq_list_view(request) :
    object_list = Faq.objects.all().order_by('-id')
    return render(request, 'support/FAQ_list.html', {'object_list' : object_list})

def faq_detail_view(request, id):
    # if request.method == 'POST' :
    #     Faq.question
    return render(request, 'support/FAQ_detail.html')

def faq_create_view(request):
    return render(request, 'support/FAQ_form.html')

def faq_update_view(request, id):
    return render(request, 'support/FAQ_form.html')

def faq_delete_view(request, id):
    return render(request, 'support/FAQ_confirm_delete.html')