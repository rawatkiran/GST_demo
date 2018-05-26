from django.shortcuts import render
import requests
import datetime
from django.http import HttpResponse
# Create your views here.
import time
from gst.models import Product
def index(request):
    data=Product.objects.all()
    return render(request,'gst/index.html',{'data':data})
def chart(request):
    gst5 = Product.objects.filter(gst=5).count()
    gst12 = Product.objects.filter(gst=12).count()
    gst18 = Product.objects.filter(gst=18).count()
    gst28 = Product.objects.filter(gst=28).count()

    data=Product.objects.all()
    dataCount = data.count()
    gst5p = (gst5/dataCount)*100
    gst12p = (gst12/dataCount)*100
    gst18p = (gst18/dataCount)*100
    gst28p = (gst28/dataCount)*100
    #print(gst28p)
    context = {
        "data": data,
        "gst5p": gst5,
        "gst12p": gst12,
        "gst18p": gst18,
        "gst28p": gst28,
    }
    return render(request,'gst/chart.html', context)


# noinspection PyInterpreter
def add_product(request):
    print("Form will be submitted here")
    nam = request.POST['name']
    price = request.POST['price']
    gst = request.POST['gst']
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    totalPrice = requests.get("http://api.mathjs.org/v4/?expr="+str(price)+"%2B"+str(price)+"*("+str(gst)+"%2F"+str(100)+")").text
    #print(totalPrice)
    product = Product(product_name=nam, product_price=price, gst= gst,totalPrice=totalPrice, timestamp=st)
    product.save()
    data = Product.objects.all()
    return render(request, 'gst/index.html',{'data':data})
