import math
import uuid

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout as logouts
from django.shortcuts import render,redirect
from .models import register, service_center, state, city, service_center_location, service_request, chatroom, Message
from .forms import RegisterForm, LoginForm, service_center_form, EditCustomerForm, EditService_Center_Form, \
    EditUserForm, Request_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=post_email).exists():
                messages.warning(request,"Email Id Already Exists")
                return redirect('/register/')
            else:
                form.save()
                uname=register.objects.get(email=post_email)
                register.objects.filter(reg_id=uname.reg_id).update(state=state,city = city)
                User.objects.create_user(username=uname,email=post_email)
                messages.warning(request,"Registration Successfull")
                return redirect('/register/')
    else:
        form_value = RegisterForm()
        return render(request,"main/register.html", {'form_key': form_value})

def service_center_register(request):
    if request.method == 'POST':
        form = service_center_form(request.POST,request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            state = request.POST.get('state')
            city = request.POST.get('city')
            if User.objects.filter(email=post_email).exists():
                messages.warning(request,"Email Id Already Exists")
                return redirect('/register/')
            else:
                form.save()
                uname=service_center.objects.get(email=post_email)
                service_center.objects.filter(center_id=uname.center_id).update(state=state, city=city)
                User.objects.create_user(username=uname,email=post_email)
                messages.warning(request,"Registration Successfull")
                return redirect('/register/')
    else:
        form_value = service_center_form()
        return render(request,"main/service_center_register.html", {'form_key': form_value})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
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
                           if user.usertype==1:
                               return redirect('/admin_home/%s' % user.reg_id) # change user home to admin home
                           else:
                               return redirect('/user_home/%s' % user.reg_id)
                    except register.DoesNotExist:
                        user1 = None
                        messages.warning(request,"Incorrect Password")
                        return redirect('/login/')
            except register.DoesNotExist:
                try:
                    user = service_center.objects.get(email=email_val)
                    if user:
                        try:
                            user1 = service_center.objects.get(Q(center_id=user.center_id) & Q(password=pswd))
                            if user1:
                                if user.status == True:
                                    request.session['session_id'] = user.center_id
                                    return redirect('/service_center_home/%s' % user.center_id)
                                else:
                                    return redirect('/login/')
                        except service_center.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                except service_center.DoesNotExist:
                    user = None
                    messages.warning(request, "Invalid Email Id")
                    return redirect('/login/')
    else:
        form1 = LoginForm()
        return render(request,"main/login.html",{'form_key': form1})

def user_home(request,uid):
    if request.session.get('session_id'):
        return render(request,'user/user_home.html',{'reg_id':uid})
    else:
        return render('/login/')
def approveservice_center(request,uid, id):
    if request.session.get('session_id'):
        servicer = service_center.objects.filter(center_id=id).update(status=True)
        return redirect('/Approveservicecenterlist/%s' % uid)
    else:
        return render('/login/')
def rejectservice_center(request,uid, id):
    if request.session.get('session_id'):
        service = service_center.objects.get(center_id=id)
        user = User.objects.get(email=service.email)
        user.delete()
        servicer = service_center.objects.filter(center_id=id).delete()
        return redirect('/Approveservicecenterlist/%s' % uid)
    else:
        return redirect('/login/')


def approvecustomer(request, uid,id):
    user = register.objects.filter(reg_id=id).update(status=True)
    return redirect('/admin_home/%s' % id)

def rejectcustomer(request, uid,id):
    user = register.objects.filter(reg_id=id).delete()
    return redirect('/admin_home/%s' % id)

def admin_home(request,uid):
    if request.session.get('session_id'):
        return render(request,'admin/admin_home.html',{'reg_id':uid})
    else:
        return render('/login/')

def Service_center_home(request,uid):
    if request.session.get('session_id'):
        return render(request,'service_center/service_center_home.html',{'center_id':uid})
    else:
        return render('/login/')

def Approveservicecenterlist(request,uid):
    if request.session.get('session_id'):
        service = service_center.objects.filter(status=False)
        page_num = request.GET.get('page',1)
        paginator = Paginator(service,5)
        try:
            page_obj=paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'admin/service_center_admin.html',{'page_obj':page_obj,'reg_id':uid})
    else:
        return redirect('/login/')


