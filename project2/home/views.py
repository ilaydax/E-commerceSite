from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting
from product.models import Product

from product.models import Category

from product.models import Images


"""
def index(request):
    #setting = Setting.objects.get(pk=1)

    try:
        setting = Setting.objects.get(pk=1)
    except Setting.DoesNotExist:
        setting = None
    sliderData = Product.objects.all()[:4]
    category = Category.objects.all()
    context = {'setting': setting,
               'page':'home',
               'sliderData':sliderData}
    return render(request, 'index.html', context)

def index (request, products=None):
    category = Category.objects.all()
    context = {'products' : products, 'category' : category }
    return render (request, 'index.html',context)
"""


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata':sliderdata,
               'dayproducts':dayproducts,
               'lastproducts':lastproducts,
               'randomproducts':randomproducts}
    return render (request, 'index.html',context)

"""
def index(request):
    setting = Setting.objects.get(pk=1)
    sliderData = Product.objects.all()[:4]
    category = Category.objects.all()

    context = {'setting': setting,
               'category': category,
               'page':'home',
               'sliderData':sliderData}
    return render(request, 'index.html', context)
"""

def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,
               'category': category,
               'page':'hakkimizda'}
    return render(request,'hakkimizda.html',context)

def referanslarimiz(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,
               'category': category,
               'page':'referanslarimiz',
               }
    return render(request,'referanslarimiz.html',context)

def iletisim(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,
               'category': category,
               'page':'iletisim'}
    return render(request,'iletisim.html',context)




"""
def hakkimizda(request):
    #setting = Setting.objects.get(pk=1)

    try:
        setting = Setting.objects.get(pk=1)
    except Setting.DoesNotExist:
        setting = None
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)
    
def referanslarimiz(request):

    try:
        setting = Setting.objects.get(pk=1)
    except Setting.DoesNotExist:
        setting = None
    context = {'setting': setting, 'page':'referanslarimiz'}
    return render(request, 'referanslarimizda.html', context)
    
def iletisim(request):

    try:
        setting = Setting.objects.get(pk=1)
    except Setting.DoesNotExist:
        setting = None
    context = {'setting': setting, 'page':'iletisim'}
    return render(request, 'iletisim.html', context)
"""
def category_products (request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products':products,
               'category': category,
               'categorydata':categorydata
               }
    return render(request,'products.html',context)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'product': product,
               'category': category,
               'images': images,
               }

    #mesaj = "Ürün",id,"/",slug
    return render(request, 'product_detail.html', context)



