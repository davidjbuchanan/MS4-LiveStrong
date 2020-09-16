# [Live Strong](https://lockdown-data-centric.herokuapp.com/)

<img src="https://github.com/davidjbuchanan/lockdownagain/blob/master/static/images/mockups/Lockdown-Multi-Device-Website-Mockup.png" alt="lockdown multidevice views" width="100%">

Whilst we are enduring Covid-10 let us look after ourselves and our loved ones with this helpful app! [Lockdown and Thrive](https://lockdown-data-centric.herokuapp.com/) is a place to find simple recipes; find ways to entertain younger ones and how to look after oneselves mental wellbeing. You can access the resources and contribute any number of resources to share with the world! 

This website was produced to fulfill a coursework assignment for the [Code Institute's](https://codeinstitute.net/) **Full Stack Frameworks with Django Milestone Project**. The objective for this milestone project is to "*Create a full-stack site based around business logic used to control a centrally-owned dataset. It must consist of multiple apps including an authentication mechanism. Also it must provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.web application with multiple apps*".

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)
    - [**User Testing**](#User-testing)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

The website focuses on the workout-at-home market as it is an attractive approach to health and fitness whilst managing Covid-19 restrictions. The UX design is intended to draw users in using a well defined color scheme that is enjoyably interacive. On each page there is a navigation and search jumbotron placed to enable swift access around the site. Additional features applied include the use of javascript for mouseeneter and mouseleave events enabling users to gain feedback and indications of the site's products.

The overall theme of the design is clean straight edges with block elements in order to give a utilitarian vibe whilst the black and red color scheme is intended to make the site feel sporty and sexy. Remiscent of the inspirations for this design (see onepeleton and Les Mills) use of imagery is primarily for motivational and explannatory puposes whereby potential consumers understand that they are subscribing to an online service whereby they can login and access televised workout classes.

The commercial potential for this idea is vast and so the up-to-purchase UX of this site's products has been refined to make the process as simple as possible. Users are able to browse, add to cart, apply coupons and finalise purchases all within an authenticated user. They can also make purchases as a guest. 

minimal with a link to a 'store' (which is under construction) but has been included to indicate that the site could be used commercially. Similarly the home page's 'call-out' is primarily to enable users to subscribe to the site's **CRUD** operations, this could also be commercialised to enable a subscription fee to be collected.

The vision for this site is to have three consummables (equipment, services and blog) The equipment and services are grouped together as products, that derive cash income, and can be managed and consumed using the products, bag and checkout apps. The blog is a loss-leader that derives no income it is used a s a 'hook' to entice users to register and create a profile thus allowing them access to the blog and, of course, paid for products.

The products themselves are represented within a fully searchable products app, allowing the user rapid access to information. The tangible products, i.e. equipment, are deliverable and there is a shipping functionality that is self explannatory. For the services there is no demonstration of the product; nor access to the product; nor explannations as to how a consumer would access the product after purchase.
There are several placeholder for undeveloped features. It was important to partition these topics clearly for ease of use. To acheive this the navbar displayed each of these topics in its own discrete, but essentially identical, dropdown menus. Likewise the homepage's body presents three uniform rows, one for each topic. 

Each page displays an identical navbar, masthead (with search functionality) and footer this was deliberate to aid users' navigation of the site. The navbar is elaborated for smaller viewports. 

### User Stories

Who is the user? Essentially this could be anyone wanting to participate in group exercise at home, via the internet. 

"**_As a guest / non authenticated user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *register* to become an **authenticated user**.
- :white_check_mark: *view* all **products and services**
    - :white_check_mark: *search products and services* by **product name**.
    - :white_check_mark: *search products and services* by by **partial product name**.
    - :white_check_mark: *search products and services* by by **product description**.
- :white_check_mark: *add* a **discount coupon**.
- :white_check_mark: *edit* a **bag content**.
- :white_check_mark: *delete* a **bag content**.
- :white_check_mark: *purchase* any **product(s) and service(s)**.


"**_As an authenticated user, I would like the additional priviledge to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *generate* a **user profile**.
- :white_check_mark: *view* all **published blogs**
- :white_check_mark: *post comments* on **published blogs**


"**_As a staff user, I would like the additional priviledge to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *author* a **draft blog entry**


### Design

A modern Bootstrap landing page design (https://startbootstrap.com/themes/landing-page/)  was chosen for this site that had a contemporary navbar and masthead that persisted on all web pages. The masthead contained a jumbotron with product/service searchbar for the user's convenience. 

Inspired by the Boutique Ado, Les Mills and One Peleton websites the use of full viewport width imagery was employed for visual impact. For the landing, products and purchasing pages the rendered pages were split into three vertical sections : 1) A uniform navbar and masthead with search facility; 2) the body / page specific content; and 3) a uniform footer.  


#### Framework

