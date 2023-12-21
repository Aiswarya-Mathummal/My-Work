from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout as logouts
from django.shortcuts import render, redirect
from .models import customers, recycling_unit, product, category, product_request, recycle_product, \
    recycle_product_request
from .forms import registerform, Loginform,  Editcustomerform, Loginform,recyclingform,Editrecyclingform, Addproductsform, editproductsform,addCategoryForm,editCategoryForm
from django.contrib import messages
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def help(request):
    return render(request, 'main/help.html')



def approve(request, uid,id):
    if request.session.get('session_id'):
        customers.objects.filter(reg_id=id).update(status=True)
        return redirect('/approvecustomer/%s' % uid)
    else:
        return  redirect('/login/')


def reject(request, uid,id):
    if request.session.get('session_id'):
        cust = customers.objects.get(reg_id=id)
        user = User.objects.get(email=cust.email)
        user.delete()
        customers.objects.filter(reg_id=id).delete()
        return redirect('/approvecustomer/%s' % uid)
    else:
        return redirect('/login/')



def customer_reg(request):
    # if request.session.get('session_id'):
    #     user = reg.objects.get(reg_id=id)
        if request.method == 'POST':
            form = registerform(request.POST, request.FILES)
            if form.is_valid():
                post_email = form.cleaned_data['email']
                if User.objects.filter(email=post_email).exists():
                    messages.warning(request, "Email Id Already Exist")
                    return redirect('/register_views/')
                else:
                    form.save()
                    uname = customers.objects.get(email=post_email)
                    User.objects.create_user(username=uname, email=post_email)
                    # fname = form.cleaned_data['firstname']
                    # lname = form.cleaned_data['lastname']
                    # subject = 'welcome to GFG world'
                    # message = f'Hi {fname} {lname}, thank you for registering in geeksforgeeks.'
                    # email_from = settings.EMAIL_HOST_USER
                    # recipient_list = ['aiswaryam421@gmail.com', ]
                    # send_mail(subject, message, email_from, recipient_list)
                    messages.warning(request, "Registration Successful")
                    return redirect('/register_views/')

        else:
            form_value = registerform()
            return render(request, "main/customer_reg.html", {'form_key':form_value})


def customer_list(request,uid):
    if request.session.get('session_id'):
        customer = customers.objects.filter(user_type=2)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(customer, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/customer_list.html",
                      {'page_obj': page_obj,'login_id':uid})
    else:
        return redirect('/login/')



def login(request):
        if request.method == 'POST':
            form = Loginform(request.POST)
            if form.is_valid():
                email_val = form.cleaned_data['email']
                pswd = form.cleaned_data['password']
                try:
                    user = customers.objects.get(email=email_val)
                    if user:
                        try:
                            user1 = customers.objects.get(Q(reg_id=user.reg_id) & Q(password=pswd))
                            if user1:
                                request.session['session_id'] = user.reg_id
                                if user.status==True:

                                    if user.user_type == 1:
                                        return redirect('/admin_home/%s' % user.reg_id)
                                    else:
                                        return redirect('/customer_home/%s' % user.reg_id)
                                else:
                                    messages.warning(request, "Your account has not been aproved yet")
                                    return redirect('/login/')
                        except customers.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                except customers.DoesNotExist:
                    try:
                        user = recycling_unit.objects.get(email=email_val)
                        if user:
                            try:
                                user1 = recycling_unit.objects.get (Q(recycle_id=user.recycle_id) & Q(password=pswd))
                                if user1:
                                    if user.status==True:
                                        request.session['session_id'] = user.recycle_id
                                        return redirect('/recy_home/%s' % user.recycle_id)
                                    else:
                                        return redirect('/login/')
                            except recycling_unit.DoesNotExist:
                                user1 = None
                                messages.warning(request, "Incorrect Password")
                                return redirect('/login/')
                    except recycling_unit.DoesNotExist:
                        user = None
                        messages.warning(request, "Invalid Email Id")
                        return redirect('/login/')
        else:
            form1 = Loginform()
            return render(request, "main/login.html", {'form2': form1})