def ServiceCenterList(request,uid):
    if request.session.get('session_id'):
        service = service_center.objects.filter(status=True)
        page_num = request.GET.get('page',1)
        paginator = Paginator(service,5)
        try:
            page_obj=paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'admin/ServiceCenterList.html',{'page_obj':page_obj,'reg_id':uid})
    else:
        return redirect('/login/')

def deleteServiceCenter(request,uid, id):
    if request.session.get('session_id'):
        service = service_center.objects.get(center_id=id)
        user = User.objects.get(email=service.email)
        user.delete()
        servicer = service_center.objects.filter(center_id=id).delete()
        return redirect('/ServiceCenterList/%s' % uid)
    else:
        return redirect('/login/')

def CustomerList(request,uid):
    if request.session.get('session_id'):
        service = register.objects.filter(usertype=2)
        page_num = request.GET.get('page',1)
        paginator = Paginator(service,5)
        try:
            page_obj=paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'admin/CustomerList.html',{'page_obj':page_obj,'reg_id':uid})
    else:
        return redirect('/login/')

def deleteCustomer(request,uid, id):
    if request.session.get('session_id'):
        customer = register.objects.get(reg_id=id)
        user = User.objects.get(email=customer.email)
        user.delete()
        servicer = register.objects.filter(reg_id=id).delete()
        return redirect('/CustomerList/%s' % uid)
    else:
        return redirect('/login/')

def profile(request,uid,id):
    if request.session.get('session_id'):
        user = register.objects.filter(reg_id=id)
        return render(request,'register.html',{'users':user,'reg_id':id})
    else:
        return redirect('/login/')

def user_profile(request, uid):
    if request.session.get('session_id'):
        user = register.objects.get(reg_id=uid)
        return render(request, "user/user_profile.html", {'user': user,'reg_id': uid})
    else:
        return redirect('/login/')

def edit_user_profile(request, uid):
    if request.session.get('session_id'):
        user = register.objects.get(reg_id=uid)
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/user_profile/%s' % uid)

        else:
            form_value = EditUserForm(instance=user)
            return render(request, "user/edit_user_profile.html",
                          {'form_key': form_value, 'user': user,'reg_id': uid})
    else:
        return redirect('/login/')

def edit_profile(request, uid):
    if request.session.get('session_id'):
        customer = register.objects.get(reg_id=uid)
        if request.method == 'POST':
            form = EditCustomerForm(request.POST, instance=customer)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/admin_profile/%s' % uid)

        else:
            form_value = EditCustomerForm(instance=customer)
            return render(request, "admin/edit_profile.html",
                          {'form_key': form_value, 'customer': customer,'reg_id': uid})
    else:
        return redirect('/login/')



def admin_profile(request,uid):
    if request.session.get('session_id'):
        user = register.objects.get(reg_id=uid)
        return render(request,'admin/admin_profile.html',{'customer':user,'reg_id':uid})
    else:
        return redirect('/login/')

def service_center_profile(request, uid):
    if request.session.get('session_id'):
        service = service_center.objects.get(center_id=uid)
        return render(request, "service_center/service_center_profile.html", {'service': service,'center_id': uid})
    else:
        return redirect('/login/')

def edit_service_center_profile(request, uid):
    if request.session.get('session_id'):
        service = service_center.objects.get(center_id=uid)
        if request.method == 'POST':
            form = EditService_Center_Form(request.POST,request.FILES, instance=service)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/service_center_profile/%s' % uid)

        else:
            form_value = EditService_Center_Form(instance=service)
            return render(request, "service_center/edit_service_center_profile.html",
                          {'form_key': form_value, 'service': service, 'center_id': uid})
    else:
        return redirect('/login/')

