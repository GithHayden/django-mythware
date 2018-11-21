[![Build Status](https://travis-ci.org/GithHayden/django-mythware.svg?branch=master)](https://travis-ci.org/GithHayden/django-mythware)

# Mythware

Mythware is an agile project management software application.

Bug: Terminal 'run' = ImportError: No module named 'stripe'. Solution = sudo pip3 install stripe.
Bug: Error = django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty = updated settings.py with if os.path.exists('env.py'): import env
Bug: auth pages/accounts not styling as required - bootstrap cdn link was from bootstrap. Updated with egneral bootstrap styling link.
Bug: Update to have homepage and products as seperate apps for more streamlined build?
Bug: Password reset.
Bug: Stripe payment not processing. Fix - Will only process when deloyed?
Bug: Travis - failing due to requirements libraries not required/out of date. Failed due to import env code required updating. Travis error - use pip freeze, rather than pip3 freeze.

Future Features
Remove image func from products or keep for future iterations?
Blog.


Installations/Technologies
sudo pip3 install django-forms-bootstrap
sudo pip3 install Pillow
sudo pip3 install stripe
https://github.com/BlackrockDigital/startbootstrap-scrolling-nav
Include all libraries/requirements.txt, eg from django import forms