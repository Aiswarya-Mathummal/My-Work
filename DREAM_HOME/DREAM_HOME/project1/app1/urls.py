
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),

    path('admin_home/<int:uid>/',views.admin_home, name='admin_home'),
    path('architect_home/<int:uid>/', views.architect_home, name='architect_home'),
    path('customer_home/<int:uid>/', views.customer_home, name='customer_home'),
    path('exterior_designer_home/<int:uid>/', views.exterior_designer_home, name='exterior_designer_home'),
    path('interior_designer_home/<int:uid>/', views.interior_designer_home, name='interior_designer_home'),

    path('customer_reg/', views.customer_reg, name='customer_reg'),
    path('architect_reg/', views.architect_reg, name='architect_reg'),
    path('interior_designer_reg/', views.interior_designer_reg, name='interior_designer_reg'),
    path('exterior_designer_reg/', views.exterior_designer_reg, name='exterior_designer_reg'),

    path('customer_list/<int:uid>/', views.view_customer_list, name='customer_list'),
    path('architect_list/<int:uid>/', views.view_architect_list, name='architect_list'),
    path('interior_designer_list/<int:uid>/', views.view_interior_designer_list, name='interior_designer_list'),
    path('exterior_designer_list/<int:uid>/', views.view_exterior_designer_list, name='exterior_designer_list'),

    path('delete_customer/<int:uid>/<int:id>',views.delete_customer,name='delete_customer'),
    path('delete_architect/<int:uid>/<int:id>', views.delete_architect, name='delete_architect'),
    path('delete_interior_designer/<int:uid>/<int:id>', views.delete_interior_designer, name='delete_interior_designer'),
    path('delete_exterior_designer/<int:uid>/<int:id>', views.delete_exterior_designer, name='delete_exterior_designer'),

    path('approve_architect_list/<int:uid>',views.approve_architect_list,name='approve_architect_list'),
    path('approve_architect/<int:uid>/<int:id>',views.approve_architect,name='approve_architect'),
    path('reject_architect/<int:uid>/<int:id>',views.reject_architect,name='reject_architect'),

    path('approve_interior_designer_list/<int:uid>',views.approve_interior_designer_list,name='approve_interior_designer_list'),
    path('approve_interior_designer/<int:uid>/<int:id>',views.approve_interior_designer,name='approve_interior_designer'),
    path('reject_interior_designer/<int:uid>/<int:id>',views.reject_interior_designer,name='reject_interior_designer'),

    path('approve_exterior_designer_list/<int:uid>',views.approve_exterior_designer_list,name='approve_exterior_designer_list'),
    path('approve_exterior_designer/<int:uid>/<int:id>',views.approve_exterior_designer,name='approve_exterior_designer'),
    path('reject_exterior_designer/<int:uid>/<int:id>',views.reject_exterior_designer,name='reject_exterior_designer'),

    path('customer_profile/<int:uid>', views.customer_profile, name='customer_profile'),
    path('edit_customer_profile/<int:uid>', views.edit_customer_profile, name='edit_customer_profile'),

    path('architect_profile/<int:uid>', views.architect_profile, name='architect_profile'),
    path('edit_architect_profile/<int:uid>', views.edit_architect_profile, name='edit_architect_profile'),

    path('interior_designer_profile/<int:uid>', views.interior_designer_profile, name='interior_designer_profile'),
    path('edit_interior_designer_profile/<int:uid>', views.edit_interior_designer_profile, name='edit_interior_designer_profile'),

    path('exterior_designer_profile/<int:uid>', views.exterior_designer_profile, name='exterior_designer_profile'),
    path('edit_exterior_designer_profile/<int:uid>', views.edit_exterior_designer_profile,name='edit_exterior_designer_profile'),

    path('admin_profile/<int:uid>', views.admin_profile, name='admin_profile'),
    path('edit_admin_profile/<int:uid>', views.edit_admin_profile, name='edit_admin_profile'),

#-----------------------------------------------plans-------------------------------------------------------------------

#architect --- add,edit,delete,list plans

    path('add_plan/<int:uid>', views.add_plan, name='add_plan'),

    path('edit_plan/<int:uid>/<int:id>', views.edit_plan, name='edit_plan'),
    path('plan_list/<int:uid>', views.plan_list, name='plan_list'),
    path('delete_plan/<int:uid>/<int:id>', views.delete_plan, name='delete_plan'),

#admin  --- approve,reject,list plans

    path('approve_plan_list/<int:uid>', views.approve_plan_list, name='approve_plan_list'),
    path('approve_plan/<int:uid>/<int:id>', views.approve_plan, name='approve_plan'),
    path('reject_plan/<int:uid>/<int:id>', views.reject_plan, name='reject_plan'),

    path('admin_plan_list/<int:uid>/', views.admin_plan_list, name='admin_plan_list'),
    path('admin_delete_plan/<int:uid>/<int:id>', views.admin_delete_plan, name='admin_delete_plan'),

#--------------------------------Exterior designs-----------------------------------------------------------------------

#Exterior designer-add,edit,delete,list designs

    path('add_exterior_design/<int:uid>', views.add_exterior_design, name='add_exterior_design'),

    path('edit_exterior_design/<int:uid>/<int:id>', views.edit_exterior_design, name='edit_exterior_design'),
    path('exterior_design_list/<int:uid>', views.exterior_design_list, name='exterior_design_list'),
    path('delete_exterior_design/<int:uid>/<int:id>', views.delete_exterior_design, name='delete_exterior_design'),

