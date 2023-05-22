from modeltranslation.translator import register, TranslationOptions
from . models import (About_Us, About_Titles, Team_Members, Service_Titles, Our_services, Booking_Titles, 
                      Contact_Titles, Contact_Info, Review_Titles, Review_Info, OurTeam_Titles, Login_Titles, Register_Titles,
                      Menu_Titles, Menu_Group, Menu_list,Footer_Company, Contact_Adress, Footer_Opening, Header_Titles, Home_Titles
                      )



@register(Home_Titles)
class Home_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'about', 'btn')


@register(Header_Titles)
class Header_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'page_name', 'block_name1', 'block_name2', 'block_name3', 'block_name4', 'block_name5', 'block_name6',
              'block_name7', 'block_name8', 'block_name9', 'block_name10', 'block_name11', 'block_name12', 'block_name13')
    

@register(About_Titles)
class About_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'about', 'subtitle', 'subtitle_text')


@register(About_Us)
class About_UsTranslationOptions(TranslationOptions):
    fields = ('name', 'title1', 'title2', 'text1', 'text2', 'years_text', 'experience', 'chef_status', 'chef_text', 'btn_name')


@register(Team_Members)
class Team_MembersTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


@register(Service_Titles)
class Service_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'service', 'subtitle', 'subtitle_text')


@register(Our_services)
class Our_servicesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Contact_Titles)
class Contact_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'contact', 'subtitle', 'subtitle_text')


@register(Contact_Info)
class Contact_InfoTranslationOptions(TranslationOptions):
    fields = ('booking', 'general', 'technical', 'name', 'email', 'subject', 'message', 'btn')


@register(Contact_Adress)
class Contact_AdressTranslationOptions(TranslationOptions):
    fields = ('title', 'adress')


@register(OurTeam_Titles)
class OurTeam_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'team')


@register(Booking_Titles)
class Booking_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'booking', 'subtitle', 'subtitle_text', 'name', 'email', 'date', 'people', 'request', 'btn')


@register(Review_Titles)
class Review_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'review', 'subtitle', 'subtitle_text')


@register(Review_Info)
class Review_InfoTranslationOptions(TranslationOptions):
    fields = ('title', 'name', 'email', 'profession', 'message', 'btn')


@register(Login_Titles)
class Login_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'login', 'subtitle', 'username1', 'password1', 'btn')



@register(Menu_Titles)
class Menu_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'menu', 'subtitle', 'subtitle_text')


@register(Menu_Group)
class Menu_GroupTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',)


@register(Menu_list)
class Menu_listTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Footer_Company)
class Footer_CompanyTranslationOptions(TranslationOptions):
    fields = ('title', 'about', 'contact', 'reserv', 'privacy', 'terms')


@register(Footer_Opening)
class Footer_OpeningTranslationOptions(TranslationOptions):
    fields = ('title', 'work_day', 'work_hours', 'delivery', 'delivery_hours')

@register(Register_Titles)
class Register_TitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'home', 'pages', 'signup', 'subtitle', 'username1', 'firstname', 'lastname', 'email', 'password1', 'password2', 'btn')
