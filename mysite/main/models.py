from django.db import models
# Create your models here.


# -------------------------------  Home page models start -------------------

class Home_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    about = models.CharField('About', max_length=256)
    btn = models.CharField('Booking button', max_length=60)
    img = models.ImageField('Home image', upload_to='images')

    class Meta:
        verbose_name = 'Home_Titles'
        verbose_name_plural = 'Home_Titles'


# -------------------------------  Home page models end -------------------



# -------------------------------  About page models start -------------------

class About_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    about = models.CharField('About', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    subtitle_text = models.CharField('Subtitle text', max_length=60)

    class Meta:
        verbose_name = 'About_Titles'
        verbose_name_plural = 'About_Titles'

    def __str__(self) -> str:
        return self.title



class About_img(models.Model):

    img = models.ImageField('About image', upload_to='images')



class About_Us(models.Model):
    name = models.CharField('Name', max_length=60)
    title1 = models.CharField('Title 1', max_length=60)
    title2 = models.CharField('Title 2', max_length=60)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    years = models.IntegerField('Experience years')
    years_text = models.CharField('Years text', max_length=60)
    experience = models.CharField('Experience text', max_length=60)
    chef_count = models.IntegerField('Chef count')
    chef_status = models.CharField('Chef status', max_length=60)
    chef_text = models.CharField('Chef text', max_length=60)
    btn_name = models.CharField('Button name', max_length=60)

    class Meta:
        verbose_name = 'About_Us'
        verbose_name_plural = 'About_Us'

    def __str__(self) -> str:
        return self.name
    


class Team_Members(models.Model):
    name = models.CharField('Member name', max_length=60)
    img = models.ImageField('Member image', upload_to='images')
    position = models.CharField('Member designation', max_length=60)
    site_1 = models.CharField('Site 1 name', max_length=20, blank=True)
    site_1_link = models.URLField('site_1_link', max_length=50, blank=True)
    site_2 = models.CharField('Site 2 name', max_length=20, blank=True)
    site_2_link = models.URLField('site_2_link', max_length=50, blank=True)
    site_3 = models.CharField('Site 3 name', max_length=20, blank=True)
    site_3_link = models.URLField('site_3_link', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Team_Members'
        verbose_name_plural = 'Team_Members'

    def __str__(self) -> str:
        return self.name

# -------------------------------  About page models end -------------------


# -------------------------------  Service page models start -------------------

class Service_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    service = models.CharField('Service', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    subtitle_text = models.CharField('Subtitle text', max_length=60)

    class Meta:
        verbose_name = 'Service_Titles'
        verbose_name_plural = 'Service_Titles'

    def __str__(self) -> str:
        return self.title
    

class Our_services(models.Model):
    title = models.CharField('Title', max_length=60)
    fa_name = models.CharField('Fa icon name', max_length=50)
    text = models.TextField('Text 1')
    delay = models.FloatField('Show Delay seconds', default=0.1)

    class Meta:
        verbose_name = 'Our_services'
        verbose_name_plural = 'Our_services'

    def __str__(self) -> str:
        return self.title
# -------------------------------  Service page models end -------------------


# -------------------------------  Contact page models start -------------------

class ContactUs(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('User message')

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self) -> str:
        return self.name
    

class Contact_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    contact = models.CharField('Contact', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    subtitle_text = models.CharField('Subtitle text', max_length=60)

    class Meta:
        verbose_name = 'Contact_Titles'
        verbose_name_plural = 'Contact_Titles'

    def __str__(self) -> str:
        return self.title


class Contact_Info(models.Model):
    booking = models.CharField('Title booking', max_length=60)
    booking_email = models.EmailField('Booking email page')
    general = models.CharField('Title general', max_length=60)
    general_email = models.EmailField('General email page')
    technical = models.CharField('Title technical', max_length=60)
    technical_email = models.EmailField('Technical email page')
    map_link = models.URLField('Map adress link', max_length=500)
    name = models.CharField('Your name', max_length=60)
    email = models.CharField('Your email', max_length=60)
    subject = models.CharField('Your subject', max_length=60)
    message = models.CharField('Your message', max_length=60)
    btn = models.CharField('Button name', max_length=60)

    class Meta:
        verbose_name = 'Contact_Info'
        verbose_name_plural = 'Contact_Info'



class Contact_Adress(models.Model):
    title = models.CharField('Block title', max_length=60)
    adress_link = models.URLField('Adress link')
    adress = models.CharField('Adress', max_length=100)
    phone = models.CharField('Phone number', max_length=60)
    email = models.EmailField('email')
    social_name1 = models.CharField('Social name 1', max_length=50)
    social_link1 = models.URLField('Link 1')
    social_name2 = models.CharField('Social name 2', max_length=50)
    social_link2 = models.URLField('Link 2')
    social_name3 = models.CharField('Social name 3', max_length=50)
    social_link3 = models.URLField('Link 3')
    social_name4 = models.CharField('Social name 4', max_length=50)
    social_link4 = models.URLField('Link 4')

    class Meta:
        verbose_name = 'Contact_Adress'
        verbose_name_plural = 'Contact_Adress'


    
# -------------------------------  Contact page models end -------------------


# -------------------------------  Our team page models start -------------------

class OurTeam_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    team = models.CharField('Team', max_length=60)

    class Meta:
        verbose_name = 'OurTeam_Titles'
        verbose_name_plural = 'OurTeam_Titles'

    def __str__(self) -> str:
        return self.title

# -------------------------------  Our team page models end -------------------



# -------------------------------  Booking page models start -------------------


class Booking_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    booking = models.CharField('Booking', max_length=60)
    video_link = models.URLField('Video link')
    subtitle = models.CharField('Subtitle', max_length=60)
    subtitle_text = models.CharField('Subtitle text', max_length=60)
    name = models.CharField('Your name', max_length=60)
    email = models.CharField('Your email', max_length=60)
    date = models.CharField('Date & Time', max_length=60)
    people = models.CharField('No Of People', max_length=60)
    request = models.CharField('Special Request', max_length=60)
    btn = models.CharField('Button name', max_length=60)

    class Meta:
        verbose_name = 'Booking_Titles'
        verbose_name_plural = 'Booking_Titles'

    def __str__(self) -> str:
        return self.title



class Booking(models.Model):
    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    date = models.CharField('Booking date', max_length=50)
    people_count = models.PositiveIntegerField('People count')
    message = models.TextField('User message')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking'

    def __str__(self) -> str:
        return self.name

# -------------------------------  Booking page models end -------------------


# -------------------------------  Testimonial page models start -------------------

class Review(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    profession = models.CharField('User profession', max_length=50, null=True)
    message = models.TextField('User review')
    img = models.ImageField('User image', default='users/img_default.png', upload_to='users')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'

    def __str__(self) -> str:
        return self.name



class Review_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    review = models.CharField('Review', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    subtitle_text = models.CharField('Subtitle text', max_length=60)

    class Meta:
        verbose_name = 'Review_Titles'
        verbose_name_plural = 'Review_Titles'

    def __str__(self) -> str:
        return self.title


class Review_Info(models.Model):
    title = models.CharField('Title', max_length=60)
    name = models.CharField('Your name', max_length=60)
    email = models.CharField('Your email', max_length=60)
    profession = models.CharField('Your profession', max_length=60)
    message = models.CharField('Your message', max_length=60)
    btn = models.CharField('Button name', max_length=60)

    class Meta:
        verbose_name = 'Review_Info'
        verbose_name_plural = 'Review_Info'


# -------------------------------  Testimonial page models end -------------------



# -------------------------------  Login and signup page models start -------------------

class Login_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    login = models.CharField('Login', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    username1 = models.CharField('Username', max_length=60)
    password1 = models.CharField('Password', max_length=60)
    btn = models.CharField('Button name', max_length=60)

    class Meta:
        verbose_name = 'Login_Titles'
        verbose_name_plural = 'Login_Titles'

    def __str__(self) -> str:
        return self.title


class Register_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    signup = models.CharField('Signup', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    username1 = models.CharField('Username', max_length=60)
    firstname = models.CharField('Firstname', max_length=60)
    lastname = models.CharField('Lasttname', max_length=60)
    email = models.CharField('Your email', max_length=60)
    password1 = models.CharField('Password-1', max_length=60)
    password2 = models.CharField('Password-2', max_length=60)
    btn = models.CharField('Button name', max_length=60)

    class Meta:
        verbose_name = 'Register_Titles'
        verbose_name_plural = 'Register_Titles'

    def __str__(self) -> str:
        return self.title

# -------------------------------  Login and signup page models end -------------------


# -------------------------------  Menu page models start -------------------

class Menu_Titles(models.Model):
    title = models.CharField('Title', max_length=60)
    home = models.CharField('Home', max_length=60)
    pages = models.CharField('Pages', max_length=60)
    menu = models.CharField('Menu', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    subtitle_text = models.CharField('Subtitle text', max_length=60)

    class Meta:
        verbose_name = 'Menu_Titles'
        verbose_name_plural = 'Menu_Titles'

    def __str__(self) -> str:
        return self.title
    

class Menu_Group(models.Model):
    title = models.CharField('Menu Group name', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=60)
    num = models.IntegerField('Menu Group number')
    fa_name = models.CharField('Fa icon name', default='utensils', max_length=50)
    
    class Meta:
        verbose_name = 'Menu_Group'
        verbose_name_plural = 'Menu_Group'

    def __str__(self) -> str:
        return self.title
    

class Menu_list(models.Model):

    group = models.ForeignKey(Menu_Group, on_delete=models.CASCADE, related_name='menugroup')
    title = models.CharField('Item name', max_length=60)
    text = models.CharField('Item about', max_length=100)
    price = models.CharField('Item price', max_length=60)
    img = models.ImageField('Item image', upload_to='menu', blank=True)

    class Meta:
        verbose_name = 'Menu_List'
        verbose_name_plural = 'Menu_List'

    def __str__(self) -> str:
        return self.title
    
# -------------------------------  Menu page models end -------------------



# -------------------------------  Header models start -------------------

class Header_Titles(models.Model):
    title = models.CharField('Page title', max_length=60)
    page_name = models.CharField('Page name', max_length=60)
    block_name1 = models.CharField('Block name home', max_length=60)
    block_name2 = models.CharField('Block name about', max_length=60)
    block_name3 = models.CharField('Block name service', max_length=60)
    block_name4 = models.CharField('Block name menu', max_length=60)
    block_name5 = models.CharField('Block name pages', max_length=60)
    block_name6 = models.CharField('Block name booking', max_length=60)
    block_name7 = models.CharField('Block name team', max_length=60)
    block_name8 = models.CharField('Block name review', max_length=60)
    block_name9 = models.CharField('Block name contact', max_length=60)
    block_name10 = models.CharField('Block name logout', max_length=60)
    block_name11 = models.CharField('Block name login', max_length=60)
    block_name12 = models.CharField('Block name signup', max_length=60)
    block_name13 = models.CharField('Block name book a table', max_length=60)

    class Meta:
        verbose_name = 'Header_Titles'
        verbose_name_plural = 'Header_Titles'



# -------------------------------  Header models end -------------------



# -------------------------------  Footer models start -------------------


class Footer_Company(models.Model):
    title = models.CharField('Block title', max_length=60)
    about = models.CharField('About name', max_length=60)
    contact = models.CharField('Contact name', max_length=60)
    reserv = models.CharField('Reservation name', max_length=60)
    privacy = models.CharField('Privacy name', max_length=60)
    terms = models.CharField('Terms name', max_length=60)

    class Meta:
        verbose_name = 'Footer_Company'
        verbose_name_plural = 'Footer_Company'


class Footer_Opening(models.Model):
    title = models.CharField('Block title', max_length=60)
    work_day = models.CharField('Working days', max_length=60)
    work_hours = models.CharField('Working hours', max_length=60)
    delivery = models.CharField('Delivery', max_length=60)
    delivery_hours = models.CharField('Delivery hours', max_length=60)

    class Meta:
        verbose_name = 'Footer_Opening'
        verbose_name_plural = 'Footer_Opening'

# -------------------------------  Footer models end -------------------


# -------------------------------  Bg_image models start -------------------

class Bg_img(models.Model):
    bg_img = models.ImageField('BG Image', upload_to='bg_images')
    video_img = models.ImageField('Video Image', upload_to='bg_images')

    class Meta:
        verbose_name = 'Bg_img'
        verbose_name_plural = 'Bg_img'

# -------------------------------  Bg_image models end -------------------
