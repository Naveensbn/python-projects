from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models import Products
from store.models import Category
from django.views import View


# Create your views here.
class Index(View):


    def post(self , request):
        product = request.POST.get('product') # it get the product_id
        remove = request.POST.get('remove')   # remove the product from card
        # print(cart,'CARD VALUE==')

        cart = request.session.get('cart')  # update the card session
        print(cart,'CARD VALUE==')
        if cart:
            quantity = cart.get(product)

            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # request.session. = cart
        print('cart...' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):  # this get method allowed get request
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):  # 1st execute store function
    cart = request.session.get('cart')
    print(cart,'store card---')
    # Checks if the cart exists in the session;
    # if not, it initializes an empty cart in the session.
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories
    print(data,'datavalue-----')
    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

'''
from django.views import View
from django.shortcuts import render,redirect,HttpResponseRedirect
from store.models import Category
from store.models import Products

class Index(View):

    def post(self,request):
        product = request.POST.get('product') # get product id 101
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(cart)
        if cart:
            quantity = cart.get(product)
        else:
            cart={}
            cart[product] = 1  # {101:1}
        request.session['card'] =cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_category_id(categoryID)
    else:
        products = Products.get_all_products()

    data={}
    data['products'] = products
    data['category'] = categories

    print('you are: ===', request.session.get('email') )
    m='hi hello'
    print(data,'-------')
    return render(request,'index.html', {'m':m})
'''
