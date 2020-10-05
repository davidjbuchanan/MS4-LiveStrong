# [Live Strong](https://live-strong.herokuapp.com/)

<img src="https://github.com/davidjbuchanan/ML4/blob/master/media/mockups/multidevice_showcase.png" alt="live strong multidevice views" width="100%">

[Live Strong](https://live-strong.herokuapp.com/) is a 'one-stop-shop' for those who want to exercise at home! A place to find live and pre-recorded classes that you can participate without having to got ot gym or sports centre. Find yoga, bike and running classes that are ready to be use from the moment you purchase. These classes are essentially 'on-demand' for the user:
**How it works**: 
1. Register for an account or visit as a guest user using the home.
2. Browse and purchase products using the products, coupon, bag and checkout apps.
3. Receive a confirmation email which is a proof of purchase.
4. Receive a seond email containing your credentials and instructions. From there you can access the classes.

This website was produced to fulfill a coursework assignment for the **[Code Institute's](https://codeinstitute.net/)** **Full Stack Frameworks with Django Milestone Project**. The objectives for this milestone project is to "Create a full-stack site based around business logic used to control a centrally-owned dataset. It must consist of multiple apps including an authentication mechanism. Also it must provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.web application with multiple apps".

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
    - [**User Testing**](#user-testing)
    - [**Defensive Design**](#defensive-design)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**README**](#readme)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

The website focuses on the workout-at-home market as it is an attractive approach to health and fitness whilst managing Covid-19 restrictions but also for those with pre-existing conditions (e.g. supressed immune system); no access to local classes; and of course those who would prefer to just workout-at-home. The UX design is intended to draw users in using a well defined color scheme with enjoyably interacive elements. On each page there is a navigation and search jumbotron placed to enable swift access around the site. 

The overall theme of the design is clean straight edges with block elements in order to give a utilitarian vibe whilst the black and red color scheme is intended to make the site feel sporty and sexy. Remiscent of the inspirations for this design (see [onepeleton](https://www.onepeloton.co.uk/) and [Les Mills](https://www.lesmills.com/uk/)) the use of imagery is primarily for motivational and explannatory puposes whereby potential consumers understand that they are purchasing an online service where they can login and access televised workout classes.

The commercial potential for this idea is vast and so the up-to-purchase UX of this site's products has been refined to make the process as simple as possible. Users are able to browse, add to cart, apply coupons and finalise purchases all within an authenticated user. They can also make purchases as a guest. 

The vision for this site is to have three consummables (equipment, services and blog) The equipment and services are grouped together as products, that derive cash income, and can be managed and consumed using the products, bag and checkout apps. The blog is a loss-leader that derives no income it is used as a 'hook' to entice users to register and create a profile thus allowing them access to the blog and, of course,paid for products.

The products themselves are represented within a fully searchable products app, allowing the user rapid access to information. The tangible products, i.e. equipment, are deliverable and there is a shipping functionality that is self explannatory. For the services there is no demonstration of the product; nor access to the product; nor explannations as to how a consumer would access the product after purchase.
There are several placeholder for undeveloped features. It was important to partition these topics clearly for ease of use. To acheive this the navbar displayed each of these topics in its own discrete, but essentially identical, dropdown menus. Likewise the homepage's body presents three uniform rows, one for each topic. 

Each page displays an identical navbar, masthead (with search functionality) and footer this was deliberate to aid users' navigation of the site. For users on smaller vieworts there has been an effort to aid navigation by installation of a bespoke hamburger/dropdown navbar: The user is presented with 4 selections. When selected. by the user, the selection slides to the top of the dropdown menu and any sub menu is displayed beneath it. This was incorporated to ensure the navbar did not expand beyond the page height and become disorientating for the user. 

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
- :white_check_mark: *add* a **coupon** to receive a discount on their shopping.
- :white_check_mark: *update* a **bag content**.
- :white_check_mark: *delete* a **bag content**.
- :white_check_mark: *purchase* any **product(s) and service(s)**.


"**_As an authenticated user, I would like the additional priviledge to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *generate* a **user profile**.
- :white_check_mark: *view* all **published blogs**
- :white_check_mark: *create comments* on **published blogs**


"**_As a staff user, I would like the additional priviledge to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *create* a **draft blog entry**


"**_As a superuser, I would like the additional priviledge to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *update* a **draft blog entry** by promoting it to *published* status
- :white_check_mark: *create* a **product**
- :white_check_mark: *update* a **product**
- :white_check_mark: *delete* a **product**
- :white_check_mark: *create* a **coupon**


### Design

A modern Bootstrap landing page design (https://startbootstrap.com/themes/landing-page/)  was chosen for this site that had a contemporary navbar and masthead that persisted on all web pages. The masthead contained a jumbotron with product/service searchbar for the user's convenience. 

Inspired by the Boutique Ado, [onepeleton](https://www.onepeloton.co.uk/) and [Les Mills](https://www.lesmills.com/uk/) websites the use of full viewport width imagery was employed for visual impact. For the landing, products and purchasing pages the rendered pages were split into three vertical sections : 1) A uniform navbar and masthead with search facility; 2) the body / page specific content; and 3) a uniform footer.  


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

The index page was designed to show 3 main sections. On top a callout/searchbar superimposed upon a background image; in the middle an icon grid to allow user links to products and services; and in the lower part a showreel. The lower, features, section is disproportionately larger due to the desire to advertise the full range of the business' services. As you can see as the viewport narrows the detail and number of features is reduced:

<img src="https://github.com/davidjbuchanan/ML4/blob/master/media/mockups/Index_pages.png" alt="Live Strong index pages on multiple viewports" width="100%">

The page most populated with elements is for the products' page. This required a simple clear display that was responsive as the width of the viewport decreases; this was resolved by stacking the elements. 

<img src="https://github.com/davidjbuchanan/ML4/blob/master/media/mockups/Blog.png" alt="Live Strong blog views" width="100%">

The complete set of wireframes for this project can be found [here](https://github.com/davidjbuchanan/ML4/blob/master/media/mockups) in the *mockups* sub-directory.

##### back to [top](#table-of-contents)

---

## Features

### Existing Features

#### Home App
**Dashboard page**
- Page presents a full overview of the site's content enabling rapid movement around site by use of the ample links and a search bar.


#### Products App and Search functionality
**Search the database**
- If a user would like to search for a particular category of class or item of equipment they can use the search bar (on the Masthead of each page) to search by name, category or by word in the products description. This results in the display of a refinned 'Products' page to the user.
-Alternatively users can use the built-in filters on the navbar's product dropdown menu to access equipment or classes as categorised by exercise tupe e.g. yoga, running etc.
- A third option is found exclusively on the landing page's Icons Grid section where there are some interactive buttons to access the equipment, classes and blog.

**View all essential equipment (also referred to as 'essentials')**         
- This is a C**R**UD feature:
- on the filtered *products* page, all equipment are displayed with a photo, name and price. These products can be explored further on clicking their image or name; the user is taken to a details page where they can add the item to their e-commerce basket.

**View all classes**
- This is a C**R**UD feature:
- on the filtered *classes* page, all classes are displayed with a photo, name and price. These products can be explored further on clicking their image or name; the user is taken to a details page where they can add the item to their e-commerce basket.

**Add a product to the database**
- This is a **C**RUD feature:
- From the navbar option *Product Addition* renders a form. Completion of that form allows the addition of a product with category, rating, image, price and description.
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
**Add a coupon to a bag**
- This is a CR**U**D feature:
- A coupon code can be added in the *bag page*. If valid (vaidated by time, date and status i.e. 'active') a discount is applied, this is reflected in the user's total. The coupon code (and resultant discount) is held within the contexts processor and any subsequent addition of products to the bag will have the validated discount applied. The navbar 'shopping bag' icon shows a running total beneath it. This reflects any discounts applied. The coupon code is discarded at the end of the session for security purposes. 
- Although the model for the coupon system resides in the coupon app, it is the bag app and checkout app that utilise the actual model, i.e. it is in their views.py and contexts.py (Bag app only) that the coupon logic and coupon GUI is manifested.

**Add a coupon to the database**
- This is a **C**RUD feature:
- From the navbar option *coupon Addition* renders a form. Completion of that form allows the addition of a coupon with name, validity and value.
- only the authenticated superuser can access this app feature


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
- Using the navbar a user can navigate to an *add post* page, which is a form, there they can author a post which will be held in draft until published by a superuser.
- only the authenticated superuser can access this app feature

**View and publish a blog post**
- This is a **C**R**U**D feature:
- Using the navbar a user can navigate to a *draft post* page, where a list of all draft posts are rendered for review by the superuser. Each post is displayed in its entirety. Thus allowing quick review prior to selection of an individual post which is a form, there they can author a post which will be held in draft until published by a superuser.
- only the authenticated superuser can access this app feature

**Pagination**
- To maintane a positive UX the blog list is limited to 6 blog posts per page.


#### Use of a hosting site
- The use of a 3rd party image hosting site (e.g. Cloudinary and Amazon S3) would allow users to upload their own images rather than relying existing web images.


### Features Left to Implement
**Content Elaboration**
- Of the other two other main topics (Play & Learn and Rest & Relax) and the store page to add a commercial element.

**Confirmation modals**
- Addition of confirmation models allows the user the opportunity to review seletions and choices. This would be a valuable addition for the prevention of inadvertant deletion of records.

**Elaboration of search facility**
- This could be extended to include a search of the blog app's content. At the moment it is limited to just commecial products and services.

**Elaborate management of coupons**
- Introduce views capable of rendering active and inactive coupons in the user's GUI; allowing the editing of existing coupons; and allowing the deletion of coupons.
- For the 'Coupon Addition' page: currently the *discount* input field allows numbers to be either positive or negative as well as exceed 100%. The introduction of JQuery would limit this to more appropriate numbers. Note: form validation is in place to disallow the submission of negative percentages or numbers greater than 100%.
- For the 'Coupon Addition' page: currently the valid from and valid to dates and times need to be entered using a specific format. A date/time picker would be for more contemporary and less likely to fail form validation thus enhancing UX.

**Elaborate UX of blog posts**
- Introduce blog post tags and subject streams for posts of similar content/theme.
- Elaborate the 'draft post list' and 'publish post' views to include an *update* or *feedback* feature. Thus allowing the reviewer to constructively criticise if the post is not suitable for publication.
- At the moment only staff and superusers can author a post; and they must be authenticated to do so. Similarly users are unable to *comment* on a post unless they have performed registration and authentication. The reason for this is to protect the content of the comments section i.e. to avoid spam. A more sophisticated method could involve making the blog totally open to guest users and making the comments section reviewable prior to publication of the comment. Thus the blog posts would be a 'draw' for new customers whilst the content protected.


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
    - [django-allauth 0.42.0](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication..
    - [requests-oauthlib 1.3.0](https://pypi.org/project/requests-oauthlib/0.3.1/) - This project provides first-class OAuth library support for Requests.
    - [django-crispy-forms 1.9.2](https://django-crispy-forms.readthedocs.io/en/latest/) - django-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way. Have full control without writing custom form templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application..
    

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

## Testing

:white_check_mark: *denotes items that have been successfully implemented*

**Basic navigation** (Tested on Lenovo ThinkVision L2250p 22" Widescreen LCD Monitor, iPhone X and iPad)
done    - :white_check_mark: Links tested on navbar (& navbar toggle button) and footer
done    - :white_check_mark: Footer's Social icons openning to link in a new webpage
done    - :white_check_mark: Links tested on icons grid
done    - :white_check_mark: Links tested on 'under construction page'
done    - :white_check_mark: Alert dismiss on toasts
done    - :white_check_mark: Product links navigate to product detail page
done    - :white_check_mark: Update product links navigate to product detail page and update occurs
done    - :white_check_mark: Delete product links navigate to product detail page and deletion occurs
done    - :white_check_mark: Blog post links navigate to blog post detail page
done    - :white_check_mark: Blog post list page pagination links toggle back and forth between pages
done    - :white_check_mark: Draft blog post links navigate to draft blog post detail page
done    - :white_check_mark: Draft blog post list page pagination links toggle back and forth between pages
done    - :white_check_mark: Draft blog post update to publish status ocurrs

**Search page / functionality:**
- :white_check_mark: Search bar tested on Masthead (product name and product detail content)

**Responsiveness** 
Tested on portrait and landscape viewport for the following viewports
todo    - :white_check_mark: Apple iPad pro
todo    - :white_check_mark: Apple iPad pro
todo    - :white_check_mark: Apple iPad
todo    - :white_check_mark: Apple iPhone 5/SE/6/7/8/X/6 plus/7 plus/8 plus
 
todo    Note: when tested on actual iPhone X the background-attachment: fixed was not compatible with iOS - browsers. On Chrome and Safari in           iOS, the background photos appeared zoomed-in and blurry. To fix this, the .background-attachment: scroll property - value was added in         a media query.

todo    - :white_check_mark:Samsung Galaxy S5
todo    - :white_check_mark:Pixel 2/2 XL

Responsiveness tested on landscape viewport for the following viewports
todo    - :white_check_mark: Lenovo ThinkVision L2250p 22" Widescreen LCD Monitor
todo    - :white_check_mark: Microsoft Surface 2 laptop  (1504 x 892 px)
todo    - :white_check_mark: Dell XPS laptop (13.4 inch, 1920 x 1080 px)
todo    - :white_check_mark: Desktop (1680 x 939 px)
todo    - :white_check_mark: iMac 27 inch (5120 X 2880 px)

**Shopping**
done    - :white_check_mark: Add any quantity of an item to bag
done    - :white_check_mark: Add any quantity of multiple items to the bag
done    - :white_check_mark: Update the bag by reducing or increasing the quantity of any item in bag
done    - :white_check_mark: Remove any item in the bag
            - Note: there was an error raised during developmant of this feature: 
                "POST /bag/remove/195/ HTTP/1.1" 403 2513
                Forbidden (CSRF token missing or incorrect.): /bag/remove/195/ 
                - The JQuery function for this feature was moved into the bag template HTML to prevent recurrence.
done    - :white_check_mark: add coupon codes to bag contents and have the costs updated

**Stripe Payments and Transaction Data**
done    - :white_check_mark: Transactions are recorded in the Postgress db and can be accessed and selectively edited
done    - :white_check_mark: Payments are recorded on Stripe
done    - :white_check_mark: Stripe webhooks 

**Form validation**
- **Registration form.** Required input fields include:
done    - :white_check_mark: email address: input field requires an '@' character
done    - :white_check_mark: username
done    - :white_check_mark: password
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Login form.** Required input fields include:
done    - :white_check_mark: email address: input field requires an '@' character
done    - :white_check_mark: username
done    - :white_check_mark: password
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Password Reset form.** Required input fields include:
done    - :white_check_mark: email address: input field requires an '@' character
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Add draft blog post form.** Required input fields include:
done    - :white_check_mark: Post title
done    - :white_check_mark: Post slug
done    - :white_check_mark: Post content
done    - *:white_check_mark: Requires staff user status to access page*
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Update/publish draft blog post form.** Required input fields include:
done    - :white_check_mark: status
done    - *:white_check_mark: Requires superuser status to access page*
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Add comment (to blog post) form.** Required input fields include:
done    - :white_check_mark: name
done    - :white_check_mark: email address: input field requires an '@' character
done    - :white_check_mark: message
done    - *:white_check_mark: Requires authenticated user status to access comments form*
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Add item to bag form.** Required input fields include:
done    - :white_check_mark: quantity (1 min., 99 max.)
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Checkout form.** Required input fields include:
done    - :white_check_mark: full name
done    - :white_check_mark: email address: input field requires an '@' character
done    - :white_check_mark: phone number
done    - :white_check_mark: country
done    - :white_check_mark: town of city
done    - :white_check_mark: street address
done    - :white_check_mark: card details
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Add product form.** Required input fields include:
done    - :white_check_mark: category
done    - :white_check_mark: product name
done    - :white_check_mark: product description
done    - :white_check_mark: price ($9999.9 max.)
done    - *:white_check_mark: Requires superuser status to access page*
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

- **Update product form.** Required input fields include:
done    - :white_check_mark: category
done    - :white_check_mark: product name
done    - :white_check_mark: product description
done    - :white_check_mark: price
done    - *:white_check_mark: Requires superuser status to access page*
- *:white_check_mark: On successful completion of the form the user is presented with a toast notification*

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) 
    - All code is perfectly validating without errors. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
- **Property Errors**
    -   *abbr[data-original-title], abbr[title]* - Property text-decoration-skip-ink doesn't exist : none
    -   *.toast* - Property backdrop-filter doesn't exist : blur(10px) 
- These errors incurred no impact on the rendered pages and were therefore ignored.

**JavaScript**
- [JShint](https://jshint.com/)
    - "There are **52** functions in this file.
    Function with the largest signature take **1** arguments, while the median is **0**.
    Largest function has **19** statements in it, while the median is **3**.
    The most complex function has a cyclomatic complexity value of **3** while the median is **1**."

- [JSesprima](http://esprima.org/demo/validate.html)
    - "Code is syntactically valid."

- [Beautify Tools](http://beautifytools.com/javascript-validator.php)
    - 'e' is defined but never used in bag.js
    - 'e' is defined but never used in stripe_elements.js
    - 'Stripe' is not defined in stripe_elements.js

**Python**
- [PEP8 Online](http://pep8online.com/)
    The Python files were PEP8 compliant apart from the falure to adhere to the E501 (line too long) requirement in the following apps and files:

    - blog app
        views.py    Line:98
    - checkout app
        models.py   Lines: 18, 29, 30, 31, 33, 46, 48, 68, 69, 71, 72, 73, 74, 75 and 84.   
        urls.py     Lines: 7 and 8.
        views.py    Lines: 1, 88, 94 and 101.
        w'k_h's.py  Lines: 71, 72, 102, 131 and 148.
        w'hooks.py  Line: 42.
    - coupons app
        views.py    Line: 20.
    - products app
        models.py   Lines: 24 and 29.
        urls.py     Line: 9.
        views.py    Lines: 41, 44, 83 and 109. 
    - profiles app
        forms.py    Line: 33.
        models.py   Lines: 13, 14, 15 and 16.  
        urls.py     Line: 6.
        views.py    Line: 21.


### Compatibility
todo - :white_check_mark: Microsoft Edge (version ):  Images within cards were found to be distorted on initial tsting, i.e. not in width but in height, where the height reverted to that of the original image. To rectify the distortion a .d-block class was added to the parent div i.e. div class="card d-block h-100 shadow". Credit jeroendesloovere @ https://github.com/twbs/bootstrap/issues/21885. 
todo - :white_check_mark: Mozilla (Version 81.0.1 (64-bit)).
todo - :white_check_mark: Safari (Version 14.0.1).
todo - :white_check_mark: Microsoft Edge (Version 85.0.564.68 (Official build) (64-bit)).
todo - :white_check_mark: Google Chrome (Version 85.0.4183.121 (Official Build) (64-bit)).

### Known Issues

During development, I discovered two issues after committing to GitHub. 

- **Flaw with bag apps JQuery 'remove' function**
    - as described in the testing section, above, the function that allows for the removal of items from the bag (a.k.a. cart) does not function unless the function is appended to the bottom of the bag.html template. This is due to its reference of csrf token. 
- **Flaw with cross-site resources for images and icons**
    - http://fontawesome.com cookie is set with sameSite attribute.


### User-testing
- Testing to select group of targeted users and a development professional highlighted these 5 points:
    -   Toasts are not uniform across the site and often contain extraneous information; e.g. the bag's contents always shows even when the toast is for something as unrelated as a coupon management task. 
    -   The 'subsrcibe' link on the navbar was identified as potentially premature and that a "give away" should be offered to the user prior promotion of a subscription servive.
    -   Images uploaded by user's should be hamdled ny a third party in order to give the user greater autonomy over the image used and not reliant on web available images.
    - Edit buttons allowing addition and deletion of fields in the 'add recipe' and 'edit recipe' should be "more available" to the user i.e. at the bottom or side of a growing list.


### Defensive Design
- It was important to ensure that the apps run correctly and continue to run no matter what actions a user takes. That is why rigorous testing, for all possibilities, was undertaken focusing on the 5 following areas:

Defensive design encompasses three areas:
- **Validation**
    - Form validation using *crispy forms* and *required* fields in the apps' models ensured that users only input acceptable data.
    - No significant security or bug issues have been presented.
- **Sanitisation**
    - The code has been hidden in files (e.g. env.py) or indeed IDE settings to prevent access to vulnerable secret keys, URLs and passwords. In addition a tiered level of access from users, authenticated users, staff users and superusers has been employed thus allowing different users different levels of access to the sites' content. Examples of this are most noticable in the **coupons app**, **products app** and **blog app** views.py files where an authenticated login is required to access the CRUD functionalties of these apps. 
    - No significant security or bug issues have been presented.
- **Authentication**
    - this is all handled with the allauth authentication system.
    - No significant security or bug issues have been presented.
- **Maintenance**
    - The filing system is uniform and standard throught the numerous apps. All apps have been tested against the standard validators for code.
    - No significant security or bug issues have been presented.
- **Testing**
    - Rigorous user testing has been performed to ensure the functionality of the site on multiple browsers and viewpost sizes.
    - No significant security or bug issues have been presented.


##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

1. Some basic requirments for the deployment include:
    - [Python3](https://www.python.org/downloads) to run the application.
    - [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
    - An IDE such as [Gitpod](https://www.gitpod.io/) or [Microsoft Visual Studio Code](https://code.visualstudio.com).
    - [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
    - [Github account]() for saving repositories
    - [Stripe account]() for managing payment system 

Now, there is a series of steps to take in order to proceed with local deployment:

2. Here are three options for downloading this repo to your IDE: 
    - (1) If you have added the Chrome/Firefox Gitpod extension you can clone by clicking the green *Gitpod* button at the top right of this repo. to open a workspace within the Gitpod IDE; 
    - (2) download the project as a zip-file (remember to unzip it first); and then upload/drag it into your workspace.
    - (3) by entering the following into the Git cli terminal: `git clone https://github.com/davidjbuchanan/lockdownagain.git'.
    - Note: when using Gitpod IDE it may be advantageous to goto the Code Instute's Github page and clone their [template](https://github.com/Code-Institute-Org/gitpod-full-template). This will give the developer administration rights.
3. Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
4. The `requirements.txt` will list the required packages required to successfully launch the site for local and remote deployment; the list should look like the following (Note: many of these packages are required for remote deployment - see section below): 
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
    
5. Set up your development app. with the following two configuration variables:
    - **SECRET_KEY** : `<typically a lower case alpha numeric code with symbols>`
    - **DEVELOPMENT** : `1`
    - Here are two options for storing these:
        - (1) Create an `env.py` file. It should look something like this:
                ```
                import os

                os.environ['SECRET_KEY'] = '<lower case alpha numeric with symbols>'
                os.environ['DEVELOPMENT'] = '1'
                
                ```   
        - (2) Use Gitpod's IDE settings option from the drop-down menu. Place the config vars in **Settings**.
        - Note: It is important that these do not get uploaded during a Github commit/push and that they do not appear in your repository for security reasons

6. Make migrations using the following command in the IDE's cli: `python3 manage.py migrate`

7. Set yourself as a superuser using `python3 manage.py createsuperuser`
    - add a usernmame and passwords

8. The site should now render, on the development server, using the following command in the IDE's cli: `python3 manage.py runserver`
    - However there will be no products rendered to the site and the checkout app will error if openned.
    - you will be able to access the Django admin at HTTPS ending `/admin`
    - In order to access the GUI as a superuser you can login through `/admin`
        - Go to the *Accounts* app
        - select *Add Email Address*
        - as you are the only user you are *user* number 1
        - add your *email address* (which should be the same as the one used to generate a superuser)
        - check the *verified* and *primary* box and then press *save*
        - **You can now login as a superuser using the GUI's navbar (my accounts) dropdown menu option** 
    - Alternatively you can register through the GUI like a normal user would. The steps for that are the following:
        - Navigate to the login page and login with your superuser username and passwords
        - return to the development terminal and follow the link, thus verifying your email address.

9. To add products you will need to define product categories as well as products themselves.
    - Create them using the examples in products/fixtures/categories.json and products.json files as a template; input the details relevant to your business and then upload the products and categories to the db.sglite3 database using cli commands `python3 manage.py loaddata categories` then `python3 manage.py loaddata products`. Alternatively you could add them all individually through the django admin app at `/admin` using the **products** app.

10. Set up a payment system through [Stripe](https://github.com/Code-Institute-Org/gitpod-full-template) and obtain values for the following configuration variables:
    - **STRIPE_PUBLIC_KEY** : `<upper and lowercase alphanumeric with symbols>`
    - **STRIPE_SECRET_KEY** : `<upper and lowercase alphanumeric with symbols>`
    - **STRIPE_WH_SECRET** : `<upper and lowercase alphanumeric with symbols>`
    - Add these to your Gitpod **Settings** or put them in `env.py`. If you choose the latter it should now look something like this:
    ```
    import os

    os.environ['SECRET_KEY'] = '<lower case alpha numeric with symbols>'
    os.environ['DEVELOPMENT'] = '1'
    os.environ['STRIPE_PUBLIC_KEY'] = '<upper and lowercase alphanumeric with symbols>'
    os.environ['STRIPE_SECRET_KEY'] = '<upper and lowercase alphanumeric with symbols>'
    os.environ['STRIPE_WH_SECRET'] = '<upper and lowercase alphanumeric with symbols>'
    ``` 
    - To get values for **STRIPE_PUBLIC_KEY** and **STRIPE_SECRET_KEY** from your Stripe account. Goto the 'Developers' section and look on 'API keys' where they referred to as the 'Publishable key' and 'Secret key' respectively.
    - To get a value for **STRIPE_WH_SECRET** from your Stripe account. Goto the 'Developers' section:
        - Click 'Webhooks' then 'Add endpoint'
        - Enter Endpoint URL: e.g. 'https://8000-b2a1760c-3736-458a-ba16-2e5a7fea662e.ws-eu01.gitpod.io/'
        - Select 'receive all events' and then click 'Add Endpoint'
        - collect the 'Signing secret' and add it to the config vars. Note: this secret is specific to the developer's server. I.e. You will need a different key for remote deployment.

11. With this all in place the app should render and accept payments. 
    - `python3 manage.py runserver`. This may require a prefix of `sudo` if you do not have administration rights on your IDE.
    - The app should now be running on *localhost* and, when using Gitpod IDE, render an address similar to `https://8080-bce9ad25-9922-4648-b249-d83204aa0bf4.ws-eu01.gitpod.io/`.
    - All emails (e.g. authentications, transaction details) will now be sent to the development terminal.


### Remote Deployment

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku,the following steps were taken:

1. Perform the steps required, as described above, for local deployment.
2. Sign up for a free Heroku account and create your project app.
    - Once done, use the *'resource'* tab to search for an add-on called *Heroku Postgress*
        - Note: Django's db.sqlite3 is fine for local development but is not robust for long term storage of data as it is ephemeral.
3. Install dj-database-url and psycopg2-binary packages and then add them to the requirements.txt file if not already done so.
4. Now you need to replicate the steps performed previously for the setup of the db.sqlite3 development server but this time it is for the Postgress server. These steps will consist of establishing a link to the external database; making migrations; uploading products to the db; and seting up a superuser access on the Postgress db. 
    - (1) update the `DATABASES` section in setings.py by 'commenting-out' the if/else block and adding some temporary code beneath it as shown below. Where you see *ENTER_URL_HERE* you should enter the **DATABASE_URL** configuration variable supplied by Heroku (you can find config vars under the 'settings' tab of your Heroku app.'s dashboard):
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
    ```
    - **Note: there is a security issue with this activity!** You could divulge configuration variables on Github if you commit and push to Github at this stage. Therefore this change to code should be reverted prior to commiting. 
    - (2) Make migrations using `python3 manage.py migrate`
    - (3) Add categories and products as previously described in the *Local Deployment* section above. This time you will upload this data to the Postgress db using the same cli commands as before: `python3 manage.py loaddata categories` then `python3 manage.py loaddata products`. 
    - (4) Create a superuser using `python3 manage.py createsuperuser`
        - add a usernmame and password
    - (5) With that done you should now uncomment the `DATABASES` code block and delete the temporary code to give:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```     
    - (6) Install gunicorn and add it to the requirements.txt file if not already done so.
    - (7) Update the **Procfile** to tell Heroku what type of application is being deployed. This will create a web dyno which will run unicorn and serve our django app.
        - My file can be found [here](https://github.com/davidjbuchanan/lockdownagain/blob/master/Procfile).
    - (8) Disable 'collect static' in the Heroku cofiguration variables using the Heroku GUI, use the **Settings** tab on your app's dashboard. 
        - Note: The static files will be used for development purposes but we will use a cloud based system for the deployed site. 
    - (9) In settings.py update `ALLOWED_HOSTS = ['live-strong.herokuapp.com', 'localhost']` to reflect the name of your app., if different.
    - (10) Set up a git remote link from your IDE to Heroku if you haven't already i.e. `heroku git:remote -a live-strong` or set automatic deployments, from Github, using the deploy tab in Heroku's GUI.
        - This allows you to push the code from your IDE to Heroku via Github. In Heroku click the **Deploy** tab, which is where you can *Connect GitHub* as the *Deployment Method*, and select *Enable Automatic Deployment*.
    - (11) Set a SECRET_KEY in the Heroku (you already have one for Local Deployment as discussed in the section above).
        - This secures the app as per code in settings.py: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
    - (12) Add the Stripe keys generated in the Local Deployment section to the configuration variables section in your Heroku app. You can get the values for these from your Stripe account. Goto the 'Developers' section and look on 'API keys'. Alternatively get them from wherever you stored them for local deployment as they are the same keys.)
        - Your Heroku app's configuration variables should now look like the following: 
            - **DATABASE_URL** : starts `postgress://` then `<alphanumeric>`
            - **DISABLE_COLLECTSTATIC** : `1`
            - **SECRET_KEY** : `<lower case alpha numeric with symbols>` (this was set-up during local deployment)
            - **STRIPE_PUBLIC_KEY** : `<upper and lowercase alphanumeric with symbols>` (this was set-up during local deployment)
            - **STRIPE_SECRET_KEY** : `<upper and lowercase alphanumeric with symbols>` (this was set-up during local deployment)
        - your env.py file will look the same as it did in the Local Deployment section:
            ```
            import os

            os.environ['SECRET_KEY'] = '<lower case alpha numeric with symbols>'
            os.environ['DEVELOPMENT'] = '1'
            os.environ['STRIPE_PUBLIC_KEY'] = '<upper and lowercase alphanumeric with symbols>'
            os.environ['STRIPE_SECRET_KEY'] = '<upper and lowercase alphanumeric with symbols>'
            ``` 

At this point you should be able to initiate a *Build* on Heroku by performing a 'git push' on your IDE's cli as this 'push' will go through to Heroku. The rendered Heroku app will contain HTML content but none of the static content; that comes from the AWS systems that have yet to set-up.

5. Setup an AWS account.
    - (1) Access S3 (safe storage services) for the purposes of storing your static files in the S3 cloud-based storage system.
        - create a bucket 
            - allow public access.
            - allow static website hosting.
            - Under *CORS configuration* write a CORS configuration, e.g.:
                ```
                <?xml version="1.0" encoding="UTF-8"?>
                <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
                <CORSRule>
                <AllowedOrigin>*</AllowedOrigin>
                <AllowedMethod>GET</AllowedMethod>
                <MaxAgeSeconds>3000</MaxAgeSeconds>
                <AllowedHeader>Authorization</AllowedHeader>
                </CORSRule>
                </CORSConfiguration>
                ```
            - Under *Bucket Policy* generate an S3 bucket policy to allow access to all resources in bucket.
                - allow all principals
                - set the action as 'GetObject'
                - E.g.:
                    ```
                    {
                        "Version": "2012-10-17",
                        "Id": "Policy",
                        "Statement": [
                            {
                                "Sid": "Stmt",
                                "Effect": "Allow",
                                "Principal": "*",
                                "Action": "s3:GetObject",
                                "Resource": "arn:aws:s3:::ml4-djb/*"
                            }
                        ]
                    }
                    ```
                - Under *Access Control List* set the *Public Access* for *Groups* to **everyone**
    - (2) Access IAM (Identity and Access Management) for the purposes of creating users capable of accessing the bucket for management purposes.
        - create a group with an access policy attached that allows full (public) access to the S3 bucket.
            - For this project the 'AmazonS3FullAccess' policy was imported from the pre-built managed policies and was customised to allow access to the bucket using the bucket's ARN number.
            - E.g.:
            ```
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:*",
                        "Resource": [
                            "arn:aws:s3:::ml4-djb",
                            "arn:aws:s3:::ml4-djb/*"
                        ]
                    }
                ]
            }
            ```
        - create a user and associate that user with the group. Collect the .csv file with the users credentials as you will input them into Heruko's configuration variables:
            - an *Access key ID* 
            - and a *Secret access key*
            - Note: it is important that these secrets do not aoear in your repository as there could be a financial penalty for fraudulent use.
            
6. Configure Django to connect to s3 using the IAM keys and upload static files to s3.
    - Install boto3 and django-storages and add them to the requirements.txt file if not already done so.
    - Update the Heroku app's configuration variables to synchronise with the settings.py code snippets below:
        - For `if 'USE_AWS' in os.environ:` set a config vars of *USE_AWS* with a value of *True*;
        - For `AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')` set a config vars of *AWS_ACCESS_KEY_ID* with a value of the *Access key ID* generated from IAM;
        - and for `AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')` set a config vars of *AWS_ACCESS_KEY_ID* with a value of the *Secret access key* from IAM
        - Your Heroku app's configuration variables should now look like the following: 
                - **AWS_ACCESS_KEY_ID** : `<capitalised alphanumeric>`
                - **AWS_SECRET_ACCESS_KEY** : `<upper and lowercase alphanumeric with symbols>` 
                - **DATABASE_URL** : starts `postgress://` then `<alphanumeric>` (this was set-up during local deployment)
                - **DISABLE_COLLECTSTATIC** : `1`
                - **SECRET_KEY** : `<lower case alpha numeric with symbols>` (this was set-up during local deployment)
                - **STRIPE_PUBLIC_KEY** : `<upper and lowercase alphanumeric with symbols>` (this was set-up during local deployment)
                - **STRIPE_SECRET_KEY** : `<upper and lowercase alphanumeric with symbols>` (this was set-up during local deployment)
                - **USE_AWS** : `True`
    - the *DISABLE_COLLECTSTATIC* config vars can now be deleted as the site should now pull the static files from the Github repo. through to the AWS bucket.

At this point you should be able to inititiate a *Build* on Heroku by performing a 'git push' on your IDE's cli as this 'push' will go through to Heroku. The rendered Heroku app will contain HTML, CSS and JQuery content but none of the media content; that comes from further addition to the AWS bucket.

7. We want to use S3 to store our media files too:
    - Access the S3 bucket, create a folder and call it 'media'.
    - Select the desired photos with filenames corresponding to those in the CSS.
    - Grant public read access to these files.
    - Upload files

At this point you should be able to inititiate a *Build* on Heroku by performing a 'git push' on your IDE's cli as this 'push' will go through to Heroku. The rendered Heroku app will contain HTML, CSS, JQuery and media content.

8. Verify superuser 
    - open the heroku app and goto the /admin url
    - goto *Accounts* app. and click on your address (the one you entered when you created the superuser from your IDE's cli) and click *Primary* and *Verified*. Further details, on this topic, are to be found in the Local Deployment section above.

At this point you should be able to login to the app website and have full superuser access.

9. Add a Stripe webhook endpoint and generate a 'Signing secret' for the Heroku deployed site. Remember previous webhooks would have been for the local site only.
    - Goto the 'Developers' section:
        - Click 'Webhooks' then 'Add endpoint'
        - Enter Endpoint URL: e.g. 'https://live-strong.herokuapp.com/checkout/wh/'
        - Select 'receive all events' and then click 'Add Endpoint'
        - collect the 'Signing secret' and add it to the Heroku apps config vars under a name of 'STRIPE_WH_SECRET'. Note: this will be a different key to the one used in the local site's 'env.py' file or Gitpod settings.

The site is now deployed and anyone on the internet can browse products, create a profile, and even check out using a test credit card number.
If a user makes a purchase there order is created in the django admin. And if they authenticate their login their order will be attached to their profile and displayed in their order history.

10. Linking emails to site using Gmail:
    - Goto 'settings'; then 'Accounts and Imports'; then 'Other Google Accounts Settings'; and then 'security' to access the security page:
        - Then go into 2-step verification and complete the steps. Once complete return to the security page.
        - Then go into App passwords and from the 2 dropdown menus 'select app' 'select device' choose *mail* and *other* and call it Django.
            - obtain a 16 digit code
    - Go to the Heroku app's settings and generate two new config vars
        - EMAIL_HOST_PASS
        - EMAIL_HOST_USER
        - the values for these will be the 16 digit code and the Gmail email address used to set up the verification.

Once all that is done you need to run a commit on your IDE and force a build on Heroku; then the updated app will be able to send real emails. 

11. To personalise the emails sent from the remotely deploued site you will need to login to admin as a asuperuser. Go to *Sites* and update the domain name to suit your app.
        
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


Your app should be successfully deployed to Heroku at this point.

##### back to [top](#table-of-contents)


---

## Credits

### Content

- **Blog content** 
    - [Les Mills](https://www.lesmills.com/uk/fit-planet/)

### Media

Sources of the images used on this site:

- **Photographic Images** : 
    - [Argos](https://www.argos.co.uk/)
    - [onepeleton](https://www.onepeloton.co.uk/)
    - [Les Mills](https://www.lesmills.com/uk/)
    
- **mockup image in README** : 
    - [techsini](https://techsini.com/multi-mockup/)

### Code

- **HTML template**
    - [David T. Miller - Landing Page](https://startbootstrap.com/themes/landing-page/)    

- **Bag app**
    - ckz8780 [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) was the template for the following areas:
        - the file structure including the template, HTML and Python code
        - the following views were all taken from Boutique Ado repo.: view_bag, add_to_bag, adjust_bag and remove_from_bag.
        - the coupons app (see below) is merged with this app; specifically the template, contexts file and views file.

- **Blog app**
    - Django 3 By Example: Build powerful and reliable Python web applications from scratch, 3rd Edition Paperback – 31 Mar. 2020
      by Antonio Mele (Author); and published by [Packt](www.packtpub.com). The contents were used for the following:
        - HTML, CSS and Python for the post_list view and its pagination.
        - HTML, CSS and Python for the post_detail view and its comments section.
        - the add_blog_entry view, draft_list view and post_publish view used the styling and several elements from the book but these views were not covered in the book nor was the concept of defensive design (i,e, authentication of users to access these views and the use of if/else template logic to control rendered pages to authenticated users). So although there are similarities with the book's content (especially for draft_list view), the urls, HTML and Python were developed to allow the the app to function.  
        - the JQuery is bespoke and is used throughout the project.

- **Checkout app**
    - ckz8780 [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) was the template for the following areas:
        - the file structure including the template, HTML and Python code
        - the following views were all taken from Boutique Ado repo.: cache_checkout_data, checkout and checkout_success.
        - all Stripe payment systems, webhooks and associated JQuery were taken from this project. 
        - the coupons app (see below) is merged with this app; see the template and views file.
        
- **Coupons app**
    - Two influences for this app:
        (1) Django 3 By Example: Build powerful and reliable Python web applications from scratch, 3rd Edition Paperback – 31 Mar. 2020
            by Antonio Mele (Author); and published by [Packt](www.packtpub.com). The contents were used for the following:
            - the model, urls and view were adapted for purpose. 
        (2) Donna's [aka skies09](https://github.com/skies09/omega-sk8-ds) repository was an influence:
            - the placement of the coupon_apply view inside the bag apps' views file. 
        - HTML, CSS, JQuery and Python were developed to merge into the bag apps' templates, views, contexts and urls files.
    - the add_coupon views and forms files were developed independantly 

- **Home app**
    - this is a standard home app with a 404 view and url. It is very similar to that of the Code Institute's [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) repo.

- **Products app and Profiles app**
    - ckz8780 [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) apps were used in its entirety aside from styling.

### README
- **Template and content**
    - Influenced heavily by the work of [Tim Nelson - TravelTimN](https://github.com/TravelTimN/ci-milestone04-dcd)

### Acknowledgements
- Victor Miclovich 
    - My Code Institute mentor.
- Code Institute Tutors
    - Fine tuning of code
<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

##### back to [top](#table-of-contents)