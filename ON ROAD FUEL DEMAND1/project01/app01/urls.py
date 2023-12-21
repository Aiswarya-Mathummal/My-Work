from django.urls import path
from . import views


urlpatterns = [
    # main
    path('', views.first, name='first'),
    path('login/', views.login, name='login'),
    path('reg/', views.Register, name='reg'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),

    # user
    path('user_home/<int:uid>', views.user_home, name='user_home'),
    path('customer_list/<int:uid>', views.customer_list, name='customer_list'),
    path('add_city/', views.add_city, name='add_city'),
    path('fuel_deta/<int:uid>', views.fuel_deta, name='fuel_deta'),
    path('req_form/<int:uid>/<int:id>', views.fuel_req, name='req_form'),
    path('customer_profile/<int:uid>', views.customer_profile,name='customer_profile'),
    path('edit_customer_profile/<int:uid>', views.edit_user_profile, name='edit_customer_profile'),
    path('request_history/<int:uid>', views.request_history, name='request_history'),


    # admin
    path('approve_bunk_details/<int:uid>', views.approve_bunk_details, name='approve_bunk_details'),
    path('list/<int:uid>', views.approved_users, name='list'),
    path('approve/<int:uid>/<int:id>', views.approve, name='approve'),
    path('reject/<int:uid>/<int:id>', views.reject, name='reject'),
    path('edit/<int:id>', views.edit_fuel, name='edit'),
    path('editu/<int:id>', views.edit_user, name='editu'),
    path('Delete/<int:uid>/<int:id>', views.delete, name='Delete'),
    path('adhome/<int:uid>', views.Adhome, name='adhome'),
    path('fuel_det/<int:uid>', views.fuel_det, name='fuel_det'),
    path('add_fuel_details/<int:uid>', views.add_fuel_details, name='add_fuel_details'),
    path('admin_profile/<int:uid>', views.admin_profile,name='admin_profile'),
    path('edit_admin_profile/<int:uid>', views.edit_admin_profile, name='edit_admin_profile'),

    # bunk
    path('petrol_bunk/', views.petrol_bunk_reg, name='petrol_bunk'),
    path('bunk_home/<int:uid>', views.bunk_home, name='bunk_home'),
    path('bunk_details/<int:uid>', views.bunk_details, name='bunk_details'),
    path('fuel_requests/<int:uid>', views.fuel_requests, name='fuel_requests'),
    path('bunk_profile/<int:uid>', views.bunk_profile, name='bunk_profile'),
    path('edit_bunk_profile/<int:uid>', views.edit_bunk_profile, name='edit_bunk_profile'),
    path('accept_request/<int:uid>/<int:id>', views.accept_request, name='accept_request'),
    path('approved_requests/<int:uid>', views.approved_requests, name='approved_requests'),




    path('logout/', views.logout, name='logout'),
    path('get_states/', views.get_states, name='get_states'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('calculate_price/', views.calculate_price, name='calculate_price'),

    # jquery
    path('nearby_bunks/<int:uid>/<bunks>', views.nearby_bunks, name='nearby_bunks'),
    path('get_bunk_status/', views.get_bunk_status, name='get_bunk_status'),
    path('activate_bunk/', views.activate_bunk, name='activate_bunk'),
    path('get_nearby_bunks/', views.get_nearby_bunks, name='get_nearby_bunks'),

]
