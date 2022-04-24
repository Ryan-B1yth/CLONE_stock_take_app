# Take Stock

![4 size view of the website's home page]()

<!-- Description -->
Take Stock is a data handling app for small buisnesses to take care of their stock and product information. A company can create a profile, add stock items, add products, and then link stock items to each product. The app will then tell the user exactly how many of each product they can make based on what they have in stock. 

## User Experience (UX)

### User Stories / Epics 

- Epic
  - As a user/company, I'd like to have an app where I can store information about my products; including it's:
    - Name
    - List of parts (Bill of Materials (BOM))
    - How many of each item I have in stock
    - How many of each product I can make
  - I would like to be able to update the products BOM at any time, as well as the stock list.
  - Login/logout should be quick and easy.
         
- First time visitor goals:
  - Have the first visit easily explain the site, how it works, what it can do, etc.
  - Have the app be easy to navigate and intuitive to user.
  - Be able to sign up for an account as easily as possible.

- Returning visitor goals:
  - Be able to login and see data stored from previous visits.
  - Be able to easily login and view my data.

- Frequent user goals:
  - Be able to quickly see what I have in stock and how many products I can make.
  - Be able to add new products and/or stock quickly and easily and see that
    immediately reflected in the interface.

- Admin user goals:
  - Have access to other user data to be able to check for and remove objectionable inputs.

- Site owner goals: 
  - Have the interface be easy to navigate and reflect recent actions to the user. 
  - Show the user exactly how many of each product they can make.
  - Have user data be only accessable to that specific user.

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

### Design
- Color Scheme
  - Sleek, black on white with sophisticated color scheme accents to portray professionalism.

- Typography
  - Nanum Gothic is and easy to read, block-like typeface. The motif of the app is professional which the font follows.

- Imagery
  - No imagery as the app is informational based. Screenshots on the home page and the "how-to-use" page to show functionality and use.

- Wireframes 
  - 


<!-- HTML used instead of markdown to control image size as images were very large when testing. -->

## Features

### Existing features
- Users can add stock and products, as well as link stock items to products.
- The app will show users exactly how many of each product the user can make given the amount of stock they have.
- The app has all features of CRUD functionality.

### Landing page

- The landing page has two versions of itself: a logged in and a logged out version. The logged out landing page gives brief information about the app and a help guide as to how the app works. The logged in landing page allows a user user access to their stock list and product list. From these pages they can manipulate their data however they choose to.

## Future updates

- An orders page where users can specify how many of each product they need to make, and the app with tell them how many they can make, and how much stock they would need to aquire to complete each order.
- Roles relevant to different departments. For example:
  - Managers: Full access to all features
  - Sales: Able to add, update, and change orders
  - Storage: Able to change stock numbers and items
  - Production Hands: Able to read data but not able to change or update data.

## Languages Used

- HTML5
- CSS3
- JavaScript
- Python and Django

## Frameworks used

- [Google Fonts](https://fonts.google.com/)
- Git
- GitHub
- jQuery

## Agile development

- The project was constructed using Agile methodology, as can be seen in the GitHub repository's Projects section. 
<!-- Explain how cards were transferred from paper / Word doc to projects section half way through development -->
<!-- Show images / screenshots of early project goals -->

## Using the app

- 
- 
- 

## Testing

<!-- Talk about unitest first -->
- The original project was constructed on a laptop with a screen size of 12.3 inches. The code was also put through validators and passed through without any issues.

  - [W3C Markup Validator]()

  - [W3C CSS Validator]()

  - Javascript Validator - JShint
  <!-- Images here -->

  - The JavaScript code was passed with /* jshint esversion: 6 */ above it which removed warnings for setting variables with 'let'.

### Known bugs

## Further testing
- The site was tested on Google Chrome using their developer tools and viewed on Firefox, Microsoft Edge, and Safari to ensure it worked across multiple platforms. The site was also viewed on multiple devices of varying screen sizes and this continued to not be an issue in actual use.
<!-- Say more  -->

- Google Chrome's DevTools Lighthouse:
  - Desktop
        ![Lighthouse score for desktop]()
  - Mobile
        ![Lighthouse score for mobile]()

## Deployment 
<!-- Heroku deployment here -->
<!-- Deployment code and content taken straight from Code Institutes README template -->

- You can view the live site [here]().

## Credits 

### Code

- Code
  - All code was written by the developer.

### Content

- Content
  - All content was written by the developer.

### Acknowledgements
    
- Tutor support at Code Institute for all their support throughout.

- Friends and family for viewing the site and giving feedback.