def recycling_reg(request):
    if request.method == 'POST':
        form = recyclingform(request.POST, request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/recycling_reg/')
            else:
                form.save()
                uname = recycling_unit.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/recycling_reg/')


    else:
        form_value = recyclingform()
        return render(request, "main/recy_reg.html", {'form_key': form_value})


def recycling_list(request,uid):
    if request.session.get('session_id'):
        recycling = recycling_unit.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(recycling, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/recycling_list.html",
                      {'page_obj': page_obj,'login_id':uid})
    else:
        return redirect('/login/')





def delete_customer(request,  uid,id):
    if request.session.get('session_id'):
        cust = customers.objects.get(reg_id=id)
        user = User.objects.get(email=cust.email)
        user.delete()
        customers.objects.filter(reg_id=id).delete()
        return redirect('/customer_list/%s' % uid)
    else:
        return redirect('/login/')


def delete_recycling_unit(request,  uid,id):
    if request.session.get('session_id'):
        recy = recycling_unit.objects.get(recycle_id=id)
        user = User.objects.get(email=recy.email)
        user.delete()
        recycling_unit.objects.filter(recycle_id=id).delete()
        return redirect('/recycling_list/%s' % uid)
    else:
        return redirect('/login/')



def approvecustomer(request, uid):
    if request.session.get('session_id'):
        customer = customers.objects.filter(status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(customer, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)


        return render(request, "admin/approve_customer.html",
                      {'customer': customer, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_recycling_unit_list(request, uid):
    if request.session.get('session_id'):
        recycling= recycling_unit.objects.filter(status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(recycling,3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        return render(request, "admin/approve_recyling.html",
                      {'recycling_unit': recycling_unit, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_recycling_unit(request, uid,id):
    if request.session.get('session_id'):
         recycling_unit.objects.filter(recycle_id=id).update(status=True)
         return redirect('/approve_recycling_unit_list/%s' % uid)
    else:
        return  redirect('/login/')

def reject_recycling_unit(request, uid, id):
    if request.session.get('session_id'):
        recycling = recycling_unit.objects.get(recycle_id=id)
        user = User.objects.get(email=recycling.email)
        user.delete()
        recycling_unit.objects.get(recycle_id=id).delete()
        return redirect('/approve_recycling_unit_list/%s' % uid)
    else:
        return redirect('/login/')



def admin_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "admin/admin_home.html", {'login_id': uid})
    else:
        return redirect('/login/')

def product_list(request, uid):
    if request.session.get('session_id'):
        products = product.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(products, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/product_list.html", {'products': products, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def admin_delete_product(request, uid, id):
    if request.session.get('session_id'):
        product.objects.get(product_id=id).delete()
        return redirect('/product_list/%s' % uid)
    else:
        return redirect('/login/')

def add_category(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = addCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.warning(request, "Category Added Successfully")
                return redirect('/add_category/%s' % uid)
        else:
            form_value = addCategoryForm()
            return render(request, "admin/add_category.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_category(request, uid, id):
    if request.session.get('session_id'):
        categories = category.objects.get(category_id=id)
        if request.method == 'POST':
            form = editCategoryForm(request.POST, instance=categories)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/category_list/%s' % uid)
        else:
            form_value = editCategoryForm(instance=categories)
            return render(request, "admin/edit_category.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')



def delete_category(request, uid, id):
    if request.session.get('session_id'):
        category.objects.get(category_id=id).delete()
        return redirect('/category_list/%s' % uid)
    else:
        return redirect('/login/')
def category_list(request, uid):
    if request.session.get('session_id'):
        categories = category.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(categories, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/category_list.html",
                      {'categories': categories, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

#--------------------------------------------CUSTOMER-------------------------------------------------


def get_category():
    categories = category.objects.all()
    return categories

def customer_home(request, uid):
    if request.session.get('session_id'):
        categories = get_category()
        return render(request, "customer/customer_home.html", {'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')

def customer_profile(request, uid):
    if request.session.get('session_id'):
        customer = customers.objects.get(reg_id=uid)
        categories = get_category()
        return render(request, "customer/customer_Profile.html", {'customer': customer, 'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')


def edit_customer_profile(request, uid):
    if request.session.get('session_id'):
        customer = customers.objects.get(reg_id=uid)

        if request.method == 'POST':
            form = Editcustomerform(request.POST, request.FILES,instance=customer)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/customer_profile/%s' % uid)

        else:
            categories = get_category()
            form_value = Editcustomerform(instance=customer)
            return render(request, "customer/edit_customer_profile.html",
                          {'form_key': form_value, 'customer': customer, 'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')



def customer_product_list(request, uid):
    if request.session.get('session_id'):
        categories = get_category()
        products = product.objects.filter(Q(customers_id=uid) & Q(product_status=True))
        page_num = request.GET.get('page', 1)
        paginator = Paginator(products, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "product/customer_product_list.html",
                      {'products': products, 'page_obj': page_obj, 'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')



def add_product(request, uid):

    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addproductsform(request.POST, request.FILES)
            if form.is_valid():
                categories = form.cleaned_data['categories']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                price = form.cleaned_data['price']
                image = form.files['image']
                uploaded_on = datetime.now().date()
                expiry_date = uploaded_on + relativedelta(months=+6)
                reg_id = customers.objects.get(reg_id=uid)
                product.objects.create(categories=categories, name=name, description=description, price=price, image=image,
                                       customers_id=reg_id,expire_date=expiry_date)
                messages.warning(request, "Product Added Successfully")
                return redirect('/add_product/%s' % uid)
        else:
            categories = get_category()
            form_value = Addproductsform()
            return render(request, "product/add_product.html", {'form_key': form_value, 'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')

#
def edit_product(request, uid, id):
    if request.session.get('session_id'):
        products = product.objects.get(product_id=id)
        if request.method == 'POST':
            form = editproductsform(request.POST, request.FILES, instance=products)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/customer_product_list/%s' % uid)
        else:
            categories = get_category()
            form_value = editproductsform(instance=products)
            return render(request, "product/edit_products.html",
                          {'form_key': form_value, 'products': products, 'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')
#
#
def delete_product(request, uid, id):
    if request.session.get('session_id'):
        product.objects.get(product_id=id).delete()
        return redirect('/customer_product_list/%s' % uid)
    else:
        return redirect('/login/')

def get_products(request, uid, id):
    if request.session.get('session_id'):
        products = product.objects.filter(~Q(customers_id=uid) & Q(categories=id) & Q(product_status=True))
        categories=get_category()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(products, 10)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "customer/view_products.html", {'page_obj': page_obj, 'login_id': uid, 'categories':categories})
    else:
        return redirect('/login/')

def product_more_details(request, uid, id):
        if request.session.get('session_id'):
            products = product.objects.get(product_id=id)
            categories = get_category()
            return render(request, "customer/product_more_details.html",
                          {'products': products, 'login_id': uid, 'categories': categories})
        else:
            return redirect('/login/')


def buyer_product_request(request,uid,id):
    if request.session.get('session_id'):
        if product_request.objects.filter(Q(product_id=id) & Q(buyer_id=uid)).exists():
            messages.warning(request, "You Have Already Requested")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            product_id= product.objects.get(product_id=id)
            seller_id= customers.objects.get(reg_id=product_id.customers_id.reg_id)
            buyer_id= customers.objects.get(reg_id=uid)
            products=product_request.objects.create(product_id=product_id,seller_id=seller_id,buyer_id=buyer_id)
            product.objects.filter(product_id=products.product_id.product_id).update(product_status=False)
            messages.warning(request, "Product Request Send Successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/login/')

def view_product_request(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = product_request.objects.filter(Q(seller_id=uid) & Q(req_status=True) & Q(approve_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/product_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "No New Requests")
            return render(request, "customer/product_requests.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')


def approve_request(request,uid, id):
    if request.session.get('session_id'):
        products = product_request.objects.filter(req_id=id).update(approve_status=True)
        # buyer_fname = user.buyer_id.firstname
        # buyer_lname = user.buyer_id.lastname
        # seller_fname = user.seller_id.firstname
        # seller_lname = user.seller_id.lastname
        # seller_address=user.seller_id.address
        # seller_phone=user.seller_id.phone
        # subject = 'TRASHOUT-Product Request Approved'
        # message = f'Hi {buyer_fname} {buyer_lname}, I am {seller_fname} {seller_lname}, Thank you for choosing the product. You are welcome to pick up the product at the address given below. If you would need further information, please call the number provided.\n' \
        #           f'Address : {seller_address} \n' \
        #           f'Phone no : {seller_phone} \n' \
        #           f'Thank you..'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['', ]
        # send_mail(subject, message, email_from, recipient_list)
        messages.warning(request, "Product Request Approved")
        return redirect('/view_product_request/%s' % uid)
    else:
        return render('/login/')

def reject_request(request,uid, id):
    if request.session.get('session_id'):
        user = product_request.objects.get(req_id=id)
        product.objects.filter(product_id=user.product_id.product_id).update(product_status=True)
        products = product_request.objects.filter(req_id=id).delete()
        return redirect('/view_product_request/%s' % uid)
    else:
        return redirect('/login/')


def view_approved_product_request(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = product_request.objects.filter(Q(seller_id=uid) & Q(req_status=True) & Q(approve_status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/approved_product_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "No requests have been approved by you.")
            return render(request, "customer/approved_product_requests.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')


def cancel_request(request,uid, id):
    if request.session.get('session_id'):
        products = product_request.objects.get(req_id=id)
        product.objects.filter(product_id=products.product_id.product_id).update(product_status=True)
        product_request.objects.filter(req_id=id).delete()
        return redirect('/view_approved_product_request/%s' % uid)
    else:
        return redirect('/login/')


def product_collected(request,uid, id):
    if request.session.get('session_id'):
        products = product_request.objects.get(req_id=id)
        product.objects.filter(product_id=products.product_id.product_id).update(product_status=False)
        product_request.objects.filter(req_id=id).update(req_status=False,approve_status=False)
        return redirect('/view_approved_product_request/%s' % uid)
    else:
        return render('/login/')


def sold_products(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = product_request.objects.filter(Q(seller_id=uid) & Q(req_status=False) & Q(approve_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/sold_products.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "You haven't made any sales.")
            return render(request, "customer/sold_products.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')

def orders(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = product_request.objects.filter(Q(buyer_id=uid) & Q(req_status=True) & Q(approve_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/orders.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "You haven't placed any orders yet.")
            return render(request, "customer/orders.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')

def cancel_order(request,uid, id):
    if request.session.get('session_id'):
        products = product_request.objects.get(req_id=id)
        product.objects.filter(product_id=products.product_id.product_id).update(product_status=True)
        product_request.objects.filter(req_id=id).delete()
        return redirect('/approved_orders/%s' % uid)
    else:
        return redirect('/login/')

def approved_orders(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = product_request.objects.filter(Q(buyer_id=uid) & Q(req_status=True) & Q(approve_status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/approved_orders.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "No Approved Requests")
            return render(request, "customer/approved_orders.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')


def order_history(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = product_request.objects.filter(Q(buyer_id=uid) & Q(req_status=False) & Q(approve_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/order_history.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "You haven't made any Order.")
            return render(request, "customer/order_history.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')

def check_expiry_date(request):
    today=datetime.now().date()
    products=product.objects.all()
    for i in products:
        if today > i.expire_date:
            if recycle_product.objects.filter(product_id=i.product_id).exists():
                continue
            else:
                product_id = product.objects.get(product_id=i.product_id)
                recycle_product.objects.create(product_id=product_id)
                product.objects.filter(product_id=i.product_id).update(product_status=False)
        else:
            pass
    data = {'status': True}
    return JsonResponse(data)


def update_rating(request):
    product_id = request.GET.get('product_id')  # Use POST instead of GET
    new_rating = request.GET.get('new_rating')
    products = product.objects.get(product_id=product_id)
    if products.rating_status:
        print("---------------------------------------------------------------------",products)
        products.rating = new_rating
        products.rating_status=False
        products.save()
        return JsonResponse({'status':True,'message': 'Rating updated successfully'})
    else:
        return JsonResponse({'status':False,'message': 'already rated'})

def recycle_update_rating(request):
    rc_product_id = request.GET.get('product_id')  # Use POST instead of GET
    new_rating = request.GET.get('new_rating')
    products = recycle_product.objects.get(rc_product_id=rc_product_id)
    if products.rating_status:
        print("---------------------------------------------------------------------",products)
        products.rating = new_rating
        products.rating_status=False
        products.save()
        return JsonResponse({'status':True,'message': 'Rating updated successfully'})
    else:
        return JsonResponse({'status':False,'message': 'already rated'})

#--------------------------------------------RECYCLE UNIT---------------------------------------------


def recycling_unit_home(request, uid):
    if request.session.get('session_id'):
        categories = get_category()
        return render(request, "recycling_unit/recy_home.html", {'login_id': uid,'categories':categories})
    else:
        return redirect('/login/')



def edit_recycling_unit_profile(request, uid):
    if request.session.get('session_id'):
        categories = get_category()
        recycling = recycling_unit.objects.get(recycle_id=uid)
        if request.method == 'POST':
            form = Editrecyclingform(request.POST, instance=recycling)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/recycling_unit_profile/%s' % uid)

        else:
            form_value = Editrecyclingform(instance=recycling)
            return render(request, "recycling_unit/edit_recycling_profile.html",{'categories':categories,'form_key': form_value, 'recycling':recycling, 'login_id': uid})
    else:
          return redirect('/login/')



def recycling_unit_profile(request, uid):
    if request.session.get('session_id'):
        categories = get_category()
        recycling = recycling_unit.objects.get(recycle_id=uid)
        return render(request, "recycling_unit/recycling_profile.html", {'categories':categories,'recycling': recycling, 'login_id': uid})
    else:
        return redirect('/login/')



def unit_get_products(request, uid, id):
    if request.session.get('session_id'):
        products = recycle_product.objects.filter(Q(product_id__categories=id) & Q(product_status=True))
        categories=get_category()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(products, 10)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "recycling_unit/view_products.html", {'page_obj': page_obj, 'login_id': uid, 'categories':categories})
    else:
        return redirect('/login/')

def unit_product_more_details(request, uid, id):
        if request.session.get('session_id'):
            products = recycle_product.objects.get(rc_product_id=id)
            categories = get_category()
            return render(request, "recycling_unit/product_more_details.html",
                          {'products': products, 'login_id': uid, 'categories': categories})
        else:
            return redirect('/login/')


def unit_product_request(request,uid,id):
    if request.session.get('session_id'):
        if recycle_product_request.objects.filter(Q(rc_product_id=id) & Q(recycle_id=uid)).exists():
            messages.warning(request, "You Have Already Requested")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            rc_product_id= recycle_product.objects.get(rc_product_id=id)
            recycle_id= recycling_unit.objects.get(recycle_id=uid)
            products=recycle_product_request.objects.create(rc_product_id=rc_product_id,recycle_id=recycle_id)
            recycle_product.objects.filter(rc_product_id=products.rc_product_id.rc_product_id).update(product_status=False)
            # cust_fname = products.rc_product_id.product_id.customers_id.firstname
            # cust_lname = products.rc_product_id.product_id.customers_id.lastname
            # unit_name = products.recycle_id.unit_name
            # unit_phone=products.recycle_id.phone
            # subject = 'TRASHOUT-Product Accepted By Recycling Unit'
            # message = f'Hi {cust_fname} {cust_lname}, We Are From {unit_name} , We have accepted your product and will be there to pick it up from you within two days. Before we pick up, you can expect a call from us from the phone number provided.\n' \
            #           f'Phone no : {unit_phone} \n' \
            #           f'Thank you..'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = ['', ]
            # send_mail(subject, message, email_from, recipient_list)
            messages.warning(request, "Product Accepted")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/login/')



def view_expired_products(request, uid):
        if request.session.get('session_id'):
            categories = get_category()
            products = recycle_product.objects.filter(Q(product_id__customers_id=uid) & Q(product_status=True))
            page_num = request.GET.get('page', 1)
            paginator = Paginator(products, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "customer/expired_product_list.html",
                          {'products': products, 'page_obj': page_obj, 'login_id': uid, 'categories': categories})
        else:
            return redirect('/login/')


def delete_recycle_product(request, uid, id):
    if request.session.get('session_id'):
        products=recycle_product.objects.get(rc_product_id=id)
        product.objects.filter(product_id=products.product_id.product_id).delete()
        recycle_product.objects.filter(rc_product_id=id).delete()
        return redirect('/view_expired_products/%s' % uid)
    else:
        return redirect('/login/')


def accepted_products(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = recycle_product_request.objects.filter(Q(rc_product_id__product_id__customers_id=uid) & Q(accept_status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/accepted_products.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "No Accepted Products")
            return render(request, "customer/accepted_products.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')

def recycle_sold_products(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = recycle_product_request.objects.filter(Q(rc_product_id__product_id__customers_id=uid) & Q(accept_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/recycle_sold_products.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "Nothing To Show.")
            return render(request, "customer/recycle_sold_products.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')


def accepted_orders(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = recycle_product_request.objects.filter(Q(recycle_id=uid) & Q(accept_status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'recycling_unit/accepted_orders.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "No Accepted Products")
            return render(request, "recycling_unit/accepted_orders.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')

def recycle_product_collected(request,uid, id):
    if request.session.get('session_id'):
        products = recycle_product_request.objects.get(req_id=id)
        recycle_product.objects.filter(product_id=products.rc_product_id.rc_product_id).update(product_status=False)
        recycle_product_request.objects.filter(req_id=id).update(accept_status=False)
        return redirect('/accepted_orders/%s' % uid)
    else:
        return render('/login/')

def recycle_order_history(request,uid):
    if request.session.get('session_id'):
        categories = get_category()
        req = recycle_product_request.objects.filter(Q(recycle_id=uid) & Q(accept_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 3)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'recycling_unit/recycle_order_history.html', {'page_obj': page_obj, 'login_id': uid,'count': 1,'categories':categories})
        else:
            messages.warning(request, "Nothing To Show.")
            return render(request, "recycling_unit/recycle_order_history.html", {'login_id': uid, 'count': 0,'categories':categories})

    else:
        return redirect('/login/')



def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')













#
def product_details(request):
    return render(request, 'main/index.html')

#
#
#















