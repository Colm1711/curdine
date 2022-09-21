# Contents
* [**Project Goals**](<#project-goals>)
    *  [User Goals](#user-goals)
    *  [Site Owner Goals](#site-owner-goals)
* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
   1. [Structure](#structure)
        1. [Website pages](#website-pages)
        2. [Code Structure](#code-structure)
        3. [Database](#database)
        4. [Physical database model](#physical-database-model)
        5. [Models](#models)
            1. [User Model](#user-model)
            2. [Profile Model](#profile-model)
            3. [Food_item Model](#food_item-model)
            4. [Review Model](#review-model)
            5. [Order Model](#order-model)
            6. [AboutMe Model](#aboutme-model)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    4. [Surface](#surface)
        1. [Design Choices](#design-choices)
        2. [Colour](#colours)
        3. [Fonts](#fonts)
6. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
7. [Features](#features)
8. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [JS Validation](#JS-validation)
    4. [Python Validation](#py-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Device testing](#performing-tests-on-various-devices)
    8. [Browser compatibility](#browser-compatibility)
    9. [Testing user stories](#testing-user-stories)
9. [Bugs](#Bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals
*Placeholder


## User Experience (UX)

-   ### Target Audience
1. Users looking to retrieve order food online.

## User stories

-   ### User

1.    I want to be able to see menu and what I can order.
2.    I want to be able to navigate site easily.
3.    I want clear information on where the restaurant is located.
4.    I want to be able to order food online.
5.    I want to be able to know my order has been accepted.
6.    I want to view reviews so that I know what others thought of previous orders.
7.    I want to be able to cancel my order.
8.    I want to be able to modify my order.
9.    I want to view About me page so that I know more about the company
10.   I want to see confirmation page of my order so that I know how much it will cost and they have my correct details.

-   ### Registered User

1.    I want to be able to register my information and have it stored so I can easily order without having to fill out details.
2.    I want to be able to leave reviews.
3.    I want to delete my review.
4.    I want to modify my review.
5.    I want to see my order history.
6.    I want to modify my profile details
    
-   ### Site Owner

9.    I want to be able to manage reviews
10.   I want to be able to approve reviews
11.   I want to be to approve orders
12.   I want to be able to reject orders

## Scope

1. For first release, the scope is to provide users ability to register, login and oder food.
2. Future scope:
    1. User can cancel order
    2. User modify my order
    3. User see order history


#### Overview

Article from above is from 2021. The listed most popular takeaway by Irish people during lockdown was chippers and after chips the most ordered item was sauce. My brother is heading away soon to begin his adventure in Canada in honour of him and his help for this project it lead me to pay homage by picking the most popular dish there Poutine, which is a delicacy


## Structure
### Code Structure
The project is organised into a two applications, developed using the Django Framework.

App details as follows:
- customer - this app contains information about the user and is extended by the profile model to contain further details such as email, fullname, phone number and address details.
- takeaway - this app contains the menu structure, users can choose between the varies meals from menu.  Clicking individual items opens a sub  page where users can see detailed food information and can leave a review if they are a rigestered user.

To complement the apps there are
- project: Project level files - settings.py for project level settings and urls.py to route the website URLS
- templates: Containing the base.html, allauth(django authentication)
- templates (app level): each app has it's own templates directory for HTML to consider portability and re-use.
- urls (app level): each app has it's own url.py file to consider portability and re-use.
- static: Base css and Javascript files
- manage.py: This file is used to start the site and perform funcions during development
- README.md: Readme documentation
- Procfile: To run the application on Heroku
- Requirements.txt: Containing the project dependencies
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings


#### Physical database model

This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database 
<br>![Database model]()

#### Models
- The following models were created to represent the database model structure for the website

##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, is_staff, is_active, is_superuser, last_login, date_joined

##### Profile Model
- The Meal model contains information about user such as contains further details such as email, fullname, phone number and address details for delivery purposes.
- It contains User as a foreign-key.
- The model contains the following fields:  email, Name, phone_number, address1, address2, city, county, eir_code

##### Food_item Model
- The category model contains the available meal items
- The model contains the following fields: food_name, food_image, description, price, slug

##### Review Model
- The Review model is the review model for food items for user to leave a review on a food item to let restraunt and others know thoughts on food item.
- It contains Food_item as a foreign-key.
- When user submits review it is sent to the back end for the admin to approve before being displayed to the site.
- The model contains the following fields: Food_item, name, email, body, creation_date, approved.

##### Order Model
- The Order model the user to be able to submit order from the website with items and address details.
- The model contains the following fields: creation_date, email, name, phone_number, address1, address2, city, county, eir_code.

##### AboutMe Model
- The About me model for the site owner to be able to update about me section of website with text on backend.
- The model contains the following fields: about_text_body, date_modified.

## Scope
### User stories:

#### First time user
1.	As a first time user, I want to be able to see menu and what I can order.
2.	As a first time user, I want to be able to navigate site easily
3.	As a first time user, I want clear information on where the restaurant is located
4.	As a first time user, I want to be able to order food online
5.	As a first time user, I want to view reviews so that I know what others thought of previous orders
6.	As a first time user, I want to view About me page so that I know more about the company and it’s ethos
7.	As a logged in user, I want to be able to see other user’s comments and reviews
8.	As a logged in user, I want to be able to be able to leave reviews
9.	As a first time user, I want to be able to delete my review
10.	As a first time user, I want to see confirmation page of my order so that I know how much it will cost and they have my correct details
11.	As a first time user, I want to be able to know my order has been accepted
12.	As a first time user, I want to know about the business and it’s ethos
13.	As a first time user, I want to be able to cancel my order
14. As a logged in user, I want to be able to to sign in to, or create an account
15. As a logged in user, I want to be able to log out of an account
16. As a first time user, I want to see confirmation page of my order so that I know how much it will cost and they have my correct details
17. As a first time user, I want to be able to view the business’ social media
18. As a logged in user, I want to be able to cancel my order
19. As a logged in user, I want to be able to modify my order


#### Site Owner
20.	As a site owner, I want to be able to Approve reviews
21.	As a site owner, I want users to be to view our full menu
22.	As a site owner, I want users to be able to view the food descriptions and prices
23.	As a site owner, I want to Manage reviews
24.	As a site owner, I want users to be able to see location of business
25.	As a site owner, I want users to be able to leave a comment or review
26.	As a site owner, I want users to be able to view other comments and reviews
27.	As a site owner, I want users to be able to edit and delete comments or reviews
28.	As a site owner, I want users to be able to find out about our business ethos
29.	As a site owner, I want users to be able to navigate the site easily and quickly
30. As a site owner, I want users to be able to sign in to, or create an account
31. As a site owner, I want users to be able to log out of their account
32. As a site owner, I want users to be able to see the menu
33. As a logged in administrator, I want to be able to review and approve or delete user comments.
34. As a site owner, I want users to be able to view the business’ social media
35. As a logged in administrator, I want to be able to create, edit or remove content on the website.

#### Error Flow
36. As first time, I user should be able to navigate back through the site structure in case of page not found without using the browser back button.
37. As a site owner, I want a 400 page that enables users to be able to return to valid areas of the site without using browser controls.
38. As a site owner, I want a 403 page that enables users to be able to return to valid areas of the site without using browser controls.
39. As a site owner, I want a 404 page that enables users to be able to return to valid areas of the site without using browser controls.
40. As a site owner, I want a 500 page that enables users to be able to return to valid areas of the site without using browser controls.

