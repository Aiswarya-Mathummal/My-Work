import decimal
import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, loginForm, editForm, bunkForm, fuel_detForm, cityForm, fuelreqform, Edituserform, \
    Editadminprofileform
from .models import customer, fuel_details, Petrol_bunk, state, city, bunk_location, fuel_request
from django.contrib.auth import logout as logouts
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
# reg and login nav link page
def first(request):
    return render(request, "main/first.html")


def bunk_home(request,uid):
    return render(request, "bunk/bunk_home.html", {'login_id': uid})


def user_home(request, uid):
    return render(request, "customer/user_home.html", {'login_id': uid})


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def service(request):
    return render(request, "main/service.html")


def Adhome(request, uid):
    return render(request, "admin/adhome.html", {'login_id': uid})


def home(request):
    return render(request, "home.html")


def nav(request):
    return render(request, "nav.html")


def bunk_details(request, uid):
    users = Petrol_bunk.objects.all()
    # user = gallery.objects.all()
    return render(request, "bunk/bunk_details.html", {'users': users, 'login_id': uid})


def fuel_det(request, uid):
    users = fuel_details.objects.all()
    return render(request, "admin/fuel_det.html", {'user': users, 'login_id': uid})


def fuel_deta(request, uid):
    users = fuel_details.objects.all()
    return render(request, "customer/fuel_deta.html", {'user': users, 'login_id': uid})


def add_fuel_details(request, uid):
    if request.session.get('session_id'):
        if request.method == "POST":
            form = fuel_detForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/add_fuel_details/%s' % uid)
        else:

            form1 = fuel_detForm()
            return render(request, "admin/add_fuel_details.html", {'form': form1, 'login_id': uid})
    else:
        return redirect('/login/')


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = customer.objects.get(email=email)
                if user:

                    try:
                        user1 = customer.objects.get(Q(email=email) & Q(password=password))
                        if user1:

                            if user.User_type == 1:
                                request.session['session_id'] = user.user_id
                                return redirect('/adhome/%s' % user.user_id)
                            else:
                                request.session['session_id'] = user.user_id
                                return redirect('/user_home/%s' % user.user_id)
                    except customer.DoesNotExist:
                        user1 = None
                        messages.warning(request, "Incorrect Password")
                        return redirect('/login/')
            except customer.DoesNotExist:
                try:
                    user = Petrol_bunk.objects.get(email=email)
                    if user:
                        try:
                            user1 = Petrol_bunk.objects.get(Q(bunk_id=user.bunk_id) & Q(password=password))
                            if user1:
                                if user.status == True:
                                    request.session['session_id'] = user.bunk_id
                                    return redirect('/bunk_home/%s' % user.bunk_id)
                                else:
                                    messages.warning(request, "You are not yet approved")
                                    return redirect('/login/')
                        except Petrol_bunk.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                except Petrol_bunk.DoesNotExist:
                    try:
                        user = customer.objects.get(email=email)
                        if user:
                            try:
                                user1 = customer.objects.get(Q(user_id=user.user_id) & Q(password=password))
                                if user1:
                                    request.session['session_id'] = user.user_id
                                    return redirect('/user_home/')
                            except customer.DoesNotExist:
                                user1 = None
                                messages.warning(request, "Incorrect Password")
                                return redirect('/login/')
                    except customer.DoesNotExist:
                        user = None
                        messages.warning(request, "Invalid Email Id")
                        return redirect('/login/')
    else:
        form1 = loginForm()
        return render(request, "main/login.html", {'form': form1})


def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/reg/')
            else:
                form.save()
                uname = customer.objects.get(email=email)
                customer.objects.filter(user_id=uname.user_id).update(state=state, city=city)
                User.objects.create_user(username=uname, email=email)
            return redirect('/login/')
    else:

        form1 = RegisterForm()
        return render(request, "main/reg.html", {'form': form1})


def petrol_bunk_reg(request):
    if request.method == "POST":
        form = bunkForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/petrol_bunk/')
            else:
                form.save()
                uname = Petrol_bunk.objects.get(email=email)
                Petrol_bunk.objects.filter(bunk_id=uname.bunk_id).update(state=state, city=city)
                User.objects.create_user(username=uname, email=email)
                return redirect('/login/')
    else:
        form1 = bunkForm()
        return render(request, "bunk/petrol_bunk.html", {'form': form1})


