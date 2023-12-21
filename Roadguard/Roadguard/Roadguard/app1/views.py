from datetime import datetime

from django.core.paginator import Paginator,Page, PageNotAnInteger, EmptyPage
from django.core.serializers import serialize
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth import logout as logouts
from django.http import HttpResponse,JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from .models import register, Officers, state, city, traffic_rule_violation, vehicle_details, offences, offenders
from .forms import RegisterForm, loginForm, EdituserForm, Editadminprofileform, addOfficerForm, addvehicledetailsform, \
    editvehicledetailsform, EditOfficerForm, editviolationform, Addviolationform, reportoffenceform, editoffenceform
from django.contrib import messages
import random
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def first(request):
    return render(request, "main/first.html")



def service(request):
    return render(request, "service.html")



def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = register.objects.get(email=email)
                try:
                    user1 = register.objects.get(Q(reg_id=user.reg_id) & Q(password=password))
                    if user.User_type == 1:
                        request.session['session_id'] = user.reg_id
                        return redirect('/adhome/%s' % user.reg_id)
                    else:
                        if user.status == True:
                            request.session['session_id'] = user.reg_id
                            return redirect('/users_home/%s' % user.reg_id)
                        else:
                            return redirect('/login/')
                except register.DoesNotExist:
                    messages.warning(request, "Incorrect Password")
                    return redirect('/login/')
            except register.DoesNotExist:
                try:
                    user = Officers.objects.get(email=email)
                    try:
                        user1 = Officers.objects.get(Q(officer_id=user.officer_id) & Q(password=password))
                        if user1:
                            request.session['session_id'] = user.officer_id
                            return redirect('/officers_home/%s' % user.officer_id)
                    except Officers.DoesNotExist:
                        messages.warning(request, "Incorrect Password")
                        return redirect('/login/')
                except Officers.DoesNotExist:
                    try:
                        user = register.objects.get(email=email)
                        try:
                            user1 = register.objects.get(Q(user_id=user.user_id) & Q(password=password))
                            request.session['session_id'] = user.user_id
                            return redirect('/offenders_home/%s' % user.user_id)
                        except register.DoesNotExist:
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                    except register.DoesNotExist:
                        messages.warning(request, "Invalid Email Id")
                        return redirect('/login/')
    else:
        form1 = loginForm()
        return render(request, "main/login.html", {'form': form1})


def register_func(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=post_email).exists():
                messages.warning(request,"Email Id Already Exist")
                return redirect('/register/')
            else:
                form.save()
                uname = register.objects.get(email=post_email)
                register.objects.filter(reg_id=uname.reg_id).update(state = state,city = city)
                User.objects.create_user(username=uname,email=post_email)
                messages.warning(request,"Registration Successful")
                return redirect('/login/')

    else:

        form = RegisterForm()
        return render(request, "main/register.html", {'form': form})

