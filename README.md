[![Build Status](https://travis-ci.org/GithHayden/django-mythware.svg?branch=master)](https://travis-ci.org/GithHayden/django-mythware)

# Mythware

Mythware is an agile project management software application, developed using **Django**, a Python web-framework. The target audience is any user/team who would like (software application fictious for purpose of this project), to manage projects. Mythware provides a user authentication feature, allowing users to request free bug fixes and paid upgrades. User profiles also provide access to an issues tracker, allowing users to track issues.

## UX
The following section describes the UX process for this project.

#### UX Process
1. **Layout** - Reviewed the Code Institute education to date and Bootstrap themes to extract design ideas.
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
2. **Issues Tracker - Status** - Add a feature for status color to auto change as satus is updated.
3. **Issues, # Open and Closed** - As Tracker List grows add, search, sort, scroll/indexing, ID#, upvotes, # Open/Closed.


## Technologies Used
The following section describes all technologies used to construct this project.


django-forms-bootstrap, Pillow, Stripe API, Boostrap - https://github.com/BlackrockDigital/startbootstrap-scrolling-nav

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - This project used **Cloud 9**, an online integrated development environment, to construct the code end to end.
- [Bootstrap](https://getbootstrap.com/)
    - This project used **Bootstrap**, a library of website themes. The [Business Casual Template](https://startbootstrap.com/template-overviews/business-casual/), was used for this project.
        - **Static folder**: All files except the `custom.css`, `bg.jpg`,`intro.jpg` files, were copied from the bootstrap template.
        - **.html files**: All `.html` files used the bootstrap `.html` files as boiler plate code. The project developer then amended and built upon each of these files to suit this project.
        - **gulpfile.js, package-lock.json, package.json files**: Each of these files were included with the bootstrap template.
        - **All Other Code**: Compiled by the project developer.
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask**, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries.
- [mLab](https://mlab.com/)
    - This project uses **mLab**, a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers. The developer used an mLab sandbox DB, which is for learning and prototyping. Json value pairs were added into the mLab document to align with the recipe wireframe. For example, 'Recipe_Title: Title', is the json value pair within the mLab database for the Recipe Title.
- [MongoDB](https://www.mongodb.com/)
    - This project uses **mongoDB**, a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.
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
Bug: Error = django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty = updated settings.py with if os.path.exists('env.py'): import env
Bug: OPEN = Password reset. ERROR = ConnectionRefusedError at /accounts/password-reset/.
Bug: OPEN = Stripe payment not processing. Fix - Will only process when deloyed?
Bug: Travis - failing due to requirements libraries not required/out of date. Failed due to import env code required updating. Travis error - use pip freeze, rather than pip3 freeze.
Bug: TemplateDoesNotExist at /accounts/login/ = remove brackets in commentary {% extends "base.html" %}.
Bug: AttributeError at /issues/16/ | 'Post' object has no attribute 'views' = Removed post.views += 1 from issues views.py, obsolete code.
Bug: Cart, checkout total and button not aligned / not responsive - wrapped div container around section.
Bug: Issues Tracker Not Responsive, data overlaying - udated with correct bootstrap col grid layout for items to stack on smaller devices.
Bug: Issues Details: Not Fully Responsive. Updated divs, p tags and margins.


1. **Navbar - Home**:
    1. Select 'Contact' on the navbar and move the user away from the home page.
    2. Select 'Home' on the navbar.
    3. Verify that 'Home' is highlighted on the navbar and that the user is moved to the home page.
    4. Verify that the page header, footer, social links, image and text are displayed as intended.
        - **Bug 1** - Application not rendering in the browser.
            - **Issue** - app.py file `@app.route('add_recipe')` not correct.
            - **Fix** - Added missing `/`, to `@app.route('/add_recipe')`.
        - **Bug 2** - Application not rendering in the browser.
            - **Issue** - Incorrectly spelled code as `{{ endfor }}`.
            - **Fix** - Scanned all code. Updated code to `{% endfor %}`. 
        - **Bug 3** - Home is not highlighted on the navbar.
            - **Issue** - Overwrote bootstrap nav html tags, losing bootstrap div styling classes.
            - **Fix** - Added `active` class to 'Home' navbar menu. Corrected on all navbar menu items, within each `html` file.
2. **Navbar - Recipes**:
    1. Select 'Recipes' on the navbar.
    2. Verify that 'Recipes' is highlighted on the navbar and that the user is moved to the recipes page.
    3. Verify that the page header, footer, social links and all recipes are displayed as intended.
    4. Select 'View Recipe' and verify that the button is highlighted.
    5. Verify that the user is brought to a new page and that all the recipe details are displayed as intended.
    6. Select 'Update Recipe' and verify that the user is brought to a new page, where a form is displayed.
    7. Verify that this form contains all of the recipe details, which can be updated and over-written.
    8. Verify that a red alert box is displayed, guiding the user as intended. Select X on the alert box and verify that the message disappears.
    9. Once the Recipe has been updated, select 'Update Recipe'.
    10. Verify that the user is brought to the recipes page and that the updated recipe is added to this page.
    11. Verify that the old recipe is still on the recipes page for the user to refer back to if required and for the user to delete once satisfied with their updated recipe.
    12. Select 'View Recipe' on the newly updated/added recipe.
    13. Verify that the user is brought to a new page and that the recipes details are displayed.
    14. Verify that a red alert box is displayed, guiding the user as intended. Select X on the alert box and verify that the message disappears.
    15. Select 'Delete Forever'. Verify that the user is brought to the recipe page and that the recipe is deleted.
        - **Bug 1** - Recipe cards not aligning vertically.
            - **Issue** - The html `divs` require adjusting.
            - **Fix** - Added `<div style="text-align: center">`.
        - **Bug 2** - No spacing between the recipe cards.
            - **Issue** - Recipe cards require margin styling.
            - **Fix** - Added Bootstrap spacing classes i.e. mt and mb, to the relevant `divs`.
        - **Bug 3** - Recipe cards are not all the same height.
            - **Issue** - Recipe card sizes only stretching as far as the recipe description text, rather than aligning with the height of that `div` row.
            - **Fix** - Added `d-flex align-items-stretch` to the relevant `div`.
        - **Bug 4** - Recipe card buttons displaying randomly, rather than aligned at the end of each card.
            - **Issue** - Card sizes only stretching as far as the recipe description text, rather than aligning with the design of that div row.
            - **Fix** - Moved the button, down a `div`.
3. **Navbar - New Recipes**:
    1. Select 'New Recipes' on the navbar.
    2. Verify that 'New Recipes' is highlighted on the navbar and that the user is moved to the new recipes page.
    3. Verify that the page header, footer, social links and a blank form are displayed as intended.
    5. Leave all form fields blank and select 'Add Recipe'. Verify that the user is required to populate all fields before a new recipe can be added.
    6. Input dummy data into each form field. Select 'Add Recipe'. Verify that the user is brought to the recipes page and that the new recipe is added.
        - **Bug 1** - Date posted field is populating but not displaying when the recipe is added to the recipes page.
            - **Issue** - Incorrectly spelled `{{recipe.posted_date}}`.
            - **Fix** - Updated to `{{recipe.date_posted}}`, as the words were the incorrect way around.
4. **Navbar - Contact**:
    1. Select 'Contact' on the navbar.
    2. Verify that 'Contact' is highlighted on the navbar and that the user is moved to the contact page.
    3. Verify that the page header, footer, social links and a blank form are displayed as intended.
    5. Input dummy data into each form field. Select Submit, button highlighted but no further action happens. (This contact page is not currently wired up to an email account as this is not a real business.)
5. **Responsive Testing**:
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
9. Deployed via Heroku: [Raw Dessert Recipes](https://cookbook-mongodb.herokuapp.com/).

## Credits

### Acknowledgements
- For the technical skills used in this project, I harnessed the knowledge gained from the [Code Institute - Diploma in Software Development](https://www.codeinstitute.net/), [Stack Overflow](https://stackoverflow.com/), [W3 Schools](https://www.w3schools.com/), [Bootstrap](http://getbootstrap.com/) and [Bootsnipp](https://bootsnipp.com/).