- [Bootstrap Grid v4.4.1](https://getbootstrap.com/)
    - 
- [jQuery 3.5.1](https://code.jquery.com/jquery/)
    - To keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Django 3.0.8](https://www.djangoproject.com/download/)
    - Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap. 
#### Color Scheme

In keeping with the overall *simple/clean* theme, I have opted for a muted color scheme. 
  
- ![#ffffff](https://placehold.it/15/ffffff/ffffff) `#ffffff` **white** - field input box background; icons grid background; borders; button text / icon
- ![#000000](https://placehold.it/15/000000/000000) `#000000` **black** - navbar blackground; button background; footer blackground; and text
- ![#ff0000](https://placehold.it/15/ff0000/ff0000) `#ff0000` **red** - Fontawesome icons (navbar, icons grid), borders (on hover)
- ![#f8f9fa](https://placehold.it/15/f8f9fa/f8f9fa) `#f8f9fa` **off-white** - showreal background


#### Icons

- **Social Links, Navbar Links, Icons Grid Links** : [Font Awesome Icons](https://fontawesome.com/icons?d=gallery)

#### Typography

- [Google Fonts](https://fonts.google.com/)
- [Lato](https://fonts.google.com/specimen/Lato)

### Wireframes

[Lucid Chart](https://www.lucidchart.com/pages/) have been used due to their eases of use:

The index page was designed to show 3 main sections. On top a callout/searchbar superimposed upon a background image; in the middle an icon grid to allow user likns to products and services; and in the lower part a showreel. The lower, features, section is disproportionately larger due to the desire to advertise the full range of the business' services. As you can see as the viewport narrows the detail and number of features is reduced:

<img src="https://github.com/davidjbuchanan/lockdownagain/blob/master/static/images/mockups/Lockdown_Data_Centric_Development_Project_Index_page.png" alt="lockdown index page views" width="100%">

The page most populated with elements is for the products' page. This required a simple clear display that was responsive as the width of the viewport decreases; this was resolved by stacking the elements. 

<img src="https://github.com/davidjbuchanan/lockdownagain/blob/master/static/images/mockups/Lockdown_Data_Centric_Development_Project_add_recipe_page.png" alt="lockdown add recipe page views" width="100%">

The complete set of wireframes for this project can be found [here](https://github.com/davidjbuchanan/lockdownagain/blob/master/static/images/mockups) in the *mockups* sub-directory.

##### back to [top](#table-of-contents)

---

## Features

### Existing Features

#### Home App

**Dashboard page**
- Page presents a full overview of the site's content enabling rapid movement around site by use of the ample links and a search bar.

#### Products App

**Search the database**
- If a user would like to search for a particular category of class or item of equipment they can use the search bar (on the Masthead of each page) to search by name, category or by word in the products description. This results in the display of a refinned 'Products' page to the user.
-Alternatively users can use the built-in filters on the navbar's product dropdown menu to access equipment or classes as categorised by exercise tupe e.g. yoga, running etc.
- A third option is found exclusively on the landing page's Icons Grid section where there are some interactive buttons to access the equipment, classes and blog.

**View all essential equipment (also referred to as 'essentials')**         
- This is a C**R**UD feature:
- on the filtered *products* page, all equipment are displayed with a photo, name and price. These products can be explored further on clicking their image or name; the user is taken to a details page where they can add the item to their e-commerce basket.

**View all classes**
- This is a C**R**UD feature:
- on the filtered *classes* page, all equipment are displayed with a photo, name and price. These products can be explored further on clicking their image or name; the user is taken to a details page where they can add the item to their e-commerce basket.

**Search the database**
- If a user would like to search for a particular category of class or item of equipment they can use the search bar (on the Masthead of each page) to search by name, category or by word in the products description. This results in the display of a filtered 'Products' page to the user.

**Add a product to the database**
- This is a **C**RUD feature:
- From the navbar option *Product Management* there is a form to complete that allows the addition of a product with category, rating, image, price and description.
- only the authenticated superuser can access this app feature

**Update a product from the database**
- This is a CR**U**D feature:
- From any filtered / unfiltered *Products" page or *Product Description* page there is an edit link. From there a form is rendered allowing the user to update the product's category, rating, image, price and / or description.
- only the authenticated superuser can access this app feature

**Delete a product from the database**
- This is a CRU**D** feature:
- From any filtered / unfiltered *Products" page or *Product Description* page there is a delete link. On-clicking this link the product will be immediately deleted.
- only the authenticated superuser can access this app feature


#### Checkout App
- This is a C**R**UD and a **C**RUD feature:
- Using the checkout app the user, if authenticated with a user profile, can review the database record for billing and shipping address and review prospective purchases. 
- If no profile exists for the user then they can create a billing and shipping address whilst reviewing prospective purchases


#### Profile App
**Create a user's profile**
- This is a **C**RUD and CR**U**D feature:
- A user can use a form to input or update their details; thus saving their shipping and billing details. This allows for a better UX during the checkout process.
- only authenticated users can access this app feature


**Read user's purchase history**
 This is a C**R**UD feature:
 - This allows a user to review their purchase history along side their saved (but editable) billing and shipping address.
 - only authenticated users can access this app feature


#### Authentication App
- This is a **C**RUD feature:
- Uses the allauth https://django-allauth.readthedocs.io/en/latest/installation.html
- Allows user's to register and access profile and blog services.





#### Bag App
**View all items in user's bag**
- This is a C**R**UD feature:
- All discrete product items are described in rows: the no. of units, cost per unit and sub total per product item line is detailed. The grand total is calculated as the sum total of all sub totals. 

**Edit the bag's contents**
- This is a CR**U**D and CRU**D** feature:
- The no. of units can be edited in three ways: increment, decrement and delete. All other dependent fields will update automatically

#### Coupon App
- This is a CR**U**D feature:
- A coupon code can be added in the *bag page*. If valid (vaidated by time, date and status i.e. 'active') a discount is applied, this is reflected in the user's total. The coupon code (and resultant discount) is held within the contexts processor and any subsequent addition of products to the bag will have the validated discount applied. The navbar 'shopping bag' icon shows a running total beneath it. This reflects any discounts applied. The coupon code is discarded at the end of the session for security purposes. 
- Although the model for the coupon system resides in the coupon app, it is the bag app and checkout app that utilise the actual model, i.e. it is in their views.py and contexts.py (Bag app only) that the coupon logic and coupon GUI is manifested.




#### Blog App

**View the blog list**
- This is a C**R**UD feature:
- on the *blog list* page, all blog entries are displayed with a heading, datestamp, author and partial text. The full text can be accessed and read on the *blog detail* page once clicking the blog title.
- only authenticated users can access this app feature

**Comment on a blog post**
- This is a **C**RUD feature:
- on the *blog detail* page, a user can comment on a blog post leaving email namr and comment details. This will be appended beneath the blog post in the *blog detail* page.
- only authenticated staff users can access this app feature

**Draft a blog post**
- This is a **C**RUD feature:
- Using the navbar a user can navigate to an *add blog* page, which is a form, there they can author a post which will be held in draft until published by a superuser.
- only the authenticated superuser can access this app feature

**Pagination**
- To maintane a positive UX the blog list is limited to xxxxxxxxxxxx blog posts per page.



**Use of a hosting site**
- The use of a 3rd party image hosting site (e.g. Cloudinary and Amazon S3) would allow users to upload their own images rather than relying existing web images.


### Features Left to Implement



**Content Elaboration**
- Of the other two other main topics (Play & Learn and Rest & Relax) and the store page to add a commercial element.

**Confirmation modals**
- An essential addition for inadvertant deletion of records


**Elaboration of search facility**
- User feedback in the event of 'no results found' required and more sophisticated Python code required to deal remove case sensitivity in user's input.

##### back to [top](#table-of-contents)

## Technologies Used

- [Gitpod](https://www.gitpod.io/) - Used as my primary IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of code online.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery 3.5.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Bootstrap Grid v4.4.1](https://getbootstrap.com/) - Used as the overall design framework.
- [stripe 2.49.0](https://stripe.com/en-gb) - Python library for Stripe’s API.

### Back-End Technologies

- **Django**
    - [Django 3.0.8](https://www.djangoproject.com/download/) - .
    - [django-allauth 0.42.0]() - .
    - [requests-oauthlib 1.3.0]() - .
    - [django-crispy-forms 1.9.2]() - .
    

- **AWS**
    - [boto3 1.14.58](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3. Boto provides an easy to use, object-oriented API, as well as low-level access to AWS services.
    - [django-storages 1.10](https://django-storages.readthedocs.io/en/latest/) - django-storages is a collection of custom storage backends for Django.
    


- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
    - [Heroku Postgress](https://www.heroku.com/postgres) - Used as relational SQL database plugin via Heroku.
    - [dj-database-url	0.5.0](https://pypi.org/project/dj-database-url/) - Utilizes the 12factor inspired DATABASE_URL environment variable to configure Django apps. I.e. Enables the connection to the Postgress remote database.
    - [Green Unicorn (gunicorn) 20.0.4](): A web browser for deployed browsing.
    - [psycopg2-binary 2.8.6](https://pypi.org/project/psycopg2-binary/) - Python-PostgreSQL Database Adapter. Postgres is a server-based database that runs remotely from the Django app.
        - Note: Django's db.sqlite3 is fine for local development but is not robust for long term storage of data as it is ephemeral.


- **Python**    
    - [Python 3.8.3](https://www.python.org/) - Used as the back-end programming language.
    - [pytz 2020.1]() - Brings the Olson tz database into Python.
    - [sqlparse 0.3.1]() - Non-validating SQL parser.
    - [Pillow 7.2.0](https://pillow.readthedocs.io/en/5.1.x/handbook/index.html) - Adds support for opening, manipulating, and saving many different image file formats.
    - [oauthlib 3.1.0](https://github.com/oauthlib/oauthlib/blob/master/README.rst) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
    - [python3-openid 3.2.0](https://pypi.org/project/python3-openid/) - his is a set of Python packages to support use of the OpenID decentralized identity system in an application.
    - [asgiref 3.2.10](https://github.com/django/asgiref) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.


##### back to [top](#table-of-contents)
---

# Testing

:white_check_mark: *denotes items that have been successfully implemented*

**Basic navigation**
- :white_check_mark: Links tested on navbar (& navbar toggle button) and footer
- :white_check_mark: Footer's Social icons openning to link in a new webpage
- :white_check_mark: Links tested on icons grid
- :white_check_mark: Links tested on 'under construction page'
- :white_check_mark: Alert dismiss
- :white_check_mark: Blog post links navigate to blog post detail page
- :white_check_mark: Blog post list page pagination links toggle back and forth between pages


**Search page / functionality:**
- :white_check_mark: Search bar tested on Masthead (product name, product category, product detail content)
    

**Responsiveness** 
Tested on portrait and landscape viewport for the following viewports
- :white_check_mark: Apple iPad pro
- :white_check_mark: Apple iPad
- :white_check_mark: Apple iPhone 5/SE/6/7/8/X/6 plus/7 plus/8 plus
    
Note: when tested on actual iPhone 6 the background-attachment: fixed was not compatible with iOS - browsers. On Chrome and Safari in iOS, the background photos appeared zoomed-in and blurry. To fix this, the .background-attachment: scroll property - value was added in a media query.
    
- :white_check_mark:Samsung Galaxy S5
- :white_check_mark:Pixel 2/2 XL

Responsiveness tested on landscape viewport for the following viewports
- :white_check_mark: Microsoft Surface 2 laptop  (1504 x 892 px)
- :white_check_mark: Dell XPS laptop (13.4 inch, 1920 x 1080 px)
- :white_check_mark: Desktop (1680 x 939 px)
- :white_check_mark: iMac 27 inch (5120 X 2880 px)

**Registration form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**

**Login form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**

**Logout form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**

**Password Reset form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**

**Add draft blog form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**

**Add comment (to blog post) form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**


**Add product form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**

**edit product form validation**
- **Required input fields include:**
    - :white_check_mark: Full name
    - :white_check_mark: Occupation
    - :white_check_mark: Phone number
    - :white_check_mark: Email address: input field requires an '@' character
- **:white_check_mark: On successful completion of the form the user is presented by a 'flash' feedback banner**


**Add category page / functionality:**
    - :white_check_mark: add categories and render to 'all categories' page


### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) 
    - All code is perfectly validating. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - I am using `:root{}` variables in my CSS, which isn't recognized by the validator. This is causing several **Parsing Errors**, when in fact they are not errors, and work perfectly fine.
- **Property Errors**
    -   *abbr[data-original-title], abbr[title]* - Property text-decoration-skip-ink doesn't exist : none
    -   *.toast* - Property backdrop-filter doesn't exist : blur(10px) 
- These errors incurred no impact on the rendered pages and were therefore ignored.

**JavaScript**
- [JShint](https://jshint.com/)
    - "There are **11** functions in this file.
    Function with the largest signature take **1** arguments, while the median is **0**.
    Largest function has **21** statements in it, while the median is **2**.
    The most complex function has a cyclomatic complexity value of **2** while the median is **1**."
    One undefined variables:
        - `$` (12 times - this is for jQuery)
        - line 155	'validation' is defined but never used.
- [JSesprima](http://esprima.org/demo/validate.html)
    - "Code is syntactically valid."
- [Beautify Tools](http://beautifytools.com/javascript-validator.php)
    - line 155	'validation' is defined but never used.

**Python**
- [PEP8 Online](http://pep8online.com/)
    -  E402 errors (module level import not at top of file) did not impact the functionality of the app. They were left in place due to the app comprising a single py file and listing the imports at the top seemed tidy.  
        -   line 4, from flask_pymongo import PyMongo
        -   line 5, from bson.objectid import ObjectId
        -   line 6, from datetime import datetime
        -   line 7, from os import path
Other than the list above the app.py file was PEP8 compliant

### Compatibility
- :white_check_mark: Microsoft Edge (version ):  Images within cards were found to be distorted on initial tsting, i.e. not in width but in height, where the height reverted to that of the original image. To rectify the distortion a .d-block class was added to the parent div i.e. div class="card d-block h-100 shadow". Credit jeroendesloovere @ https://github.com/twbs/bootstrap/issues/21885. 
- :white_check_mark: Mozilla (Version xxxxxxxxxxxxxxx76.0.1):
- :white_check_mark: Safari (Version xxxxxxxxxxxxxxxx14):
- :white_check_mark: Microsoft Edge (Version xxxxxxxxxxxxxxxx44.18362.449.0):
- :white_check_mark: Google Chrome (Version xxxxxxxxxxxxxxx81.0.4044.138):

### Known Issues

During development, I discovered two issues after committing to GitHub. 

- **Flaw with cross-site resources for images and icons**
    - http://fontawesome.com cookie is set with sameSite attribute.
    - Images from http://itv.com and http://bbcgoodfood.com have cookies set with sameSite attribute.
- **404 error**
    - DevTools failed to load SourceMap: Could not load content for chrome-extension://dodmmooeoklaejobgleioelladacbeki/dist/gitpodify.bundle.js.map.

### User-testing
- Testing to select group of targeted users and a development professional highlighted these 5 points:
    -   Alert text was not vertically centered. This was rectified
    -   The 'subsrcibe' link on the navbar was identified as potentially premature and that a "give away" should be offered to the user prior promotion of a subscription servive.
    -   Images uploaded by user's should be hamdled ny a third party in order to give the user greater autonomy over the image used and not reliant on web available images.
    - Edit buttons allowing addition and deletion of fields in the 'add recipe' and 'edit recipe' should be "more available" to the user i.e. at the bottom or side of a growing list.
    - The footer is not at the bottom of the page which some test users highlighted but did not seem bothered about.


##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

- Some basic requirments for the deployment include:
    - [Python3](https://www.python.org/downloads) to run the application.
    - [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
    - An IDE such as [Gitpod](https://www.gitpod.io/) or [Microsoft Visual Studio Code](https://code.visualstudio.com).
    - [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.

Now, there is a series of steps to take in order to proceed with local deployment:

- Here are three options for downloading this repo to your IDE: 
    - 1) If you have added the Chrome/Firefox Gitpod extension you can clone by clicking the green *Gitpod* button at the top right of this repo. to open a workspace within the Gitpod IDE; 
    - 2) download the project as a zip-file (remember to unzip it first); 
    - and 3) by entering the following into the Git cli terminal: `git clone https://github.com/davidjbuchanan/lockdownagain.git'.
    - Note: when using Gitpod IDE it may be advantageous to goto the Code Instute's Github page and clone their [template](https://github.com/Code-Institute-Org/gitpod-full-template). This will give the developer admin rights 
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- the `requirements.txt` will list the required packages required to successfully launch the site for local and remote deployment; the list should look like the following: 
```
asgiref==3.2.10
boto3==1.14.58
botocore==1.17.58
dj-database-url==0.5.0
Django==3.0.8
django-allauth==0.42.0
django-crispy-forms==1.9.2
django-storages==1.10
docutils==0.15.2
gunicorn==20.0.4
jmespath==0.10.0
oauthlib==3.1.0
Pillow==7.2.0
psycopg2-binary==2.8.6
python3-openid==3.2.0
pytz==2020.1
requests-oauthlib==1.3.0
s3transfer==0.3.3
sqlparse==0.3.1
stripe==2.49.0
```
To install these packages onto your IDE'S workspace you can enter the following command in the IDE's cli: `pip3 install -r requirements.txt` 
    
- Set up your development app. with the following two configuration variables:
    - **SECRET_KEY** : `<typically a lower case alpha numeric code with symbols>`
    - **DEVELOPMENT** : `1`
    - Here are two options for storing these:
        - 1) Create an `env.py` file. It should look something like this:
                ```
                import os

                os.environ['SECRET_KEY'] = '<lower case alpha numeric with symbols>'
                os.environ['DEVELOPMENT'] = '1'
                
                ```   
        - 2) Using Gitpod's IDE place the config. vars. in **Settings** using the settings option from the drop-down menu.
        - Note: It is important that these do not get uploaded during a Github commit/push and that they do not appear in your repository for security reasons

- Make migrations using the following command in the IDE's cli: `python3 manage.py migrate`    

- The site should now render, on the development server, using the following command in the IDE's cli: `python3 manage.py runserver`
    - However there will be no products rendered to the site and the checkout app will error if openned.

- To add products you will need to define product categories as well as products themselves.
    - Create them using the examples in products/fixtures/categories.json and products.json files from the repo. Input the details relevant to your business and thenpload the products and categories to the db.sglite3 database using cli commands `python3 manage.py loaddata categories` then `python3 manage.py loaddata products`. Alternatively you could add them all individually through the django admin app.

- Set up a payment system through [Stripe](https://github.com/Code-Institute-Org/gitpod-full-template) and obtain values for the following config. vars.:
    - **STRIPE_PUBLIC_KEY** : `<upper and lowercase alphanumeric with symbols>`
    - **STRIPE_SECRET_KEY** : `<upper and lowercase alphanumeric with symbols>`
    - Add these to your Gitpod **Settings** or put them in `env.py`. If you choose the latter it should now look something like this:
    ```
    import os

    os.environ['SECRET_KEY'] = '<lower case alpha numeric with symbols>'
    os.environ['DEVELOPMENT'] = '1'
    os.environ['STRIPE_PUBLIC_KEY'] = '<upper and lowercase alphanumeric with symbols>'
    os.environ['STRIPE_SECRET_KEY'] = '<upper and lowercase alphanumeric with symbols>'
    ``` 
    - you can get the values for these from your Stripe account. Goto the 'Developers' section and look on 'API keys'. Alternatively get them from wherever you stored them for local deployment as they are the same keys.

- With this all in place the app should render and accept payments. 
    - `python3 manage.py runserver`. This may require a prefix of `sudo` if you do not have administration rights on your IDE.
    - The app should now be running on *localhost* and, when using Gitpod IDE, render an address similar to `https://8080-bce9ad25-9922-4648-b249-d83204aa0bf4.ws-eu01.gitpod.io/`.
    - All emails (e.g. authentications, transaction details) will now be sent to the development terminal.




### Remote Deployment

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku,the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `pip3 freeze --local > requirements.txt` add a `sudo` prefix if you do not have admin. rights to your IDE
    - My file can be found [here](https://github.com/davidjbuchanan/lockdownagain/blob/master/requirements.txt).

4. Sign up for a free Github account and create your project repository. From your IDE commit and push to your Github repository.
4. Sign up for a free Heroku account and create your project app.
    - Once done, use the *'resource'* tab to search for an add-on called *Heroku Postgress*
        - Note: Django's db.sqlite3 is fine for local development but is not robust for long term storage of data as it is ephemeral.
    - Install dj-database-url and psycopg2-binary and then add them to the requirements.txt file if not already done.
    - Now you need to replicate the steps performed for the setup of the db.sqlite3 development server but now for the Postgress server: Establish a link to the external database; make migrations; upload products to the db; and setup superuser access on Postgress db. 
        - Step 1) update databases section in setings.py by commenting out the if/else block and adding the unique URL found in Heroku under a config. vars. where it says *ENTER_URL_HERE* below:
        ```
        # if 'DATABASE_URL' in os.environ:
        #     DATABASES = {
        #         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        #     }
        # else:
        #     DATABASES = {
        #         'default': {
        #             'ENGINE': 'django.db.backends.sqlite3',
        #             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #         }
        #     }
        
        DATABASES = {
            'default': dj_database_url.parse('ENTER_URL_HERE')
        }
        # Note: there is a security issue with the potential divulging of config. vars. on Github so this change to code should be reverted prior to commiting. 
        ```
        - Step 2) Make migrations using `python3 manage.py migrate`
        - Step 3) Within the products/fixtures/categories.json and products.json files input the details relevant to your business. Upload the products and categories to the Postgress db using cli commands `python3 manage.py loaddata categories` then `python3 manage.py loaddata products`. 
        - Step 4) Setup a superuser using `python3 manage.py createsuperuser`
        - Step 5) Install gunicorn and add it to the requirements.txt file if not already done.
        - Step 6) Create a **Procfile** to tell Heroku what type of application is being deployed. This will create a web dyno which will run unicorn and serve our django app.
            - My file can be found [here](https://github.com/davidjbuchanan/lockdownagain/blob/master/Procfile).
        - Step 7) Disable collect static using `heroku config:set DISABLE_COLLECTSTATIC=1 --app live-strong`, this can be done after logging into Heroku on the cli, i.e. using the command `heroku login -i`. Note: The static files will be used for development purposes but we will use a cloud based system for the deployed site. 
            
        - Step 8) In settings.py update `ALLOWED_HOSTS = ['live-strong.herokuapp.com', 'localhost']` to reflect the name of your app if different
        - Step 9) Set up a git remote link from your IDE if you haven't already i.e. `heroku git:remote -a live-strong` or set automatic deploys from Github using the deploy tab in Heroku's GUI.
            - This allows you to push the code from your IDE to Heroku via Github. In Heroku click the **Deploy** tab, at which point you can *Connect GitHub* as the *Deployment Method*, and select *Enable Automatic Deployment*.
        - Step 10) Set a SECRET_KEY in the Heroku cofig. vars. and Gitpod config. vars. (or use an env.py in .gitignore file) that secures the app as per code in settings.py: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
        
        more development setup than deployment    - Step 11) Found that altering : `DEBUG = True` to `DEBUG = 'DEVELOPMENT' in os.environ` resulted in the development server being unable to access static files. The cli command `export DEVELOPMENT="1"` updates the terminal and allows the development server to render the site as intended; the drawbacks to this method are that this is a temporary fix and won't extend to a new workspace: A permanent solution, in Gitpod, was to add to 'Setttings': name = DEVELOPMENT and value = "1".  

At this point you should be able to inititiate a *Build* on Heroku by performing a 'git push' on your IDE's cli as this 'push' will go through to Heroku. The rendered Heroku app will contain HTML content but none of the static content; that comes from the AWS systems that have yet to be set-up.


5. Setup an AWS account.
    - Access S3 (safe storage services) for the purposes of storing our static files in the S3 cloud-based storage system.
        - create a bucket.
    - Access IAM (Identity and Access Management) for the purposes of creating users capable of accessing the bucket for management purposes.
        - create a group with an access policy attached to it that allows full (public) s3 access to the bucket.
        - create a user that's part of the group and who has their own special access keys.
            - Obtain an *Access key ID* and *Secret access key* 


6. Configure Django to connect to s3 using the IAM keys and upload static files to s3.
    - Install boto3 and django-storages and add them to the requirements.txt file if not already done.
    - Update the app's config. vars. on Heroku to sinc with the settings.py code snippets below:
        - So for `if 'USE_AWS' in os.environ:` set a config variable of *USE_AWS* with a value of *True*;
        - for `AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')` set a config variable of *AWS_ACCESS_KEY_ID* with a value of the *Access key ID* generated from IAM;
        - and for `AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')`set a config variable of *AWS_ACCESS_KEY_ID* with a value of the *Secret access key* from IAM
    - the *DISABLE_COLLECTSTATIC* config. var. with a value of *1* can now be deleted as the site should now pull the static files from the Github repo. through to the AWS bucket.

At this point you should be able to inititiate a *Build* on Heroku by performing a 'git push' on your IDE's cli as this 'push' will go through to Heroku. The rendered Heroku app will contain HTML, CSS and JQuery content but none of the media content; that comes from further addition to the AWS bucket.
7. we want to use s3 to store our media files too:
    - Access the S3 bucket, create a folder and call it 'media'.
    - Select the desired photos with filenames corresponding to those in the CSS.
    - Grant public read access to these files.
    - Upload files

At this point you should be able to inititiate a *Build* on Heroku by performing a 'git push' on your IDE's cli as this 'push' will go through to Heroku. The rendered Heroku app will contain HTML, CSS, JQuery and media content.

8. Verify superuser 
    - open the heroku app and goto the /admin url
    - goto *accounts* and click on your address (the one you entered when you created the superuser from your IDE's cli) and clich *Primary* and *Verified*.

At this point you should be able to login to the app website and have full superuser access.

9. Add Stripe keys to the config vars section in your Heroku app. Goto the 'settings' tab and add:
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - you can get the values for these from your Stripe account. Goto the 'Developers' section and look on 'API keys'. Alternatively get them from wherever you stored them for local deployment as they are the same keys.

10. Add a Stripe webhook endpoint and generate a Signing secret for the Heroku deployed site. Remember previous webhooks would have been for the local site only.
    - Goto the 'Developers' section:
        - Click 'Webhooks' then 'Add endpoint'
        - Enter Endpoint URL: e.g. 'https://live-strong.herokuapp.com/checkout/wh/'
        - Select 'receive all events' and then click 'Add Endpoint'
        - collect the 'Signing secret' and add it to the config. vars. (as you did previously in the section above) under a name of STRIPE_WH_SECRET. Note: this will be a different key to the one used in the local site.

The site is now deployed and anyone on the internet can browse products, create a profile, and even check out using a test credit card number.
If a user makes a purchase there order is created in the django admin. And if they authenticate their login their order will be attached to their profile and displayed in their order history.

11. Linking emails to site using Gmail:
    - Goto 'settings'; then 'Accounts and Imports'; then 'Other Google Accounts Settings'; and then 'security' to access the security page:
        - Then go into 2-step verification and complete the steps. Once complete return to the security page.
        - Then go into App passwords and from the 2 dropdown menus 'select app' 'select device' choose *mail* and *other* and call it Django.
            - obtain a 16 digit code
    - Go to the Heroku app's settings and generate two new config. vars.
        - EMAIL_HOST_PASS
        - EMAIL_HOST_USER
        - the values for these will be the 16 digit code and the Gmail email address used to set up the verification.

Once all that is done you need to run a commit on your IDE and force a build on Heroku; then the updated app will be able to send real emails. 

        
so to recap in the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
- **AWS_ACCESS_KEY_ID** : `<capitalised alphanumeric>`
- **AWS_SECRET_ACCESS_KEY** : `<upper and lowercase alphanumeric with symbols>` 
- **DATABASE_URL** : starts `postgress://` then `<alphanumeric>` 
- **EMAIL_HOST_PASS** : `<lowercase alphanumeric>` 
- **EMAIL_HOST_USER** : `<the Gmail address>` 
- **SECRET_KEY** : `<lower case alpha numeric with symbols>` 
- **STRIPE_PUBLIC_KEY** : `<upper and lowercase alphanumeric with symbols>` 
- **STRIPE_SECRET_KEY** : `<upper and lowercase alphanumeric with symbols>` 
- **STRIPE_WH_SECRET** : `<upper and lowercase alphanumeric with symbols>` 
- **USE_AWS** : `true`



7. Your app should be successfully deployed to Heroku at this point.

##### back to [top](#table-of-contents)








The app building process:
Signed up for Github and Gitpod.

Went to Code Institute's (CI) Gitpod template [repo.](https://github.com/Code-Institute-Org/gitpod-full-template) and clicked *Use this template*. The new repo. was named and openned in Gitpod, straight from Github.

followed the https://github.com/davidjbuchanan/boutique_ado_v1/blob/master/instructions.txt

at line 25 put SECRET_KEY into the github settings and created an any var before initial commit







The deployment process:

To deploy the app remotely the additional list of add-ons and code are required:

Signed up for a free Heroku accounts

Postgres: A server-based database that runs remotely from the Django app. Note: Django's db.sqlite3 is fine for local development but is not robust for long term storage of data. To install Postgres use `pip3 install psycopg2-binary` from the Git CLI.
dj-database-url: Enables the connection to the Postgress remote database. To install use `pip3 install dj_database_url` from the Git CLI.
Green Unicorn (gunicorn): A web browser for deployed browsing. To install Green Unicorn use `pip3 install gunicorn` from the Git CLI.

Generation of a requirements file for the purposes of informing Heroku which files to install using pip. Migration of installed files accomplished using `pip3 freeze --local > requirements.txt` from the Git CLI.

Generation of a Procfile file for the purposes of informing Heroku that this is to be a web application with a web server called Green Unicorn.
Generate from the Git CLI using `touch Procfile`.
Input `web: gunicorn boutique_ado.wsgi:application` to make Horoku start a web dyno (Note: wsgi allows the handling of HTTP requests like run server does in our local development environment.)

From the CI template it is possible to access the Heroku CLI from the Git CLI (otherwise installation is required from [Heroku]( https://devcenter.heroku.com/articles/heroku-cli)). Using the Heroku CLI you can login using `heroku login`. 

Once authenticated it is necessary to create an app in Heroku too:
Using the CLI enter `heroku apps:create` followed by the app's name and region of creation e.g. `heroku apps:create name --region eu` or region otherwise dependant on your location. 

From the Heroku GUI goto the app; then the resources tab, and then the add-ons input field. From there add Postgress. 

To link the Postgress database in Heroku to the Django app requires an update to the settings.py file with the relevant path information ([see example of settings.py]()): 
1) `Import dj_database_url`
2) Obtain the DATABASE_URL (From the Heroku GUI or CLI using `heroku config`) and save it as an environment variable. CAUTION: see deployment security section below.
3) Add to the existing Database section in settings.py to give: 
    `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
4) Run migrations using `python3 manage.py migrate` from the CLI if safe to do so.
5) Add the Heroku host name to the ALLOWED_HOSTS section.

Upload data using `python3 manage.py loaddata categories` and then `python3 manage.py loaddata products`

Temporarily disable the collection of static files to Heroku by using `heroku config:set DISABLE_COLLECTSTATIC=1 --app app name`. This is due to the Heroku's security system not accepting them. 

Before commiting and pushing to Github ensure secret keys are hidden in environment variables. 

Deployment security:
`.gitignore`: Create a file and add to it the following files: `*.sqlite3` ,`*.pyc` and `__pycache__/`. This prevents missuse of the development database.

Create and facilitate the use of environment variables within the settings.py file for the purposes hidding the Django SECRET_KEY; hidding the ALLOWED_HOSTS;hidding the DATABASE_URL; and the setting of debug to `true` for development and `false` for deployed app.

For the setting of debug to `true` for development mode and `false` for deployed mode:
1) Create a variable called development that obtains its value from the operating system level or returns `False`: `development = os.environ.get('DEVELOPMENT', False)`
2) Set DEVELEOPMENT to True in Gitpod's IDE settings section or create a hidden file with this data in a `.gitignore` file
3) Set debug to this variable's value i.e. `DEBUG = development`. This prevents internal source code being displayed on the Heroku hosted site if there are errors.


For the purpose of hidding the Django SECRET_KEY:
1) Set the SECRET_KEY value to one supplied in an environment variable in the operating system level or returns a fail: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
2) Set SECRET_KEY to a unique and secret string in Gitpod's IDE settings section (or create a hidden file with this data in a `.gitignore` file) to allow development database. Similarly create a second SECRET_KEY environment variable and deposit it in Heroku's GUI using the environment variables section; this will allow external deployment of the site.


For the purpose of hidding the ALLOWED_HOSTS:
1) Set the ALLOWED_HOSTS value to one supplied in an environment variable in the operating system level or returns a development host only: 
`if development:`
    `ALLOWED_HOSTS = ['localhost']`
`else:`
    `ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]`
2) Set the `HEROKU_HOSTNAME` in Heroku's GUI using the environment variables section. This is the url address of the deployed app less the protocol.


For the purpose of hidding the DATABASE_URL:
1) Use an `if` statement to determine if the user is in developer mode or using it as a deployed app. Once that is determined allow access to the local database `db.sqlite3` or the Postgres database that was eluded to earlier. In the event of the latter an environment variable in Heroku will be required for security:
`if development:`
    `DATABASES = {`
        `'default': {`
            `'ENGINE': 'django.db.backends.sqlite3',`
            `'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}`
`else:`
    `DATABASES = {`
        `'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
2) Set the `DATABASE_URL` in Heroku's GUI using the environment variables section.

Now that the IDE contents can be commited and pushed to Github and Heroku the app can be tested for deployment, albeit without the base.css file due to the `DISABLE_COLLECTSTATIC` command previously executed.

The Github repository can be connected to Heroku to minimise the number of dual commits required: Using the Heroku GUI's enter the Deploy tab and set the Deployment Method to Github masterfile. Direct to the appropriate repo and select auto deploy activated.


AWS S33 was used to host the static files and product images.
Created a group. Attached an access policy to the group that allows full S3 access to the S3 'bucket'.
Created a user, that is part of the group, with a unique special access keys.



---

## Credits

### Content

- **Recipe - description, ingredients and preparation** 
    - [Jamie Oliver - A cracking burger](https://www.jamieoliver.com/recipes/beef-recipes/a-cracking-burger/)
    

### Media

Sources of the images used on this site:

- **Photographic Images** : [Pexels.com](https://www.pexels.com/)
    - [Pixabay - page not found](https://www.pexels.com/photo/building-construction-site-work-38293/)
    
- **mockup image in README** : [techsini](https://techsini.com/multi-mockup/)

### Code

- **HTML template**
    - [David T. Miller - Start Bootstrap](https://startbootstrap.com/templates/modern-business/)

- **Java Script and Query**
    - Code Institute Tutors for fine tuning of code

- **Python**
    - Code Institue course material was the basis for all Python code

### README
- **Template and content**
    - Influenced heavily by the work of [Tim Nelson - TravelTimN](https://github.com/TravelTimN/ci-milestone04-dcd)

### Acknowledgements
- Victor Miclovich 
    - My Code Institute mentor.
- Code Institute Tutors
<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

##### back to [top](#table-of-contents)