def customer_list(request, uid):
    user = customer.objects.all()
    return render(request, "admin/customer_list.html", {'user': user, 'login_id': uid})


def approve_bunk_details(request, uid):
    user = Petrol_bunk.objects.filter(status=False)
    return render(request, "admin/approve_bunk_details.html", {'user': user, 'login_id': uid})


def approved_users(request, uid):
    if request.session.get('session_id'):
        user = Petrol_bunk.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(user, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        return render(request, "admin/list.html", {'user': user, 'login_id': uid,'page_obj':page_obj})
    return redirect('/login/')

def edit_user(request, id):
    user = customer.objects.get(user_id=id)
    # print(user)
    if request.method == "POST":
        form = editForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/customer_list/%s' % user.user_id)
    # redirect for
    else:
        form = editForm(instance=user)
        return render(request, "admin/editu.html", {'form': form})


def edit_fuel(request, id):
    user = fuel_details.objects.get(fuel_id=id)
    # print(user)
    if request.method == "POST":
        form = fuel_detForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/fuel_det/%s' % user.fuel_id)
    else:
        form = fuel_detForm(instance=user)
        return render(request, "admin/edit.html", {'form1': form})


def delete(request, uid, id):
    delete_user = customer.objects.filter(user_id=id).delete()
    return redirect('/customer_list/%s' % uid)
    print(user)
    form = editForm(instance=user)
    return render(request, 'admin/customer_list.html', {'user': form})


def reject(request, uid, id):
    delete_user = Petrol_bunk.objects.filter(bunk_id=id).delete()
    return redirect('/approve_bunk_details/%s' % uid)
    print(user)
    form = editForm(instance=user)
    return render(request, 'admin/approve_bunk_details.html', {'user': form})


def accept_request(request, uid, id):
    fuel_request.objects.filter(req_id=id).update(req_status=True)
    return redirect('/fuel_requests/%s' % uid)


def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')


def approve(request, uid, id):
    Petrol_bunk.objects.filter(bunk_id=id).update(status=True)
    return redirect('/approve_bunk_details/%s' % uid)


def get_states(request):
    data1 = state.objects.all()
    print(data1)
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)


def get_cities(request):
    states = request.GET.get('state')
    state_id = state.objects.get(state=states)
    print(state_id)
    data1 = city.objects.filter(state_id=state_id.state_id)
    print(data1)
    data = serialize('json', data1)
    return JsonResponse(data, safe=False)

def admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = customer.objects.get(user_id=uid)
        return render(request, "admin/admin_profile.html", {'admin': admin, 'login_id': uid})
    else:
        return redirect('/login/')


def edit_admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = customer.objects.get(user_id=uid)
        if request.method == 'POST':
            form = Editadminprofileform(request.POST, instance=admin)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/admin_profile/%s' % uid)

        else:
            form_value = Editadminprofileform(instance=admin)
            return render(request, "admin/edit_admin_profile.html",{'form_key': form_value, 'admin': admin, 'login_id': uid})
    else:
        return redirect('/login/')