def user_service_request(request,uid,id):
    if request.session.get('session_id'):
        if request.method=='POST':
            form = Request_form(request.POST,request.FILES)
            if form.is_valid():
                center_id= service_center.objects.get(center_id=id)
                user_id=register.objects.get(reg_id=uid)
                complaint=form.cleaned_data['complaint']
                image=form.files['image']
                vehicle_type=form.cleaned_data['vehicle_type']
                service_request.objects.create(center_id=center_id,reg_id=user_id,complaint=complaint,image=image,vehicle_type=vehicle_type)
                messages.warning(request, "Service Request Send Successfully")
                return redirect('/user_service_request/%s/%s' % (uid,id))
        else:
            form=Request_form()
            return render(request, "user/request_form.html", {'form_key': form, 'reg_id': uid})
    else:
        return redirect('/login/')

def view_service_request(request,uid):
    if request.session.get('session_id'):
        req = service_request.objects.filter(Q(center_id=uid) & Q(req_status=True) & Q(service_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'service_center/service_requests.html', {'page_obj': page_obj, 'center_id': uid,'count': 1})
        else:
            messages.warning(request, "No New Requests")
            return render(request, "service_center/service_requests.html", {'center_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def approve_request(request,uid, id):
    if request.session.get('session_id'):
        service = service_request.objects.filter(req_id=id).update(service_status=True)
        return redirect('/view_service_request/%s' % uid)
    else:
        return render('/login/')

def reject_request(request,uid, id):
    if request.session.get('session_id'):
        service = service_request.objects.filter(req_id=id).delete()
        return redirect('/view_service_request/%s' % uid)
    else:
        return redirect('/login/')

def current_service(request,uid):
    if request.session.get('session_id'):
        req = service_request.objects.filter(Q(center_id=uid) & Q(req_status=True) & Q(service_status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'service_center/current_service.html', {'page_obj': page_obj, 'center_id': uid,'count': 1})
        else:
            messages.warning(request, "No Current Services")
            return render(request, "service_center/current_service.html", {'center_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def previous_services(request,uid):
    if request.session.get('session_id'):
        req = service_request.objects.filter(Q(center_id=uid) & Q(req_status=False) & Q(service_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'service_center/previous_services.html', {'page_obj': page_obj, 'center_id': uid,'count': 1})
        else:
            messages.warning(request, "No Previous Services")
            return render(request, "service_center/previous_services.html", {'center_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def complete_service(request,uid, id):
    if request.session.get('session_id'):
        service = service_request.objects.filter(req_id=id).update(req_status=False,service_status=False)
        return redirect('/current_service/%s' % uid)
    else:
        return render('/login/')

def user_my_request(request,uid):
    if request.session.get('session_id'):
        req = service_request.objects.filter(Q(reg_id=uid) & Q(req_status=True) & Q(service_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'user/service_requests.html', {'page_obj': page_obj, 'reg_id': uid,'count': 1})
        else:
            messages.warning(request, "No New Requests")
            return render(request, "user/service_requests.html", {'reg_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def cancel_request(request,uid, id):
    if request.session.get('session_id'):
        service = service_request.objects.filter(req_id=id).delete()
        return redirect('/user_my_request/%s' % uid)
    else:
        return redirect('/login/')

def user_current_service(request,uid):
    if request.session.get('session_id'):
        req = service_request.objects.filter(Q(reg_id=uid) & Q(req_status=True) & Q(service_status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'user/current_service.html', {'page_obj': page_obj, 'reg_id': uid,'count': 1})
        else:
            messages.warning(request, "No New Requests")
            return render(request, "user/current_service.html", {'reg_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def user_previous_services(request,uid):
    if request.session.get('session_id'):
        req = service_request.objects.filter(Q(reg_id=uid) & Q(req_status=False) & Q(service_status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'user/previous_services.html', {'page_obj': page_obj, 'reg_id': uid,'count': 1})
        else:
            messages.warning(request, "No New Requests")
            return render(request, "user/previous_services.html", {'reg_id': uid, 'count': 0})

    else:
        return redirect('/login/')




# def user_chat(request,uid,id,chat_key):
#     user=register.objects.get(reg_id=uid)
#     chat_room = chatroom.objects.get(chat_key=chat_key)
#     if request.method == "POST":
#         msg=request.POST.get('content')
#         room=chatroom.objects.get(chat_id=chat_room.chat_id)
#         Message.objects.create(room=room,content=msg,from_id=user.reg_id,to_id=room.req_id.center_id.center_id,chatkey=chat_key)
#         # Message.objects.create(room=chats,content=msg)
#         return redirect('/user_chat/%s/%s/%s' % (uid,id,chat_key))
#     else:
#         messages=Message.objects.filter(chatkey=chat_key)
#         return render(request,'user/chat.html', {'chat_key':chat_key,'messages':messages,'user':user,'reg_id':uid})

def create_chat(request,uid,id):
    if request.session.get('session_id'):
        req = service_request.objects.get(req_id=id)
        if chatroom.objects.filter(req_id=id).exists():
            chatkey=chatroom.objects.get(req_id=id)
            return redirect('/user_chat/%s/%s/%s' % (uid,req.req_id,chatkey.chat_key))
        else:
            chat_key=uuid.uuid1()
            chatroom.objects.create(req_id=req,chat_key=chat_key)
            return redirect('/user_chat/%s/%s/%s' % (uid,req.req_id,chat_key))
    else:
        return redirect('/login/')
def user_chat(request,uid,id,chat_key):
    if request.session.get('session_id'):
        req = service_request.objects.get(req_id=id)
        room = chatroom.objects.get(req_id=id)
        messages=Message.objects.filter(chatkey=chat_key)
        return render(request,'user/chat.html', {'messages':messages,'room':room,'req':req,'reg_id':uid})
    else:
        return redirect('/login/')


def create_user_message(request):
    reg_id = request.GET.get('reg_id')
    chatkey = request.GET.get('chatkey')
    content = request.GET.get('content')
    from_id = request.GET.get('from_id')
    to_id = request.GET.get('to_id')

    try:
        chat_room = chatroom.objects.get(chat_key=chatkey)
        Message.objects.create(room=chat_room, content=content, from_id=from_id, to_id=to_id, chatkey=chatkey)
        data = {'status': True}
    except Exception as e:
        print(e)
        data = {'status': False}

    return JsonResponse(data)


def get_chat_messages(request, chat_key):
    room = chatroom.objects.get(chat_key=chat_key)
    messages = Message.objects.filter(chatkey=chat_key)

    message_data = []
    for message in messages:
        message_data.append({
            'content': message.content,
            'timestamp': message.timestamp,
            'from_id': message.from_id,
        })

    return JsonResponse({'messages': message_data})


def center_create_chat(request,uid,id):
    if request.session.get('session_id'):
        req = service_request.objects.get(req_id=id)
        if chatroom.objects.filter(req_id=id).exists():
            chatkey=chatroom.objects.get(req_id=id)
            return redirect('/center_chat/%s/%s/%s' % (uid,req.req_id,chatkey.chat_key))
        else:
            chat_key=uuid.uuid1()
            chatroom.objects.create(req_id=req,chat_key=chat_key)
            return redirect('/center_chat/%s/%s/%s' % (uid,req.req_id,chat_key))
    else:
        return redirect('/login/')

def center_chat(request,uid,id,chat_key):
    if request.session.get('session_id'):
        req = service_request.objects.get(req_id=id)
        room = chatroom.objects.get(req_id=id)
        messages = Message.objects.filter(chatkey=chat_key)
        return render(request, 'service_center/chat.html', {'messages': messages, 'room': room, 'req': req, 'center_id': uid})
    else:
        return redirect('/login/')

def previous_center_chat(request,uid,id):
    if request.session.get('session_id'):
        req = service_request.objects.get(req_id=id)
        try:
            room = chatroom.objects.get(req_id=id)
            msg = Message.objects.filter(chatkey=room.chat_key)
            return render(request, 'service_center/previous_chat.html', {'messages': msg, 'room': room, 'req': req, 'center_id': uid})
        except chatroom.DoesNotExist:
            messages.warning(request, "You haven't initiated any chat")
            return redirect('/previous_services/%s' % uid)

    else:
        return redirect('/login/')

def previous_user_chat(request,uid,id):
    if request.session.get('session_id'):
        req = service_request.objects.get(req_id=id)
        try:
            room = chatroom.objects.get(req_id=id)
            msg = Message.objects.filter(chatkey=room.chat_key)
            return render(request, 'user/previous_chat.html', {'messages': msg, 'room': room, 'req': req, 'reg_id': uid})
        except chatroom.DoesNotExist:
            messages.warning(request, "You haven't initiated any chat")
            return redirect('/user_previous_services/%s' % uid)

    else:
        return redirect('/login/')

def create_center_message(request):
    center_id = request.GET.get('center_id')
    chatkey = request.GET.get('chatkey')
    content = request.GET.get('content')
    from_id = request.GET.get('from_id')
    to_id = request.GET.get('to_id')

    try:
        chat_room = chatroom.objects.get(chat_key=chatkey)
        Message.objects.create(room=chat_room, content=content, from_id=from_id, to_id=to_id, chatkey=chatkey)
        data = {'status': True}
    except Exception as e:
        print(e)
        data = {'status': False}

    return JsonResponse(data)


def get_center_chat_messages(request, chat_key):
    room = chatroom.objects.get(chat_key=chat_key)
    messages = Message.objects.filter(chatkey=chat_key)

    message_data = []
    for message in messages:
        message_data.append({
            'content': message.content,
            'timestamp': message.timestamp,
            'from_id': message.from_id,
        })

    return JsonResponse({'messages': message_data})






















def nearby_service_centers(request,uid,centers):
    if request.session.get('session_id'):
        center_ids = [int(id) for id in centers.split(',')]
        center_data = service_center.objects.filter(center_id__in=center_ids)
        return render(request,'user/nearby_service_centers.html',{'reg_id':uid,'center_data':center_data})
    else:
        return redirect('/login/')


def get_service_center_status(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        try:
            center=service_center.objects.get(center_id=uid)
            if center.active_status==True:
                data = {'status': True, 'active': 1}
                return JsonResponse(data)
            else:
                data = {'status': True, 'active': 0}
                return JsonResponse(data)
        except service_center.DoesNotExist:
            data = {'status': False}
            return JsonResponse(data)
    else:
        return redirect('/login/')


def activate_service_center(request):
    if request.session.get('session_id'):
        uid = request.GET.get('login_id')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        try:
            center=service_center.objects.get(center_id=uid)
            if center.active_status==True:
                service_center.objects.filter(center_id=uid).update(active_status=False)
                data = {'status': True, 'available': 0}
                return JsonResponse(data)
            else:
                service_center.objects.filter(center_id=uid).update(active_status=True)

                if latitude and longitude:
                    try:
                        center_loc = service_center_location.objects.get(center_id=uid)
                        if center_loc:
                            service_center_location.objects.filter(center_id=uid).update(latitude=latitude, longitude=longitude)
                    except:
                        service_center_location.objects.create(center_id=center, latitude=latitude, longitude=longitude)
                data = {'status': True, 'available': 1}
                return JsonResponse(data)
        except service_center.DoesNotExist:
            data = {'status': False, 'available': 2}
            return JsonResponse(data)
    else:
        return redirect('/login/')




def get_nearby_service_centers(request):
    if request.session.get('session_id'):
        uid = request.GET.get('uid')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        user_lat = float(latitude)
        user_lon = float(longitude)
        search_radius = 9.0
        nearby_centers = []
        available_centers = service_center.objects.filter(status=True, active_status=True)
        center = service_center_location.objects.filter(Q(center_id__in=available_centers))
        for i in center:
            distance = haversine(user_lat, user_lon, i.latitude, i.longitude)
            if distance <= search_radius:
                nearby_centers.append(i.center_id)
        centers=serialize('json',nearby_centers)
        if nearby_centers:
            print("heloooooooo---------------------------------------------------")
            data = {'status': True, 'centers': centers}
            return JsonResponse(data)
        else:
            data = {'status': False,'message':"No Nearby Service Centers "}
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
    return JsonResponse(data,safe=False)



def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')


