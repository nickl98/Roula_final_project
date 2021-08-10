

<h1 align="center"> Roula Store </h1> 

This Full-Stack site is designed to allow the user to peruse and purchase products available from the Roula Store that are stored in the Django database. 
In the cart section of the site, the user can create, locate, display, edit and delete items in the cart in line with CRUD functionality. 
The user does need to be signed in to make a purchase, check their profile, and process stripe credit card payments. 
The site is easy to use and allows the authenticated user a range of options including the ability to view and update their profile.
It also sends you an email when signing up make sure you log into your email and confirm your account.
The purpose of the site is to teach users about Roula and to sell merchandise to fund its launch. Keeping that in mind, I wanted to make the user experience as informative and pleasurable as possible.

<h2 align="center"><img src = "https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/responsive/reponsive-picture.png?raw=true"></h2>

Iphone X [Reponsive View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/responsive/iphonex-no-footer.png?raw=true)

The link for the app is: 

*https://nickl98-roula-store.herokuapp.com/*

The link for the Github repository is:

*https://github.com/nickl98/Roula_final_project*

## UX

To make the user experience as Informative and enjoyable as possible I went for a simple-looking site, with different shades of blues, whites, and greens. 
In addition to I also decided to use gradient blue/black hues that move from left to right, to add a subtle eye-catching effect to the site. I kept all the content for the site
in collapsable elements so that there wouldn't be any overflow issues.

To make sure users don't have any issues navigating the site I kept all the links at the top of the bag. The footer is also added for larger screens and is not displayed on 
mobile sites (iPhone-x).
Inside the footer, you can find links to Roula's social media, contact corporate, shop now, and office location links.

When using the navigation bar you will see buttons for `Merchandise, `Sign Up, `Login`, `Locations`, `Developer Team`,  `Q&A`, and `Shopping Cart` for the unauthenticated user.
Even though they are not authenticated they can still look around the site to learn. We don't want to have any sort of restrictions preventing a user from visiting.
Then once the user authenticates their account the user will then be able to store their delivery information for another time. It also provides a list of previous orders.  
The superuser of the site is presented with a navbar option where they update, add and delete merchandise. In addition, on the `Devlopers` and `Q & A` have notes to the superuser.
Django provides a useful notification bar off to the right that alerts the user to when an action such as logging in or out is successful. It also will present an error message in red if your cart is empty. For the pop-up notifications throughout the application, I used bootstrap toasts for the corresponding messages.

There is a search bar on top of the Navbar that the user can type in any word to search the products currently available. The Roula Store 
logos in the header act as links to the homepage and there are active links to Roula's Facebook, Twitter, and Instagram 
pages in the footer. 

The user must be registered and logged in to make an actual purchase on the site. To register the user needs to complete the registration form on the `sign-up` page which requests a Username, Email address, Password, and Password confirmation. Once the user confirms their account they will be able to start shopping,
and donate.

If the user wishes to add a product to their shopping cart they can do so by selecting the quantity field in the individual product panel and either using
the up / down arrows or inputting a number and pressing the `Add` button. This will add the specified quantity to the cart the total items are visually displayed on the cart icon in the navbar. The user can then select the Cart page that displays the selected products, quantities, and total price. The user can adjust the quantity in the Quantity field and press the `Update` button. If the value is set to zero the specified product will be deleted from the cart. If the user is happy with the products and quantities in their cart, they can proceed to the Checkout page using the `Checkout` button. Here the chosen products and total price are shown. The user can input their card payment details and in the Payment Details, fields provided. then press the 
`Submit Payment` button. Provided the payment is successful the user will be redirected to the homepage and a green notification banner will be displayed telling the user that they have successfully paid.  

The original concepts for the web-app pages can be seen in the *readme_pictures/wireframes folder*  
These were created in Balsamiq. There are a lot of changes since these wireframes, mainly due to learning more about the capabilities of Python and Django. 
There is also a database schema showing the original idea for the project. You can view the pictures in *readme_pictures/database folder*

The site is aimed at users who want to support the start-up behind the idea of *Data Compensation*. We appreciate all the donations and are glad the users are loving the merchandise.

