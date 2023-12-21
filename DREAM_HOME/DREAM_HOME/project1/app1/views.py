from django.contrib.auth import logout as logouts
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import (Customer, Architect, Interior_Designer, Exterior_Designer, Plan, Exterior_Design,
                     Interior_Design, Plan_Book,EXT_design_book,INT_design_book)
from .form import (CustomerForm,ArchitectForm,InteriorDesignerForm,ExteriorDesignerForm,LoginForm,
                   Editcustomerform,Editarchitectform,Editinteriordesignerform,Editexteriordesignerform,
                   Addplanform,Editplanform,Addexteriordesignform,Editexteriordesignform,Addinteriordesignform,
                   Editinteriordesignform)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.


def logout(request):
    del request.session['session_id']
    logouts(request)
    return redirect('/')


def index(request):
    return render(request, "main/index.html")


       #RegisterForm

def customer_reg(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            print("helooooo")
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/customer_reg/')
            else:
                form.save()
                uname = Customer.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                # fname = form.cleaned_data['firstname']
                # lname = form.cleaned_data['lastname']
                # subject = 'welcome to GFG world'
                # message = f'Hi {fname} {lname}, thank you for registering in geeksforgeeks.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ['aiswaryam421@gmail.com', ]
                # send_mail(subject, message, email_from, recipient_list)
                messages.warning(request, "Registration Successful")
                return redirect('/customer_reg/')

    else:
        form_value = CustomerForm()
        return render(request, "main/customer_reg.html", {'form_key': form_value})


def architect_reg(request):
    if request.method == 'POST':
        form = ArchitectForm(request.POST,request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/architect_reg/')
            else:
                form.save()
                uname = Architect.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                # fname = form.cleaned_data['firstname']
                # lname = form.cleaned_data['lastname']
                # subject = 'welcome to GFG world'
                # message = f'Hi {fname} {lname}, thank you for registering in geeksforgeeks.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ['aiswaryam421@gmail.com', ]
                # send_mail(subject, message, email_from, recipient_list)
                messages.warning(request, "Registration Successful")
                return redirect('/architect_reg/')

    else:
        form_value = ArchitectForm()
        return render(request, "main/architect_reg.html", {'form_key': form_value})


def interior_designer_reg(request):
    if request.method == 'POST':
        form = InteriorDesignerForm(request.POST,request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/interior_designer_reg/')
            else:
                form.save()
                uname = Interior_Designer.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                # fname = form.cleaned_data['firstname']
                # lname = form.cleaned_data['lastname']
                # subject = 'welcome to GFG world'
                # message = f'Hi {fname} {lname}, thank you for registering in geeksforgeeks.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ['aiswaryam421@gmail.com', ]
                # send_mail(subject, message, email_from, recipient_list)
                messages.warning(request, "Registration Successful")
                return redirect('/interior_designer_reg/')

    else:
        form_value = InteriorDesignerForm()
        return render(request, "main/interior_designer_reg.html", {'form_key': form_value})


def exterior_designer_reg(request):
    if request.method == 'POST':
        form = ExteriorDesignerForm(request.POST,request.FILES)
        if form.is_valid():
            post_email = form.cleaned_data['email']
            if User.objects.filter(email=post_email).exists():
                messages.warning(request, "Email Id Already Exist")
                return redirect('/exterior_designer_reg/')
            else:
                form.save()
                uname = Exterior_Designer.objects.get(email=post_email)
                User.objects.create_user(username=uname, email=post_email)
                # fname = form.cleaned_data['firstname']
                # lname = form.cleaned_data['lastname']
                # subject = 'welcome to GFG world'
                # message = f'Hi {fname} {lname}, thank you for registering in geeksforgeeks.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ['aiswaryam421@gmail.com', ]
                # send_mail(subject, message, email_from, recipient_list)
                messages.warning(request, "Registration Successful")
                return redirect('/exterior_designer_reg/')

    else:
        form_value = ExteriorDesignerForm()
        return render(request, "main/exterior_designer_reg.html", {'form_key': form_value})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_val = form.cleaned_data['email']
            pswd = form.cleaned_data['password']
            try:
                    user = Customer.objects.get(email=email_val)
                    if user:
                        try:
                            user1 = Customer.objects.get(Q(customer_id=user.customer_id) & Q(password=pswd))
                            if user1:
                                request.session['session_id'] = user.customer_id
                                #if user.status==True:
                                if user.user_type==1:
                                    return redirect('/admin_home/%s' % user.customer_id)
                                else:
                                    return redirect('/customer_home/%s' % user.customer_id)
                                #else:
                                    #return redirect('/login/')
                        except  Customer.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
            except Customer.DoesNotExist:
                try:
                    user = Architect.objects.get(email=email_val)
                    if user:
                        try:
                            user1 = Architect.objects.get(Q(architect_id=user.architect_id) & Q(password=pswd))
                            if user1:
                                if user.status == True:
                                    request.session['session_id'] = user.architect_id
                                    return redirect('/architect_home/%s' % user.architect_id)
                                else:
                                    return redirect('/login/')
                        except Architect.DoesNotExist:
                            user1 = None
                            messages.warning(request, "Incorrect Password")
                            return redirect('/login/')
                except Architect.DoesNotExist:
                    try:
                        user = Interior_Designer.objects.get(email=email_val)
                        if user:
                            try:
                                user1 = Interior_Designer.objects.get(Q(interior_designer_id=user.interior_designer_id) & Q(password=pswd))
                                if user1:
                                    if user.status == True:
                                        request.session['session_id'] = user.interior_designer_id
                                        return redirect('/interior_designer_home/%s' % user.interior_designer_id)

                                    else:
                                        return redirect('/login/')
                            except Interior_Designer.DoesNotExist:
                                user1 = None
                                messages.warning(request, "Incorrect Password")
                                return redirect('/login/')
                    except Interior_Designer.DoesNotExist:
                        try:
                            user = Exterior_Designer.objects.get(email=email_val)
                            if user:
                                try:
                                    user1 = Exterior_Designer.objects.get(Q(exterior_designer_id=user.exterior_designer_id) & Q(password=pswd))
                                    if user1:
                                        if user.status == True:
                                            request.session['session_id'] = user.exterior_designer_id
                                            return redirect('/exterior_designer_home/%s' % user.exterior_designer_id)
                                        else:
                                            return redirect('/login/')
                                except Exterior_Designer.DoesNotExist:
                                    user1 = None
                                    messages.warning(request, "Incorrect Password")
                                    return redirect('/login/')
                        except Exterior_Designer.DoesNotExist:
                            user = None
                            messages.warning(request, "Invalid Email Id")
                            return redirect('/login/')
    else:
        form1 = LoginForm()
        return render(request, "main/login.html", {'form': form1})


def admin_home(request,uid):
    if request.session.get('session_id'):
        return render(request, "admin/admin_home.html",{'login_id':uid})
    else:
        return redirect('/login/')


def architect_home(request,uid):
    if request.session.get('session_id'):
        return render(request, "architect/architect_home.html",{'login_id':uid})
    else:
        return redirect('/login/')


def customer_home(request,uid):
    if request.session.get('session_id'):
        return render(request, "customer/customer_home.html",{'login_id':uid})
    else:
        return redirect('/login/')


def exterior_designer_home(request,uid):
    if request.session.get('session_id'):
        return render(request, "exterior designer/exterior_designer_home.html",{'login_id':uid})
    else:
        return redirect('/login/')


def interior_designer_home(request,uid):
    if request.session.get('session_id'):
        return render(request, "interior designer/interior_designer_home.html",{'login_id':uid})
    else:
        return redirect('/login/')


#registerd Users--------------------------------------------------------------------------------------------------------

def view_customer_list(request,uid):
    if request.session.get('session_id'):
        customer = Customer.objects.filter(user_type=2)

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
                      {'customer': customer, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')




def view_architect_list(request,uid):
    if request.session.get('session_id'):
        architect = Architect.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(architect, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/architect_list.html",
                      {'architect': architect, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def view_interior_designer_list(request,uid):
    if request.session.get('session_id'):
        interior_designer= Interior_Designer.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator( interior_designer, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/interior_designer_list.html",
                      {' interior_designer':  interior_designer, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def view_exterior_designer_list(request,uid):
    if request.session.get('session_id'):
        exterior_designer= Exterior_Designer.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator( exterior_designer, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/exterior_designer_list.html",
                      {' exterior_designer':  exterior_designer, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

#delete users-----------------------------------------------------------------------------------------------------------


def delete_customer(request, uid, id):
    if request.session.get('session_id'):
        customer= Customer.objects.get(customer_id=id)
        user = User.objects.get(email=customer.email)
        user.delete()
        Customer.objects.filter(customer_id=id).delete()
        return redirect('/customer_list/%s' % uid)
    else:
        return redirect('/login/')

def delete_architect(request, uid, id):
    if request.session.get('session_id'):
        architect= Architect.objects.get(architect_id=id)
        user = User.objects.get(email=architect.email)
        user.delete()
        Architect.objects.filter(architect_id=id).delete()
        return redirect('/architect_list/%s' % uid)
    else:
        return redirect('/login/')

def delete_interior_designer(request, uid, id):
    if request.session.get('session_id'):
        interior_designer= Interior_Designer.objects.get(interior_designer_id=id)
        user = User.objects.get(email=interior_designer.email)
        user.delete()
        Interior_Designer.objects.filter(interior_designer_id=id).delete()
        return redirect('/interior_designer_list/%s' % uid)
    else:
        return redirect('/login/')


def delete_exterior_designer(request, uid, id):
    if request.session.get('session_id'):
        exterior_designer = Exterior_Designer.objects.get(exterior_designer_id=id)
        user = User.objects.get(email=exterior_designer.email)
        user.delete()
        Exterior_Designer.objects.filter(exterior_designer_id=id).delete()
        return redirect('/exterior_designer_list/%s' % uid)
    else:
        return redirect('/login/')

#approve architect------------------------------------------------------------------------------------------------------

def approve_architect_list(request,uid):
    if request.session.get('session_id'):
        architect = Architect.objects.filter(user_type=3,status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(architect, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_architect_list.html",
                      {'architect': architect, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def approve_architect(request, uid, id):
    if request.session.get('session_id'):
        Architect.objects.filter(architect_id=id).update(status=True)
        return redirect('/approve_architect_list/%s' % uid)
        #return redirect('/architect_list/%s' % uid)
    else:
        return redirect('/login/')

def reject_architect(request, uid, id):
    if request.session.get('session_id'):
        architect = Architect.objects.get(architect_id=id)
        user = User.objects.get(email=architect.email)
        user.delete()
        Architect.objects.get(architect_id=id).delete()
        #return redirect('/approve_architect_list/%s' % uid)
        return redirect('/approve_architect_list/%s' % uid)
    else:
        return redirect('/login/')

#approve Interior designer----------------------------------------------------------------------------------------------

def approve_interior_designer_list(request,uid):
    if request.session.get('session_id'):
        interior_designer = Interior_Designer.objects.filter(user_type=4,status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(interior_designer, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_interior_designer_list.html",
                      {'interior_designer': interior_designer, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_interior_designer(request, uid, id):
    if request.session.get('session_id'):
        Interior_Designer.objects.filter(interior_designer_id=id).update(status=True)
        return redirect('/approve_interior_designer_list/%s' % uid)
        #return redirect('/architect_list/%s' % uid)
    else:
        return redirect('/login/')

def reject_interior_designer(request, uid, id):
    if request.session.get('session_id'):
        interior_designer = Interior_Designer.objects.get(interior_designer_id=id)
        user = User.objects.get(email=interior_designer.email)
        user.delete()
        Interior_Designer.objects.get(interior_designer_id=id).delete()
        #return redirect('/approve_architect_list/%s' % uid)
        return redirect('/approve_interior_designer_list/%s' % uid)
    else:
        return redirect('/login/')

#approve exterior designer----------------------------------------------------------------------------------------------

def approve_exterior_designer_list(request,uid):
    if request.session.get('session_id'):
        exterior_designer = Exterior_Designer.objects.filter(user_type=5,status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(exterior_designer, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_exterior_designer_list.html",
                      {'exterior_designer': exterior_designer, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def approve_exterior_designer(request, uid, id):
    if request.session.get('session_id'):
        Exterior_Designer.objects.filter(exterior_designer_id=id).update(status=True)
        return redirect('/approve_exterior_designer_list/%s' % uid)
        #return redirect('/architect_list/%s' % uid)
    else:
        return redirect('/login/')

def reject_exterior_designer(request, uid, id):
    if request.session.get('session_id'):
        exterior_designer = Exterior_Designer.objects.get(exterior_designer_id=id)
        user = User.objects.get(email=exterior_designer.email)
        user.delete()
        Exterior_Designer.objects.get(exterior_designer_id=id).delete()
        #return redirect('/approve_architect_list/%s' % uid)
        return redirect('/approve_exterior_designer_list/%s' % uid)
    else:
        return redirect('/login/')


#customer profile view and edit-----------------------------------------------------------------------------------------

def customer_profile(request, uid):
    if request.session.get('session_id'):
        customer = Customer.objects.get(customer_id=uid)
        return render(request, "customer/customer_profile.html", {'customer': customer,'login_id': uid})
    else:
        return redirect('/login/')


def edit_customer_profile(request, uid):
    if request.session.get('session_id'):
        customer = Customer.objects.get(customer_id=uid)
        if request.method == 'POST':
            form = Editcustomerform(request.POST, instance=customer)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/customer_profile/%s' % uid)

        else:
            form_value = Editcustomerform(instance=customer)
            return render(request, "customer/edit_customer_profile.html",
                          {'form_key': form_value, 'customer': customer, 'login_id': uid})
    else:
        return redirect('/login/')

#architect profile view and edit----------------------------------------------------------------------------------------

def architect_profile(request, uid):
    if request.session.get('session_id'):
        architect = Architect.objects.get(architect_id=uid)
        return render(request, "architect/architect_profile.html", {'architect': architect,'login_id': uid})
    else:
        return redirect('/login/')


def edit_architect_profile(request, uid):
    if request.session.get('session_id'):
        architect = Architect.objects.get(architect_id=uid)
        if request.method == 'POST':
            form = Editarchitectform(request.POST, request.FILES,instance=architect)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/architect_profile/%s' % uid)

        else:
            form_value = Editarchitectform(instance=architect)
            return render(request, "architect/edit_architect_profile.html",
                          {'form_key': form_value, 'architect':architect, 'login_id': uid})
    else:
        return redirect('/login/')


#interior designer profile view and edit--------------------------------------------------------------------------------

def interior_designer_profile(request, uid):
    if request.session.get('session_id'):
        interior_designer = Interior_Designer.objects.get(interior_designer_id=uid)
        return render(request, "interior designer/interior_designer_profile.html", {'interior_designer': interior_designer,'login_id': uid})
    else:
        return redirect('/login/')


def edit_interior_designer_profile(request, uid):
    if request.session.get('session_id'):
        interior_designer = Interior_Designer.objects.get(interior_designer_id=uid)
        if request.method == 'POST':
            form = Editinteriordesignerform(request.POST,request.FILES, instance=interior_designer)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/interior_designer_profile/%s' % uid)

        else:
            form_value = Editinteriordesignerform(instance=interior_designer)
            return render(request, "interior designer/edit_interior_designer_profile.html",
                          {'form_key': form_value, 'interior_designer':interior_designer, 'login_id': uid})
    else:
        return redirect('/login/')


#exterior designer profile view and edit--------------------------------------------------------------------------------

def exterior_designer_profile(request, uid):
    if request.session.get('session_id'):
        exterior_designer = Exterior_Designer.objects.get(exterior_designer_id=uid)
        return render(request, "exterior designer/exterior_designer_profile.html", {'exterior_designer': exterior_designer,'login_id': uid})
    else:
        return redirect('/login/')


def edit_exterior_designer_profile(request, uid):
    if request.session.get('session_id'):
        exterior_designer = Exterior_Designer.objects.get(exterior_designer_id=uid)
        if request.method == 'POST':
            form = Editexteriordesignerform(request.POST,request.FILES, instance=exterior_designer)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/exterior_designer_profile/%s' % uid)

        else:
            form_value = Editexteriordesignerform(instance=exterior_designer)
            return render(request, "exterior designer/edit_exterior_designer_profile.html",
                          {'form_key': form_value, 'exterior_designer':exterior_designer, 'login_id': uid})
    else:
        return redirect('/login/')

#admin profile view and edit--------------------------------------------------------------------------------------------

def admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = Customer.objects.get(customer_id=uid)
        return render(request, "admin/admin_profile.html", {'admin': admin,'login_id': uid})
    else:
        return redirect('/login/')


def edit_admin_profile(request, uid):
    if request.session.get('session_id'):
        admin = Customer.objects.get(customer_id=uid)
        if request.method == 'POST':
            form = Editcustomerform(request.POST,request.FILES, instance=admin)

            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/admin_profile/%s' % uid)

        else:
            form_value = Editcustomerform(instance=admin)
            return render(request, "admin/edit_admin_profile.html",
                          {'form_key': form_value, 'admin': admin, 'login_id': uid})
    else:
        return redirect('/login/')

#-----------------------------------------------------plan--------------------------------------------------------------


#plan add,edit,delete,list-architect-----

def add_plan(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addplanform(request.POST, request.FILES)
            if form.is_valid():
                plan_name = form.cleaned_data['plan_name']
                sqft = form.cleaned_data['sqft']
                floor = form.cleaned_data['floor']
                budget = form.cleaned_data['budget']
                plan_image = form.files['plan_image']
                blueprint = form.files['blueprint']
                architect_id = Architect.objects.get(architect_id=uid)
                Plan.objects.create(plan_name=plan_name, sqft=sqft, floor=floor, budget=budget, plan_image=plan_image,blueprint=blueprint,
                                       architect_id=architect_id)
                messages.warning(request, "Plan Added Successfully")
                return redirect('/add_plan/%s' % uid)
        else:
            form_value = Addplanform()
            return render(request, "plan/add_plan.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')

def edit_plan(request, uid, id):
    if request.session.get('session_id'):
        plan = Plan.objects.get(plan_id=id)
        if request.method == 'POST':
            form = Editplanform(request.POST, request.FILES, instance=plan)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/plan_list/%s' % uid)
        else:
            form_value = Editplanform(instance=plan)
            return render(request, "plan/edit_plan.html",
                          {'form_key': form_value, 'plan': plan, 'login_id': uid})
    else:
        return redirect('/login/')

def plan_list(request, uid):
    if request.session.get('session_id'):
        plan = Plan.objects.filter(Q(architect_id=uid) & Q(status=True))
        page_num = request.GET.get('page', 1)
        paginator = Paginator(plan, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "plan/plan_list.html",
                      {'plan': plan, 'page_obj': page_obj, 'login_id': uid})
    else:
        return redirect('/login/')


def delete_plan(request, uid, id):
    if request.session.get('session_id'):
        Plan.objects.get(plan_id=id).delete()
        return redirect('/plan_list/%s' % uid)
    else:
        return redirect('/login/')


#plans approve,reject,list-admin---------------------------------------------------------------------------------------

def approve_plan_list(request,uid):
    if request.session.get('session_id'):
        plan = Plan.objects.filter(status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(plan, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_plan_list.html",
                      {'plan': plan, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def approve_plan(request, uid, id):
    if request.session.get('session_id'):
        Plan.objects.filter(plan_id=id).update(status=True)
        return redirect('/approve_plan_list/%s' % uid)
    else:
        return redirect('/login/')


def reject_plan(request, uid, id):
    if request.session.get('session_id'):
        plan = Plan.objects.get(plan_id=id)
        Plan.objects.get(plan_id=id).delete()
        return redirect('/approve_plan_list/%s' % uid)
    else:
        return redirect('/login/')

#---------------------------------admin- plan list-,delete--------------------------------------------------------------------

def admin_plan_list(request,uid):
    if request.session.get('session_id'):
        plan = Plan.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(plan, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/admin_plan_list.html",
                      {'plan': plan, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def admin_delete_plan(request, uid, id):
    if request.session.get('session_id'):
        Plan.objects.get(plan_id=id).delete()
        return redirect('/admin_plan_list/%s' % uid)
    else:
        return redirect('/login/')

#------------------------------------------exterior design--------------------------------------------------------------

#exterior designer -add,edit,delete,list designs


def add_exterior_design(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addexteriordesignform(request.POST, request.FILES)
            if form.is_valid():
                details = form.cleaned_data['details']
                budget = form.cleaned_data['budget']
                exterior_design_image = form.files['exterior_design_image']
                exterior_designer_id = Exterior_Designer.objects.get(exterior_designer_id=uid)
                Exterior_Design.objects.create(details= details , budget=budget, exterior_design_image=exterior_design_image,
                                       exterior_designer_id=exterior_designer_id)
                messages.warning(request, "Design Added Successfully")
                return redirect('/add_exterior_design/%s' % uid)
        else:
            form_value = Addexteriordesignform()
            return render(request, "exterior_design/add_exterior_design.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')



def edit_exterior_design(request, uid, id):
    if request.session.get('session_id'):
        exterior_design= Exterior_Design.objects.get(exterior_design_id=id)
        if request.method == 'POST':
            form = Editexteriordesignform(request.POST, request.FILES, instance=exterior_design)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/exterior_design_list/%s' % uid)
        else:
            form_value = Editexteriordesignform(instance=exterior_design)
            return render(request, "exterior_design/edit_exterior_design.html",
                          {'form_key': form_value, 'exterior_design': exterior_design, 'login_id': uid})
    else:
        return redirect('/login/')

def exterior_design_list(request, uid):
    if request.session.get('session_id'):
        exterior_design = Exterior_Design.objects.filter(Q(exterior_designer_id=uid) & Q(status=True))
        page_num = request.GET.get('page', 1)
        paginator = Paginator(exterior_design, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "exterior_design/exterior_design_list.html",
                      {'exterior_design': exterior_design, 'page_obj': page_obj, 'login_id': uid})
    else:
        return redirect('/login/')


def delete_exterior_design(request, uid, id):
    if request.session.get('session_id'):
        Exterior_Design.objects.get(exterior_design_id=id).delete()
        return redirect('/exterior_design_list/%s' % uid)
    else:
        return redirect('/login/')


#admin- approve,reject,designs---------------------------------------------------------------------------


def approve_exterior_design_list(request,uid):
    if request.session.get('session_id'):
        exterior_design = Exterior_Design.objects.filter(status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(exterior_design, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_exterior_design_list.html",
                      {'exterior_design': exterior_design, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def approve_exterior_design(request, uid, id):
    if request.session.get('session_id'):
        Exterior_Design.objects.filter(exterior_design_id=id).update(status=True)
        return redirect('/approve_exterior_design_list/%s' % uid)
    else:
        return redirect('/login/')


def reject_exterior_design(request, uid, id):
    if request.session.get('session_id'):
        exterior_design = Exterior_Design.objects.get(exterior_design_id=id)
        Exterior_Design.objects.get(exterior_design_id=id).delete()
        return redirect('/approve_exterior_design_list/%s' % uid)
    else:
        return redirect('/login/')

#admin-list design and delete--------------------------------------------------------------------------------

def admin_exterior_design_list(request,uid):
    if request.session.get('session_id'):
        exterior_design = Exterior_Design.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(exterior_design, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/admin_exterior_design_list.html",
                      {'exterior_design': exterior_design, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def admin_delete_exterior_design(request, uid, id):
    if request.session.get('session_id'):
        Exterior_Design.objects.get(exterior_design_id=id).delete()
        return redirect('/admin_exterior_design_list/%s' % uid)
    else:
        return redirect('/login/')


#--------------------------------------interior design-----------------------------------------------------------------

#interior designer -add,edit,delete,list designs

def add_interior_design(request, uid):
    if request.session.get('session_id'):
        if request.method == 'POST':
            form = Addinteriordesignform(request.POST, request.FILES)
            if form.is_valid():
                details = form.cleaned_data['details']
                budget = form.cleaned_data['budget']
                interior_design_image = form.files['interior_design_image']
                interior_designer_id = Interior_Designer.objects.get(interior_designer_id=uid)
                Interior_Design.objects.create(details= details , budget=budget, interior_design_image=interior_design_image,
                                       interior_designer_id=interior_designer_id)
                messages.warning(request, "Design Added Successfully")
                return redirect('/add_interior_design/%s' % uid)
        else:
            form_value = Addinteriordesignform()
            return render(request, "interior_design/add_interior_design.html", {'form_key': form_value, 'login_id': uid})
    else:
        return redirect('/login/')


def edit_interior_design(request, uid, id):
    if request.session.get('session_id'):
        interior_design= Interior_Design.objects.get(interior_design_id=id)
        if request.method == 'POST':
            form = Editinteriordesignform(request.POST, request.FILES, instance=interior_design)
            if form.is_valid():
                form.save()
                messages.warning(request, "Updated Successfully")
                return redirect('/interior_design_list/%s' % uid)
        else:
            form_value = Editinteriordesignform(instance=interior_design)
            return render(request, "interior_design/edit_interior_design.html",
                          {'form_key': form_value, 'interior_design': interior_design, 'login_id': uid})
    else:
        return redirect('/login/')

def interior_design_list(request, uid):
    if request.session.get('session_id'):
        interior_design = Interior_Design.objects.filter(Q(interior_designer_id=uid) & Q(status=True))
        page_num = request.GET.get('page', 1)
        paginator = Paginator(interior_design, 3)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "interior_design/interior_design_list.html",
                      {'interior_design': interior_design, 'page_obj': page_obj, 'login_id': uid})
    else:
        return redirect('/login/')


def delete_interior_design(request, uid, id):
    if request.session.get('session_id'):
        Interior_Design.objects.get(interior_design_id=id).delete()
        return redirect('/interior_design_list/%s' % uid)
    else:
        return redirect('/login/')


#admin- approve,reject,designs---------------------------------------------------------------------------


def approve_interior_design_list(request,uid):
    if request.session.get('session_id'):
        interior_design = Interior_Design.objects.filter(status=False)

        page_num = request.GET.get('page', 1)
        paginator = Paginator(interior_design, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/approve_interior_design_list.html",
                      {'interior_design': interior_design, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def approve_interior_design(request, uid, id):
    if request.session.get('session_id'):
        Interior_Design.objects.filter(interior_design_id=id).update(status=True)
        return redirect('/approve_interior_design_list/%s' % uid)
    else:
        return redirect('/login/')


def reject_interior_design(request, uid, id):
    if request.session.get('session_id'):
        interior_design = Interior_Design.objects.get(interior_design_id=id)
        Interior_Design.objects.get(interior_design_id=id).delete()
        return redirect('/approve_interior_design_list/%s' % uid)
    else:
        return redirect('/login/')


 # admin-list design and delete--------------------------------------------------------------------------------

def admin_interior_design_list(request,uid):
    if request.session.get('session_id'):
        interior_design = Interior_Design.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(interior_design, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "admin/admin_interior_design_list.html",
                      {'interior_design': interior_design, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def admin_delete_interior_design(request, uid, id):
    if request.session.get('session_id'):
        Interior_Design.objects.get(interior_design_id=id).delete()
        return redirect('/admin_interior_design_list/%s' % uid)
    else:
        return redirect('/login/')

#----------------------------------------------customer-plans--------------------------------------------------


def view_plan_list(request,uid):
    if request.session.get('session_id'):
        plan = Plan.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(plan, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "customer/view_plan_list.html",
                      {'plan': plan, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def user_book_plan(request,uid,aid,pid):
    if request.session.get('session_id'):
                customer_id=Customer.objects.get(customer_id=uid)
                architect_id= Architect.objects.get(architect_id=aid)
                plan_id=Plan.objects.get(plan_id=pid)
                Plan_Book.objects.create(customer_id=customer_id,architect_id=architect_id,plan_id=plan_id)
                return redirect('/view_plan_list/%s' % uid)
    else:
        return redirect('/login/')

def view_plan_requests(request,uid):
    if request.session.get('session_id'):
        req = Plan_Book.objects.filter(Q(architect_id=uid) & Q(status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'architect/view_plan_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "architect/view_plan_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def approved_plan_requests(request,uid):
    if request.session.get('session_id'):
        req = Plan_Book.objects.filter(Q(architect_id=uid) & Q(status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'architect/approved_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "architect/approved_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def approve_plan_request(request,uid, id):
    if request.session.get('session_id'):
        plan_book = Plan_Book.objects.filter(plan_book_id=id).update(status=True)
        return redirect('/view_plan_requests/%s' % uid)
    else:
        return render('/login/')

def reject_plan_request(request,uid, id):
    if request.session.get('session_id'):
        plan_book = Plan_Book.objects.filter(plan_book_id=id).delete()
        return redirect('/view_plan_requests/%s' % uid)
    else:
        return redirect('/login/')

def view_my_plan_requests(request,uid):
    if request.session.get('session_id'):
        req = Plan_Book.objects.filter(Q(customer_id=uid) & Q(status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/view_plan_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "customer/view_plan_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def view_approved_plan_requests(request,uid):
    if request.session.get('session_id'):
        req = Plan_Book.objects.filter(Q(customer_id=uid) & Q(status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/view_approved_plan_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "customer/view_approved_plan_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')



#---------------------------------customer-view ext designs------------------------------------------------
def view_exterior_design_list(request,uid):
    if request.session.get('session_id'):
        exterior_design = Exterior_Design.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(exterior_design, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "customer/view_exterior_design_list.html",
                      {'exterior_design': exterior_design, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')

def user_book_exterior_design(request,uid,aid,pid):
    if request.session.get('session_id'):
                customer_id=Customer.objects.get(customer_id=uid)
                exterior_designer_id= Exterior_Designer.objects.get(exterior_designer_id=aid)
                exterior_design_id= Exterior_Design.objects.get(exterior_design_id=pid)
                EXT_design_book.objects.create(customer_id=customer_id,exterior_designer_id=exterior_designer_id,exterior_design_id=exterior_design_id)
                return redirect('/view_exterior_design_list/%s' % uid)
    else:
        return redirect('/login/')

def view_exterior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = EXT_design_book.objects.filter(Q(exterior_designer_id=uid) & Q(status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'exterior designer/view_exterior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "exterior designer/view_exterior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def approve_exterior_design_request(request,uid, id):
    if request.session.get('session_id'):
        ext_design_book = EXT_design_book.objects.filter(exterior_design_book_id=id).update(status=True)
        return redirect('/view_exterior_design_requests/%s' % uid)
    else:
        return render('/login/')

def reject_exterior_design_request(request,uid, id):
    if request.session.get('session_id'):
        ext_design_book = EXT_design_book.objects.filter(exterior_design_book_id=id).delete()
        return redirect('/view_exterior_design_requests/%s' % uid)
    else:
        return redirect('/login/')



def approved_exterior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = EXT_design_book.objects.filter(Q(exterior_designer_id=uid) & Q(status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'exterior designer/approved_exterior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "exterior designer/approved_exterior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def view_my_exterior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = EXT_design_book.objects.filter(Q(customer_id=uid) & Q(status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/view_exterior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "customer/view_exterior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def view_approved_exterior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = EXT_design_book.objects.filter(Q(customer_id=uid) & Q(status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/view_approved_exterior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "customer/view_approved_exterior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')






#--------------------------------customer view int designs--------------------------------------------------------------------------
def view_interior_design_list(request,uid):
    if request.session.get('session_id'):
        interior_design = Interior_Design.objects.filter(status=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(interior_design, 5)  # 6 employees per page
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "customer/view_interior_design_list.html",
                      {'interior_design': interior_design, 'login_id': uid, 'page_obj': page_obj})
    else:
        return redirect('/login/')


def user_book_interior_design(request,uid,aid,pid):
    if request.session.get('session_id'):
                customer_id=Customer.objects.get(customer_id=uid)
                interior_designer_id= Interior_Designer.objects.get(interior_designer_id=aid)
                interior_design_id= Interior_Design.objects.get(interior_design_id=pid)
                INT_design_book.objects.create(customer_id=customer_id,interior_designer_id=interior_designer_id,interior_design_id=interior_design_id)
                return redirect('/view_interior_design_list/%s' % uid)
    else:
        return redirect('/login/')

def view_interior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = INT_design_book.objects.filter(Q(interior_designer_id=uid) & Q(status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'interior designer/view_interior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "interior designer/view_interior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


def approve_interior_design_request(request,uid, id):
    if request.session.get('session_id'):
        int_design_book = INT_design_book.objects.filter(interior_design_book_id=id).update(status=True)
        return redirect('/view_interior_design_requests/%s' % uid)
    else:
        return render('/login/')

def reject_interior_design_request(request,uid, id):
    if request.session.get('session_id'):
        int_design_book = INT_design_book.objects.filter(interior_design_book_id=id).delete()
        return redirect('/view_interior_design_requests/%s' % uid)
    else:
        return redirect('/login/')



def approved_interior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = INT_design_book.objects.filter(Q(interior_designer_id=uid) & Q(status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'interior designer/approved_interior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "interior designer/approved_interior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')




def view_my_interior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = INT_design_book.objects.filter(Q(customer_id=uid) & Q(status=False))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/view_interior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "customer/view_interior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')

def view_approved_interior_design_requests(request,uid):
    if request.session.get('session_id'):
        req = INT_design_book.objects.filter(Q(customer_id=uid) & Q(status=True))
        if req:
            page_num = request.GET.get('page', 1)
            paginator = Paginator(req, 5)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            return render(request, 'customer/view_approved_interior_design_requests.html', {'page_obj': page_obj, 'login_id': uid,'count': 1})
        else:
            messages.warning(request, "No Requests")
            return render(request, "customer/view_approved_interior_design_requests.html", {'login_id': uid, 'count': 0})

    else:
        return redirect('/login/')


#-----------------------------------------------------------------------------------------------------------------------