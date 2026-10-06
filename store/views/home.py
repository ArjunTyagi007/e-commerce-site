from django.shortcuts import render, redirect
from django.views import View

from store.models.products import Products
from store.models.category import Category


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        if not request.session.get('customer'):
            return redirect('/login/?return_url=/')


        cart = request.session.get('cart', {})

        if product:
            pid = str(product)
            quantity = cart.get(pid, 0)

            if remove:
                if quantity <= 1:
                    cart.pop(pid, None)
                else:
                    cart[pid] = quantity - 1
            else:
                cart[pid] = quantity + 1

            request.session['cart'] = cart

        return redirect('homepage')

    def get(self, request):
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Products.get_all_products_by_categoryid(categoryID)
        else:
            products = Products.get_all_products()

        data = {
            'products': products,
            'categories': categories
        }

        return render(request, 'index.html', data)


def store(request):
    cart = request.session.get('cart', {})

    if not cart:
        request.session['cart'] = {}

    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {
        'products': products,
        'categories': categories
    }

    return render(request, 'index.html', data)