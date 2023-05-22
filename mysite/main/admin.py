from django.contrib import admin
from . models import (About_img, About_Us, About_Titles, Team_Members, Service_Titles, Our_services, ContactUs, Booking, Booking_Titles, 
                      Contact_Titles, Contact_Info, Review, Review_Titles, Review_Info, OurTeam_Titles, Login_Titles, Register_Titles,
                      Menu_Titles, Menu_Group, Menu_list,Footer_Company, Contact_Adress, Footer_Opening, Header_Titles, Home_Titles, Bg_img
                      )

# ----------------------------------------------------------
# from modeltranslation.admin import TranslationAdmin

# class Home_TitlesAdmin(TranslationAdmin):
#     pass
# -----------------------------------------------------------
# Register your models here.


admin.site.register(About_img)
admin.site.register(About_Us)
admin.site.register(About_Titles)
admin.site.register(Team_Members)
admin.site.register(Service_Titles)
admin.site.register(Our_services)
admin.site.register(ContactUs)
admin.site.register(Contact_Titles)
admin.site.register(Contact_Info)
admin.site.register(Booking)
admin.site.register(Booking_Titles)
admin.site.register(Review)
admin.site.register(Review_Titles)
admin.site.register(Review_Info)
admin.site.register(OurTeam_Titles)
admin.site.register(Login_Titles)
admin.site.register(Register_Titles)
admin.site.register(Menu_Titles)
admin.site.register(Menu_Group)
admin.site.register(Menu_list)
admin.site.register(Footer_Company)
admin.site.register(Contact_Adress)
admin.site.register(Footer_Opening)
admin.site.register(Header_Titles)
admin.site.register(Home_Titles)
admin.site.register(Bg_img)

