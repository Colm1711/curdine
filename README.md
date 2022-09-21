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
            2. [Profile Model](#meal-model)
            3. [Food_item Model](#category-model)
            4. [Review Model](#allergen-model)
            5. [Order Model](#drink-model)
            6. [AboutMe Model](#drinkcategory-model)
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

