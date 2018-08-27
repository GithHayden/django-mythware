# Websolver

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- Feature 1: User Authentication. The project should include an authentication mechanism, allowing a user to register and log in. There should be a good reason as to why the users would need to log in e.g. a user would have to register to persist their shopping cart between sessions, otherwise it will be lost.
- Feature 2: Stripe Payments (Django App). At least one of your Django apps should contain some e-commerce functionaity usins Stripe. This may be a shopping cart checkout, subscription-based payments or single payments etc.
- Feature 3: User Requests. Include at least one form with validation that will allow users to create and edit models in the backend, in addition to the authentication mechanism.
- Feature 4: Responsive UI. The UI should be responsive, use either media queries or a resonsive framework such as Bootstrap to make sure the site looks well on all commonly-used devices.

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Django]()
    - This project uses **Django** and is composed of multiple apps, an app for each reusable component in the project.
- [Database]()
    - The project will need to connect to a database e.g. sqlite or Postgres, using Django's ORM.
- [JavaScript]()
    - The front end should contain some JavaScript to enhance the user experience.
- [Python/Django packages]()
    - Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Django Rest Frawmwork, etc. Strive to choose the best tool for each purpose.
- [Travis CI]()
    - Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to users, under any circumstance. Use autoamted Django tests wherever possible.
- [Jasmine Tests]()
    - For your JavaScript code, consider using Jasmine tests.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
