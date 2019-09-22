from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import UserRegisterForm, User_Details, Hospital_Details, Bank_Details, Address_, Donate
from .models import Address, UserDetails, HospitalDetails, BankDetails, DoantionLogDetails
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .tables import SimpleTable, BloodType, BloodTypeSearch
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        user_details_form = User_Details(request.POST)
        address_form = Address_(request.POST)

        if form.is_valid() and user_details_form.is_valid() and address_form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            details = user_details_form.save(commit=False)
            add = address_form.save(commit=False)
            details.user = user
            details.save()
            add.user = user
            add.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered for {username}')
            return redirect('dashboard')

    else:
        form = UserRegisterForm()
        user_details_form = User_Details()
        address_form = Address_()
    return render(request, 'bloodcare/user_register.html', {'form': form, 'user_details_form': user_details_form, 'address_form': address_form, 'title': 'Register'})


def hospital_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        hospital_details_form = Hospital_Details(request.POST)
        address_form = Address_(request.POST)

        if form.is_valid() and hospital_details_form.is_valid() and address_form.is_valid():
            user = form.save()
            group = Group.objects.get(name='hospital')
            user.groups.add(group)
            details = hospital_details_form.save(commit=False)
            add = address_form.save(commit=False)
            details.user = user
            details.save()
            add.user = user
            add.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered for {username}')
            return redirect('dashboard')

    else:
        form = UserRegisterForm()
        hospital_details_form = Hospital_Details()
        address_form = Address_()
    return render(request, 'bloodcare/hospital_register.html', {'form': form, 'hospital_details_form': hospital_details_form, 'address_form': address_form, 'title': 'Register'})


def bank_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        bank_details_form = Bank_Details(request.POST)
        address_form = Address_(request.POST)

        if form.is_valid() and bank_details_form.is_valid() and address_form.is_valid():
            user = form.save()
            group = Group.objects.get(name='blood_bank')
            user.groups.add(group)
            details = bank_details_form.save(commit=False)
            add = address_form.save(commit=False)
            details.user = user
            details.save()
            add.user = user
            add.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered for {username}')
            return redirect('dashboard')

    else:
        form = UserRegisterForm()
        bank_details_form = Bank_Details()
        address_form = Address_()
    return render(request, 'bloodcare/bank_register.html', {'form': form, 'bank_details_form': bank_details_form, 'address_form': address_form, 'title': 'Register'})


def home(request):
    return render(request, 'bloodcare/home.html', {'title': 'Home'})

@login_required
def dashboard(request):
    
    user = request.user
    username = user.username
    if user.groups.filter(name = 'customer').exists():
        print("----------------------------------------user")
        var = DoantionLogDetails.objects.filter(donated_from__username = username)
        table = SimpleTable(var)
        var2 = UserDetails.objects.filter(user__username=username)[0]
        add = Address.objects.filter(user__username=username)[0]

        return render(request, 'bloodcare/user_dashboard.html', {'table': table, 'title': 'Dashboard', 'var2': var2, 'add': add})

    elif user.groups.filter(name='hospital').exists():
        print("----------------------------------------hospital")
        var = DoantionLogDetails.objects.filter(donated_to__username=username)
        var2 = HospitalDetails.objects.filter(user__username=username)[0]
        add = Address.objects.filter(user__username=username)[0]
        table = SimpleTable(var)

        return render(request, 'bloodcare/hospital_dashboard.html', {'table': table, 'title': 'Dashboard', 'var2': var2, 'add': add})

    elif user.groups.filter(name='blood_bank').exists():
        print("----------------------------------------bank")
        var = DoantionLogDetails.objects.filter(donated_to__username=username) or DoantionLogDetails.objects.filter(donated_from__username=username)
        table = SimpleTable(var)
        var2 = BankDetails.objects.filter(user__username=username)
        add = Address.objects.filter(user__username=username)[0]
        table2 = BloodType(var2)
        var2 = var2[0]

        return render(request, 'bloodcare/bank_dashboard.html', {'table': table, 'title': 'Dashboard', 'table2': table2, 'var2': var2, 'add': add})
    



@login_required
def search_alert(request):
    if request.method == 'POST':

        if request.POST.get('search'):
            username = request.user.username
            var2 = request.POST.get('blood_type')
            city = Address.objects.filter(user__username=username)[0].city
            addr_list = Address.objects.filter(city=city)
            var = []
            for i in addr_list:
                var.append(i.user.username)
            l = BankDetails.objects.filter(user__username__in=var)
            l2 = []
            for i in l:
                j = i.__dict__
                if j[var2] > 0:
                    l2.append(i) 
            table = BloodTypeSearch(l2)
            return render(request, 'bloodcare/search_alert.html', {'table': table, 'status': False})

        elif request.POST.get('notify'):
            d = {
                "a_positive" : "A+",
                "a_negative" : "A-",
                "b_positive" : "B+",
                "b_negative" : "B-",
                "o_positive" : "O+",
                "o_negative" : "O-",
                "ab_positive" : "AB+",
                "ab_negative" : "AB-",
                }

            username = request.user.username
            var2 = request.POST.get('blood_type')
            city = Address.objects.filter(user__username=username)[0].city
            addr_list = Address.objects.filter(city=city)
            var = []
            for i in addr_list:
                var.append(i.user.username)
            l = UserDetails.objects.filter(user__username__in=var)
            l2 = []
            for i in l:
                if i.blood_type == d[var2]:
                    l2.append(i.user.email)

            subject = "Blood Donation Request"
            msg_mail = """Dear User,
                    This is a sample alert from bloodcare.
                """+ str(l2) + """
            Thankyou
            BloodCare
            """
            from_email = "500052357@stu.upes.ac.in"
            try:
                send_mail(subject, msg_mail, from_email, l2, fail_silently = False)
                messages.success(request, f'mail sent.')
            except BadHeaderError or SMTPAuthenticationError:
                messages.success(request, f'mail failed.')

            return redirect('dashboard')


    else:
        return render(request, 'bloodcare/search_alert.html', {'status': True})


@login_required
def use(request):
    pass


@login_required
def donate(request):
    user = request.user
    if request.method == 'POST':
        form = Donate(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            ins = User.objects.filter(username=name)[0]
            var = form.save(commit=False)
            var.donated_to = request.user
            var.donated_from = ins
            var.save()

            if user.groups.filter(name='blood_bank').exists():

                if var.blood_type == 'A+':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].a_positive
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(a_positive=num)

                elif var.blood_type == 'A-':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].a_negative
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(a_negative=num)

                elif var.blood_type == 'B+':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].b_positive
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(b_positive=num)

                elif var.blood_type == 'B-':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].b_negative
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(b_negative=num)

                elif var.blood_type == 'O+':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].o_positive
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(o_positive=num)

                elif var.blood_type == 'O-':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].o_negative
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(o_negative=num)

                elif var.blood_type == 'AB+':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].ab_positive
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(ab_positive=num)

                elif var.blood_type == 'AB-':
                    num = BankDetails.objects.filter(user__username=request.user.username)[0].ab_negative
                    num += 1
                    BankDetails.objects.filter(user=request.user).update(ab_negative=num)


            return redirect('dashboard')

    else:
        form = Donate()
        return render(request, 'bloodcare/donate.html', {'form': form})
