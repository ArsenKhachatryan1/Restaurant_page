from django.shortcuts import render, redirect
from . models import (About_img, About_Us, About_Titles, Team_Members, Service_Titles, Our_services, Contact_Titles,
                    	ContactUs, Contact_Info, Booking, Booking_Titles, Review, Review_Titles, Review_Info, OurTeam_Titles,
		      			Login_Titles, Register_Titles, Menu_Titles, Menu_Group, Menu_list, Footer_Company, Contact_Adress,
					    Footer_Opening, Header_Titles, Home_Titles, Bg_img
		      )
from .forms import ContactForm, BookingForm, ReviewForm, NewUserForm

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User


# Create your views here.
message = ''

def index(request):
	global message
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	home_titles = Home_Titles.objects.all()[0]
	booking_title = Booking_Titles.objects.all()[0]
	review = Review.objects.all().order_by('-id')[:15]
	review_title = Review_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	if request.method == 'POST':
		form = BookingForm(request.POST)
		if request.user.is_authenticated:
			if form.is_valid():
				Booking.objects.create(**form.cleaned_data)
				message = 'You booked a table successfully. Thank You!!!'
				return redirect('answer')
			
		else:
			message = 'Please LogIn or SignUp for Booking. Thank You!!!'
			return redirect('answer')
		form = BookingForm()


	return render(request,'main/index.html', context={
	'act':'index',
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'home_titles':home_titles,
	'booking_title':booking_title,
	'review':review,
	'review_title':review_title,
	'bg_img':bg_img,
	})



def about(request):
	img_1 = About_img.objects.all()[0]
	img_2 = About_img.objects.all()[1]
	img_3 = About_img.objects.all()[2]
	img_4 = About_img.objects.all()[3]
	about_us = About_Us.objects.all()[0]
	about_title = About_Titles.objects.all()[0]
	team_members = Team_Members.objects.all()
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	return render(request,'main/about.html', context={
	'img_1':img_1,
	'img_2':img_2,
	'img_3':img_3,
	'img_4':img_4,
	'act':'about',
	'about_us':about_us,
	'team_members':team_members,
	'about_title':about_title,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})





def booking(request):
	global message
	booking_title = Booking_Titles.objects.all()[0]
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	if request.method == 'POST':
		form = BookingForm(request.POST)
		if request.user.is_authenticated:
			if form.is_valid():
				Booking.objects.create(**form.cleaned_data)
				message = 'You booked a table successfully. Thank You!!!'
				return redirect('answer')
			
		else:
			message = 'Please LogIn or SignUp for Booking. Thank You!!!'
			return redirect('answer')
		form = BookingForm()
	
	return render(request,'main/booking.html', context={
	'act':'booking',
	'booking_title':booking_title,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})



def contact(request):
	title = Contact_Titles.objects.all()[0]
	contact_info = Contact_Info.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	footer_company = Footer_Company.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	global message

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			ContactUs.objects.create(**form.cleaned_data)
			message = 'Your email has been sent successfully. Thank You!!!'
			return redirect('answer')
		
	else:
		form = ContactForm()
	return render(request,'main/contact.html', context={
	'form':form,
	'act':'contact',
	'title':title,
	'contact_info':contact_info,
	'contact_adress':contact_adress,
	'footer_company':footer_company,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})



def menu(request):
	menu_title = Menu_Titles.objects.all()[0]
	menu_group = Menu_Group.objects.all()
	menu_list = Menu_list.objects.all()
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	return render(request,'main/menu.html', context={
	'act':'menu',
	'menu_title':menu_title,
	'menu_group':menu_group,
	'menu_list':menu_list,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})



def service(request):
	title = Service_Titles.objects.all()[0]
	our_services = Our_services.objects.all()
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	return render(request,'main/service.html', context={
	'act':'service',
	'title':title,
	'our_services':our_services,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})



def team(request):
	team_members = Team_Members.objects.all()
	about_title = About_Titles.objects.all()[0]
	team_title = OurTeam_Titles.objects.all()[0]
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	return render(request,'main/team.html', context={
	'act':'team',
	'team_members':team_members,
	'about_title':about_title,
	'team_title':team_title,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})



def testimonial(request):
	review = Review.objects.all().order_by('-id')[:15]
	review_title = Review_Titles.objects.all()[0]
	review_info = Review_Info.objects.all()[0]
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	global message

	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			Review.objects.create(**form.cleaned_data)
			message = 'Your review has been sent successfully. Thank You!!!'
			return redirect('answer')
		
	else:
		form = ReviewForm()

	return render(request,'main/testimonial.html', context={
	'form':form,
	'act':'testimonial',
	'review':review,
	'review_title':review_title,
	'review_info':review_info,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})


def answer(request):
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	return render(request,'main/answer.html', context={
	'message':message,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})



def register_request(request):
    
	register_titles = Register_Titles.objects.all()[0]
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	if request.method == 'POST':  
		form = NewUserForm(request.POST)  
		if form.is_valid():  
			user = form.save(commit=False)  
			user.is_active = False  
			user.save()  
			current_site = get_current_site(request)  
			mail_subject = 'Activation link has been sent to your email id'  
			message = render_to_string('main/acc_active_email.html', {  
				'user': user,  
				'domain': current_site.domain,  
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
				'token':account_activation_token.make_token(user),  
			})  
			to_email = form.cleaned_data.get('email')  
			email = EmailMessage(  
						mail_subject, message, to=[to_email]  
			)  
			email.send()  
			return HttpResponse('Please confirm your email address to complete the registration')  
	else:  
		form = NewUserForm()
	
	return render(request, 'main/register.html', {
	'form':form, 
	'act':'register_request','register_titles':register_titles,
	'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
	})  




def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  



def login_request(request):
	global message
	login_titles = Login_Titles.objects.all()[0]
	footer_company = Footer_Company.objects.all()[0]
	contact_adress = Contact_Adress.objects.all()[0]
	opening = Footer_Opening.objects.all()[0]
	header_titles = Header_Titles.objects.all()[0]
	bg_img = Bg_img.objects.all()[0]

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
			message = 'Please Enter valid Username and Password. Thank You!!!'
			return redirect('answer')
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={
		'form':form,
	    'act':'login_request',
	    'login_titles':login_titles,
	    'footer_company':footer_company,
	'contact_adress':contact_adress,
	'opening':opening,
	'header_titles':header_titles,
	'bg_img':bg_img,
        })



def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")