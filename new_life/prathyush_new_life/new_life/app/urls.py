from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=''),
    path('user_reg/',views.user_reg_func,name='user_reg'),
    path('ambulance_driver_reg/',views.ambulance_driver_reg,name='ambulance_driver_reg'),
    path('hospital_reg/',views.hospital_reg,name='hospital_reg'),
    path('login/',views.login,name='login'),
    path('admin_home/<int:uid>',views.admin_home,name='admin_home'),
    path('user_home/<int:uid>',views.user_home,name='user_home'),
    path('ambulance_driver_home/<int:uid>',views.ambulance_driver_home,name='ambulance_driver_home'),
    path('hospital_home/<int:uid>',views.hospital_home,name='hospital_home'),
    path('admin_profile/<int:uid>', views.admin_profile, name='admin_profile'),
    path('edit_admin_profile/<int:uid>', views.edit_admin_profile, name='edit_admin_profile'),
    path('user_profile/<int:uid>', views.user_profile, name='user_profile'),
    path('edit_user_profile/<int:uid>', views.edit_user_profile, name='edit_user_profile'),
    path('ambulance_driver_profile/<int:uid>', views.ambulance_driver_profile, name='ambulance_driver_profile'),
    path('edit_ambulance_driver_profile/<int:uid>', views.edit_ambulance_driver_profile, name='edit_ambulance_driver_profile'),
    path('hospital_profile/<int:uid>', views.hospital_profile, name='hospital_profile'),
    path('edit_hospital_profile/<int:uid>', views.edit_hospital_profile, name='edit_hospital_profile'),
    path('users_list/<int:uid>',views.users_list,name='users_list'),
    path('delete_user/<int:uid>/<int:id>', views.delete_user, name='delete_user'),
    path('ambulance_drivers_list/<int:uid>',views.ambulance_drivers_list,name='ambulance_drivers_list'),
    path('delete_ambulance_driver/<int:uid>/<int:id>',views.delete_ambulance_driver,name='delete_ambulance_driver'),
    path('approve_ambulance_driver_list/<int:uid>',views.approve_ambulance_driver_list,name='approve_ambulance_driver_list'),
    path('approve_ambulance_driver/<int:uid>/<int:id>',views.approve_ambulance_driver,name='approve_ambulance_driver'),
    path('reject_ambulance_driver/<int:uid>/<int:id>',views.reject_ambulance_driver,name='reject_ambulance_driver'),
    path('hospitals_list/<int:uid>',views.hospitals_list,name='hospitals_list'),
    path('delete_hospital/<int:uid>/<int:id>', views.delete_hospital, name='delete_hospital'),
    path('approve_hospitals_list/<int:uid>', views.approve_hospitals_list, name='approve_hospitals_list'),
    path('approve_hospital/<int:uid>/<int:id>', views.approve_hospital, name='approve_hospital'),
    path('reject_hospital/<int:uid>/<int:id>', views.reject_hospital, name='reject_hospital'),
    path('ambulance_details/<int:uid>',views.ambulance_details,name='ambulance_details'),
    path('add_ambulance_details/<int:uid>',views.add_ambulance_details,name='add_ambulance_details'),
    path('edit_ambulance_details/<int:uid>/<int:id>',views.edit_ambulance_details,name='edit_ambulance_details'),
    path('book_ambulance/<int:uid>/',views.book_ambulance,name='book_ambulance'),
    # path('book_ambulance_city/<int:uid>',views.book_ambulance_city,name='book_ambulance_city'),
    path('confirm_booking/<int:uid>/<int:id>/<int:driver_id>',views.confirm_booking,name='confirm_booking'),
    path('track_booking/<int:uid>/<int:id>',views.track_booking,name='track_booking'),
    path('track_patient/<int:uid>/<int:id>',views.track_patient,name='track_patient'),
    path('track_request/<int:uid>/<int:id>',views.track_request,name='track_request'),
    path('cancel_booking/<int:uid>/<int:id>',views.cancel_booking,name='cancel_booking'),
    path('booking_history/<int:uid>/',views.booking_history,name='booking_history'),
    path('patient_details/<int:uid>/',views.patients_details,name='patient_details'),
    path('ambulance_request/<int:uid>/',views.ambulance_request,name='ambulance_request'),
    path('request_history/<int:uid>/',views.request_history,name='request_history'),
    # path('update_location/<int:uid>/',views.update_location,name='update_location'),
    path('create_complaint/<int:uid>/<int:id>',views.create_complaint,name='create_complaint'),
    path('give_reply/<int:uid>/<int:id>',views.give_reply,name='give_reply'),
    path('complaints_list/<int:uid>',views.complaints_list,name='complaints_list'),
    path('view_complaints_list/<int:uid>',views.view_complaints_list,name='view_complaints_list'),
    path('get_vehicle_status/',views.get_vehicle_status,name='get_vehicle_status'),
    path('activate_ambulance/',views.activate_ambulance,name='activate_ambulance'),
    path('get_states/',views.get_states,name='get_states'),
    path('get_cities/',views.get_cities,name='get_cities'),
    path('get_location/',views.get_location,name='get_location'),
    path('get_hospitals/',views.get_hospitals,name='get_hospitals'),
    path('new_request/',views.new_request,name='new_request'),
    path('logout/',views.logout,name='logout'),
]