from django.urls import path
from .views import HomeView, ShopView, BlogView, CheckoutView, OrderSummaryView, ItemDetailView, about, contact, add_to_cart, add_single_item_to_cart, remove_from_cart, remove_single_item_from_cart, PaymentView, addCouponView, RequestRefundView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', addCouponView.as_view(), name='add-coupon'),
    path('add-single-item-to-cart/<slug>/',
         add_single_item_to_cart, name='add-single-item-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
