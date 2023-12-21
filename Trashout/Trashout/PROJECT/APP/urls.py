from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register_views/',views.customer_reg,name='register_template'),
    path('login/',views.login,name='login'),
    path('regi/',views.recycling_reg,name='regi'),
    path('help/',views.help,name='help'),
    path('recycling_reg/',views.recycling_reg,name='recy_reg'),
    path('approve/<int:uid>/<int:id>', views.approve, name='approve'),
    path('reject/<int:uid>/<int:id>', views.reject, name='reject'),
    # path('gallery/<int:uid>/', views.gallery1, name='gallery'),
    path('recycling_list/<int:uid>', views.recycling_list, name='recycling_list'),
    path('customer_list/<int:uid>',views.customer_list,name='customer_list'),
    path('approve_recycling_unit/<int:uid>',views.approve_recycling_unit,name='approve_recycling_unit'),

    path('delete_customer/<int:uid>/<int:id>', views.delete_customer, name='delete_customer'),
    path('delete_recycling_unit/<int:uid>/<int:id>', views.delete_recycling_unit, name='delete_recycling_unit'),

    path('customer_list/<int:uid>', views.customer_list, name='customer_list'),
    path('category_list/<int:uid>', views.category_list, name='category_list'),
    path('customer_product_list/<int:uid>', views.customer_product_list, name='customer_product_list'),
    path('product_list/<int:uid>', views.product_list, name='product_list'),
    path('add_category/<int:uid>', views.add_category, name='add_category'),
    path('add_product/<int:uid>', views.add_product, name='add_product'),
    path('delete_category/<int:uid>/<int:id>', views.delete_category, name='delete_category'),
    path('delete_product/<int:uid>/<int:id>', views.delete_product, name='delete_product'),
    path('edit_category/<int:uid>/<int:id>', views.edit_category, name='edit_category'),
    path('edit_product/<int:uid>/<int:id>', views.edit_product, name='edit_product'),
    path('product-details/<int:uid>',views.product_details,name='product-details'),
    path('admin_delete_product/<int:uid>/<int:id>', views.admin_delete_product, name='admin_delete_product'),
    path('get_products/<int:uid>/<int:id>', views.get_products, name='get_products'),
    path('product_more_details/<int:uid>/<int:id>', views.product_more_details, name='product_more_details'),
    path('approvecustomer/<int:uid>', views.approvecustomer, name='approvecustomer'),
    path('approve_recycling_unit_list/<int:uid>', views.approve_recycling_unit_list, name='approve_recycling_unit_list'),
    path('approve_recycling_unit/<int:uid>/<int:id>', views.approve_recycling_unit, name='approve_recycling_unit'),
    path('reject_recycling_unit/<int:uid>/<int:id>', views.reject_recycling_unit, name='reject_recycling_unit'),
    path('admin_home/<int:uid>', views.admin_home, name='admin_home'),
    path('customer_home/<int:uid>', views.customer_home, name='customer_home'),
    path('recy_home/<int:uid>', views.recycling_unit_home, name='recy_home'),
    path('customer_profile/<int:uid>', views.customer_profile, name='customer_profile'),
    path('recycling_unit_profile/<int:uid>', views.recycling_unit_profile, name='recycling_unit_profile'),
    path('edit_recycling_unit_profile/<int:uid>', views.edit_recycling_unit_profile, name='edit_recycling_unit_profile'),
    path('edit_customer_profile/<int:uid>', views.edit_customer_profile, name='edit_customer_profile'),
    path('buyer_product_request/<int:uid>/<int:id>', views.buyer_product_request, name='buyer_product_request'),
    path('view_product_request/<int:uid>', views.view_product_request, name='view_product_request'),
    path('orders/<int:uid>', views.orders, name='orders'),
    path('approve_request/<int:uid>/<int:id>', views.approve_request, name='approve_request'),
    path('reject_request/<int:uid>/<int:id>', views.reject_request, name='reject_request'),
    path('view_approved_product_request/<int:uid>', views.view_approved_product_request, name='view_approved_product_request'),
    path('approved_orders/<int:uid>', views.approved_orders, name='approved_orders'),
    path('cancel_request/<int:uid>/<int:id>', views.cancel_request, name='cancel_request'),
    path('cancel_order/<int:uid>/<int:id>', views.cancel_order, name='cancel_order'),
    path('product_collected/<int:uid>/<int:id>', views.product_collected, name='product_collected'),
    path('sold_products/<int:uid>', views.sold_products, name='sold_products'),
    path('order_history/<int:uid>', views.order_history, name='order_history'),
    path('check_expiry_date/', views.check_expiry_date, name='check_expiry_date'),
    path('unit_get_products/<int:uid>/<int:id>', views.unit_get_products, name='unit_get_products'),
    path('unit_product_more_details/<int:uid>/<int:id>', views.unit_product_more_details, name='unit_product_more_details'),
    path('unit_product_request/<int:uid>/<int:id>', views.unit_product_request, name='unit_product_request'),
    path('view_expired_products/<int:uid>', views.view_expired_products, name='view_expired_products'),
    path('accepted_products/<int:uid>', views.accepted_products, name='accepted_products'),
    path('recycle_sold_products/<int:uid>', views.recycle_sold_products, name='recycle_sold_products'),
    path('delete_recycle_product/<int:uid>/<int:id>', views.delete_recycle_product, name='delete_recycle_product'),
    path('accepted_orders/<int:uid>', views.accepted_orders, name='accepted_orders'),
    path('recycle_order_history/<int:uid>', views.recycle_order_history, name='recycle_order_history'),
    path('recycle_product_collected/<int:uid>/<int:id>', views.recycle_product_collected, name='recycle_product_collected'),

    path('update_rating/', views.update_rating, name='update_rating'),
    path('recycle_update_rating/', views.recycle_update_rating, name='recycle_update_rating'),

    path('logout/', views.logout, name='logout'),

]







