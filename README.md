# Contents
* [**Project Goals**](<#project-goals>)
    *  [User Goals](#user-goals)
    *  [Site Owner Goals](#site-owner-goals)
* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
    *  [Scope](<#scope>)
    *  [Design](<#design>)
    *  [Technical Design](<#technical-design>)
* [**Features**](<#features>)
    * [Current Features](<#current-features>)
    * [Future Features](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages Used](<#languages-used>)
    * [Frameworks Libraries & Programs Used](<#frameworks-libraries-programs-used>)
    * [Libraries](<#libraries>)
* [**Testing**](<#testing>)
    * [Validation](<#validation>)
    * [Testing User Stories from User Experience](<#testing-user-experienece>)
* [**Bugs**](<#bugs>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
*  [**Acknowledgements**](<#acknowledgements>)

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


## Technical Design

* The flow for how the application operates was mapped out on lucidcharts

<details><summary>Site Flow</summary>
<img src="#">
</details>

<details><summary></summary>
<img src="#">
</details>

<details><summary></summary>
<img src="#">
</details>

### Data Modeling

<details><summary></summary>
<img src="#">
</details>




[Back to top](<#contents>)

## Features

### Current Features

- User can login with their email and password.

- User can reigster their details, again this is checked at time of registration to avoid unnecessary follow up of details.




### Future Features

- Admin can reject orders.

[Back to top](<#contents>)

## Technologies Used

### Languages Used

-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks Libraries & Programs Used
1. [Git](https://git-scm.com/) - Git was used for version control.
2. [GitHub](https://github.com/) - Github was used as a remote repository to store project code.
3. [Gitpod](https://gitpod.io/) - Gitpod was the IDE user to write the code of the project code.
4. [Lucidcharts](https://www.lucidchart.com/) - Lucidcharts was used to map out the flowcharts for the project.
5. [Googlesheets](https://www.google.com/sheets/about/) -  Googlesheets was used to act as the backend database to store snesitive information to be queried.
6. [Google Cloud Platform](https://cloud.google.com/) - Google cloud is iused to manage the access to the google services, google authorization, google sheets.
7. [Twitter](https://developer.twitter.com/en) -  Twitter developer was used to access the Twitter API. With use of OAUthandler to access live tweets from timeline.
8. [Yahoo finance](https://finance.yahoo.com/) -  Yahoo finance was used to access the Yahoo Stock API, this gives appliction access to live data.

#### Libraries

1. os -  for environs.


##### 3rd Party Libraries



[Back to top](<#contents>)

## Testing

### Validation

### PEP8:

<details><summary>Placeholder for code</summary>
<img src="#">
</details>



### Testing User Stories from User Experience (UX) Section

### Testing User Experienece
1. As a user I want a clear menu with options that are clear on intention.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find main menu       |      No action needed      | User is presented with welcome page | `Works as expected` |

<details><summary>Screenshots</summary>
<img src="assets/images/main-menu.png">
</details>

                                         
                                       
## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |

[Back to top](<#contents>)

## Deployment

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

By forking this GitHub repository you are making a copy of the original to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/dannymagnus/CI_MS3_MitsurukiFMS).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/dannymagnus/CI_MS3_MitsurukiFMS).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

[Back to top](<#contents>)

## Credits

### Code

### Content

-   All content was written by the developer.

### Acknowledgements

The app was completed as a Portfolio 4 Project for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor Mo Shami, my class mates, the Slack community, and all at the Code Institute for their help and support. 

Also to my friends and family who helped test site & provide feedback and most importantly patient with me during this time!

[Back to top](<#contents>)