from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Product,Category

def product_list (resquest):
    products=Product.objects.all()
    categories = Category.objects.all()
    return render(resquest,'product_list.html',{'products':products,"categories":categories})

def product_detail(request,id):
    product=get_object_or_404(Product,id=id)
    return render(request,'product_detail.html',{'product':product})

def products_by_category (request,category_id):
    categories=Category.objects.all()
    selected_category= get_object_or_404(Category,id=category_id)
    products=Product.objects.filter(category=selected_category)
    return render(request,"product_list.html",
                  {"products":products,
                   "categories":categories,
                   "selected_category":selected_category})

def add_to_cart (request,product_id):
    cart=request.session.get('cart',{})
    cart[product_id]=cart.get(product_id,0)+1
    request.session['cart']=cart
    return redirect('product_list')

def cart_view(request):
    cart=request.session.get('cart',{})
    products=Product.objects.filter(id__in=cart.keys())
    cart_items=[]
    total_price=0
    for product in products:
        quantity=cart[str(product.id)]
        item_total=product.price*quantity
        total_price+=item_total
        cart_items.append({'product':product,'quantity':quantity,'item_total':item_total,})
    context={
        'cart_items':cart_items,
        "total_price":total_price
    }
    return render(request,'cart.html',context)

def decrease_quantity (request,product_id):
    cart=request.session.get('cart',{})
    if str(product_id) in cart :
        if cart[str(product_id)] >1:
            cart[str(product_id)]-=1
        else:
            del cart[str(product_id)]
    request.session['cart']=cart
    return redirect('cart_view')

def increase_quantity(request,product_id):
    cart=request.session.get('cart',{})
    cart[str(product_id)]=cart.get(str(product_id),0)+1
    request.session['cart']=cart
    return redirect('cart_view')