from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import ContactUs, Booking, Review


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['name', 'email', 'profession', 'message']


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'people_count', 'message']


class NewUserForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email',  'password1', 'password2')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
        

