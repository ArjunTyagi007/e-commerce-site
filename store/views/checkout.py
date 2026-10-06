from django.shortcuts import redirect
from django.views import View

from store.models.customer import Customer
from store.models.products import Products
from store.models.orders import Order


class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        customer_id = request.session.get('customer')
        cart = request.session.get('cart', {})

        products = Products.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(
                customer=Customer(id=customer_id),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id))
            )

            order.save()

        request.session['cart'] = {}

        return redirect('cart')