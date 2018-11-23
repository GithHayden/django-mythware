[![Build Status](https://travis-ci.org/GithHayden/django-mythware.svg?branch=master)](https://travis-ci.org/GithHayden/django-mythware)

# Mythware

Mythware is an agile project management software application, developed using **Django**, a Python web-framework. The target audience is any user who would like to manage projects. Mythware provides a user authentication feature, allowing users to request free bug fixes and paid upgrades via an issues tracker.


## UX
The following section describes the UX process for this project.

#### UX Process
1. **Layout** - Reviewed Code Institute education and Bootstrap themes to extract design ideas.
2. **User Stories** - Walked through user stories.
    1. **Homepage - Header** - As a user, I want to be able to understand the purpose of this website and what to do next.
    2. **Navbar - Features** - As a user, I want to be able to understand the feaures of the software application.
    2. **Navbar - Pricing** - As a user, I want to be able to understand the pricing for all products.
    3. **Navbar - Documentation** - As a user, I want to be able to access documentation for the software application to refer to.
    4. **Navbar - Contact** - As a user, I want to be able to contact the company and developers to offer feedback and suggestions.
    5. **Navbar - Social Links** - As a user, I want to be able to follow Mythware on social media, to interact with this community online.
    5. **Navbar - Mythware** - As a user, I want to be able to go back to the homepage header whilst navigating any page.
    5. **Navbar - Sign Up** - As a user, I want to be able to create a new account, to purchase the software application, to purchase upgrades and to log/track issues.
    6. **Navbar - Sign In** - As a user, I want to be able to sign in to my account and to log/track issues.
    7. **Navbar - Cart** - As a user, I want to be able to add products to a cart, and for the cart to persist on all pages during my session.
    8. **Navbar - Profile** - As a user, I want to be able to view my profile, and log/track issues.
    9. **Navbar - Sign Out** - As a user, I want to be able to sign out of my account.
    10. **Navbar - Issues** - As a user, I want to be able to view and track all issues. I also want to be able to click into each issue to view/edit the issues details.
    11. **Navbar - New Issues** - As a user, I want to be able to create a new issues that is added to the issues tracker.
3. **Wireframe** - Sketched the wireframe on paper, to include the features for each user story.


## Features

### Existing Features
The following section describes the front-end features in this project.

1. **Homepage - Header** - Provides users with a homepage header, which provides a summary of the purpose of this website. The header also provides a call-to-action, 'get started' button, which brings users to the pricing section.
2. **Navbar - Features** - Provides users with a navbar menu, which brings users to the homepage features section, displaying an overview of the software features.
3. **Navbar - Pricing** - Provides users with a navbar menu, which brings users to the homepage pricing section, displaying a pricing card for each product. Each card has a feature that allows users to add as many number of products as they would like to the cart. When a user selects add, the chosen items are added to the cart. The cart navbar menu item is then highlighted with a badge number, displaying how many items have been added to the cart. The Pricing section also includes a link to 'Log and rack a new issue', which brings a user to the sign in page, which is required to access the issues tracker, via a users profile.
4. **Navbar - Documentation** - Provides users with a navbar menu, which brings users to the products/homepage documentation section. This section includes a link to 'technical documentation', wihch brings users to the documenation required for reference whilst using this software application.
5. **Navbar - Contact** - Provides users with a navbar menu item, which brings users to the products/homepage contact section. This sections displays contact information, which allows users to contact the company and developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business).
6. **Navbar - Social Links** - Provides users with links to the website social media pages (no current social media pages for this project as this is not a real business), for users to be part of the online community.
7. **Navbar - Mythware** - Provides users with a navbar menu, displayed on all pages, which brings users back to the homepage.
8. **Navbar - Sign Up** - Provides users with a navbar menu, which brings users to a sign up page. After signing up the users profile is displayed on the navbar menu, providing user with access to their profile.
9. **Navbar - Sign In** - Provides users with a navbar menu, which brings users to a sign in page. After signing in the users profile is displayed on the navbar menu, providing user with access to their profile.
10. **Navbar - Cart** - Provides users with a navbar menu, which brings users to the cart page. On the cart page users can process products in their cart, to a checkout and process payment for their items, via a form.
11. **Navbar - Profile** - Provides users with a navbar menu, which brings users to their profile, where users can track and log issues.
12. **Navbar - Sign Out** - Provides users with a navbar menu, which allows users to sign out of their account.
13. **Navbar - Issues** - Provides users with a navbar menu, which brings users to an issues tracker, allowing users to track and edit issues.
14. **Navbar - New Issues** - Provides users with a navbar menu, which brings users to a new form, allowing users to log a new issue.

### Features to Implement
1. **Blog** - Add a feature to include a blog page.
2. **Issues Tracker (Status)** - Add a feature for status color to auto change as satus is updated.
3. **Issues Tracker** - Add search, sort, scroll/indexing, ID#, upvotes, # Open/Closed.


## Technologies Used
The following section describes all technologies used to develop this project.

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - This project used **Cloud 9**, an online integrated development environment, to construct the code end to end.
- [Django](https://www.djangoproject.com/)
    - This project uses **Django**, a Python web-framework. Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and pluggability of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.
- [Bootstrap](https://getbootstrap.com/)
    - This project used **Bootstrap**, a library of website themes. The [Scrolling Nav Template](https://github.com/BlackrockDigital/startbootstrap-scrolling-nav), was used for this project.
        - **Static folder**: All files except the `custom.css` and `stripe.js` files, were copied from the bootstrap template.
        - **.html files**: All `.html` files used the bootstrap `.html` files as boiler plate code. The project developer then amended and built upon each of these files to suit this project.
        - **All Other Code**: Compiled by the project developer.
- [Django Bootstrap Forms](https://django-bootstrap-form.readthedocs.io/en/latest/)
    - This project uses **Bootstrap Forms**, a library to allow quicker implementation of forms throughout the project.
- [Stripe API](https://stripe.com/)
    - This project uses **Stripe API**, which allows individuals and businesses to receive payments over the Internet
- [Jinga](http://jinja.pocoo.org/)
    - This project uses **Jinja**, a template engine for Python, jinja code is included within the curly brackets.
- [Python](https://www.python.org/)
    - This project uses **Python**, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which is included within the `.html` files.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - This project uses **CSS**, a style sheet language, used to add styling to a website. The `custom.css` file was added to this project, to add additional styling on top of the Bootstrap template.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - This project uses **JavaScript**, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
    - This project uses **Chrome Dev Tools**, a set of web developer tools, to continuously test and inspect that the web pages are rendering as intended within the browser.
- [GitHub](https://github.com/)
    - This project uses **GitHub**, a web hosting service, for version control and final project backup.
- [Heroku](https://www.heroku.com/home)
    - This project uses **Heroku**, a web hosting service that supports Python applications, for final project deployment.
- [All Other Technologies](https://startbootstrap.com/template-overviews/business-casual/)
    - All other technologies within this project were included with the Bootstrap template.


## Testing
The following is an overview of testing to ensure all functionality works as intended in this project.


Bug: Terminal 'run' = ImportError: No module named 'stripe'. Solution = sudo pip3 install stripe.
Bug: OPEN = Password reset. ERROR = ConnectionRefusedError at /accounts/password-reset/.
Bug: OPEN = Stripe payment not processing. Fix - Will only process when deloyed?
Bug: Travis - failing due to requirements libraries not required/out of date. Failed due to import env code required updating. Travis error - use pip freeze, rather than pip3 freeze.
Bug: TemplateDoesNotExist at /accounts/login/ = remove brackets in commentary {% extends "base.html" %}.
Bug: AttributeError at /issues/16/ | 'Post' object has no attribute 'views' = Removed post.views += 1 from issues views.py, obsolete code.
Bug: Cart, checkout total and button not aligned / not responsive - wrapped div container around section.
Bug: Issues Tracker Not Responsive, data overlaying - udated with correct bootstrap col grid layout for items to stack on smaller devices.
Bug: Issues Details: Not Fully Responsive. Updated divs, p tags and margins.



1. **Homepage - Header**
    1. Select 'Contact' on the navbar and move the user away from the home page.
    2. Select 'Mythware' on the navbar.
    3. Verify that the header section is displayed.
    4. Select 'Get Started' button.
    5. Verify that the button is highligted when hoovered.
    6. Verify that a scrolling action happens and that the pricing section is displayed.
        - **Bug 1** - Browser error, 'django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty'.
            - **Issue** - Settings.py not updated.
            - **Fix** - Updated settings.py with if os.path.exists('env.py'): import env.
        - **Bug 2** - When Get Started selected, pricing action not displayed.
            - **Issue** - Pricing section id is not included.
            - **Fix** - Added id="pricing" to pricing section div.
2. **Navbar - Features**
    1. Select 'Features' on the navbar.
    2. Verify navbar menu highlights.
    3. Verify features section is displayed.
3. **Navbar - Pricing**



4. **Navbar - Documentation**
    1. Select 'Documentation' on the navbar.
    2. Verify navbar menu highlights.
    3. Verify features section is displayed.
    4. Select 'technical documenation' link.
    5. Verify link works as intended. Placeholder link for this project therefore no documents will be displayed at this point.
5. **Navbar - Contact**
    1. Select 'Contact' on the navbar.
    2. Verify navbar menu highlights.
    3. Verify features section is displayed.
6. **Navbar - Social Links**
    1. Select each social link.
    2. Verify link works as intended. Placeholder links for this project therefore no social websites will be displayed at this point.
7. **Navbar - Mythware**
    1. Select 'Mythware' on the navbar.
    2. Verify the homepage header is displayed.


8. **Navbar - Sign Up**
9. **Navbar - Sign In**
10. **Navbar - Cart**
11. **Navbar - Profile**
12. **Navbar - Sign Out**
13. **Navbar - Issues**
14. **Navbar - New Issues**
15. **Responsive Testing - All Device Sizes**:
    1. In Chrome, right click anywhere on the website and select 'inspect', to open the Chrome Dev tools.
    2. Select the toggle device icon at the top of the window, to open the responsive testing window.
    3. Test how the website is rendering on each device size from Galaxy S5 to iPad Pro.


## Deployment
The following section describes the process to deploy this project to Heroku.

1. Ensure all required technologies are installed locally, as per the `requirements.txt`file.
2. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Mythware](#).


## Credits

### Acknowledgements
- For the technical skills used in this project, I harnessed my own knowledge and the knowledge gained from the [Code Institute - Diploma in Software Development](https://www.codeinstitute.net/), [Stack Overflow](https://stackoverflow.com/), [W3 Schools](https://www.w3schools.com/), [Bootstrap](http://getbootstrap.com/) and [Bootsnipp](https://bootsnipp.com/).
