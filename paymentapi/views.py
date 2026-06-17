from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
import razorpay
def home(request):
    if request.method=="POST":
        a=request.POST.get('amount')
        request.session["l"]=a
        j=int(float(a)*100)
        request.session["amount"]=j
        return redirect("payment")
    return render(request,"home.html")



def payment(request):
    
    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID,
              settings.RAZORPAY_KEY_SECRET)
             
    )

    payment = client.order.create({
        "amount": int(request.session.get("amount")),   # Rs.500 in paise
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "payment": payment,
        "key": settings.RAZORPAY_KEY_ID,
        "k":int(request.session.get("l"))
    }

    return render(request, "payment.html", context)













def success(request):
    return HttpResponse("Payment Successful")