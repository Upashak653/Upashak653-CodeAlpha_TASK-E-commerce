from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import  Order,AboutUs, Feedback, ItemList, Items
from django.contrib import messages

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def OrderView(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number1 = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        order = request.POST.get('order')

        if phone_number1 != '' and email != '' and name != '':
         data1 = Order(Name=name, 
                         Phone_number=phone_number1,
                         Email=email,
                         Order=order)
         data1.save()
         messages.success(request,"Hurray we have got your order.Please take your seat for a while")
        else:
             print("Validation failed:")
             print(f"Name valid: {bool(name)}")
             print(f"Phone number valid: {phone_number1.isdigit() and len(phone_number1) == 10}")
             print(f"Email valid: {bool(email)}")
             print(f"Order valid: {bool(order.strip())}")
             messages.error(request, "try again")
    return render(request, 'book_table.html')



def FeedbackView(request):
     if request.method == 'POST':
       clientname= request.POST.get('user_name')
       clientexperience= request.POST.get('Description')
       clientrating=request.POST.get('total_rating')

       if clientname !='' and clientexperience !='' and clientrating != '' :
         data2= Feedback( User_name=clientname,
                       Description=clientexperience,
                       Rating=clientrating,)
         data2.save()
         messages.success(request,"Thank you for your rating")
       else:
             print("Validation failed:")
             print(f"Name valid: {bool(clientname)}")
             print(f"Email valid: {bool(clientexperience)}")
             print(f"Order valid: {bool(clientrating)}")
     return render(request,'feedback.html')
    