def bunk_profile(request, uid):
    if request.session.get('session_id'):
        bunk = Petrol_bunk.objects.get(bunk_id=uid)
        return render(request, "bunk/bunk_profile.html", {'bunk': bunk, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_bunk_profile(request, uid):
    if request.session.get('session_id'):
        bunk = Petrol_bunk.objects.get(bunk_id=uid)
        return render(request, "bunk/edit_bunk_profile.html", {'bunk': bunk, 'login_id': uid})
    else:
        return redirect('/login/')


def add_city(request):
    if request.method == 'POST':
        form = cityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_city/')
    else:
        form = cityForm()
    return render(request, 'customer/add_city.html', {'form': form})

# petrolbunk=petrol_bank.objects.filter(city="kanothumchal")

def approved_requests(request, uid):
    user = fuel_request.objects.filter(req_status=True)
    return render(request, "bunk/approved_requests.html", {'user': user, 'login_id': uid})

def request_history(request, uid):
    user = fuel_request.objects.all()
    return render(request, "customer/request_history.html", {'user': user, 'login_id': uid})


def fuel_requests(request, uid):
    user = fuel_request.objects.filter(req_status=False)
    return render(request, "bunk/fuel_requests.html", {'user': user, 'login_id': uid})


def fuel_req(request,uid,id):
    if request.method == "POST":
        form = fuelreqform(request.POST)
        if form.is_valid():
            quantity= form.cleaned_data['quantity']
            price= form.cleaned_data['price']
            fuel_type=form.cleaned_data['fuel_type']
            user = customer.objects.get(user_id=uid)
            bunk = Petrol_bunk.objects.get(bunk_id=id)
            fuel_request.objects.create(quantity=quantity,price=price,fuel_type=fuel_type,userid=user,bunkid=bunk)
            return redirect('/request_history/%s' % uid)

    else:

        form1 = fuelreqform()
        return render(request, "customer/req_form.html", {'form': form1,'login_id':uid})




def calculate_price(request):
        quantity=decimal.Decimal(request.GET.get('quantity', 0.0)) # Convert to float for calculation
        type1 = request.GET.get('type')
        fuel=fuel_details.objects.get(fuel_id=type1)
        # Convert to float for calculation
        price = quantity * fuel.Rate  # Replace with your actual calculation
        print("-------------------------------------------------------------",price)
        return JsonResponse({'price': price})



def customer_profile(request, uid):
    if request.session.get('session_id'):
        users = customer.objects.get(user_id=uid)
        return render(request, "customer/customer_profile.html", {'users': users,'login_id': uid})
    else:
        return redirect('/login/')

def edit_user_profile(request, uid):
    if request.session.get('session_id'):
        users = customer.objects.get(user_id=uid)
        if request.method == 'POST':
            form = Edituserform(request.POST, instance=users)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/customer_profile/%s' % uid)

        else:
            form_value = Edituserform(instance=users)
            return render(request, "customer/edit_customer_profile.html",
                          {'form_key': form_value, 'users': users, 'login_id': uid})
    else:
        return redirect('/login/')


# def home(request):
#     if request.session.get('session_id'):
#        return render(request, "home.html")
#     else:
#         return redirect('/login/')



def get_bunk_status(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        try:
            bunk=Petrol_bunk.objects.get(bunk_id=uid)
            if bunk.active_status==True:
                data = {'status': True, 'active': 1}
                return JsonResponse(data)
            else:
                data = {'status': True, 'active': 0}
                return JsonResponse(data)
        except Petrol_bunk.DoesNotExist:
            data = {'status': False}
            return JsonResponse(data)
    else:
        return redirect('/login/')


def activate_bunk(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        try:
            bunk=Petrol_bunk.objects.get(bunk_id=uid)
            if bunk.active_status==True:
                Petrol_bunk.objects.filter(bunk_id=uid).update(active_status=False)
                data = {'status': True, 'available': 0}
                return JsonResponse(data)
            else:
                Petrol_bunk.objects.filter(bunk_id=uid).update(active_status=True)

                if latitude and longitude:
                    try:
                        bunk_loc = bunk_location.objects.get(bunk_id=uid)
                        if bunk_loc:
                            bunk_location.objects.filter(bunk_id=uid).update(latitude=latitude, longitude=longitude)
                    except:
                        bunk_location.objects.create(bunk_id=bunk, latitude=latitude, longitude=longitude)
                data = {'status': True, 'available': 1}
                return JsonResponse(data)
        except Petrol_bunk.DoesNotExist:
            data = {'status': False, 'available': 2}
            return JsonResponse(data)
    else:
        return redirect('/login/')
def nearby_bunks(request,uid,bunks):
    if request.session.get('session_id'):
        bunk_ids = [int(id) for id in bunks.split(',')]
        bunk_data = Petrol_bunk.objects.filter(bunk_id__in=bunk_ids)
        return render(request,'customer/nearby_bunks.html',{'login_id':uid,'bunk_data':bunk_data})
    else:
        return redirect('/login/')
def get_nearby_bunks(request):
    if request.session.get('session_id'):
        uid = request.GET.get('uid')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        user_lat = float(latitude)
        user_lon = float(longitude)
        search_radius = 5.0
        nearby_bunks = []
        available_bunks = Petrol_bunk.objects.filter(status=True, active_status=True)
        bunk = bunk_location.objects.filter(Q(bunk_id__in=available_bunks))
        for i in bunk:
            distance = haversine(user_lat, user_lon, i.latitude, i.longitude)
            if distance <= search_radius:
                nearby_bunks.append(i.bunk_id)
        bunks=serialize('json',nearby_bunks)
        if bunk:
            data = {'status': True, 'bunks': bunks}
            return JsonResponse(data)
        else:
            data = {'status': False, 'message': 'No nearby bunks found'}
            return JsonResponse(data)
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
