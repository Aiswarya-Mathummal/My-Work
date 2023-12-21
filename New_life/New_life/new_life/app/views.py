from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout as logouts
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userregisterform, ambulancedriverregform, Edithospitalregform, Edituserform, \
    Editambulancedriverregform, hospitalregform, Loginform, Editadminprofileform, Addambulanceform, editambulanceform, \
    Patientdetailsform, updateDriverstatusForm,createComplaintForm,replyComplaintForm
from .models import ambulance_drivers, user_reg, hospital, ambulance, state, city, patient_details, booking_details, \
    complaints, driver_location
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


def user_reg_func(request):
    if request.method == 'POST':
        form = userregisterform(request.POST)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/user_reg/')
            else:
                form.save()
                uname = user_reg.objects.get(email=post_email)
                user_reg.objects.filter(reg_id=uname.reg_id).update(state=state, city=city)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/user_reg/')

    else:
        form_value = userregisterform()
        return render(request, "main/register.html", {'form_key': form_value})


def ambulance_driver_reg(request):
    if request.method == 'POST':
        form = ambulancedriverregform(request.POST, request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/supplier_reg/')
            else:
                form.save()
                uname = ambulance_drivers.objects.get(email=post_email)
                ambulance_drivers.objects.filter(driver_id=uname.driver_id).update(state=state, city=city)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/ambulance_driver_reg/')

    else:
        form_value = ambulancedriverregform()
        return render(request, "main/ambulance_driver_reg.html", {'form_key': form_value})

def hospital_reg(request):
    if request.method == 'POST':
        form = hospitalregform(request.POST, request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/hospital_reg/')
            else:
                form.save()
                uname = hospital.objects.get(email=post_email)
                hospital.objects.filter(hospital_id=uname.hospital_id).update(state=state,city=city)
                User.objects.create_user(username=uname, email=post_email)
                messages.warning(request, "Registration Successful")
                return redirect('/hospital_reg/')

    else:
        form_value = hospitalregform()
        return render(request, "main/hospital_reg.html", {'form_key': form_value})


def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            email_val = form.cleaned_data['email']
            pswd = form.cleaned_data['password']
            try:
                user = user_reg.objects.get(email=email_val)
                if user:

                    try:
                        user1 = user_reg.objects.get(Q(reg_id=user.reg_id) & Q(password=pswd))
                        if user1:
                            request.session['session_id'] = user.reg_id
                            if user.usertype == 1:
                                return redirect('/admin_home/%s' % user.reg_id)
                            else:
                                return redirect('/user_home/%s' % user.reg_id)
                    except user_reg.DoesNotExist:
                        user1 = None
                        messages.warning(request, "Incorrect Password")
                        return redirect('/login/')
            except user_reg.DoesNotExist:
                try:
                    user = ambulance_drivers.objects.get(email=email_val)
                    if user:
                        try:
                            user1 = ambulance_drivers.objects.get(Q(driver_id=user.driver_id) & Q(password=pswd))
                            if user1:
                                if user.status == True:
                                    request.session['session_id'] = user.driver_id
                                    return redirect('/ambulance_driver_home/%s' % user.driver_id)
                                else:
                                    messages.warning(request, "You are not yet approved")
                                    return redirect('/login/')
                        except ambulance_drivers.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                except ambulance_drivers.DoesNotExist:
                    try:
                        user = hospital.objects.get(email=email_val)
                        if user:
                            try:
                                user1 = hospital.objects.get(Q(hospital_id=user.hospital_id) & Q(password=pswd))
                                if user1:
                                    if user.status == True:
                                        request.session['session_id'] = user.hospital_id
                                        return redirect('/hospital_home/%s' % user.hospital_id)
                                    else:
                                        messages.warning(request, "You are not yet approved")
                                        return redirect('/login/')
                            except hospital.DoesNotExist:
                                user1 = None
                                messages.warning(request, "Incorrect Password")
                                return redirect('/login/')
                    except hospital.DoesNotExist:
                        user = None
                        messages.warning(request, "Invalid Email Id")
                        return redirect('/login/')
    else:
        form1 = Loginform()
        return render(request, "main/login.html", {'form': form1})


def user_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "users/user_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def admin_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "admin/admin_home.html", {'login_id': uid})
    else:
        return redirect('/login/')

def ambulance_driver_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "ambulance_driver/ambulance_driver_home.html", {'login_id': uid})
    else:
        return redirect('/login/')


def hospital_home(request, uid):
    if request.session.get('session_id'):
        return render(request, "hospital/hospital_home.html", {'login_id': uid})
    else:
        return redirect('/login/')



def admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = user_reg.objects.get(reg_id=uid)
        return render(request, "admin/admin_profile.html", {'admin': admin, 'login_id': uid})
    else:
        return redirect('/login/')


def edit_admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = user_reg.objects.get(reg_id=uid)
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



def user_profile(request, uid):
    if request.session.get('session_id'):
        users = user_reg.objects.get(reg_id=uid)
        return render(request, "users/user_profile.html", {'users': users,'login_id': uid})
    else:
        return redirect('/login/')


def edit_user_profile(request, uid):
    if request.session.get('session_id'):
        users = user_reg.objects.get(reg_id=uid)
        if request.method == 'POST':
            form = Edituserform(request.POST, instance=users)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/user_profile/%s' % uid)

        else:
            form_value = Edituserform(instance=users)
            return render(request, "users/edit_user_profile.html",
                          {'form_key': form_value, 'users': users, 'login_id': uid})
    else:
        return redirect('/login/')



def hospital_profile(request, uid):
    if request.session.get('session_id'):
        hospitals = hospital.objects.get(hospital_id=uid)
        return render(request, "hospital/hospital_profile.html", {'hospital': hospitals,'login_id': uid})
    else:
        return redirect('/login/')


def edit_hospital_profile(request, uid):
    if request.session.get('session_id'):
        hospitals = hospital.objects.get(hospital_id=uid)
        if request.method == 'POST':
            form = Edithospitalregform(request.POST, instance=hospitals)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/hospital_profile/%s' % uid)

        else:
            form_value = Edithospitalregform(instance=hospitals)
            return render(request, "hospital/edit_hospital_profile.html",
                          {'form_key': form_value, 'hospital': hospitals, 'login_id': uid})
    else:
        return redirect('/login/')




def ambulance_driver_profile(request, uid):
    if request.session.get('session_id'):
        driver = ambulance_drivers.objects.get(driver_id=uid)
        return render(request, "ambulance_driver/ambulance_driver_profile.html", {'driver': driver,'login_id': uid})
    else:
        return redirect('/login/')


def edit_ambulance_driver_profile(request, uid):
    if request.session.get('session_id'):
        driver = ambulance_drivers.objects.get(driver_id=uid)
        if request.method == 'POST':
            form = Editambulancedriverregform(request.POST, instance=driver)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/ambulance_driver_profile/%s' % uid)

        else:
            form_value = Editambulancedriverregform(instance=driver)
            return render(request, "ambulance_driver/edit_ambulance_driver_profile.html",
                          {'form_key': form_value, 'driver': driver, 'login_id': uid})
    else:
        return redirect('/login/')


def users_list(request, uid):
    if request.session.get('session_id'):
        users = user_reg.objects.filter(usertype=2)

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
        return render(request, "admin/users_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_user(request, uid, id):
    if request.session.get('session_id'):
        users = user_reg.objects.get(reg_id=id)
        user = User.objects.get(email=users.email)
        user.delete()
        user_reg.objects.filter(reg_id=id).delete()
        return redirect('/users_list/%s' % uid)
    else:
        return redirect('/login/')



def ambulance_drivers_list(request, uid):
    if request.session.get('session_id'):
        drivers = ambulance_drivers.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(drivers, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/ambulance_drivers_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_ambulance_driver(request, uid, id):
    if request.session.get('session_id'):
        drivers = ambulance_drivers.objects.get(driver_id=id)
        user = User.objects.get(email=drivers.email)
        user.delete()
        ambulance_drivers.objects.get(driver_id=id).delete()
        return redirect('/ambulance_drivers_list/%s' % uid)
    else:
        return redirect('/login/')


def approve_ambulance_driver_list(request, uid):
    if request.session.get('session_id'):
        drivers = ambulance_drivers.objects.filter(status=False)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(drivers, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_ambulance_drivers.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_ambulance_driver(request, uid, id):
    if request.session.get('session_id'):
        ambulance_drivers.objects.filter(driver_id=id).update(status=True)
        return redirect('/approve_ambulance_driver_list/%s' % uid)
    else:
        return redirect('/login/')


def reject_ambulance_driver(request, uid, id):
    if request.session.get('session_id'):
        drivers = ambulance_drivers.objects.get(driver_id=id)
        user = User.objects.get(email=drivers.email)
        user.delete()
        ambulance_drivers.objects.get(driver_id=id).delete()
        return redirect('/approve_ambulance_driver_list/%s' % uid)
    else:
        return redirect('/login/')




def hospitals_list(request, uid):
    if request.session.get('session_id'):
        hospitals = hospital.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(hospitals, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/hospitals_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def delete_hospital(request, uid, id):
    if request.session.get('session_id'):
        hospitals = hospital.objects.get(hospital_id=id)
        user = User.objects.get(email=hospitals.email)
        user.delete()
        hospital.objects.get(hospital_id=id).delete()
        return redirect('/hospitals_list/%s' % uid)
    else:
        return redirect('/login/')


def approve_hospitals_list(request, uid):
    if request.session.get('session_id'):
        hospitals = hospital.objects.filter(status=False)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(hospitals, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_hospital_list.html",
                      {'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_hospital(request, uid, id):
    if request.session.get('session_id'):
        hospital.objects.filter(hospital_id=id).update(status=True)
        return redirect('/approve_hospitals_list/%s' % uid)
    else:
        return redirect('/login/')


def reject_hospital(request, uid, id):
    if request.session.get('session_id'):
        hospitals = hospital.objects.get(hospital_id=id)
        user = User.objects.get(email=hospitals.email)
        user.delete()
        hospital.objects.get(hospital_id=id).delete()
        return redirect('/approve_hospitals_list/%s' % uid)
    else:
        return redirect('/login/')

def ambulance_details(request, uid):
    if request.session.get('session_id'):
        try:
            ambulances= ambulance.objects.get(owner_id=uid)
            return render(request, "ambulance_driver/ambulance_details.html", {'ambulance': ambulances,'login_id': uid})
        except ambulance.DoesNotExist:
            return redirect('/add_ambulance_details/%s' % uid)
    else:
        return redirect('/login/')


def add_ambulance_details(request, uid):
    driver = ambulance_drivers.objects.get(driver_id=uid)
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addambulanceform(request.POST,request.FILES)
            if form.is_valid():
                image = form.files['image']
                vehicle_no = form.cleaned_data['vehicle_no']
                if ambulance.objects.filter(vehicle_no=vehicle_no).exists():
                    messages.warning(request, "Ambulance Already Registered")
                    return redirect('/add_ambulance_details/%s' % uid)
                else:
                    ambulance.objects.create(image=image,owner_id=driver,vehicle_no=vehicle_no)

                    messages.warning(request, "Ambulance Details Added Successfully")
                    return redirect('/ambulance_details/%s' % uid)
        else:
            form_value = Addambulanceform()
            return render(request, "ambulance_driver/add_ambulance_details.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_ambulance_details(request, uid, id):
    if request.session.get('session_id'):
        ambulances = ambulance.objects.get(ambulance_id=id)
        if request.method == 'POST':
            form = editambulanceform(request.POST,request.FILES, instance=ambulances)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/ambulance_details/%s' % uid)
        else:
            form_value = editambulanceform(instance=ambulances)
            return render(request, "ambulance_driver/edit_ambulance_details.html", {'ambulance':ambulances,'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def get_vehicle_status(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        try:
            ambulances=ambulance_drivers.objects.get(driver_id=uid)
            if ambulances.available==True:
                data = {'status': True, 'active': 1}
                return JsonResponse(data)
            else:
                data = {'status': True, 'active': 0}
                return JsonResponse(data)
        except ambulance_drivers.DoesNotExist:
            data = {'status': False}
            return JsonResponse(data)
    else:
        return redirect('/login/')

def book_ambulance(request,uid):
    if request.session.get('session_id'):
        user = user_reg.objects.get(reg_id=uid)
        hospitals=hospital.objects.filter(status=True).filter(city=user.city).union(
        hospital.objects.filter(status=True).exclude(city=user.city))
        if request.method == 'POST':
            lat = request.POST.get('latitude')
            lon = request.POST.get('longitude')
            user_lat=float(lat)
            user_lon=float(lon)
            search_radius = 5.0
            nearest_distance = float('inf')
            available_ambulance_drivers = ambulance_drivers.objects.filter(status=True, available=True)
            driver = driver_location.objects.filter(Q(driver_id__in=available_ambulance_drivers))
            for i in driver:
                distance = haversine(user_lat,user_lon, i.latitude, i.longitude)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_driver = i.driver_id
            if driver:
                form = Patientdetailsform(request.POST)
                hosp = request.POST.get('hospital')
                if form.is_valid():
                    name= form.cleaned_data['name']
                    age=form.cleaned_data['age']
                    gender=form.cleaned_data['gender']
                    reason=form.cleaned_data['reason']
                    hospital_id=hospital.objects.get(hospital_id=hosp)
                    patient=patient_details.objects.create(latitude=lat,longitude=lon,state=user.state,city=user.city,name=name,age=age,gender=gender,reason=reason,hospital=hospital_id,requestor_id=user)
                    return redirect('/confirm_booking/%s/%s/%s' % (uid, patient.patient_id, nearest_driver))
            else:
                messages.warning(request, "No drivers currently available at this location")
                return redirect('/book_ambulance/%s' % uid)

        else:
            form_value = Patientdetailsform()
            return render(request, "users/book_ambulance.html",{'form_key': form_value,'hospitals':hospitals, 'login_id': uid})
    else:
        return redirect('/login/')


def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

def book_ambulance_city(request,uid):
    if request.session.get('session_id'):
        user = user_reg.objects.get(reg_id=uid)
        if request.method == 'POST':
                city = request.POST.get('city')
                driver = ambulance_drivers.objects.filter(Q(status=True) & Q(available=True) & Q(city=city)).first()
                if driver:
                    form = Patientdetailsform(request.POST)
                    hosp = request.POST.get('hospital')
                    if form.is_valid():
                        name= form.cleaned_data['name']
                        age=form.cleaned_data['age']
                        gender=form.cleaned_data['gender']
                        reason=form.cleaned_data['reason']
                        state=request.POST.get('state')
                        hospital_id=hospital.objects.get(hospital_id=hosp)
                        patient=patient_details.objects.create(state=state,city=city,name=name,age=age,gender=gender,reason=reason,hospital=hospital_id,requestor_id=user)
                        return redirect('/confirm_booking/%s/%s' % (uid, patient.patient_id))
                else:
                    messages.warning(request, "No drivers currently available at this location")
                    return redirect('/book_ambulance/%s' % uid)
        else:
            form_value = Patientdetailsform()
            return render(request, "users/book_ambulance_by_city.html",{'form_key': form_value,'login_id': uid})
    else:
        return redirect('/login/')


def confirm_booking(request,uid,id,driver_id):
    if request.session.get('session_id'):
        patient=patient_details.objects.get(patient_id=id)
        driver = ambulance_drivers.objects.get(driver_id=driver_id)
        ambulances = ambulance.objects.get(owner_id=driver.driver_id)
        if request.method == 'POST':
            booking=booking_details.objects.create(driver_id=driver,patient_id=patient)
            ambulance.objects.filter(owner_id=driver.driver_id).update(vehicle_status=False)
            ambulance_drivers.objects.filter(driver_id=driver.driver_id).update(available=False)
            return redirect('/track_booking/%s/%s' %(uid,booking.booking_id))
        else:
            return render(request, "users/confirm_booking.html",{ 'ambulance':ambulances,'patient': patient,'driver':driver,'login_id': uid})
    else:
        return redirect('/login/')

def track_booking(request,uid,id):
    if request.session.get('session_id'):
        booking=booking_details.objects.get(booking_id=id)
        return render(request, "users/track_booking.html", {'booking': booking, 'login_id': uid})
    else:
        return redirect('/login/')


def cancel_booking(request, uid, id):
    if request.session.get('session_id'):
        patient_details.objects.get(patient_id=id).delete()
        return redirect('/book_ambulance/%s' % uid)
    else:
        return redirect('/login/')


def booking_history(request,uid):
    if request.session.get('session_id'):
        booking=booking_details.objects.filter(patient_id__requestor_id=uid).order_by('-booked_on')
        if booking:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(booking, 3)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "users/booking_history.html", {'page_obj': page_obj, 'login_id': uid,'count':1})
        else:
            messages.warning(request, "You have no previous bookings")
            return render(request, "users/booking_history.html", {'login_id': uid,'count':0})

    else:
        return redirect('/login/')


def patients_details(request,uid):
    if request.session.get('session_id'):
        booking=booking_details.objects.filter(patient_id__hospital=uid).order_by('-booked_on')
        if booking:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(booking, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "hospital/patients_details.html", {'page_obj': page_obj, 'login_id': uid,'count':1})
        else:
            messages.warning(request, "You have no previous bookings")
            return render(request, "hospital/patients_details.html", {'login_id': uid,'count':0})

    else:
        return redirect('/login/')

def track_patient(request,uid,id):
    if request.session.get('session_id'):
        booking=booking_details.objects.get(booking_id=id)
        return render(request, "hospital/track_patient.html", {'booking': booking, 'login_id': uid})
    else:
        return redirect('/login/')


def ambulance_request(request,uid):
    if request.session.get('session_id'):
        try:
            booking=booking_details.objects.get(Q(driver_id=uid) & Q(booking_status=False))
            if request.method == 'POST':
                form = updateDriverstatusForm(request.POST,instance=booking)
                if form.is_valid():
                    driver_status=form.cleaned_data['driver_status']
                    if driver_status == "Ride Completed":
                        form.save()
                        booking_details.objects.filter(driver_id=uid).update(booking_status=True)
                        ambulance_drivers.objects.filter(driver_id=uid).update(available=True)
                        ambulance.objects.filter(Owner_id=uid).update(vehicle_status=True)
                        return redirect('/ambulance_request/%s' % uid)
                    else:
                        form.save()
                        messages.warning(request, "Status Updated Successfully")
                        return redirect('/ambulance_request/%s' % uid)
            else:
                form=updateDriverstatusForm(instance=booking)
                return render(request, "ambulance_driver/ambulance_request.html", {'booking': booking, 'login_id': uid,'count':1,'form':form})
        except:
            messages.warning(request, "You have no new request")
            return render(request, "ambulance_driver/ambulance_request.html", {'login_id': uid,'count':0})

    else:
        return redirect('/login/')



def request_history(request,uid):
    if request.session.get('session_id'):
        booking=booking_details.objects.filter(driver_id=uid).order_by('-booked_on')
        if booking:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(booking, 5)  # 6 employees per page
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                # if page is not an integer, deliver the first page
                page_obj = paginator.page(1)
            except EmptyPage:
                # if the page is out of range, deliver the last page
                page_obj = paginator.page(paginator.num_pages)
            return render(request, "ambulance_driver/request_history.html", {'page_obj': page_obj, 'login_id': uid,'count':1})
        else:
            messages.warning(request, "You have no previous requests")
            return render(request, "ambulance_driver/request_history.html", {'login_id': uid,'count':0})

    else:
        return redirect('/login/')

def track_request(request,uid,id):
    if request.session.get('session_id'):
        booking=booking_details.objects.get(booking_id=id)
        return render(request, "ambulance_driver/track_request.html", {'booking': booking, 'login_id': uid})
    else:
        return redirect('/login/')


def update_location(request,uid):
    if request.session.get('session_id'):
        if request.method=='POST':
            state = request.POST.get('state')
            city = request.POST.get('city')
            ambulance_drivers.objects.filter(driver_id=uid).update(state=state, city=city)
            return redirect('/update_location/%s' % uid)
        else:
            return render(request, "ambulance_driver/update_location.html", {'login_id': uid})
    else:
        return redirect('/login/')




def create_complaint(request, uid,id):
    if request.session.get('session_id'):
        try:
            complaint=complaints.objects.get(booking_id=id)
            messages.warning(request, "Complaint Already Raised")
            return redirect('/booking_history/%s' % uid)
        except:
            booking = booking_details.objects.get(booking_id=id)
            if request.method == 'POST':
                form = createComplaintForm(request.POST)
                if form.is_valid():
                    complaint=form.cleaned_data['complaint']
                    complaints.objects.create(complaint=complaint,booking_id=booking)
                    messages.warning(request, "Complaint Raised Successfully")
                    return redirect('/booking_history/%s' % uid)
            else:
                form_value = createComplaintForm()
                return render(request, "users/create_complaint.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def give_reply(request, uid,id):
    if request.session.get('session_id'):
            complaint=complaints.objects.get(complaint_id=id)
            if complaint.reply_status == 0:
                messages.warning(request, "You have Already Replied")
                return redirect('/view_complaints_list/%s' % uid)
            else:
                if request.method == 'POST':
                    form = replyComplaintForm(request.POST)
                    if form.is_valid():
                        reply=form.cleaned_data['reply']
                        complaints.objects.filter(complaint_id=id).update(reply=reply,reply_status=False)
                        messages.warning(request, "Reply Sent Successfully")
                        return redirect('/view_complaints_list/%s' % uid)
                else:
                    form_value = replyComplaintForm()
                    return render(request, "admin/give_reply.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def complaints_list(request, uid):
    if request.session.get('session_id'):
        complaint = complaints.objects.filter(booking_id__patient_id__requestor_id=uid)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(complaint, 4)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "users/complaints_list.html",
                      { 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def view_complaints_list(request, uid):
    if request.session.get('session_id'):
        complaint = complaints.objects.all().order_by('-complaint_id')
        page_num = request.GET.get('page', 1)
        paginator = Paginator(complaint, 4)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/view_complaints_list.html",
                      { 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def get_location(request):
        lat = request.GET.get('latitude')
        lon = request.GET.get('longitude')
        driver_id = request.GET.get('driver_id')
        print("*************************************************",lat)
        print("*************************************************",lon)
        print("*************************************************",driver_id)
        if lat and lon:
            try:
                driver=driver_location.objects.get(driver_id=driver_id)
                if driver:
                    driver_location.objects.filter(driver_id=driver_id).update(latitude=lat,longitude=lon)
            except:
                driver = ambulance_drivers.objects.get(driver_id=driver_id)
                driver_location.objects.create(driver_id=driver,latitude=lat, longitude=lon)
            # You can process the latitude and longitude here
            return JsonResponse({'message': 'Location received.'})
        else:
            return JsonResponse({'error': 'Latitude and longitude not provided.'}, status=400)




def activate_ambulance(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        try:
            ambulances=ambulance.objects.get(owner_id=uid)
            if ambulances.vehicle_status==True:
                ambu = ambulance.objects.filter(owner_id=uid).update(vehicle_status=False)
                ambulance_drivers.objects.filter(driver_id=uid).update(available=False)

                data = {'status': True, 'available': 0}
                return JsonResponse(data)
            else:
                ambu = ambulance.objects.filter(owner_id=uid).update(vehicle_status=True)
                ambulance_drivers.objects.filter(driver_id=uid).update(available=True)
                data = {'status': True, 'available': 1}
                return JsonResponse(data)
        except ambulance.DoesNotExist:
            data = {'status': False, 'available': 2}
            return JsonResponse(data)
    else:
        return redirect('/login/')






def get_hospitals(request):
    desired_city=request.GET.get('city')
    # data1 = hospital.objects.filter(Q(city=city) & Q(status=True))

    data1 = hospital.objects.filter(status=True).filter(city=desired_city).union(
        hospital.objects.filter(status=True).exclude(city=desired_city))
    print(data1)
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)

def get_states(request):
    data1 = state.objects.all()
    print(data1)
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)

def get_cities(request):
    states=request.GET.get('state')
    state_id=state.objects.get(state=states)
    print(state_id)
    data1 = city.objects.filter(state_id=state_id.state_id)
    print(data1)
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)


def new_request(request):
    if request.session.get('session_id'):
        uid=request.GET.get('login_id')
        condition1=Q(driver_id=uid)
        condition2=Q(booking_status=False)
        try:
            booking_details.objects.get(condition1 and condition2)
            data = {'status': True, 'count': 1 }
            return JsonResponse(data)
        except booking_details.DoesNotExist:
            data = {'status': False, 'count': 0}
            return JsonResponse(data)
    else:
        return redirect('/login/')


def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')