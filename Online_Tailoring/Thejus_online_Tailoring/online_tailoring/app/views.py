from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout as logouts
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import tailorregform, designerregform, manufacturerregform, registerform, Editmanufacturerregform, \
    Editcustomerform, Edittailorregform, Editdesignerregform, addDeliveryAgentForm, Loginform, Editadminprofileform, \
    editCategoryForm, addCategoryForm, editmaterialform, Addmaterialform, editdesignform, Adddesignform, \
    sewing_measurement_form, update_tailor_status_form
from .models import register, manufacturer, tailor, designer, delivery_agent, category, designs, materials, \
    sewing_request, sewing_measurements, sewing_details, orders, material_request, assign_delivery_agent
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from django.core.serializers import serialize
import math



def index(request):
    return render(request, "main/index.html")

def register_func(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/register/')
            else:
                form.save()
                uname = register.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/register/')

    else:
        form_value = registerform()
        return render(request, "main/register.html", {'form_key': form_value})


def tailor_reg(request):
    if request.method == 'POST':
        form = tailorregform(request.POST, request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/tailor_reg/')
            else:
                form.save()
                uname = tailor.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/tailor_reg/')

    else:
        form_value = tailorregform()
        return render(request, "main/tailor_register.html", {'form_key': form_value})

def manufacturer_reg(request):
    if request.method == 'POST':
        form = manufacturerregform(request.POST, request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/manufacturer_reg/')
            else:
                form.save()
                uname = manufacturer.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/manufacturer_reg/')

    else:
        form_value = manufacturerregform()
        return render(request, "main/manufacturer_register.html", {'form_key': form_value})


def designer_reg(request):
    if request.method == 'POST':
        form = designerregform(request.POST, request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/designer_reg/')
            else:
                form.save()
                uname = designer.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/designer_reg/')

    else:
        form_value = designerregform()
        return render(request, "main/designer_register.html", {'form_key': form_value})




def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            email_val = form.cleaned_data['email']
            pswd = form.cleaned_data['password']
            try:
                user = register.objects.get(email=email_val)
                if user:
                    try:
                        user1 = register.objects.get(Q(reg_id=user.reg_id) & Q(password=pswd))
                        if user1:
                            request.session['session_id'] = user.reg_id
                            if user.usertype == 1:
                                return redirect('/admin_home/%s' % user.reg_id)
                            else:
                                return redirect('/customer_home/%s' % user.reg_id)
                    except register.DoesNotExist:
                        user1 = None
                        messages.warning(request, "Incorrect Password")
                        return redirect('/login/')
            except register.DoesNotExist:
                try:
                    user = tailor.objects.get(email=email_val)
                    if user:
                        try:
                            user1 = tailor.objects.get(Q(tailor_id=user.tailor_id) & Q(password=pswd))
                            if user1:
                                if user.status == True:
                                    request.session['session_id'] = user.tailor_id
                                    return redirect('/tailor_home/%s' % user.tailor_id)
                                else:
                                    messages.warning(request, "You are not yet approved")
                                    return redirect('/login/')
                        except tailor.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                except tailor.DoesNotExist:
                    try:
                        user = delivery_agent.objects.get(email=email_val)
                        if user:
                            try:
                                user1 = delivery_agent.objects.get(Q(agent_id=user.agent_id) & Q(password=pswd))
                                if user1:
                                    request.session['session_id'] = user.agent_id
                                    return redirect('/delivery_agent_home/%s' % user.agent_id)
                            except delivery_agent.DoesNotExist:
                                user1 = None
                                messages.warning(request, "Incorrect Password")
                                return redirect('/login/')
                    except delivery_agent.DoesNotExist:
                        try:
                            user = manufacturer.objects.get(email=email_val)
                            if user:
                                try:
                                    user1 = manufacturer.objects.get(Q(manufacturer_id=user.manufacturer_id) & Q(password=pswd))
                                    if user1:
                                        if user.status == True:
                                            request.session['session_id'] = user.manufacturer_id
                                            return redirect('/manufacturer_home/%s' % user.manufacturer_id)
                                        else:
                                            messages.warning(request, "You are not yet approved")
                                            return redirect('/login/')
                                except manufacturer.DoesNotExist:
                                    user1 = None
                                    messages.warning(request, "Incorrect Password")
                                    return redirect('/login/')
                        except manufacturer.DoesNotExist:
                            try:
                                user = designer.objects.get(email=email_val)
                                if user:
                                    try:
                                        user1 = designer.objects.get(
                                            Q(designer_id=user.designer_id) & Q(password=pswd))
                                        if user1:
                                            if user.status == True:
                                                request.session['session_id'] = user.designer_id
                                                return redirect('/designer_home/%s' % user.designer_id)
                                            else:
                                                messages.warning(request, "You are not yet approved")
                                                return redirect('/login/')
                                    except designer.DoesNotExist:
                                        user1 = None
                                        messages.warning(request, "Incorrect Password")
                                        return redirect('/login/')
                            except designer.DoesNotExist:
                                user = None
                                messages.warning(request, "Invalid Email Id")
                                return redirect('/login/')
    else:
        form1 = Loginform()
        return render(request, "main/login.html", {'form': form1})


def delivery_agent_reg(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = addDeliveryAgentForm(request.POST,request.FILES)
            length_of_string = 10
            sample_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@$^&*/!"
            pswd = ''.join(random.choices(sample_str, k=length_of_string))
            if form.is_valid():
                name = form.cleaned_data['name']
                post_email = form.cleaned_data['email']
                id_proof = form.files['id_proof']
                profile_pic = form.files['profile_pic']
                if User.objects.filter(email=post_email).exists():
                    messages.warning(request, "Email Id Already Exist")
                    return redirect('/delivery_agent_reg/%s' % uid)
                else:
                    delivery_agent.objects.create(name=name, email=post_email, password=pswd,id_proof=id_proof,profile_pic=profile_pic)
                    uname = delivery_agent.objects.get(email=post_email)
                    User.objects.create_user(username=uname, email=post_email)
                    name = form.cleaned_data['name']
                    # subject = 'Welcome to Organic Store'
                    # message = f'Hi {name}, Thank you for accepting our invitaion to join Organic Store.\n' \
                    #           f'Your Email Id and Password has been provided below :\n' \
                    #           f'Email Id : {post_email} \n' \
                    #           f'Password : {pswd} \n' \
                    #           f'Thank you..'
                    # email_from = settings.EMAIL_HOST_USER
                    # recipient_list = ['', ]
                    # send_mail(subject, message, email_from, recipient_list)
                    messages.warning(request, "Delivery Agent Added Successfully")
                    return redirect('/delivery_agent_reg/%s' % uid)
        else:
            form_value = addDeliveryAgentForm()
            return render(request, "admin/add_delivery_agent.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def customer_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "customers/customer_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def admin_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "admin/admin_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def tailor_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "tailor/tailor_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def manufacturer_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "manufacturer/manufacturer_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def designer_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "designer/designer_home.html", {'login_id': uid})
    else:
        return redirect('/login/')

def delivery_agent_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "delivery/delivery_agent_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def customer_list(request, uid):
    if request.session.get('session_id'):
        customer = register.objects.filter(usertype=2)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(customer, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/customer_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def delete_customer(request, uid, id):
    if request.session.get('session_id'):
        cust = register.objects.get(agent_id=id)
        user = User.objects.get(email=cust.email)
        user.delete()
        register.objects.filter(reg_id=id).delete()
        return redirect('/customer_list/%s' % uid)
    else:
        return redirect('/login/')


def approvetailors(request, uid):
    if request.session.get('session_id'):
        tailors = tailor.objects.filter(status=False)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(tailors, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_tailors.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_tailor(request, uid, id):
    if request.session.get('session_id'):
        tailor.objects.filter(tailor_id=id).update(status=True)
        return redirect('/approvetailors/%s' % uid)
    else:
        return redirect('/login/')


def reject_tailor(request, uid, id):
    if request.session.get('session_id'):
        tailors = tailor.objects.get(tailor_id=id)
        user = User.objects.get(email=tailors.email)
        user.delete()
        tailor.objects.get(tailor_id=id).delete()
        return redirect('/approvetailors/%s' % uid)
    else:
        return redirect('/login/')


def tailor_list(request, uid):
    if request.session.get('session_id'):
        tailors = tailor.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(tailors, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/tailor_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_tailor(request, uid, id):
    if request.session.get('session_id'):
        tailors = tailor.objects.get(tailor_id=id)
        user = User.objects.get(email=tailors.email)
        user.delete()
        tailor.objects.get(tailor_id=id).delete()
        return redirect('/tailor_list/%s' % uid)
    else:
        return redirect('/login/')



def approvemanufacturers(request, uid):
    if request.session.get('session_id'):
        manufacturers = manufacturer.objects.filter(status=False)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(manufacturers, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_manufacturer.html",
                      { 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_manufacturer(request, uid, id):
    if request.session.get('session_id'):
        manufacturer.objects.filter(manufacturer_id=id).update(status=True)
        return redirect('/approvemanufacturers/%s' % uid)
    else:
        return redirect('/login/')


def reject_manufacturer(request, uid, id):
    if request.session.get('session_id'):
        manufacturers = manufacturer.objects.get(manufacturer_id=id)
        user = User.objects.get(email=manufacturers.email)
        user.delete()
        manufacturer.objects.get(manufacturer_id=id).delete()
        return redirect('/approvemanufacturers/%s' % uid)

    else:
        return redirect('/login/')

def manufacturer_list(request, uid):
    if request.session.get('session_id'):
        manufacturers = manufacturer.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(manufacturers, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/manufacturer_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_manufacturer(request, uid, id):
    if request.session.get('session_id'):
        manufacturers = manufacturer.objects.get(manufacturer_id=id)
        user = User.objects.get(email=manufacturers.email)
        user.delete()
        manufacturer.objects.get(manufacturer_id=id).delete()
        return redirect('/manufacturer_list/%s' % uid)
    else:
        return redirect('/login/')



def approvedesigners(request, uid):
    if request.session.get('session_id'):
        designers = designer.objects.filter(status=False)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(designers, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_designer.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_designer(request, uid, id):
    if request.session.get('session_id'):
        designer.objects.filter(designer_id=id).update(status=True)
        return redirect('/approvedesigners/%s' % uid)
    else:
        return redirect('/login/')


def reject_designer(request, uid, id):
    if request.session.get('session_id'):
        designers = designer.objects.get(designer_id=id)
        user = User.objects.get(email=designers.email)
        user.delete()
        designer.objects.get(designer_id=id).delete()
        return redirect('/approvedesigners/%s' % uid)
    else:
        return redirect('/login/')


def designer_list(request, uid):
    if request.session.get('session_id'):
        designers = designer.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(designers, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/designer_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_designer(request, uid, id):
    if request.session.get('session_id'):
        designers = designer.objects.get(designer_id=id)
        user = User.objects.get(email=designers.email)
        user.delete()
        designer.objects.get(designer_id=id).delete()
        return redirect('/designer_list/%s' % uid)
    else:
        return redirect('/login/')


def delivery_agent_list(request, uid):
    if request.session.get('session_id'):
        agent = delivery_agent.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(agent, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        return render(request, "admin/delivery_agent_list.html",
                      {'agents': agent, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_delivery_agent(request, uid, id):
    if request.session.get('session_id'):
        agent = delivery_agent.objects.get(agent_id=id)
        user = User.objects.get(email=agent.email)
        user.delete()
        delivery_agent.objects.get(agent_id=id).delete()
        return redirect('/delivery_agent_list/%s' % uid)
    else:
        return redirect('/login/')




def admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = register.objects.get(reg_id=uid)
        return render(request, "admin/admin_profile.html", {'admin': admin, 'login_id': uid})
    else:
        return redirect('/login/')


def edit_admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = register.objects.get(reg_id=uid)
        if request.method == 'POST':
            form = Editadminprofileform(request.POST, instance=admin)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/admin_profile/%s' % uid)

        else:
            form_value = Editadminprofileform(instance=admin)
            return render(request, "admin/edit_admin_profile.html",
                          {'form_key': form_value, 'admin': admin, 'login_id': uid})
    else:
        return redirect('/login/')



def customer_profile(request, uid):
    if request.session.get('session_id'):
        users = register.objects.get(reg_id=uid)
        return render(request, "customers/customer_profile.html", {'users': users,'login_id': uid})
    else:
        return redirect('/login/')


def edit_customer_profile(request, uid):
    if request.session.get('session_id'):
        users = register.objects.get(reg_id=uid)
        if request.method == 'POST':
            form = Editcustomerform(request.POST, instance=users)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/customer_profile/%s' % uid)

        else:
            form_value = Editcustomerform(instance=users)
            return render(request, "customers/edit_customer_profile.html",
                          {'form_key': form_value, 'users': users, 'login_id': uid})
    else:
        return redirect('/login/')



def manufacturer_profile(request, uid):
    if request.session.get('session_id'):
        manufacturers = manufacturer.objects.get(manufacturer_id=uid)
        return render(request, "manufacturer/manufacturer_profile.html", {'manufacturers': manufacturers,'login_id': uid})
    else:
        return redirect('/login/')


def edit_manufacturer_profile(request, uid):
    if request.session.get('session_id'):
        manufacturers = manufacturer.objects.get(manufacturer_id=uid)
        if request.method == 'POST':
            form = Editmanufacturerregform(request.POST,request.FILES, instance=manufacturers)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/manufacturer_profile/%s' % uid)

        else:
            form_value = Editmanufacturerregform(instance=manufacturers)
            return render(request, "manufacturer/edit_manufacturer_profile.html",
                          {'form_key': form_value, 'manufacturers': manufacturers, 'login_id': uid})
    else:
        return redirect('/login/')




def designer_profile(request, uid):
    if request.session.get('session_id'):
        designers= designer.objects.get(designer_id=uid)
        return render(request, "designer/designer_profile.html", {'designers': designers,'login_id': uid})
    else:
        return redirect('/login/')


def edit_designer_profile(request, uid):
    if request.session.get('session_id'):
        designers = designer.objects.get(designer_id=uid)
        if request.method == 'POST':
            form = Editdesignerregform(request.POST, request.FILES,instance=designers)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/designer_profile/%s' % uid)

        else:
            form_value = Editdesignerregform(instance=designers)
            return render(request, "designer/edit_designer_profile.html",
                          {'form_key': form_value, 'designers': designers, 'login_id': uid})
    else:
        return redirect('/login/')




def tailor_profile(request, uid):
    if request.session.get('session_id'):
        tailors= tailor.objects.get(tailor_id=uid)
        return render(request, "tailor/tailor_profile.html", {'tailors': tailors,'login_id': uid})
    else:
        return redirect('/login/')


def edit_tailor_profile(request, uid):
    if request.session.get('session_id'):
        tailors = tailor.objects.get(tailor_id=uid)
        if request.method == 'POST':
            form = Edittailorregform(request.POST,request.FILES, instance=tailors)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/tailor_profile/%s' % uid)

        else:
            form_value = Edittailorregform(instance=tailors)
            return render(request, "tailor/edit_tailor_profile.html",
                          {'form_key': form_value, 'tailors': tailors, 'login_id': uid})
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


def category_list(request, uid):
    if request.session.get('session_id'):
        categories = category.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(categories, 5)  # 6 employees per page
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


def delete_category(request, uid, id):
    if request.session.get('session_id'):
        category.objects.get(category_id=id).delete()
        return redirect('/category_list/%s' % uid)
    else:
        return redirect('/login/')



def add_design(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Adddesignform(request.POST, request.FILES)
            if form.is_valid():
                categories = form.cleaned_data['categories']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                price = form.cleaned_data['price']
                image = form.files['image']
                designer_id = designer.objects.get(designer_id=uid)
                designs.objects.create(categories=categories, name=name, description=description, price=price, image=image,
                                       designer_id=designer_id)
                messages.warning(request, "Design Added Successfully")
                return redirect('/add_design/%s' % uid)
        else:
            form_value = Adddesignform()
            return render(request, "designer/add_design.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def edit_design(request, uid, id):
    if request.session.get('session_id'):
        design = designs.objects.get(design_id=id)
        if request.method == 'POST':
            form = editdesignform(request.POST, request.FILES, instance=design)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/designs_list/%s' % uid)
        else:
            form_value = editdesignform(instance=design)
            return render(request, "designer/edit_design.html",
                          {'form_key': form_value, 'design': design, 'login_id': uid})
    else:
        return redirect('/login/')


def designs_list(request, uid):
    if request.session.get('session_id'):
        design = designs.objects.filter(designer_id=uid)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(design, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "designer/designs_list.html",
                      {'design': design, 'page_obj': page_obj, 'login_id': uid})
    else:
        return redirect('/login/')


def delete_design(request, uid, id):
    if request.session.get('session_id'):
        designs.objects.get(design_id=id).delete()
        return redirect('/designs_list/%s' % uid)
    else:
        return redirect('/login/')


def admin_delete_design(request, uid, id):
    if request.session.get('session_id'):
        designs.objects.get(design_id=id).delete()
        return redirect('/admin_designs_list/%s' % uid)
    else:
        return redirect('/login/')


def admin_designs_list(request, uid):
    if request.session.get('session_id'):
        design = designs.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(design, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/designs_list.html", { 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')



def add_material(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addmaterialform(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                image = form.files['image']
                manufacturer_id = manufacturer.objects.get(manufacturer_id=uid)
                materials.objects.create( name=name, price=price, image=image,manufacturer_id=manufacturer_id)
                messages.warning(request, "Material Added Successfully")
                return redirect('/add_material/%s' % uid)
        else:
            form_value = Addmaterialform()
            return render(request, "manufacturer/add_material.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def edit_material(request, uid, id):
    if request.session.get('session_id'):
        material = materials.objects.get(material_id=id)
        if request.method == 'POST':
            form = editmaterialform(request.POST, request.FILES, instance=material)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/materials_list/%s' % uid)
        else:
            form_value = editmaterialform(instance=material)
            return render(request, "manufacturer/edit_material.html",
                          {'form_key': form_value, 'material': material, 'login_id': uid})
    else:
        return redirect('/login/')


def materials_list(request, uid):
    if request.session.get('session_id'):
        material = materials.objects.filter(manufacturer_id=uid)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(material, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "manufacturer/materials_list.html",
                      { 'page_obj': page_obj, 'login_id': uid})
    else:
        return redirect('/login/')


def delete_material(request, uid, id):
    if request.session.get('session_id'):
        materials.objects.get(material_id=id).delete()
        return redirect('/materials_list/%s' % uid)
    else:
        return redirect('/login/')


def admin_delete_material(request, uid, id):
    if request.session.get('session_id'):
        materials.objects.get(material_id=id).delete()
        return redirect('/admin_materials_list/%s' % uid)
    else:
        return redirect('/login/')


def admin_materials_list(request, uid):
    if request.session.get('session_id'):
        material = materials.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(material, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/materials_list.html", { 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def get_designs(request, uid, id):
    if request.session.get('session_id'):
        design = designs.objects.filter(categories=id)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(design, 8)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "customers/view_designs.html", {'page_obj': page_obj, 'login_id': uid,})

    else:
        return redirect('/login/')


def design_more_details(request, uid, id):
    if request.session.get('session_id'):
        design = designs.objects.get(design_id=id)
        return render(request, "customers/design_more_details.html",{'design': design, 'login_id': uid})
    else:
        return redirect('/login/')

def request_tailor(request,uid,id):
    if request.session.get('session_id'):
        design = designs.objects.get(design_id=id)
        user= register.objects.get(reg_id=uid)
        if request.method=='POST':
            material=request.POST.getlist('material')
            tailors=request.POST.get('tailor')
            delivery_date=request.POST.get('delivery_date')

            if material == [] :
                messages.warning(request, "You did not choose any fabric!!!")
                return redirect('/design_more_details/%s/%s' % (uid, id))
            else:
                fabric1=''
                fabric2=''
                fabric3=''
                if tailors == None :
                    messages.warning(request, "You did not choose any Tailor!!!")
                    return redirect('/design_more_details/%s/%s' % (uid, id))
                else:
                    tailor_id = tailor.objects.get(tailor_id=tailors)
                    length=len(material)
                    if length==1:
                        fabric1 = materials.objects.get(material_id=material[0])
                        sewing_request.objects.create(design_id=design,material_id1=fabric1.material_id,user_id=user,tailor_id=tailor_id,delivery_date=delivery_date)
                        messages.warning(request, "Please be patient for the tailor's response!!!")
                        return redirect('/design_more_details/%s/%s' % (uid, id))
                    elif length==2:
                        fabric1 = materials.objects.get(material_id=material[0])
                        fabric2 = materials.objects.get(material_id=material[1])
                        sewing_request.objects.create(design_id=design, material_id1=fabric1.material_id,material_id2=fabric2.material_id, user_id=user,tailor_id=tailor_id, delivery_date=delivery_date)
                        messages.warning(request, "Please be patient for the tailor's response!!!")
                        return redirect('/design_more_details/%s/%s' % (uid, id))
                    elif length == 3:
                        fabric1 = materials.objects.get(material_id=material[0])
                        fabric2 = materials.objects.get(material_id=material[1])
                        fabric3 = materials.objects.get(material_id=material[2])
                        sewing_request.objects.create(design_id=design,material_id1=fabric1.material_id,material_id2=fabric2.material_id,material_id3=fabric3.material_id,user_id=user,tailor_id=tailor_id,delivery_date=delivery_date)
                        messages.warning(request, "Please be patient for the tailor's response!!!")
                        return redirect('/design_more_details/%s/%s' % (uid,id))
        else:
            fabric =materials.objects.all()
            page_num = request.GET.get('page', 1)
            paginator = Paginator(fabric, 8)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            tailors =  tailor.objects.filter(status=True)
            return render(request, "customers/request_tailor.html",{'tailors':tailors,'page_obj':page_obj,'design': design, 'login_id': uid})
    else:
        return redirect('/login/')


def customer_request_history(request, uid):
    if request.session.get('session_id'):
        req = sewing_request.objects.filter(measurement_status=False)
        if req:
                page_num = request.GET.get('page', 1)
                paginator = Paginator(req, 5)  # 6 employees per page
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    # if page is not an integer, deliver the first page
                    page_obj = paginator.page(1)
                except EmptyPage:
                    # if the page is out of range, deliver the last page
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, "customers/customer_request_history.html",
                              {'login_id': uid, 'page_obj': page_obj, 'count': 1})
        else:
            messages.warning(request, "There are no new requests")
            return render(request, "customers/customer_request_history.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')


def view_sew_requests(request, uid):
    if request.session.get('session_id'):
        req = sewing_request.objects.filter(Q(tailor_id=uid) & Q(request_status=False))
        if req:
                page_num = request.GET.get('page', 1)
                paginator = Paginator(req, 5)  # 6 employees per page
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    # if page is not an integer, deliver the first page
                    page_obj = paginator.page(1)
                except EmptyPage:
                    # if the page is out of range, deliver the last page
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, "tailor/view_sew_request.html",
                              {'login_id': uid, 'page_obj': page_obj, 'count': 1})
        else:
            messages.warning(request, "You have no new request")
            return render(request, "tailor/view_sew_request.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')


def accept_request(request, uid, id):
    if request.session.get('session_id'):
        sewing_request.objects.filter(req_id=id).update(request_status=True)
        return redirect('/view_sew_requests/%s' % uid)
    else:
        return redirect('/login/')


def reject_request(request, uid, id):
    if request.session.get('session_id'):
        sewing_request.objects.filter(req_id=id).delete()
        return redirect('/view_sew_requests/%s' % uid)
    else:
        return redirect('/login/')

def cancel_request(request, uid, id):
    if request.session.get('session_id'):
        sewing_request.objects.filter(req_id=id).delete()
        return redirect('/customer_request_history/%s' % uid)
    else:
        return redirect('/login/')

def track_request(request,uid,id):
    if request.session.get('session_id'):
        req=sewing_request.objects.get(req_id=id)
        fabric1 = ''
        fabric2 = ''
        fabric3 = ''
        if req.material_id1:
            fabric1 = materials.objects.get(material_id=req.material_id1)
        if req.material_id2:
            fabric2 = materials.objects.get(material_id=req.material_id2)
        if req.material_id3:
            fabric3 = materials.objects.get(material_id=req.material_id3)
        return render(request, "tailor/track_request.html", {'req': req,'fabric3':fabric3,'fabric2':fabric2,'fabric1':fabric1, 'login_id': uid})
    else:
        return redirect('/login/')

def customer_orders(request, uid):
    if request.session.get('session_id'):
        resp = sewing_details.objects.filter(Q(request_id__user_id=uid) & Q(sewing_status=False))
        if resp:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(resp, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "customers/orders.html",
                          {'login_id': uid, 'page_obj': page_obj})
        else:
            messages.warning(request, "Tailor has not Responded yet")
            return render(request, "customers/orders.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')


def accept_order_rate(request, uid, id):
    if request.session.get('session_id'):
        order_date= datetime.today().date()
        sewing_details.objects.filter(request_id=id).update(sewing_status=True)
        sewing_id=sewing_details.objects.get(request_id=id)
        orders.objects.create(order_date=order_date,sewing_id=sewing_id)
        return redirect('/order_placed/%s' % uid)
    else:
        return redirect('/login/')

def order_placed(request, uid):
    if request.session.get('session_id'):
        order=orders.objects.get(sewing_id__request_id__user_id=uid)
        return render(request, "customers/order_placed.html", {'login_id': uid,'order':order})
    else:
        return redirect('/login/')
def reject_order_rate(request, uid, id):
    if request.session.get('session_id'):
        sewing_request.objects.get(req_id=id).delete()
        return redirect('/customer_orders/%s' % uid)
    else:
        return redirect('/login/')
def my_orders(request, uid):
    if request.session.get('session_id'):
        order=orders.objects.filter(Q(sewing_id__request_id__user_id=uid) & Q(order_status=True))
        if order:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(order, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "customers/my_orders.html",
                          {'login_id': uid, 'page_obj': page_obj,'count': 1})

        else:
            messages.warning(request, "Currently No Orders")
            return render(request, "customers/my_orders.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')

def customer_order_history(request, uid):
    if request.session.get('session_id'):
        order=orders.objects.filter(Q(sewing_id__request_id__user_id=uid) & Q(order_status=False))
        if order:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(order, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "customers/order_history.html",
                          {'login_id': uid, 'page_obj': page_obj,'count': 1})

        else:
            messages.warning(request, "No Orders")
            return render(request, "customers/order_history.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')

def sewing_rate_details(request, uid,id):
    if request.session.get('session_id'):
        req = sewing_request.objects.get(req_id=id)
        measurement_id=sewing_measurements.objects.get(request_id=id)
        rate=sewing_details.objects.get(request_id=id)
        fabric1 = ''
        fabric2 = ''
        fabric3 = ''
        if req.material_id1:
            fabric1 = materials.objects.get(material_id=req.material_id1)
        if req.material_id2:
            fabric2 = materials.objects.get(material_id=req.material_id2)
        if req.material_id3:
            fabric3 = materials.objects.get(material_id=req.material_id3)
        return render(request, "customers/sewing_rate_details.html", { 'rate':rate,'fabric3': fabric3, 'fabric2': fabric2, 'fabric1': fabric1,'req':req,'measurement':measurement_id,'login_id': uid})
    else:
        return redirect('/login/')


def customer_track_request(request, uid, id):
        if request.session.get('session_id'):
            req = sewing_request.objects.get(req_id=id)
            fabric1 = ''
            fabric2 = ''
            fabric3 = ''
            if req.material_id1:
                fabric1 = materials.objects.get(material_id=req.material_id1)
            if req.material_id2:
                fabric2 = materials.objects.get(material_id=req.material_id2)
            if req.material_id3:
                fabric3 = materials.objects.get(material_id=req.material_id3)
            return render(request, "customers/track_request.html",
                          {'req': req, 'fabric3': fabric3, 'fabric2': fabric2, 'fabric1': fabric1, 'login_id': uid})
        else:
            return redirect('/login/')


def give_measurement(request, uid,id):
    if request.session.get('session_id'):
        req = sewing_request.objects.get(req_id=id)
        if req.request_status:
            if request.method == 'POST':
                form = sewing_measurement_form(request.POST)
                if form.is_valid():
                    brand_size = form.cleaned_data['brand_size']
                    chest_measurement = form.cleaned_data['chest_measurement']
                    waist_measurement = form.cleaned_data['waist_measurement']
                    hip_measurement = form.cleaned_data['hip_measurement']
                    shoulder_measurement = form.cleaned_data['shoulder_measurement']
                    sleeve_length = form.cleaned_data['sleeve_length']
                    outseam_length = form.cleaned_data['outseam_length']
                    sewing_measurements.objects.create(brand_size=brand_size, chest_measurement=chest_measurement,
                                                       waist_measurement=waist_measurement, hip_measurement=hip_measurement,shoulder_measurement=shoulder_measurement,sleeve_length=sleeve_length,outseam_length=outseam_length,request_id=req)
                    messages.warning(request, "Measurement Given Successfully, Please wait for tailor response")
                    sewing_request.objects.filter(req_id=req.req_id).update(measurement_status=True)
                    return redirect('/customer_request_history/%s' % uid)
            else:
                fabric1 = ''
                fabric2 = ''
                fabric3 = ''
                if req.material_id1:
                    fabric1 = materials.objects.get(material_id=req.material_id1)
                if req.material_id2:
                    fabric2 = materials.objects.get(material_id=req.material_id2)
                if req.material_id3:
                    fabric3 = materials.objects.get(material_id=req.material_id3)
                form_value = sewing_measurement_form()
                return render(request, "customers/give_measurement.html", { 'fabric3': fabric3, 'fabric2': fabric2, 'fabric1': fabric1,'form_key': form_value,'req':req,'login_id': uid})
        else:
            messages.warning(request, "The tailor has not accepted your request yet.")
            return redirect('/customer_request_history/%s' % uid)
    else:
        return redirect('/login/')




def tailor_order_list(request, uid):
    if request.session.get('session_id'):
        req = sewing_request.objects.filter(measurement_status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(req, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "tailor/order_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def give_rate_details(request, uid,id):
    if request.session.get('session_id'):
        req = sewing_request.objects.get(req_id=id)
        measurement_id=sewing_measurements.objects.get(request_id=id)
        if req.request_status:
            if request.method == 'POST':
                    fabric1_qty = request.POST.get('qty1')
                    fabric2_qty = request.POST.get('qty2')
                    fabric3_qty = request.POST.get('qty3')
                    price1 = request.POST.get('price1')
                    price2 = request.POST.get('price2')
                    price3 = request.POST.get('price3')
                    sewing_charge = request.POST.get('sewing_charge')
                    design_charge = request.POST.get('design_charge')
                    total_price = request.POST.get('totalPrice')
                    sewing_details.objects.create(fabric1_qty=fabric1_qty,fabric2_qty=fabric2_qty,fabric3_qty=fabric3_qty,price1=price1,price2=price2,price3=price3,sewing_charge=sewing_charge,total_price=total_price,request_id=req,measurement_id=measurement_id,design_charge=design_charge)
                    sewing_request.objects.filter(req_id=req.req_id).update(rate_given=True)
                    messages.warning(request, "Rate Deatils Given Successfully")
                    return redirect('/tailor_order_list/%s' % uid)
            else:
                fabric1 = ''
                fabric2 = ''
                fabric3 = ''
                if req.material_id1:
                    fabric1 = materials.objects.get(material_id=req.material_id1)
                if req.material_id2:
                    fabric2 = materials.objects.get(material_id=req.material_id2)
                if req.material_id3:
                    fabric3 = materials.objects.get(material_id=req.material_id3)
                return render(request, "tailor/give_rate_details.html", { 'fabric3': fabric3, 'fabric2': fabric2, 'fabric1': fabric1,'req':req,'measurement':measurement_id,'login_id': uid})
        else:
            messages.warning(request, "You have no new orders")
            return redirect('/tailor_order_list/%s' % uid)
    else:
        return redirect('/login/')



def tailor_order_details(request, uid,id):
    if request.session.get('session_id'):
        order=orders.objects.get(sewing_id__request_id=id)
        req = sewing_request.objects.get(req_id=id)
        measurement_id=sewing_measurements.objects.get(request_id=id)
        rate=sewing_details.objects.get(request_id=id)
        fabric1 = ''
        fabric2 = ''
        fabric3 = ''
        if req.material_id1:
            fabric1 = materials.objects.get(material_id=req.material_id1)
        if req.material_id2:
            fabric2 = materials.objects.get(material_id=req.material_id2)
        if req.material_id3:
            fabric3 = materials.objects.get(material_id=req.material_id3)
        return render(request, "tailor/order_details.html", {'order':order, 'rate':rate,'fabric3': fabric3, 'fabric2': fabric2, 'fabric1': fabric1,'req':req,'measurement':measurement_id,'login_id': uid})
    else:
        return redirect('/login/')

def tailor_orders(request, uid):
        if request.session.get('session_id'):
            order = orders.objects.filter(Q(sewing_id__request_id__tailor_id=uid) & Q(order_status=True))
            if order:
                page_num = request.GET.get('page', 1)
                paginator = Paginator(order, 5)  # 6 employees per page
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    # if page is not an integer, deliver the first page
                    page_obj = paginator.page(1)
                except EmptyPage:
                    # if the page is out of range, deliver the last page
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, "tailor/orders.html",
                              {'login_id': uid, 'page_obj': page_obj, 'count': 1})

            else:
                messages.warning(request, "Currently No Orders")
                return render(request, "tailor/orders.html", {'login_id': uid, 'count': 0})
        else:
            return redirect('/login/')

def tailor_order_history(request, uid):
        if request.session.get('session_id'):
            order = orders.objects.filter(Q(sewing_id__request_id__tailor_id=uid) & Q(order_status=False))
            if order:
                page_num = request.GET.get('page', 1)
                paginator = Paginator(order, 5)  # 6 employees per page
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    # if page is not an integer, deliver the first page
                    page_obj = paginator.page(1)
                except EmptyPage:
                    # if the page is out of range, deliver the last page
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, "tailor/order_history.html",
                              {'login_id': uid, 'page_obj': page_obj, 'count': 1})

            else:
                messages.warning(request, "No Orders")
                return render(request, "tailor/order_history.html", {'login_id': uid, 'count': 0})
        else:
            return redirect('/login/')



def material_requests(request,uid,sewing_id,material_id):
    if request.session.get('session_id'):
        order=orders.objects.get(sewing_id=sewing_id)
        material_id=materials.objects.get(material_id=material_id)
        req_id=order.sewing_id.request_id.req_id
        try:
            material_request.objects.get(Q(order_id=order.order_id) & Q(material_id=material_id.material_id))
            messages.warning(request, "You have already requested")
            return redirect('/tailor_order_details/%s/%s' % (uid,req_id))

        except material_request.DoesNotExist:
            requested_on = datetime.today().date()
            manufacturer_id=manufacturer.objects.get(manufacturer_id=material_id.manufacturer_id.manufacturer_id)
            material_request.objects.create(order_id=order,requested_on=requested_on,material_id=material_id,manufacturer_id=manufacturer_id)
            messages.warning(request, "Requested")
            return redirect('/tailor_order_details/%s/%s' % (uid,req_id))
    else:
        return redirect('/login/')


def fabric_request(request, uid):
    if request.session.get('session_id'):
        req = material_request.objects.filter(order_id__sewing_id__request_id__tailor_id=uid).order_by('requested_on')
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "tailor/fabric_request.html",
                          {'login_id': uid, 'page_obj': page_obj, 'count': 1})

        else:
            messages.warning(request, "No Requests")
            return render(request, "tailor/fabric_request.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')


def material_requests_history(request, uid):
    if request.session.get('session_id'):
        req = material_request.objects.filter(Q(manufacturer_id=uid) & Q(request_status=True)).order_by('-requested_on')
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "manufacturer/material_request_history.html",
                          {'login_id': uid, 'page_obj': page_obj, 'count': 1})

        else:
            messages.warning(request, "No Requests")
            return render(request, "manufacturer/material_request_history.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')

def material_requests_list(request, uid):
    if request.session.get('session_id'):
        req = material_request.objects.filter(Q(manufacturer_id=uid) & Q(request_status=False)).order_by('requested_on')
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "manufacturer/material_requests.html",
                          {'login_id': uid, 'page_obj': page_obj, 'count': 1})

        else:
            messages.warning(request, "No Requests")
            return render(request, "manufacturer/material_requests.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')


def accept_material_request(request, uid, id,order_id):
    if request.session.get('session_id'):
        material_request.objects.filter(req_id=id).update(request_status=True)
        request_completed = material_request.objects.filter(order_id=order_id, request_status=False).exists()
        if request_completed == False:
            orders.objects.filter(order_id=order_id).update(material_req_status=True)
        return redirect('/material_requests_list/%s' % uid)
    else:
        return redirect('/login/')


def update_tailor_status(request,uid,id):
    if request.session.get('session_id'):
        status=orders.objects.get(order_id=id)
        if status.material_req_status == True:
            if status.delivery_agent_status==False:
                    if request.method == 'POST':
                        form = update_tailor_status_form(request.POST,instance=status)
                        if form.is_valid():
                            tailor_status=form.cleaned_data['tailor_status']
                            if tailor_status == "stitching finished":
                                form.save()
                                agent = delivery_agent.objects.filter(available=True).first()
                                pickup_date = datetime.now() + timedelta(days=1)
                                assign_delivery_agent.objects.create(agent_id=agent,pickup_date=pickup_date,order_id=status)
                                orders.objects.filter(order_id=id).update(deliver_status="Delivery Agent assigned",delivery_agent_status=True,pickup_date=pickup_date)
                                messages.warning(request, "Delivery Agent assigned")
                                return redirect('/tailor_orders/%s' % uid)
                            else:
                                form.save()
                                messages.warning(request, "Status Updated Successfully")
                                return redirect('/tailor_orders/%s' % uid)
                    else:
                        form=update_tailor_status_form(instance=status)
                        return render(request, "tailor/update_status.html", { 'login_id': uid,'form':form})
            else:
                messages.warning(request, "Delivery Agent assigned")
                return redirect('/tailor_orders/%s' % uid)
        else:
            messages.warning(request, "fabrics not yet received")
            return redirect('/tailor_orders/%s' % uid)

    else:
        return redirect('/login/')


def delivery_agent_order_history(request,uid):
    if request.session.get('session_id'):
        order_list = assign_delivery_agent.objects.filter(Q(agent_id=uid) & Q(deliver_status=True)).order_by('order_id__order_date')
        page_num = request.GET.get('page', 1)
        paginator = Paginator(order_list, 4)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "delivery/my_history.html", {'page_obj': page_obj, 'login_id': uid, })
    else:
        return redirect('/login/')

def delivery_agent_orders(request,uid):
    if request.session.get('session_id'):
        order_list = assign_delivery_agent.objects.filter(Q(agent_id=uid) & Q(deliver_status=False)).order_by('order_id__order_date')
        page_num = request.GET.get('page', 1)
        paginator = Paginator(order_list, 4)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "delivery/my_orders.html", {'page_obj': page_obj, 'login_id': uid, })
    else:
        return redirect('/login/')

def pickup_order(request, uid, id):
    if request.session.get('session_id'):
        assign_delivery_agent.objects.filter(order_id=id).update(pickup_status=True)
        orders.objects.filter(order_id=id).update(pickup_status=True,deliver_status="Order Pick Up Complete",)
        return redirect('/delivery_agent_orders/%s' % uid)
    else:
        return redirect('/login/')

def deliver_order(request, uid, id):
    if request.session.get('session_id'):
        orders.objects.filter(order_id=id).update(delivery_agent_status=True,order_status=False,deliver_status="Order Delivered",)
        assign_delivery_agent.objects.filter(order_id=id).update(deliver_status=True)
        delivery_agent.objects.filter(agent_id=uid).update(available=True)
        return redirect('/delivery_agent_orders/%s' % uid)
    else:
        return redirect('/login/')


def get_categories(request):
    if request.session.get('session_id'):
            data1= category.objects.all()
            data = serialize('json', data1)
            return JsonResponse(data, safe=False)
    else:
        return redirect('/login/')


def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')