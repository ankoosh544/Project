from django.shortcuts import render, redirect
from app.forms import FoodItemsForm, CustomerForm
from app.models import FoodItemsModel,CustomerModel
from  django.contrib import messages
# Create your views here.
def showIndex(request):
    st = FoodItemsModel.objects.all()
    cd = CustomerModel.objects.all()
    return render(request, "index.html",{"foodform":FoodItemsForm(), "custform":CustomerForm(),"data":st,"data2":cd})
def saveFood(request):

    ff = FoodItemsForm(request.POST)
    if ff.is_valid():
        no = request.POST["ino"]
        na = request.POST["name"]
        p = request.POST["price"]
        print(no,na, p)
        FoodItemsModel(ino=no, name=na, price=p).save()
        messages.success(request,"Data Saved")
        return redirect("index.html")
    else:
        return showIndex(request)


def savecustomers(request):
    cf = CustomerForm(request.POST)
    if cf.is_valid():
        no = request.POST["cno"]
        n = request.POST["cname"]
        c = request.POST["contactno"]
        fidno = request.POST.getlist("foodid")
        b = CustomerModel(cno=no, cname=n,contactno=c)
        b.save()
        b.foodid.set(fidno)
        return showIndex(request)
    else:
        print("not Okay")
        return showIndex(request)