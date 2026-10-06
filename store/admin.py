from django.contrib import admin

from store.models.category import Category
from store.models.customer import Customer
from store.models.products import Products
from store.models.orders import Order


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)