#admin- approve,reject,list designs

    path('approve_exterior_design_list/<int:uid>', views.approve_exterior_design_list, name='approve_exterior_design_list'),
    path('approve_exterior_design/<int:uid>/<int:id>', views.approve_exterior_design, name='approve_exterior_design'),
    path('reject_exterior_design/<int:uid>/<int:id>', views.reject_exterior_design, name='reject_exterior_design'),

    path('admin_exterior_design_list/<int:uid>/', views.admin_exterior_design_list, name='admin_exterior_design_list'),
    path('admin_delete_exterior_design/<int:uid>/<int:id>', views.admin_delete_exterior_design, name='admin_delete_exterior_design'),


#------------------------------------------------interior Design--------------------------------------------------------


#Interior designer-add,edit,delete,list designs

    path('add_interior_design/<int:uid>', views.add_interior_design, name='add_interior_design'),

    path('edit_interior_design/<int:uid>/<int:id>', views.edit_interior_design, name='edit_interior_design'),
    path('interior_design_list/<int:uid>', views.interior_design_list, name='interior_design_list'),
    path('delete_interior_design/<int:uid>/<int:id>', views.delete_interior_design, name='delete_interior_design'),

#admin- approve,reject,list designs

    path('approve_interior_design_list/<int:uid>', views.approve_interior_design_list, name='approve_interior_design_list'),
    path('approve_interior_design/<int:uid>/<int:id>', views.approve_interior_design, name='approve_interior_design'),
    path('reject_interior_design/<int:uid>/<int:id>', views.reject_interior_design, name='reject_interior_design'),

    path('admin_interior_design_list/<int:uid>/', views.admin_interior_design_list, name='admin_interior_design_list'),
    path('admin_delete_interior_design/<int:uid>/<int:id>', views.admin_delete_interior_design, name='admin_delete_interior_design'),


#customer- view plans-------------------------------------------------------------------------------------------------------

    path('view_plan_list/<int:uid>', views.view_plan_list, name='view_plan_list'),
    path('user_book_plan/<int:uid>/<int:aid>/<int:pid>', views.user_book_plan, name='user_book_plan'),

    path('view_plan_requests/<int:uid>', views.view_plan_requests, name='view_plan_requests'),
    path('approve_plan_request/<int:uid>/<int:id>', views.approve_plan_request, name='approve_plan_request'),
    path('reject_plan_request/<int:uid>/<int:id>', views.reject_plan_request, name='reject_plan_request'),

    path('approved_plan_requests/<int:uid>', views.approved_plan_requests, name='approved_plan_requests'),
    path('view_my_plan_requests/<int:uid>', views.view_my_plan_requests, name='view_my_plan_requests'),
    path('view_approved_plan_requests/<int:uid>', views.view_approved_plan_requests, name='view_approved_plan_requests'),

#customer- view  int designs-------------------------------------------------------------------------------------------------------


    path('view_interior_design_list/<int:uid>/', views.view_interior_design_list, name='view_interior_design_list'),
    path('user_book_interior_design/<int:uid>/<int:aid>/<int:pid>', views.user_book_interior_design, name='user_book_interior_design'),

    path('view_interior_design_requests/<int:uid>', views.view_interior_design_requests, name='view_interior_design_requests'),
    path('approve_interior_design_request/<int:uid>/<int:id>', views.approve_interior_design_request, name='approve_interior_design_request'),
    path('reject_interior_design_request/<int:uid>/<int:id>', views.reject_interior_design_request, name='reject_interior_design_request'),

    path('approved_interior_design_requests/<int:uid>', views.approved_interior_design_requests, name='approved_interior_design_requests'),
    path('view_my_interior_design_requests/<int:uid>', views.view_my_interior_design_requests, name='view_my_interior_design_requests'),
    path('view_approved_interior_design_requests/<int:uid>', views.view_approved_interior_design_requests, name='view_approved_interior_design_requests'),

#customer- view  ext designs----------------------------------------------------------------------------------

    path('view_exterior_design_list/<int:uid>/', views.view_exterior_design_list, name='view_exterior_design_list'),
    path('user_book_exterior_design/<int:uid>/<int:aid>/<int:pid>', views.user_book_exterior_design, name='user_book_exterior_design'),

    path('view_exterior_design_requests/<int:uid>', views.view_exterior_design_requests, name='view_exterior_design_requests'),
    path('approve_exterior_design_request/<int:uid>/<int:id>', views.approve_exterior_design_request, name='approve_exterior_design_request'),
    path('reject_exterior_design_request/<int:uid>/<int:id>', views.reject_exterior_design_request, name='reject_exterior_design_request'),

    path('approved_exterior_design_requests/<int:uid>', views.approved_exterior_design_requests, name='approved_exterior_design_requests'),
    path('view_my_exterior_design_requests/<int:uid>', views.view_my_exterior_design_requests,   name='view_my_exterior_design_requests'),
    path('view_approved_exterior_design_requests/<int:uid>', views.view_approved_exterior_design_requests, name='view_approved_exterior_design_requests'),


]

