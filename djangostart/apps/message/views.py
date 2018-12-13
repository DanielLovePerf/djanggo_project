# _*_ coding: utf-8 _*_
from django.shortcuts import render

from .models import UserMessage
# Create your views here.

# def getform(request):
#     return render(request, 'message_form.html')


def getform(request):
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print message.name
    return render(request, 'message_form.html')