def officer_reg(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = addOfficerForm(request.POST,request.FILES)
            length_of_string = 10
            sample_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@$^&*/!"
            passwd = ''.join(random.choices(sample_str, k=length_of_string))
            if form.is_valid():
                name = form.cleaned_data['name']
                post_email = form.cleaned_data['email']
                station = form.cleaned_data['station']
                phone_no = form.cleaned_data['phone_no']
                state = request.POST.get('state')
                city = request.POST.get('city')
                id_proof = form.files['id_proof']
                if User.objects.filter(email=post_email).exists():
                    messages.warning(request, "Email Id Already Exist")
                    return redirect('/officer_reg/%s' % uid)
                else:
                    Officers.objects.create(phone_no=phone_no,station=station,name=name, email=post_email, password=passwd,id_proof=id_proof)
                    uname = Officers.objects.get(email=post_email)
                    Officers.objects.filter(officer_id=uname.officer_id).update(state=state, city=city)
                    User.objects.create_user(username=uname, email=post_email)

                    messages.warning(request, "Officer Registered Successfully")
                    return redirect('/officer_reg/%s' % uid)
        else:
            form_value = addOfficerForm()
            return render(request, "admin/add_officers.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def admin_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "admin/adhome.html", {'login_id': uid})
    else:
        return redirect('/login/')

def officers_list(request, uid):
    if request.session.get('session_id'):
        officer = Officers.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(officer, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/officers_list.html",
                      { 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def users_list(request, uid):
    if request.session.get('session_id'):
        user = register.objects.filter(Q(User_type=2) & Q(status=True))
        page_num = request.GET.get('page', 1)
        paginator = Paginator(user, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/users_list.html",
                      {'page_obj': page_obj, 'login_id': uid, })
    else:
        return redirect('/login/')

def approveusers(request, uid):
    if request.session.get('session_id'):
        users = register.objects.filter(status=False)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(users, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_users.html",
                      {'page_obj': page_obj, 'login_id': uid, })
    else:
        return redirect('/login/')

def approve_users(request, uid, id):
    if request.session.get('session_id'):
        register.objects.filter(reg_id=id).update(status=True)
        return redirect('/approveusers/%s' % uid)
    else:
        return redirect('/login/')

def delete_officers(request, uid, id):
    if request.session.get('session_id'):
        officer = Officers.objects.get(officer_id=id)
        Officers.objects.get(officer_id=id).delete()
        return redirect('/officers_list/%s' % uid)
    else:
        return redirect('/login/')

def reject_users(request, uid, id):
    if request.session.get('session_id'):
        users = register.objects.get(reg_id=id)
        user = User.objects.get(email=users.email)
        user.delete()
        register.objects.get(reg_id=id).delete()
        return redirect('/approveusers/%s' % uid)
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

def delete_user(request, uid, id):
    if request.session.get('session_id'):
        users = register.objects.get(reg_id=id)
        user = User.objects.get(email=users.email)
        user.delete()
        register.objects.filter(reg_id=id).delete()
        return redirect('/users_list/%s' % uid)
    else:
        return redirect('/login/')

def admin_reported_offences(request, uid):
    if request.session.get('session_id'):
        offence = offences.objects.all().order_by('-reported_on')
        if offence:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offence, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "admin/reported_offences.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offence has been reported.")
            return render(request, "admin/reported_offences.html", {'login_id': uid, 'count': 0})
    else:
        return redirect('/login/')

def admin_delete_reported_offence(request, uid, id):
    if request.session.get('session_id'):
        offences.objects.get(offence_id=id).delete()
        return redirect('/admin_reported_offences/%s' % uid)
    else:
        return redirect('/login/')

def admin_view_violations_list(request, uid):
    if request.session.get('session_id'):
        violations= traffic_rule_violation.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(violations, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/violations_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def admin_offenders_list(request, uid):
    if request.session.get('session_id'):
        offender = offenders.objects.all()
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "admin/offenders_list.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offence has been reported yet.")
            return render(request, "admin/offenders_list", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


# ----------------------------------------USERS----------------------------------------------------

def users_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "users/users_home.html", {'login_id': uid})
    else:
        return redirect('/login/')

def user_profile(request, uid):
    if request.session.get('session_id'):
        user = register.objects.get(reg_id=uid)
        return render(request, "users/users_profile.html", {'users': user, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_user_profile(request, uid):
    if request.session.get('session_id'):
        user = register.objects.get(reg_id=uid)
        if request.method == 'POST':
            form = EdituserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/user_profile/%s' % uid)

        else:
            form_value = EdituserForm(instance=user)
            return render(request, "users/edit_user_profile.html",
                          {'form_key': form_value, 'users': user, 'login_id': uid})
    else:
        return redirect('/login/')


def view_vehicles(request, uid):
    if request.session.get('session_id'):
            vehicles= vehicle_details.objects.filter(owner_id=uid)
            page_num = request.GET.get('page', 1)
            paginator = Paginator(vehicles, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)

            return render(request, "users/view_vehicles.html", {'page_obj': page_obj,'login_id': uid})
    else:
        return redirect('/login/')


def add_vehicle_details(request, uid):
    user = register.objects.get(reg_id=uid)

    if request.session.get('session_id'):
        if request.method == 'POST':
            form = addvehicledetailsform(request.POST, request.FILES)

            if form.is_valid():
                    try:
                        image = request.FILES['images']
                    except MultiValueDictKeyError:
                        messages.error(request, "Image not provided")
                        return redirect('/add_vehicle_details/%s' % uid )

                    vehicle_no = form.cleaned_data['vehicle_no']
                    vehicle_details.objects.create(images=image, owner_id=user, vehicle_no=vehicle_no)
                    messages.success(request, "Vehicle Details Added Successfully")
                    return redirect('/add_vehicle_details/%s' % uid )
            else:
                    messages.warning(request, "Vehicle with this number already exists.")
                    return redirect('/add_vehicle_details/%s' % uid)

        else:
            form_value = addvehicledetailsform()
            return render(request, "users/add_vehicle_details.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_vehicle(request, uid, id):
    if request.session.get('session_id'):
        vehicles = vehicle_details.objects.get(vehicle_id=id)
        if request.method == 'POST':
            form = editvehicledetailsform(request.POST,request.FILES, instance=vehicles)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/view_vehicles/%s' % uid)
        else:
            form_value = editvehicledetailsform(instance=vehicles)
            return render(request, "users/edit_vehicle_details.html", {'vehicle':vehicles,'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def delete_vehicle(request, uid, id):
    if request.session.get('session_id'):
        vehicle_details.objects.filter(vehicle_id=id).delete()
        return redirect('/view_vehicles/%s' % uid)
    else:
        return redirect('/login/')


def report_offence(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = reportoffenceform(request.POST, request.FILES)
            if form.is_valid():
                violation_id = form.cleaned_data['violation_id']
                details = form.cleaned_data['details']
                vehicle_no = form.cleaned_data['vehicle_no']
                officer = request.POST.get('officers')
                image = form.files['image']
                officer_id=Officers.objects.get(officer_id=officer)
                reporter_id=register.objects.get(reg_id=uid)
                offences.objects.create(officer_id=officer_id, reporter_id=reporter_id,violation_id=violation_id, details=details, vehicle_no=vehicle_no, image=image,)
                messages.warning(request, "Offence Reported")
                return redirect('/report_offence/%s' % uid)
        else:
            form_value = reportoffenceform()
            return render(request, "users/report_offence.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def reported_offences(request, uid):
    if request.session.get('session_id'):
        offence = offences.objects.filter(reporter_id=uid)
        if offence:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offence, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "users/reported_offences.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offence has been reported by you.")
            return render(request, "users/reported_offences.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def edit_reported_offence(request, uid,id):
    if request.session.get('session_id'):
        offence = offences.objects.get(offence_id=id)
        if request.method == 'POST':
            form = editoffenceform(request.POST, request.FILES,instance=offence)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/reported_offences/%s' % uid)
        else:
            form_value = editoffenceform(instance=offence)
            return render(request, "users/edit_reported_offence.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def delete_reported_offence(request, uid, id):
    if request.session.get('session_id'):
        offences.objects.get(offence_id=id).delete()
        return redirect('/reported_offences/%s' % uid)
    else:
        return redirect('/login/')

def my_offences(request, uid):
    if request.session.get('session_id'):
        offender = offenders.objects.filter(Q(user_id=uid) & Q(offender_status=True))
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "users/my_offences.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offence has been reported to You.")
            return render(request, "users/my_offences.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def user_fine_paid(request, uid):
    if request.session.get('session_id'):
        offender = offenders.objects.filter(Q(user_id=uid) & Q(fine_status=True))
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "users/fine_paid.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offence has been reported yet.")
            return render(request, "users/fine_paid.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def admin_non_user_offenders_list(request, uid):
    if request.session.get('session_id'):
        offender = offences.objects.filter(Q(offence_status=True) & Q(user_status=False))
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "admin/non_user_offenders_list.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offenders has been reported yet.")
            return render(request, "admin/non_user_offenders_list.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


# ------------------------------------------OFFICER-------------------------------------------------------


def officers_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "officers/officers_home.html", {'login_id': uid})
    else:
        return redirect('/login/')

def officer_profile(request, uid):
    if request.session.get('session_id'):
        officer = Officers.objects.get(officer_id=uid)
        return render(request, "officers/officer_profile.html", {'users': officer, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_officer_profile(request, uid):
    if request.session.get('session_id'):
        officer = Officers.objects.get(officer_id=uid)
        if request.method == 'POST':
            form = EditOfficerForm(request.POST, instance=officer)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/officer_profile/%s' % uid)
        else:
            form_value = EditOfficerForm(instance=officer)
            return render(request, "officers/edit_officer_profile.html",
                          {'form_key': form_value, 'users': officer, 'login_id': uid})
    else:
        return redirect('/login/')


def add_violations(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addviolationform(request.POST)
            if form.is_valid():
                form.save()
                messages.warning(request, "traffic violation Detail Added Successfully")
                return redirect('/add_violations/%s' % uid)
        else:
            form_value = Addviolationform()
            return render(request, "officers/add_violations.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_violations(request, uid, id):
    if request.session.get('session_id'):
        violation = traffic_rule_violation.objects.get(violation_id=id)
        if request.method == 'POST':
            form = editviolationform(request.POST, instance=violation)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/violations_list/%s' % uid)
        else:
            form_value = editviolationform(instance=violation)
            return render(request, "officers/edit_violations.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def violations_list(request, uid):
    if request.session.get('session_id'):
        violations= traffic_rule_violation.objects.all()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(violations, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "officers/violations_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_violation(request, uid, id):
    if request.session.get('session_id'):
        traffic_rule_violation.objects.get(violation_id=id).delete()
        return redirect('/violations_list/%s' % uid)
    else:
        return redirect('/login/')


def officer_reported_offences(request, uid):
    if request.session.get('session_id'):
        offence = offences.objects.filter(officer_id=uid)
        if offence:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offence, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "officers/reported_offences.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offence has been reported.")
            return render(request, "officers/reported_offences.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def verify_offender(request, uid,id,vehicle_no):
    if request.session.get('session_id'):
        offence = offences.objects.get(offence_id=id)
        try:
            owner=vehicle_details.objects.get(vehicle_no=vehicle_no)
            user_id=register.objects.get(reg_id=owner.owner_id.reg_id)
            offenders.objects.create(offence_id=offence,user_id=user_id)
            offences.objects.filter(offence_id=id).update(offence_status=True,user_status=True)
            return redirect('/officer_reported_offences/%s' % uid)
        except vehicle_details.DoesNotExist:
            offences.objects.filter(offence_id=id).update(offence_status=True)
            messages.warning(request, "Non Application User")
            return redirect('/officer_reported_offences/%s' % uid)
    else:
        return redirect('/login/')

def offenders_list(request, uid):
    if request.session.get('session_id'):
        offender = offenders.objects.filter(Q(offence_id__officer_id=uid) & Q(offender_status=True))
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "officers/offenders_list.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offenders has been reported yet.")
            return render(request, "officers/offenders_list.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def non_user_offenders_list(request, uid):
    if request.session.get('session_id'):
        offender = offences.objects.filter(Q(officer_id=uid)& Q(offence_status=True) & Q(user_status=False))
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "officers/non_user_offenders_list.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offenders has been reported yet.")
            return render(request, "officers/non_user_offenders_list.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def fine_collected(request,uid, id):
    if request.session.get('session_id'):
        fine_paid_on=datetime.now().date()
        offenders.objects.filter(offender_id=id).update(offender_status=False,fine_status=True,fine_paid_on=fine_paid_on)
        return redirect('/offenders_list/%s' % uid)
    else:
        return render('/login/')


def fine_paid(request, uid):
    if request.session.get('session_id'):
        offender = offenders.objects.filter(Q(offence_id__officer_id=uid) & Q(fine_status=True))
        if offender:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(offender, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "officers/fine_paid.html",
                          {'page_obj': page_obj, 'login_id': uid, 'count': 1})
        else:
            messages.warning(request, "No offenders has been reported yet.")
            return render(request, "officers/fine_paid.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


# def admin_offense_list(request, uid):
#     if request.session.get('session_id'):
#         offenses = offense.objects.all()
#         page_num = request.GET.get('page', 1)
#         paginator = Paginator(offenses, 3)
#         try:
#             page_obj = paginator.page(page_num)
#         except PageNotAnInteger:
#             # if page is not an integer, deliver the first page
#             page_obj = paginator.page(1)
#         except EmptyPage:
#             # if the page is out of range, deliver the last page
#             page_obj = paginator.page(paginator.num_pages)
#         return render(request, "admin/offense_list.html", {'offense': offenses, 'login_id': uid, 'page_obj': page_obj})
#     else:
#         return redirect('/login/')
# def delete_offense(request, uid, id):
#     if request.session.get('session_id'):
#         offense.objects.get(offense_id=id).delete()
#         return redirect('/offense_list/%s' % uid)
#     else:
#         return redirect('/login/')
#
# def offense_more_details(request, uid, id):
#     if request.session.get('session_id'):
#         offenses = offense.objects.get(offense_id=id)
#         return render(request, "users/offense_more_details.html",{'offense': offenses, 'login_id': uid,})
#     else:
#         return redirect('/login/')
#
#

def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')

def get_states(request):
    data1 = state.objects.all()
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)

def get_cities(request):
    states=request.GET.get('state')
    state_id=state.objects.get(state=states)
    data1 = city.objects.filter(state_id=state_id.state_id)
    data = serialize('json', data1)
    return JsonResponse(data,safe=False)

def get_officers(request):
    desired_city=request.GET.get('city')
    data1 = Officers.objects.filter(city=desired_city)
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)


def new_request(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        condition1 = Q(officer_id=uid)
        condition2 = Q(offence_status=False)

        offence = offences.objects.filter(condition1 & condition2)

        if offence.exists():  # Use exists() to check if any records match the conditions
            data = {'status': True, 'count': 1}
            return JsonResponse(data)
        else:
            data = {'status': False, 'count': 0}
            return JsonResponse(data)
    else:
        return redirect('/login/')

def offender_notification(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        print("--------------------------------",uid)
        condition1 = Q(user_id=uid)
        condition2 = Q(offender_status=True)

        offence = offenders.objects.filter(condition1 & condition2)

        if offence.exists():  # Use exists() to check if any records match the conditions
            data = {'status': True, 'count': 1}
            return JsonResponse(data)
        else:
            data = {'status': False, 'count': 0}
            return JsonResponse(data)
    else:
        return redirect('/login/')