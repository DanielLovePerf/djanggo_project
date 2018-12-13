# _*_ coding: utf-8 _*_
from django.shortcuts import render

from .models import UserMessage
# Create your views here.

# def getform(request):
#     return render(request, 'message_form.html')


def getform(request):
    # get all data
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print message.name

    # delete data
    # all_messages = UserMessage.objects.filter(name='bobby', address='beijing')
    # for message in all_messages:
    #     print message.delete()

    # save data
    # user_message = UserMessage()
    # user_message.name = "bobby2"
    # user_message.message = "helloworld2"
    # user_message.address = "上海"
    # user_message.object_id = "helloworld2"
    # user_message.save()

    # get data from message_form and save
    # if request.method == "POST":
    #     name = request.POST.get('name', '')  # 空为默认值
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld4"
    #     user_message.save()

    return render(request, 'message_form.html')
