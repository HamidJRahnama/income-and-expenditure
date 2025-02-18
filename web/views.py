from django.shortcuts import render
from django.http import HttpResponse  # برای ارسال پاسخ به کاربر

# Create your views here.
def expense(request):
    print("++++++++++++++")
    print(request)
    print("++++++++++++++")

    # ارسال یک پاسخ ساده برای کاربر (میتوانید پیام خاصی هم بفرستید)
    return HttpResponse("Expense Submitted Successfully!")  # پاسخ ساده به کاربر

# def expense(req):
#     print("++++++++++++++")
#     print("submit expense")
#     print("++++++++++++++")
#
#     return HttpResponse("Expense Submitted Successfully")