## Features

### Existing Features

The choice of features, links and buttons available to the user are:

* **Nav Bar –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/basic_navbar.png?raw=true) 
Contains the Roula Store logo that is also a homepage link. The Navbar is designed to collapse on mobile view. when the user scrolls down and reappears when the user scrolls up. This is a defensive mobile-first design that allows a better view of the actual page (e.g. Shop page) on 
smaller screens.

* **Free Delivery Banner –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/delivery_banner.png?raw=true)
This banner rests right under the Navbar, I wanted it to stand out a bit so made it larger. However, this was a problem for mobile devices. 
The Banner would take up a lot of space if it remained fixed. So I added in some Jquery so that it disappears when users scroll past it. Allowing more space for users to view the site. 

* **Unauthorised User Nav Bar –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/basic_navbar.png?raw=true)
Contains the Roula Store logo that is also a homepage link. The Navbar links available to the unauthorized user are`Merchendise`, `Sign Up`, `Log In`, `Locations`, `Developer Team`,  `Q&A`, and `Shopping Cart` This is a limited range of links that allows the user to peruse the available products, but mainly
directs the user towards either logging via the Login page or registering via the Registration page. However, if the user just wants to look around there is no issue with that!

* **Authorised User Nav Bar –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/basic_navbar.png?raw=true)
Contains the Roula Store logo that is also a homepage link. The Navbar links are available to the authorized 
Users are  `Merchandise, `Sign Up`, `Login`, `Locations`, `Devloper Team`,  `Q&A`, and `Shopping Cart` These links are designed to allow the user to interact with the site.
The links are highlighted and pulse when they are hovered on to make it clear to the user that they are links. When authorized you will be able to purchase in the shop.

* **Admin/Superuser page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/merch-view-w-superuser.png?raw=true)
When granted this access you will be able to change the details of products, in the future I would want to add that to the developer page. So then we can add new people to the team list quicker.

* **Side Nav Bar –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/responsive/iphonex-no-footer.png?raw=true)
This becomes available on smaller screen types and is present in the form of the radio-style menu icon in the top right corner of the Navbar. Once the icon is clicked the Side Navbar presents itself with all the links that are hidden in smaller view dependant on the 
users authorization status that directs the user to the specified page.

* **Mission Statement –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/responsive/iphonex-no-footer.png?raw=true)
This paragraph located below the Navbar on larger screen resolutions gives a brief synopsis of Roula and the Roula Store. What they do
and what they plan on doing in the future. 

* **Search Bar –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/basic_navbar.png?raw=true)
The search bar is available on all pages for the user to search for a specific product by name. This has been included, as it is expected that eventually there will be a vast amount of products on the site. So leaving the search bar at the top will allow users to search and add another item wherever they may be on the site.

* **Individual Product Panels –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/product-view.png?raw=true)
Each product has its panel, in which the information stored in the database is presented for each specific product (e.g. Name, Description, SKU, Rating, Category, Price, and Image). The user can input the quantity they require for each product 
and press the `Add` button, to add items to the cart.

* **Footer –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/footer.png?raw=true)
  The Footer is defensively designed to show only on larger screens. The active social links (Facebook, Twitter, and Instagram) light up a different color when hovering over them. Other links will show locations and also bring you back to the store. The footer disappears on smaller devices like the iPhone X. It is designed with a rotating gradient just like the headers.  

* **Success Message Bar –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/toast-1.png?raw=true)
When the user performs an action that requires confirmation, such as logging in or out or sending a message via the contact form, a green notification banner will appear below the Navbar to tell the user that the operation was successful. This was done using bootstrap toasts.

* **Register Page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/login-page.png?raw=true)
The registration page allows the user to register with the site by providing a username, email address, password, and password confirmation. Once they verify their email they can now make purchases thanks to Stripe.

* **Login Page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/signup.png?raw=true)
The Login page provides the user with a form where they can log in using their username or email and password. 

* **Cart Page –**[View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/shopping%20cart.png?raw=true)
 If there are no items in the Cart and the user selects the Cart page, they will be presented with a message saying 'No items in your cart' 
and a `Continue Shopping` button that redirects back to the Shop page. If the user has items in thir cart they will be displayed in the Cart page along with 
the options to `Amend` the quantity, `Checkout`, or `Continue Shoppping`. The total of the users cart is shown. If the user amends a products quantity to zero,
the item will be removed from the cart. Once an item is added to the cart the total quantity is displayed on the Cart icon in the Navbar. If the user is not 
authorised and selects the `Checkout` button, they will be redirected to the Login page.


* **Profile Page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/profile-bag.png?raw=true)
The Profile page allows the registered user to insert their name and address credentials so that these details can be prepopulated 
within the Users Checkout Form.  

* **Devloper Team Page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/dev-team.png?raw=true)
 The Developer page pulls all data from the fixture and populates each person into their card!

* **Q & A page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/features/q&a.png?raw=true)
The main part of the questions page is questions from the database that are populated into an accordion. When a user clicks on the question they will be presented with the answer and who answered the question. 

* **Locations Page –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/responsive/iphonex-no-footer.png?raw=true)
 The location page was just a little extra thing I added. Added some random locations around the world to act as head offices.

* **Logout Navbar Button –** [View](https://github.com/nickl98/Roula_final_project/blob/main/readme_pictures/responsive/iphonex-no-footer.png?raw=true)
 If pressed the user will be logged out from the site and all items in the cart will disappear, as the user is taken back to the unauthorized user homepage. The user is notified by a green notification success message banner that they have successfully logged out. 

### Features left to implement
* Star rating for reveiws on Homepage next to product. Due to time constraints this was not done. 

* No easy way yet to add new devlopers to the team. This is a work in progress.

* Add a blog that connects to the users name.

* Add more products.

* Add more CRUD to Devlopers and Questions

* Write more tests in tests.py files for each individual app.

* Add in Custom 404, 500 page and also a favicon. Ran out of timne to desgin one I like.

* Due to time constraint it was not possible to implement the functionality to have the Users create questions of thier own. This is a work in progress.


## Technologies Used
The languages, frameworks, libraries and other tools utilised for building this web-app are:

* **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for 
the web-app. https://www.gitpod.io/

* **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently 
during the development of the web-app.  https://github.com/

* **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database. 
https://heroku.com/

* **SQlite3 -** SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. 
SQLite is the most used database engine in the world. https://www.sqlite.org/index.html

* **PostgreSQL -** PostgreSQL is a powerful, open source object-relational database system. https://www.postgresql.org/

* **Django 3.2 -** Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
https://www.djangoproject.com/

* **AWS S3 -** Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, 
security, and performance. https://aws.amazon.com/s3/

* **Balsamiq -** fUsed for design of ireframes. https://balsamiq.com/

### Front-End Technologies

* **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a 
better understanding.

* **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.

* **Bootstrap 3.7.7 -** The open-source Bootstrap framework has been used to implement the layout of the site. Bootstrap is also utilised 
to accommodate the responsive and mobile first design of the dashboard. https://getbootstrap.com/

* **Django-forms-bootstrap 3.1.0 -**  A simple bootstrap filter for Django forms. Extracted from the bootstrap theme.
https://django-bootstrap3.readthedocs.io/en/latest/

* **JavaScript -** The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language.
https://www.javascript.com/

* **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 
https://www.jquery.com/jquery-3.4.1

* **Google Fonts-** The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

* **Python 3.1 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, 
and it is easy to learn for brginners. https://www.python.org/  

* **Gunicorn 20.0.4 -** Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with 
various web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/

* **Pillow 4.3.0 -** The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides
extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. 
https://pillow.readthedocs.io/en/stable/handbook/overview.html

* **Psycopg2 2.8.5 -** Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are 
the complete implementation of the Python DB API 2.0 specification and the thread safety. https://pypi.org/project/psycopg2/ 

* **AWS Boto3 -** Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS 
services, such as EC2 and S3. https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

* **Jinja -** This is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional 
sandboxed template execution environment. https://jinja.palletsprojects.com/en/2.11.x/

* **Stripe 2.60.0 -** Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices 
and is designed to increase conversion. Checkout makes it easy to build a first-class payments experience. 
https://stripe.com/docs/payments/checkout


## Testing

The main basic functions of the site that required rigorous testing in different scenarios are listed below.

*	**Navbar** 
    * All Navbar links are coded within the base.html that extends to each HTML page. The logo is a home link that has been tested from each page and each link 
    (e.g. `Shop`; `Register`; `Login`; `Cart`; `Contact`; `Profile`; `Logout`; `Locations`; `Developer Team`; `Questions`) works correctly across all devices and screen resolutions. Each link directs the 
    user to the relevant page and the `Logout` button logs the user out of the site.
    
*	**Footer** 
    * All Footer links are encoded within the base.html that extends to each HTML page. The Footer Logo links back to the homepage that works from each page.
    The Footer Social Links of `Facebook`, `Twiter`and `Instagram` have all been extensively tested to redirect the user to the relevant Blindside Social Media page. The Location and Shop Now footer buttons work as well!

*	**Search Bar** 
    * The Search bar is used to search all available products on the homepage. The search bar is available beneath the header on each page. The search bar returns items that are related to the search string, otherwise, no items will be returned. This function works correctly.

*	**Product Detail Panel**
    * Each product panel shows all information related to the individual product, the majority of which is stored in the database. Products can be added or deleted by a SuperUser in the `manage products` panel. The attributes for each product displayed in each product panel are Name, Description, rating, category, Size, Price 
    , and Image. All of these attributes have been tested and work correctly. In Products/tests.py/ there is a test configured to test the product name, which works as expected. 

*	**Quantity Denominator Field** 
    * This field inserts a selected number of each product into the Cart. Validation of this can be seen when the user presses the `Add` button and the number quantity of items can be seen in the Cart Icon in the Navbar. This is the case on larger resolution screens, but not for smaller resolutions where the Cart Menu Icon is not immediately available. Once the user views the Cart page. all of the selected items will be shown with their acquired quantity.

*	**Registration Form** 
    * In the Registration Page, the user can set up an account by inserting a Username, Email Address, Password, and Password Confirmation. The form automatically cross-checks the validity of the Email Address and Password Confirmation. There is an optional link for the user to Sign In if they already have an account.


*	**Login Page** 
    * A user who has already registered can log in to the site via the `Login` Navbar menu item. This page authenticates the user against those stored in the database. 
    A verified user will be logged in otherwise the relevant errors will be presented. There is a Forgotten password link and a link for a user who is not registered.   


*	**Questions Page** 
    * I used fixtures to store all the questions for each user. On the front end, the users see a whole list of questions and answers in an accordion view. When a user clicks on the accordion it opens with the answer, thanks to javascript and jinja I was able to create a {{ for each loop }} so each question doesn't open every other answer. Now each only opens to its matching data target.   

*	**Devloper Team Page** 
    * I used fixtures to store all the images and quotes for each user. On the front end, the users see a whole list of individual developers with their pictures and social links.   

*	**Location's Page** 
    * This was an additional page that I added in when searching for ideas for my project. StoreRocket is a cool program online where you can create all the locations for your address's and then paste the appropriate Html code. Once that's in you get a fully functional Google Maps view!   


*	**Cart Page** 
    * The Cart page displays the products that the user has selected to purchase and the total shopping price (This is in the currency of Dollars, as the site is intended for 
    American distribution). The user can amend the quantity of the products to be purchased using the `Qty` field. If the user reduces this to zero and presses the `update` 
    button, the product will be deleted from their cart. This function has been extensively tested. The 'Total' figure has been calculated by the IDs and quantities of each product within the /cart/views.py/ and has been tested repeatedly. The `Checkout` button directs the user to the Checkout page and the `Continue Shopping` button takes the user back to the Homepage with their pre-requested items still in the Cart.

*	**Profile Page - Form**
    * This form allows the user to update their credentials (e.g. Name, Phone Number, Country, and Address). This information will be stored under the 'User Profile' information in the Django database and can be utilized to pre-populate fields on the Checkout page. The `Date` field is hidden from the user in the HTML page using a widget, so the user 
    does not overtype the date and time.   


*	**Checkout Page**
    * The Checkout page displays the products that the user has selected to purchase, their related quantities and prices, and the total shopping price. These elements have 
    been tested and return the correct figures.  

*	**Checkout - Payment Details Form**
    * The Checkout Payment Details form is directly linked to the Stripe payment API and allows the user to input their Name, Phone and Address details (if the user has already 
    registered their Profile details, these fields will be prepopulated).  

*	**Checkout - Payment Card Info Form**
    * The user is able to input their Credit card information to purchase the selected quantities of products. This function has only been tested using Stripes dummy card 
    information that consists of `Credit card number` 4242424242424242; `Security Code` 123; `Month` A month in advance of current month; `Year` a year in advance of the 
    current year. This functionality has been tested and can be checked in the /admin/home/checkout/orders/ section of the Admin panel. These payments are also visible on the
    https://dashboard.stripe.com/payments page. This confirms all the payments that have been passed through the system. The payment will not submit through the `Submit Payment` 
    button if the card information is incorrect.

*	**Checkout - Submit Payment Button**
    * Submits the Payment and returns the user to the Homepage with the Django success banner 'You have successfully paid'. If payment is not successful, the user will be not 
    leave the Checkout page.


*	**AWS S3**
    * The AWS S3 allows access to stored files within the site owners AWS bucket that are shared through the users AWS account. The accompanying AWS info is linked through the relavant AWS info in the 
    `settings.py` file. The testing of this functionality is shown in the availability of the stored data in the post prodution database andsite.

*	**Responsive / Mobile First design** 
    * Each page of the web-site has a **Header**; **containers and rows** and **Footer**. These needed to display correctly accross 
      all devices and screen resolutions. primarily checks are required to ensure that the site collapses in to columns in mobile view 
      and that the information is presented in a clear and legible fashion.    
    * Various methods of testing have been carried out to test the code of the web-site. Continuous testing throughout the development has been 
      implemented to check the quality of the code. The aim is to check the functionality of the code on different devices (mobile, tablet, desktop) 
      with an overall perspective of responsive and mobile first design. The site has been viewed and tested in **Firefox**, **Safari**, **Chrome** 
      **Microsoft Edge** and **Explorer**. The devices used to test the site are  **iPad**, **iPad Pro** and
      **iPhone X**.

*	**W3 Nu Html Checker** 
    * All .html files require validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://validator.w3.org/ 

*	**W3C CSS Validator** 
    * The style.css file requires validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://jigsaw.w3.org/css-validator/validator

*	**PEP8 Online** 
    * The Python (.py) pages require validation through the online checker. This ensures that the code is more legible and does not contain formatting 
      errors. http://pep8online.com/            
       
The final database schema and desktop wireframes for the web-app can be seen in the *readme_pictures* under *database* 
These wireframes and database schema were used initially to plan the site and build around. The opinions of numerous people including my mentor, friends, 
tutors, chat forums and such like, whom were asked during various stages of the project. They provided me with ideas and helped out alot concering any bugs I ran into.

## Issue List


  | Issue  |                 Description                     |       Solution                      |  
  | ------ |:-----------------------------------------------:|:-----------------------------------:|
  |   1    |Import on Line 17 of settings.py showing '  module level import not at top of file' in PEP8 check.|This import is set up for use in the For Loop, so is left as is |
  |   2    |settings.py showing as too long in PEP8 check|Line cannot be shortened, so left in|
  |   3    |Postgres Database crashed and could not submit new products|Reset Database in Heroku|
  |   4    |When setting up Stripe under a new email for some reason stripe was connecting to Boutique Ado|I fixed this by going back to the old Stripe Account.|
  |   5    |I was getting a 404 error when deploying Stripes webhook | I fixed this by making sure stripes .env details were correct in local and Heroku. |
  |   6    |I was unable to deploy or migrate for a while. | I saw on slack whenever this happens I need to use unset PGHOSTADDR and unset DATABASE_URL |
  |   7    |I was unable to get my fixtures to update to Heroku  | I fixed this by export DATABASE_URL="{postgress url}" |
  |   8    |I was unable to view the header when building  | I fixed this by changing the headers name |
  |   9    |I was unable to view any of the images on the index page  | I fixed this by asking tutor support. They told me to change the src="relative path" to {{ static img/image.png }} and it worked|
  |   10    |I was un-happy with how much space the delivery banner took up  | I fixed this by adding in javascript to hide the element when scrolling down the page| 
|   11    |When sending webhooks I was getting 400 errors  | I fixed this by making sure my server was running publicly | 
## Deployment

The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding. 
Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it 
functioned correctly or easily find lost pieces of code. 

### To deploy the project to Github the following steps were taken:

  1. created a `master` branch in Github repository 
  2. Used Local AWS Cloud9 and Gitpod environment used to build the site
  3. Committed files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m"add message"`
  4. Pushed files to the working environment using `git push`, which then updates the repository.
  5. Published site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`
  6. The repository can be cloned by clicking `Clone or Download` on the main page of the repository 
  7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
  8. Open Git Bash Terminal
  9. Type `git clone`, and then paste the URL
  10. Press `Enter`. A local clone will be created.

### To set gitignore environment variables the following steps were taken: 

  1. Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
  2. If you don't have one already, create a file named .gitignore  in the root directory of your project.
  3. Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text: env.py
  4. At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” 
     underneath you can assign your environment variables using the following syntax:  
     `os.environ["Variable Name Here"] = "Value of Variable Goes Here"`
  5. Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project. Add this under your 
     other imports at the top of the file  
     `from os import path`
      `if path.exists("env.py"):`
      `import env` 
  6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed, for example using the following syntax:  
     `DATABASES = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}`

### To deploy the project to Heroku the following steps were taken:

  1. created a Heroku account @ https://signup.heroku.com/
  2. Create `requirements.txt` file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type 
     `pip3 freeze --local > requirements.txt`.
  3. To install the Heroku command line on Gitpod, use the following command `npm install -g heroku`
  4. Using the `New` buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us 
     to push our changes using Git to update the application at any given time. 
  5. To login to Heroku from the CLI, use the command `heroku login`
  6. To get the application up and running a `Procfile` is required that istructs Heroku which file is the entry point. Use the following command to create this: 
     `echo web: python app.py`
  7. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands:
     `git add .`
     `git commit -m "fist Heroku commit"`
     `git push`
  8. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
  9. To connect an existing repository from Github to Heroku use the following CLI syntax: `heroku git:remote -a [followed by name of Heroku app]`
  10. To push to Heroku Master Branch, then simply use `git push heroku master`
  11. To scale dynos and run the app in Heroku, use the CLI command: `heroku ps:scale web=1`
  12. In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku. To do this go to `Settings` 
      tab > `Config Variables` and input: `AWS_ACCESS_KEY_ID`; `AWS_SECRET_ACCESS_KEY`; `DATABASE_URL`; `DISABLE_COLLECTSTATIC`; `EMAIL_ADDRESS`; `EMAIL_PASSWORD`
      `EMAIL_PASSWORD`; `SECRET_KEY`; `STRIPE_PUBLISHABLE`; `STRIPE_SECRET`.  
  13. The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
  14. The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands `mmakemigrations` and `migrate` from the command line.      
  15. Once the build in Heroku is complete, click the `Open app` button.
  16. Objects can then be added to the new postgres database using the Admin Panel and logging in with your superuser credentials.  

## Credits 

### Content

This README.md file is based on the Code Institute template.

### Media 

All images and logo's utilised have been displayed with the permisson of Blindside-Brewing.


### Acknowledgments

I would like to thank all of the Code Insitute Tutors for their incredible patients and assistance and my mentor Aaron S, for his wonderful feedback, as a supervisor for this project and other projects prior. Truly a year ago from today, I had no clue I could even learn all of these things; but thanks to everyone here I have such a bigger grasp on website development. 


{"mode":"full","isActive":false}