# Take Stock

![4 size view of the website's home page](static/assets/images/4_screen_view.PNG)

<!-- Description -->
Take Stock is a data handling app for small buisnesses to take care of their stock and product information. A company can create a profile, add stock items, add products, and then link stock items to each product. The app will then tell the user exactly how many of each product they can make based on what they have in stock. This project was created as a submission for Code Institute. This repository is a clone repo, not the original development environment.

- You can view the live site [here](https://take-stock-app-v2.herokuapp.com/).

# Contents
- [**User Experience (UX)**](#user-experience-ux)
  - [**User Stories / Epics**](#user-stories--epics)
- [**Design**](#design)
- [**Features**](#features)
  - [**Existing features**](#existing-features)
    - [**Landing page**](#landing-page)
    - [**Stock page**](#stock-page)
    - [**Products page**](#products-page)
    - [**Forms**](#forms)
    - [**Admin View**](#admin-view)
- [**Future updates**](#future-updates)
- [**Languages used**](#languages-used)
- [**Frameworks used**](#frameworks-used)
- [**Agile Development**](#agile-development)
- [**Testing**](#testing)
- [**Structre**](#structure)
  - [**Database structure**](#database-structure)
  - [**Project structure**](#project-structure)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Acknowledgements**](#acknowledgements)

## **User Experience (UX)**

### **User Stories / Epics** 

- Epic
  - As a user/company, I'd like to have an app where I can store information about my products; including its:
    - Name
    - List of parts (Bill of Materials (BOM))
    - How many of each item I have in stock
    - How many of each product I can make
  - I would like to be able to update the products BOM at any time, as well as the stock list.
  - Login/logout should be quick and easy.
         
- First time visitor goals:
1. Have the first visit easily explain the site, how it works, what it can do, etc.
2. Have the app be easy to navigate and intuitive to use.
3. Be able to sign up for an account as easily as possible.

- Returning visitor goals:
4. Be able to login and see data stored from previous visits.
5. Be able to easily login and view my data.

- Frequent user goals:
6. Be able to quickly see what I have in stock and how many products I can make.
7. Be able to add new products and/or stock quickly and easily and see that
    immediately reflected in the interface.

- Admin user goals:
8. Have access to other user data to be able to check for and remove objectionable inputs.

- Site owner goals: 
9. Have the interface be easy to navigate and reflect recent actions to the user. 
10. Show the user exactly how many of each product they can make.
11. Have user data be only accessable to that specific user.

- User acceptance: 
  - Stock list and product list implemented.
  - Register/login feature to separate user data.
  - User data cannot be accessed or change by the wrong user.

- Tasks:
  - Implement login/logout features.
  - Create models to house stock and product data.
  - Create logic to link stock items to products.
  - Allow users to update and delete their data as they choose to.
  - Allow the admin access to all user data.

### **Design**
- Color Scheme
  - Sleek, black on white with sophisticated color scheme accents to portray professionalism.

- Typography
  - Nanum Gothic is and easy to read, block-like typeface. The motif of the app is professional which the font follows.

- Imagery
  - No imagery as the app is informational based. Screenshots on the home page and the "how-to-use" page to show functionality and use.

- Wireframes 

  - Wireframes were constructed in a whiteboard as the design motif was minimal. Simple lines and boxes were used throughout.
  
- Home page

<img src="static/assets/wireframes/home.jpg" style="max-height: 300px;">

- Logged in home page

<img src="static/assets/wireframes/logged_in_home.jpg" style="max-height: 300px;">

- Lists

<img src="static/assets/wireframes/stock.jpg" style="max-height: 300px;">

- Product page

<img src="static/assets/wireframes/products.jpg" style="max-height: 300px;">

- Forms

<img src="static/assets/wireframes/form.jpg" style="max-height: 300px;">

- Admin

<img src="static/assets/wireframes/admin.jpg" style="max-height: 300px;">

<!-- HTML used instead of markdown to control image size as images were very large when testing. -->

## **Features**

### **Existing features**
- Users can add stock and products, as well as link stock items to products.
- The app will show users exactly how many of each product the user can make given the amount of stock they have.
- The app has all features of CRUD functionality.

### **Landing page**

- There are two versions of the landing page: logged in and logged out. The logged out landing page gives brief information about the app and a help guide as to how the app works. The logged in landing page allows a user user access to their stock list and product list. From these pages they can manipulate their data however they choose to.

<img src="staticfiles/assets/images/home_page_1.PNG" style="max-height: 300px;">

<img src="staticfiles/assets/images/home_page_2.PNG" style="max-height: 300px;">

### **Stock page** 

- A list of all a user's stock with links to update each item or add a new one that redirect to easy to follow forms. 

<img src="staticfiles/assets/images/stock_page.PNG" style="max-height: 300px;">

### **Products page** 

- A list of all a user's products with a count as to how many of each product can be made based on the number of each linked stock item in the stock list. Each product can be navigated into which will display a list of all it's parts. New parts can be added, or parts can be removed, or the whole product can be deleted from here.

<img src="staticfiles/assets/images/products_page.PNG" style="max-height: 300px;">

### **Forms** 

- All forms follow a similar design motif with placeholders, all centered on the page to ensure ease of use.

<img src="static/assets/images/form.PNG" style="max-height: 300px;">

### **Admin View** 

- The Admin View lists all users, all their respective stock and products, and all those product's respective parts. The admin from here can delete any item if it is deemed to be objectionable. 

<img src="static/assets/images/admin_view.PNG" style="max-height: 300px;">

## **Future updates**

- An orders page where users can specify how many of each product they need to make, and the app with tell them how many they can make, and how much stock they would need to aquire to complete each order.

- Roles relevant to different departments. For example:
  - Managers: Full access to all features
  - Sales: Able to add, update, and change orders
  - Storage: Able to change stock numbers and items
  - Production Hands: Able to read data but not able to change or update data.

- Search bars on Stock and Products pages, as well as when linking parts to products for ease of use. Users will be able to fast-track their experience through the site.

## **Languages Used**

- HTML5
- CSS3
- JavaScript
- Python and Django

## **Frameworks used**

- [Google Fonts](https://fonts.google.com/)
- Git
- GitHub
- jQuery
- Whitenoise

## **Agile development**

- The project was constructed using Agile methodology, as can be seen in the GitHub repository's [Projects](https://github.com/Ryan-B1yth/stock_take_app/projects/1) section. As this repository is a clone of the original to allow for further development after submission, the project's kanban board is not located in this repo.

## **Testing**

You can read through the testing documentation [here](static/docs/TESTING.md).

## **Structure** 

### **Database structure**

#### Stock model

| name | code | number_in_stock | company |
| --- | --- | --- | --- |
| CharField | CharField | IntegerField | ForeignKey(User) |

#### Product model 

| name | stock_parts | company | 
| --- | --- | --- |
| CharField | ManyToManyField(Stock) | ForeignKey(User) | 

#### Parts model 

| product_part_belongs_to | item | number_required | company |
| --- | --- | --- | --- | 
| ForeignKey(Product) | ForeignKey(Stock) | IntegerField | ForeignKey(User)

- The descision to have each model contain a company column was made to shorten the amount of code written in views and templates. It seemed more logical to have the field be auto set in each form instance - not under the users control - than to, when referencing the company when the parts model is called, to have the code read ```parts.product_part_belongs_to.stock_parts.company``` instead of the much easier to understand ```parts.company```.

### **Project structure**
```
|--CLONE_stock_take_app
|  |--take-stock
|    |--__init__.py
|    |--asgi.py
|    |--settings.py
|    |--urls.py
|    |--views.py
|    |--wsgi.py
|  |--app
|    |--__init__.py
|    |--admin.py
|    |--apps.py
|    |--forms.py
|    |--models.py
|    |--urls.py
|    |--views.py
|  |--templates
|    |--app
|      |--index.html
|  |--static
|    |--css
|      |--index.css
|    |--js
|      |--index.js
```

- The chosen file structure for this project, in terms of template location, was project level. This allowed for all HTML to be kept in a single directory and easily locatable - in a similar way to how CSS and JS files are located at project level in the static directory.

## **Deployment** 
- The project was deployed on Heroku through the CLI following Code Institute's instructions. During development there was a data breach with GitHub and subsequently, Heroku limited its connection to the platform. As such, the steps taken to deploy the project were as follows:
  - Install:
    - pyscopg2-binary
    - gunicorn
    - dj-database-url
    - whitenoise
      - Whitenoise was used instead of the method taught on the course as it allows for the app to serve it's own static files without having to rely on external resources and is recommended for use with apps deployed on Heroku. As such, all static files are collected and stored in a directory called ```staticfiles``` in the repo when running the command ```python3 manage.py collectstatic```, however all the original static files can be found in the ```static``` directory.

 In the CLI, enter following commands:
  - `heroku login -i`
    - Login using your email and password.
  - `pip3 freeze --local > requirements.txt`
  - `heroku apps:create APPNAME --region eu`
- In the Heroku app dashboard:
  - Add Heroku Postgress in Resources.
  - In settings, reveal the config vars and create a SECRET_KEY variable using a Django secret key generator.
- In Git:
  - Add `*.sqlite3` and `__pycache__/` to the .gitignore file.
  - Create a Procfile and add `web: gunicorn --pythonpath PROJECTNAME APPNAME.wsgi:application` where APPNAME is the folder that contains the settings.py file.
  - In workspaces:
    - Create a SECRET_KEY variable that is different to the Heroku secret key.
    - Create a DEVELOPMENT variable equal to `True`.
  - In settings.py:
    ```
        SECRET_KEY = os.environ.get('SECRET_KEY')

        development = os.environ.get('DEVELOPMENT', False)
        DEBUG = development

        if development:
            ALLOWED_HOSTS = ['localhost', '127.0.0.1']

        else:
            ALLOWED_HOSTS = [
                'take-stock-app-v2.herokuapp.com'
            ]
    
        if development:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
            }
        }
        else:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
    ```

  - Add, commit with the message "Prepare to push to Heroku, set up development environment", and push to GitHub.
  - Push to heroku with `git push heroku main`.

## **Credits** 

### **Code**

- Code
  - All code was written by the developer.

### **Content**

- Content
  - All template files were written by the developer.
  - User information is written by each respective user.

### **Acknowledgements**
    
- Tutor support at Code Institute for all their support throughout.

- Friends and family for viewing the site and giving feedback.