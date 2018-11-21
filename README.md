[![Build Status](https://travis-ci.org/GithHayden/django-mythware.svg?branch=master)](https://travis-ci.org/GithHayden/django-mythware)



# Mythware

Mythware is an agile project management software application.


Terminal 'run' = ImportError: No module named 'stripe'. Solution = sudo pip3 install stripe.
Site not responsive - custom css for pricing knocked out Bootstrap responsive - updated custom css to remve body css and add .container .column margin.
Bootstrap naming conventions - update with custom for this template. Updated all on x files via Replace all and updating file names.
Sign Up - Error = Exception Type: NoReverseMatch at /accounts/register/. Exception Value: Reverse for 'index' not found. 'index' is not a valid view function or pattern name.
Terminal 'run' = ImportError: No module named 'stripe'. Solution = sudo pip3 install stripe.
raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
Error = django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty = updated settings.py with if os.path.exists('env.py'): import env
auth pages/accounts not styling as required - bootstrap cdn link was from bootstrap. Updated with eneral bootstrap styling link.
OPEN - Update to have homepage and products as seperate apps for more streamlined build?
Password reset - fix.
Bug = Update when user signs up or signs in, user is brough to the profile page and not the homepage.
Bug - Stripe payment not processing.
Update styling on all message eg - you have succesfully logged in.
Remove image func from products or keep for future iterations?
Build in link for payment to populate in issues tracker
User Signs Up/Signs In - bring them to their profile page
Implement Blog.
Travis - failing due to requirements libraries not required/out of date. Failed due to import env code required updating.
sudo pip3 install django-forms-bootstrap
sudo pip3 install Pillow
sudo pip3 install stripe
https://github.com/BlackrockDigital/startbootstrap-scrolling-nav

Include all libraries, eg from django import forms

Travis error - use pip freeze, rather than pip3 freeze