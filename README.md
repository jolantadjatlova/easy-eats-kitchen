# [Easy Eats Kitchen](https://easy-eats-kitchen-c0e4478907ac.herokuapp.com/)

Developer: Jolanta Djatlova ([jolantadjatlova](https://github.com/jolantadjatlova))

Easy Eats Kitchen is a full-stack web application that allows users to browse, search, and filter recipes, while registered users can create, edit, and delete their own recipes.

The application focuses on clean UX design, accessibility, and secure authentication, providing a simple and practical solution for everyday meal planning with full CRUD functionality.

![screenshot](docs/am_i_responsive.png) 


### Contents

- [UX](#ux)
  - [The 5 Planes of UX](#the-5-planes-of-ux)
    - [1. Strategy](#1-strategy)
    - [2. Scope](#2-scope)
    - [3. Structure](#3-structure)
    - [4. Skeleton](#4-skeleton)
    - [5. Surface](#5-surface)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)

- [Design Choices](#design-choices)
  - [Wireframes](#wireframes)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Images](#images)
  - [Responsiveness](#responsiveness)

- [Agile Development Process](#agile-development-process)
  - [Planning Tools & Workflow](#planning-tools--workflow)
    - [GitHub Projects (Kanban)](#github-projects-kanban)
    - [GitHub Issues](#github-issues)
    - [MoSCoW Prioritization](#moscow-prioritization)

- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Enhancements](#future-enhancements)

- [Data Model & Relationships](#data-model--relationships)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Models](#database-models)
  - [Database Relationships Summary](#database-relationships-summary)
  - [Database Implementation](#database-implementation)

- [CRUD Functionality](#crud-functionality)
- [Security Features](#security-features)
- [Technologies Used](#technologies-used)

- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Responsiveness Test](#responsiveness-test)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
  - [User Story Testing](#user-story-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Browser Testing](#browser-testing)

- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [Cloudinary](#cloudinary)
  - [PostgreSQL Database](#postgresql-database)
  - [WhiteNoise](#whitenoise)
  - [Local Development](#local-development)
    - [To Clone the Project](#to-clone-the-project)
  - [To Fork the Project](#to-fork-the-project)

- [Credits](#credits)
  - [Feedback, Advice and Support](#feedback-advice-and-support)
  - [Learning Help and Resources](#learning-help-and-resources)
  - [Images](#images-1)


## UX
### The 5 Planes of UX
#### 1. Strategy
##### Purpose
- Provide a simple and welcoming platform for users to discover and share recipes.
- Allow users to quickly find meal ideas based on time, category, or personal preferences.
- Encourage user engagement through recipe creation and personal recipe management.
- Offer a visually appealing and easy-to-use interface that supports stress-free cooking inspiration.

##### Primary User Needs
- Easily browse and view recipes without needing to create an account.
- Quickly search and filter recipes to find suitable meal ideas.
- Access clear and readable recipe information, including ingredients and method steps.
- Create an account to create, manage, and publish personal recipes.
- Access the website seamlessly across mobile, tablet, and desktop devices.

##### Project Goals
- Build a full-stack Django application demonstrating CRUD functionality.
- Implement user authentication to support personalised features.
- Apply UX best practices, including intuitive navigation and responsive design.
- Use consistent styling and clear typography to support readability and usability.


#### 2. Scope

##### Functional Requirements
- Users can browse a list of recipes without needing to create an account.
- Users can view full recipe details (ingredients and method steps) directly within the recipes list using an accordion layout.
- Users can search for recipes using keywords.
- Users can filter recipes by category.
- Users can register for an account and log in securely.
- Authenticated users can create new recipes.
- Authenticated users can edit their own recipes.
- Authenticated users can delete their own recipes.
- Users can log out of their account.
- The website provides clear UI feedback when forms are submitted or actions are completed.

##### Content Requirements
- Recipe titles, images, ingredients, and method instructions.
- Category-based recipe organisation.
- Clear navigation labels and page headings.
- Form labels and validation messages to guide user input.
- Accessible text and color contrast for readability.


#### 3. Structure

##### Interaction Design
The website follows a simple and intuitive user flow focused on recipe discovery and management. Public users can browse, search, and filter recipes, while authenticated users can access additional features such as creating and managing their own recipes. Clear UI feedback is provided throughout user interactions.

##### Information Architecture
Content is organised into clear sections including the homepage, recipe listings with an accordion interface for viewing full recipe details (ingredients and method), and user account functionality. Categories are used to group recipes and support easy navigation. A consistent layout is maintained across all pages using Bootstrap’s grid system.

##### Navigation Layout
A persistent navigation bar provides access to key areas of the site, including Home, Categories, and user-specific options. The navigation collapses into a mobile-friendly menu on smaller screens to ensure usability across devices.

##### User Flow
Users arrive on the homepage and can immediately browse or search for recipes. Authenticated users are able to add and manage recipes, while public users can continue browsing without registering.


#### 4. Skeleton

Wireframes were used to plan page layout, navigation placement, and content hierarchy before visual styling was applied. Key interface elements such as the navigation bar, search functionality, recipe cards, and forms were positioned to ensure clarity and ease of use across different screen sizes.

The wireframes created can be viewed in the [Wireframes](#wireframes) section.


#### 5. Surface

The surface design of *Easy Eats Kitchen* focuses on creating a warm, welcoming, and food-inspired visual experience. Natural imagery, soft neutral backgrounds, and earthy accent colours help convey a sense of comfort and home cooking. The interface prioritises clarity and readability, ensuring users can easily focus on discovering and managing recipes.

Further visual decisions are detailed in the [Typography](#typography) and [Colour Scheme](#colour-scheme) sections.


[Back to contents](#contents)

---
### User Goals

#### Public Users
- To browse and view recipes without needing to create an account.
- To search and filter recipes in order to quickly find suitable meal ideas.

#### Authenticated Users
- To create an account and log in securely to access additional features.
- To create, edit, and manage personal recipes in one place.
- To receive clear feedback when performing actions such as creating, editing, or deleting content.


### User Stories

#### Public Users
- As a public user, I want to browse a list of recipes and view full recipe details (ingredients and method steps) so that I can find inspiration and cook a meal.  
- As a public user, I want to filter recipes by category so that I can quickly find recipes that suit my preferences.  
- As a public user, I want to search for recipes by keyword so that I can locate specific dishes quickly.

#### Authenticated Users
- As an authenticated user, I want to create an account so that I can create and manage my own recipes.  
- As an authenticated user, I want to log in to my account so that I can access recipe management features.  
- As an authenticated user, I want to create new recipes so that I can save and share my own recipes.  
- As an authenticated user, I want to edit my own recipes so that I can update ingredients or method steps when needed.  
- As an authenticated user, I want to delete my own recipes so that I can remove recipes I no longer want.  




[Back to contents](#contents)

---

## Design Choices

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.

- [Landing Page (Guest View)](docs/landing_page_guest_view_wireframe.png)
- [Landing Page (Logged-in View)](docs/landing_post_log_in_view_wireframe.png)

- [Recipes (All)](docs/recipes_wireframes.png)
- [My Recipes](docs/my_recipes_wireframes.png)

- [Add Recipe Form](docs/add_recipe_form_wireframes.png)

- [Sign Up](docs/sign_up_wireframe.png)
- [Sign In](docs/sign_in_wireframe.png)

- [404 Page](docs/404_page_wireframes.png)
- [500 Page](docs/500_page_wireframes.png)


### Typography

- The **Playfair Display** typeface is used for headings to create a warm, recipe-style aesthetic that reflects the home-cooking theme of the project.  
- **Lato** is used for body text and navigation due to its clean, simple letterforms, ensuring good readability across different screen sizes.  
- Varying font weights are used to establish clear visual hierarchy between headings, navigation elements, and content text.  
- This typography pairing supports a welcoming and approachable interface while keeping the layout clear and easy to navigate.


### Colour Scheme

The colour palette was designed using [Coolors](https://coolors.co/) and inspired by the *Easy Eats Kitchen* hero imagery and overall food theme. It combines warm, earthy tones with soft neutral colours to create a natural and welcoming feel that reflects home cooking and fresh ingredients. Accent colours are used to highlight interactive elements while keeping the interface calm and easy to navigate.

![Easy Eats Kitchen Colour Palette](docs/easy-eats-palette.png)

### Contrast Grid

A contrast grid was used to ensure that text and interactive elements meet accessibility guidelines for contrast and readability across all device types.

![Easy Eats Kitchen Contrast Grid](docs/easy-eats-contrast-grid.png)

[Back to contents](#contents)
---

### Images

The background image used on the *Easy Eats Kitchen* homepage was **generated using ChatGPT (AI image generation)**.

Category images (*15 Min Meals*, *Meat*, *Fish*, *Vegetarian*) were also **AI-generated using ChatGPT** to maintain a consistent visual style across the application and support category-based navigation.

Recipe images are optional and can be uploaded by authenticated users when creating or editing a recipe. These images are displayed within recipe views and are stored and served using **Cloudinary**.

All imagery is designed to remain **non-intrusive**, ensuring that text, navigation, and interactive elements remain clear and accessible.

All images include **descriptive `alt` attributes** to support accessibility.

---
### Responsiveness

The *Easy Eats Kitchen* application is fully responsive and adapts to different screen sizes using **Bootstrap’s responsive grid system**.

The layout, typography, and interactive elements adjust to maintain usability across mobile, tablet, and desktop devices.

- Navigation collapses into a mobile-friendly menu on smaller screens.
- Images, forms, and recipe content scale appropriately without layout issues.
- Buttons and inputs remain accessible and easy to use on touch devices.

Responsiveness was tested using browser developer tools and manual viewport resizing.  
Further details can be found in the **Responsiveness Test** section.


[Back to contents](#contents)

## Agile Development Process

Easy Eats Kitchen was developed using an iterative Agile approach, focusing on delivering a clear and user-friendly Minimum Viable Product (MVP). Development was carried out in small, manageable stages, allowing functionality to be built, tested, and refined incrementally.

The workflow was managed using GitHub Projects (Kanban board) and GitHub Issues, where user stories and tasks were prioritised using the MoSCoW method. This ensured that core functionality such as recipe browsing, searching, authentication, and CRUD operations was implemented first, followed by usability and design improvements.

The overall scope and requirements of the project are outlined in the 5 Planes of UX section.

[Back to contents](#contents)

---

### Planning Tools & Workflow

To stay organised and maintain an Agile workflow throughout development, the following tools were used:

#### GitHub Projects (Kanban)
A Kanban board was created using [GitHub Projects](https://github.com/users/jolantadjatlova/projects/14) to visually manage tasks and track progress. Tasks were broken down into user stories and categorised by status:

- To Do  
- In Progress  
- Done  

This approach helped to:
- Track development progress clearly
- Maintain focus on achievable goals
- Manage workload effectively throughout the project

![GitHub Projects Board](docs/easy-eats-kitchen-project-board.png)

#### GitHub Issues

GitHub Issues were used to record user stories, development tasks and potential features, with labels applied.

Each issue included clear acceptance criteria and was linked to the relevant stage of development, supporting traceability and structured progress.

![GitHub Issues](docs/easy-eats-github-issues.png)

#### MoSCoW Prioritization

The MoSCoW prioritisation method was used to classify tasks as Must Have, Should Have or Could Have. This helped ensure that essential functionality was delivered within the project timeframe while allowing flexibility for future enhancements.


[Back to contents](#contents)

---

## Features

### Existing Features

#### Navbar

A single, responsive navigation bar is used across the entire site to provide consistent access to key areas of the application.

The navbar displays the *Easy Eats Kitchen* brand on the left and navigation links on the right. Navigation options update dynamically based on authentication status.

On smaller screens, the navbar collapses into a hamburger menu using Bootstrap’s built-in responsive behaviour.

Key features include:
- Clear site branding
- Authentication-aware navigation links
- Hover and focus styles to indicate active links
- Responsive collapse for mobile and tablet devices

[Desktop navbar](docs/navbar-desktop.png "Desktop navbar")

[Mobile navbar collapsed](docs/navbar-mobile-collapsed.png "Mobile navbar collapsed")

[Mobile navbar expanded](docs/navbar-mobile-expanded.png "Mobile navbar expanded")

---

#### Home Page

The home page acts as a welcoming entry point, allowing users to begin browsing recipes immediately without needing to register.

The page includes:
- A prominent recipe search bar
- A short welcome message introducing the site’s purpose
- Category-based navigation using visual imagery

The layout is clean and uncluttered, encouraging quick discovery of recipes while remaining accessible across all screen sizes.

[Desktop home view](docs/home-desktop.png "Home page desktop view")

[Tablet home view](docs/home-tablet.png "Home page tablet view")

[Mobile home view](docs/home-mobile.png "Home page mobile view")

---

#### Recipe Search

Users can search for recipes using keywords to quickly find relevant results.

The search functionality:
- Matches recipe titles, ingredients, and method content
- Is available to both public and authenticated users
- Updates results clearly based on the entered query

This feature improves usability by reducing the time needed to locate specific recipes.

[Recipe search bar](docs/search-bar.png "Recipe search bar")

---

#### Category Browsing

Recipes are organised into predefined categories to support intuitive navigation.

Available categories include:
- 15 min meals
- Meat
- Fish
- Vegetarian

Each category page displays only relevant recipes and supports optional keyword searching within that category.

[Category page view](docs/category-view.png "Category page view")

---

#### User Registration

New users can register for an account using a secure and user-friendly form.

The registration process includes:
- Clear form labels and guidance
- Automatic validation of required fields
- Password requirements enforced by Django

Upon successful registration, users gain access to recipe management features.

[Registration page](docs/register.png "User registration page")

---

#### Login and Logout

Registered users can log in and out securely using Django Allauth.

Key features include:
- Secure authentication handling
- Clear success messages on login and logout
- Navigation updates based on authentication status
- Redirects to appropriate pages after authentication actions

[Login page](docs/login.png "Login page")

[Logout confirmation](docs/logout.png "Logout confirmation")

---

#### Add Recipe

Authenticated users can create new recipes using a structured form.

The add recipe form allows users to:
- Enter a recipe title
- Select a category
- Upload an optional image
- Add ingredients and method steps using a rich text editor

Successful submissions display confirmation feedback and redirect users to their personal recipe list.

[Add recipe form](docs/add-recipe.png "Add recipe form")

---

#### Edit Recipe

Users can edit recipes they own.

Key features include:
- Edit access restricted to recipe owners only
- Pre-populated form fields for ease of editing
- Confirmation feedback after successful updates

This ensures users maintain full control over their own content.

[Edit recipe form](docs/edit-recipe.png "Edit recipe form")

---

#### Delete Recipe

Users can delete recipes they own through a confirmation step.

Key features include:
- Ownership-based access control
- Confirmation prompt to prevent accidental deletion
- Clear success message after deletion

[Delete recipe confirmation](docs/delete-recipe.png "Delete recipe confirmation")

---

#### My Recipes Page

The My Recipes page provides authenticated users with a central place to manage their own content.

Features include:
- Display of only the logged-in user’s recipes
- Recipes ordered by most recent creation
- Keyword search within personal recipes
- Quick access to edit and delete actions

[My Recipes page](docs/my-recipes.png "My Recipes page")

---

#### User Feedback Messages

Clear feedback messages are shown following key user actions.

Messages are displayed for:
- Successful recipe creation, editing, and deletion
- Invalid form submissions
- Authentication-related actions

Feedback messages improve clarity and user confidence throughout the application.

[Success message example](docs/success-message.png "Example of user feedback message")

---

#### Error Pages

Custom error pages are implemented to improve user experience when an issue occurs.

Included error pages:
- 404 – Page Not Found
- 500 – Server Error

These pages provide clear messaging and maintain visual consistency across the site.

[404 error page](docs/404.png "404 error page")

[500 error page](docs/500.png "500 error page")


[Back to contents](#contents)

---

### Future Enhancements

The following features were identified as potential improvements that could further enhance the functionality and scalability of *Easy Eats Kitchen* if additional development time were available:

- **Recipe Comments**  
  Allow authenticated users to leave comments on recipes to share feedback, tips, and variations. This would encourage user interaction while building on the existing authentication and ownership logic.

- **Favourite Recipes**  
  Enable users to save recipes to a personal favourites list for quick access. This could be implemented using a many-to-many relationship between users and recipes.

- **Multiple Categories per Recipe**  
  Extend the current category structure to allow recipes to belong to multiple categories (for example, a recipe could be categorised as both *Fish* and *15 Minute Meals*). This would involve changing the relationship between recipes and categories from one-to-many to many-to-many and updating the filtering logic accordingly.


[Back to contents](#contents)

---

## Data Model & Relationships

The Easy Eats Kitchen application uses a relational database structure with three main models: User, Category, and Recipe. The data model is designed to support full CRUD functionality for recipe management while maintaining clear relationships between entities.

### Entity Relationship Diagram

![Entity Relationship Diagram](docs/entity_relationship_diagram.png)

### Database Models

#### User (Django Authentication)
The User model is provided by Django's built-in authentication system and stores user account information.

**Fields:**
- `id`: AutoField (Primary Key)
- `username`: CharField(150) - Unique username for login
- `email`: EmailField - User's email address
- `password`: CharField(128) - Hashed password

**Relationships:**
- One user can create multiple recipes (One-to-Many with Recipe)

#### Category
The Category model organizes recipes into predefined categories for easy browsing and filtering.

**Fields:**
- `id`: AutoField (Primary Key)
- `name`: CharField(50) - Category name (unique)
- `slug`: SlugField(60) - URL-friendly version of the name (unique, auto-generated)

**Categories available:**
- 15 min meals
- Meat
- Fish
- Vegetarian

**Relationships:**
- One category can contain multiple recipes (One-to-Many with Recipe)

#### Recipe
The Recipe model stores all recipe information created by users.

**Fields:**
- `id`: AutoField (Primary Key)
- `owner`: ForeignKey(User) - Links recipe to the user who created it
- `category`: ForeignKey(Category) - Links recipe to a category (optional, nullable)
- `title`: CharField(120) - Recipe title
- `image`: ImageField - Optional recipe image uploaded by user
- `ingredients`: TextField - List of ingredients (one per line)
- `method`: TextField - Step-by-step cooking instructions
- `created_at`: DateTimeField - Timestamp of recipe creation (auto-generated)
- `updated_at`: DateTimeField - Timestamp of last update (auto-updated)

**Relationships:**
- Each recipe belongs to one user (owner) - Many-to-One with User
- Each recipe can belong to one category - Many-to-One with Category (optional)

### Database Relationships Summary

The application uses **One-to-Many** relationships:

1. **User → Recipe (1:N)**
   - One user can create multiple recipes
   - Each recipe belongs to exactly one user
   - Implemented via ForeignKey on Recipe model
   - `on_delete=CASCADE` ensures recipes are deleted when user is deleted

2. **Category → Recipe (1:N)**
   - One category can contain multiple recipes
   - Each recipe can belong to one category (optional)
   - Implemented via ForeignKey on Recipe model
   - `on_delete=SET_NULL` ensures recipes remain if category is deleted

### Database Implementation

The application uses **PostgreSQL** as the production database (via Heroku) and SQLite3 for local development. Django's ORM abstracts the database layer, allowing the same models to work with both database systems seamlessly.

**Production Database:**
- PostgreSQL (managed by Heroku Postgres)
- Connection configured via `DATABASE_URL` environment variable
- Parsed using `dj-database-url` package

**Local Development Database:**
- SQLite3 (Django default)
- Stored in `db.sqlite3` file (excluded from git)

[Back to contents](#contents)

---

## CRUD Functionality

The application provides full CRUD (Create, Read, Update, Delete) functionality for recipe management:

| Operation | View | Access | Description |
|-----------|------|--------|-------------|
| **Create** | `add_recipe` | Authenticated users | Create new recipes with title, category, image, ingredients, and method using a form with rich text editor |
| **Read** | `recipes_list`, `recipes_by_category`, `my_recipes` | Public (general recipes) / Authenticated (personal recipes) | Browse, search, and view recipe details with accordion interface |
| **Update** | `edit_recipe` | Recipe owner only | Edit existing recipes with pre-populated form data |
| **Delete** | `delete_recipe` | Recipe owner only | Delete recipes with confirmation step to prevent accidents |



[Back to contents](#contents)

---

## Security Features

### Authentication & Authorisation
- User authentication is implemented using **Django Allauth**.
- Only authenticated users can access protected functionality such as creating, editing, and deleting recipes.
- Users are restricted to editing and deleting **only their own recipes**.

### Access Control
- Django’s `@login_required` decorator is used to protect private views.
- Unauthorised access attempts redirect users to the login page.

### Form Validation
- Django ModelForms are used to validate user input.
- Required fields and data types are enforced automatically by Django.
- Invalid form submissions are rejected with clear user feedback messages.

### CSRF Protection
- Django’s built-in Cross-Site Request Forgery (CSRF) protection is enabled on all forms.
- CSRF tokens prevent unauthorised or malicious form submissions.

### Environment Variables & Secure Configuration
- Sensitive data such as `SECRET_KEY`, database credentials, and configuration values are stored in environment variables.
- No sensitive information is committed to the repository.
- `DEBUG` mode is controlled via environment variables and defaults to `False` in production.


[Back to contents](#contents)

---

## Technologies Used

| Technology | Purpose | Type |
|-------------|----------|------|
| [Git](https://git-scm.com/) | Track changes and manage version control throughout development. | Tool |
| [GitHub](https://github.com/) | Store the project repository and manage commits and issues. | Tool |
| [VS Code](https://code.visualstudio.com/) | Write, edit, and organise all project code. | Tool |
| [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) | Structure page content and templates. | Language |
| [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) | Style the user interface and control layout and presentation. | Language |
| [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | Enhance interactivity and user experience. | Language |
| [Python](https://www.python.org/) | Implement backend logic, views, and data handling. | Language |
| [Django](https://www.djangoproject.com/) | Backend framework used to build the full-stack application. | Framework |
| [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) | Handle user authentication and account management. | Library |
| [Bootstrap 5](https://getbootstrap.com/) | Provide responsive layout and UI components. | Library |
| [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) | Improve form rendering and styling with Bootstrap. | Library |
| [Django Summernote](https://github.com/summernote/django-summernote) | Provide a rich text editor for recipe content. | Library |
| [PostgreSQL](https://www.postgresql.org/) | Production database for storing application data. | Database |
| [SQLite3](https://www.sqlite.org/index.html) | Local development database. | Database |
| [Cloudinary](https://cloudinary.com/) | Store and serve user-uploaded recipe images. | Cloud Service |
| [Heroku](https://www.heroku.com/) | Deploy and host the live application. | Platform |
| [Balsamiq](https://balsamiq.com/) | Create wireframes for planning page layout and user flow. | Tool |
| [Coolors](https://coolors.co/) | Generate and refine the project colour palette. | Tool |
| [Eight Shapes Contrast Grid](https://contrast-grid.eightshapes.com/) | Test colour contrast and accessibility compliance. | Tool |
| [Squoosh](https://squoosh.app/) | Compress and convert images to WebP format for improved performance. | Tool |
| [remove.bg](https://www.remove.bg/) | Remove image backgrounds for cleaner visuals and consistent presentation. | Tool |
| [Google Fonts](https://fonts.google.com/) | Import and apply typography used across the site. | Library |
| [Font Awesome](https://fontawesome.com/) | Add icons to enhance usability and visual clarity. | Library |
| [ChatGPT](https://chat.openai.com/) | Assist with content writing, code refinement, and AI-generated imagery. | AI |
| [W3C HTML Validation Service](https://validator.w3.org/) | Validate HTML structure and syntax. | Tool |
| [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) | Validate CSS syntax and styling rules. | Tool |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) | Test performance, accessibility, and best practices. | Tool |
| [WAVE](https://wave.webaim.org/) | Evaluate accessibility compliance. | Tool |



[Back to contents](#contents)

---

## Testing

### Automated Testing

Automated testing was implemented using Django’s built-in testing framework.

Tests were written for:
- Models (data integrity and relationships)
- Forms (validation of required fields)
- Views (page loading, authentication, permissions, and CRUD functionality)

All tests were run using the following command:

`python manage.py test --verbosity=2`

This command displays individual test cases and confirms that all components of the application behave as expected.

![Automated tests passing](docs/automated_tests.png)


### Bugs

| **Bug** | **Status** | **Description** | **Steps to Resolve** |
|--------|------------|-----------------|----------------------|
| Low contrast search results message | Fixed | The “Found X matching recipes” message appeared in a default Bootstrap grey, making it difficult to read against the background image. | Added custom styling with improved contrast, background colour, border, and font weight to enhance readability. |
| Long recipe content caused layout overflow on mobile | Fixed | Recipes with long ingredient lists or method steps caused vertical overflow and layout issues on smaller screens. | Applied a maximum height and enabled vertical scrolling within the recipe content container. |
| Category dropdown difficult to use on mobile | Fixed | Category dropdown links were too small on mobile devices, making them difficult to tap accurately. | Increased padding and added hover and focus styles to improve touch accessibility on smaller screens. |
| Unauthorised users could access edit/delete URLs | Fixed | Although edit and delete buttons were hidden, users could manually access edit or delete URLs for recipes they did not own. | Enforced ownership checks at view level using `get_object_or_404()` filtered by the authenticated user. |
| Search trimming was not applied | Fixed | Searches containing leading or trailing spaces returned no results even when matching recipes existed. | Trimmed whitespace from the search query using `.strip()` before applying database filters. |
| Missing ownership filtering on My Recipes page | Fixed | The My Recipes view did not initially filter recipes by the logged-in user, causing recipes created by other users to appear. | Updated the queryset to filter by `owner=request.user` so only the authenticated user’s recipes are displayed. |
| Static files duplicated locally and missing in production | Fixed | After configuring static files, CSS appeared duplicated locally and some static images did not load on Heroku despite working locally. | Reviewed static files configuration, corrected file paths, and ensured static assets were available for WhiteNoise in production. |


[Back to contents](#contents)

---

### Responsiveness Test

| **Page** | **Mobile** | **Tablet** | **Desktop** | **Notes** |
|-----------|------------|------------|-------------|-----------|
| **Home / Landing** | ![Home Mobile](docs/home-mobile.png) | ![Home Tablet](docs/home-tablet.png) | ![Home Desktop](docs/home-desktop.png) | Works as expected |
| **Recipes (All)** | ![Recipes Mobile](docs/recipes-mobile.png) | ![Recipes Tablet](docs/recipes-tablet.png) | ![Recipes Desktop](docs/recipes-desktop.png) | Works as expected |
| **Recipe Search Results** | ![Search Results Mobile](docs/search-results-mobile.png) | ![Search Results Tablet](docs/search-results-tablet.png) | ![Search Results Desktop](docs/search-results-desktop.png) | Works as expected |
| **Category View** | ![Category Mobile](docs/category-mobile.png) | ![Category Tablet](docs/category-tablet.png) | ![Category Desktop](docs/category-view-desktop.png) | Works as expected |
| **My Recipes** | ![My Recipes Mobile](docs/my-recipes-mobile.png) | ![My Recipes Tablet](docs/my-recipes-tablet.png) | ![My Recipes Desktop](docs/my-recipes-desktop.png) | Works as expected |
| **Add Recipe Form** | ![Add Recipe Mobile](docs/add-recipe-mobile.png) | ![Add Recipe Tablet](docs/add-recipe-tablet.png) | ![Add Recipe Desktop](docs/add-recipe-desktop.png) | Works as expected |
| **Edit Recipe Form** | ![Edit Recipe Mobile](docs/edit-recipe-mobile.png) | ![Edit Recipe Tablet](docs/edit-recipe-tablet.png) | ![Edit Recipe Desktop](docs/edit-recipe-desktop.png) | Works as expected |
| **Delete Confirmation** | ![Delete Mobile](docs/delete-mobile.png) | ![Delete Tablet](docs/delete-tablet.png) | ![Delete Desktop](docs/delete-recipe-desktop.png) | Works as expected |
| **Login** | ![Login Mobile](docs/login-mobile.png) | ![Login Tablet](docs/login-tablet.png) | ![Login Desktop](docs/login-desktop.png) | Works as expected |
| **Register** | ![Register Mobile](docs/register-mobile.png) | ![Register Tablet](docs/register-tablet.png) | ![Register Desktop](docs/register-desktop.png) | Works as expected |



[Back to contents](#contents)

---

### Code Validation

#### HTML

All major templates were tested using the  
[W3C HTML Validator](https://validator.w3.org/)  
to ensure valid, semantic HTML markup and accessibility compliance.

**The following pages were validated with no errors:**

- [Home page](docs/home-html-validator-easy-eats.png)
- [Recipes page](docs/recipes-html-validator-easy-eats.png)
- [Category page](docs/category-html-validator-easy-eats.png)
- [My Recipes page](docs/my-recipes-html-validator-easy-eats.png)
- [Login page](docs/login-html-validator-easy-eats.png)
- [Register page](docs/register-html-validator-easy-eats.png)


[Back to contents](#contents)

---

#### CSS

CSS was tested using the [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/)  
to ensure valid syntax, consistent styling, and cross-browser compatibility.

**The following CSS was validated with no errors:**

- [Custom CSS](docs/css_validator_easy_eats.png)


[Back to contents](#contents)

---

### User Story Testing

### Public Users

| User Story | Result | Pass | Evidence |
|-----------|--------|------|----------|
| As a public user, I want to browse a list of recipes and view full recipe details so that I can find inspiration and cook a meal. | Users can view all recipes and expand individual recipes to see ingredients and method steps without logging in. | Yes | [Recipes List View](docs/recipes-list.png "Recipes List View")<br>[Expanded Recipe View](docs/expanded-recipe-view.png "Expanded Recipe View") |
| As a public user, I want to filter recipes by category so that I can quickly find recipes that suit my preferences. | Recipes are filtered correctly when a category is selected. | Yes | [Category Filter View](docs/category-filter.png "Category Filter View") |
| As a public user, I want to search for recipes by keyword so that I can locate specific dishes quickly. | Keyword search filters recipes by title, ingredients, and method. | Yes | [Search Results View](docs/search-results.png "Search Results View") |

---

### Authenticated Users

| User Story | Result | Pass | Evidence |
|-----------|--------|------|----------|
| As an authenticated user, I want to create an account so that I can create and manage my own recipes. | Users can register successfully using a secure sign-up form. | Yes | [User Registration](docs/user-registration.png "User Registration") |
| As an authenticated user, I want to log in to my account so that I can access recipe management features. | Registered users can log in and access protected pages. | Yes | [User Login](docs/user-login.png "User Login") |
| As an authenticated user, I want to create new recipes so that I can save and share my own recipes. | Logged-in users can add new recipes using a validated form. | Yes | [Add Recipe Form](docs/add-recipe.png "Add Recipe Form")<br>[My Recipes View](docs/my-recipes.png "My Recipes View") |
| As an authenticated user, I want to edit my own recipes so that I can update ingredients or method steps when needed. | Users can edit only recipes they own. | Yes | [Edit Recipe Form](docs/edit-recipe.png "Edit Recipe Form") |
| As an authenticated user, I want to delete my own recipes so that I can remove recipes I no longer want. | Users can delete their own recipes after confirmation. | Yes | [Delete Recipe Confirmation](docs/delete-recipe.png "Delete Recipe Confirmation") |


[Back to contents](#contents)

---
### Accessibility Testing

Accessibility best practices were applied throughout the site, including:

- Semantic HTML structure  
- Clear and consistent navigation  
- Appropriate heading hierarchy  
- Sufficient colour contrast  

The **[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)** was used to evaluate accessibility on key pages of the site. Minor warnings were identified, mainly relating to empty or redundant links generated by icon-based elements. These do not affect usability or prevent users from accessing content.

Accessibility testing was carried out on the following pages:

- [WAVE accessibility evaluation – Home page](docs/accessibility-home.png)
- [WAVE accessibility evaluation – Recipes page](docs/accessibility-recipes.png)
- [WAVE accessibility evaluation – Register page](docs/accessibility-register.png)

### Lighthouse Testing

Easy Eats Kitchen was tested using **Chrome DevTools Lighthouse** to evaluate overall site quality across key performance and accessibility criteria.

The following areas were assessed:

- **Performance** – measures page load speed and responsiveness.  
- **Accessibility** – evaluates usability for all users, including those using assistive technologies.  
- **Best Practices** – checks adherence to modern web development standards.  
- **SEO** – assesses search engine optimisation and discoverability.

---

**Test for Mobile:**  

![Lighthouse Mobile Test](docs/easy_eats_lighthouse_mobile.png)

**Test for Desktop:**  

![Lighthouse Desktop Test](docs/easy_eats_lighthouse_desktop.png)


[Back to contents](#contents)

---

### Browser Testing

| **Browser** | **Pages Tested** | **Result** |
|------------|-----------------|-----------|
| Google Chrome | Home, Recipes, Category, Forms, Authentication | Works as expected |
| Mozilla Firefox | Home, Recipes, Category, Forms, Authentication | Works as expected |
| Microsoft Edge | Home, Recipes, Category, Forms, Authentication | Works as expected |

[Back to contents](#contents)

---

## Deployment

The live deployed application can be found here:  
[Easy Eats Kitchen on Heroku](https://easy-eats-kitchen-c0e4478907ac.herokuapp.com/)

### Heroku Deployment

This project uses **Heroku**, a Platform as a Service (PaaS), to deploy and host the application.

Deployment steps are as follows (after creating a Heroku account):

1. From the Heroku Dashboard, select **New** → **Create new app**.
2. Enter a unique app name, select a region (EU/USA), and click **Create app**.
3. In the app **Settings**, click **Reveal Config Vars** and add the required environment variables.

**Config Vars**

| Key | Value |
|---|---|
| `SECRET_KEY` | your secret key |
| `DEBUG` | `False` |
| `DATABASE_URL` | your PostgreSQL database URL |
| `CLOUDINARY_CLOUD_NAME` | your Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | your Cloudinary API key |
| `CLOUDINARY_API_SECRET` | your Cloudinary API secret |

4. Ensure the following files exist in the repository:
   - `requirements.txt`
   - `Procfile`
   - `.python-version`

**Requirements**
- Install dependencies:
  - `pip3 install -r requirements.txt`
- If you add packages, update the file:
  - `pip3 freeze --local > requirements.txt`

**Procfile**
Create a `Procfile` containing:
- `web: gunicorn easy_eats.wsgi`

*(Replace `easy_eats` with your Django project name if different.)*

**Python version**
Add a `.python-version` file, for example:
- `3.12.0`

5. In the Heroku app **Deploy** tab, connect the app to the GitHub repository.
6. Deploy the project using **Automatic Deploys** (recommended) or **Manual Deploy** from the `main` branch.
7. Once deployed, run database migrations:
   - `python manage.py migrate`
8. Create a superuser (optional):
   - `python manage.py createsuperuser`

---

### Cloudinary

This project uses **Cloudinary** to store and serve uploaded recipe images, as Heroku does not persist user-uploaded media.

To set up Cloudinary:
1. Create a Cloudinary account.
2. Copy your Cloud name, API key, and API secret from the Cloudinary dashboard.
3. Add them to both your local `env.py` file and Heroku Config Vars.

---

### PostgreSQL Database

This project uses **PostgreSQL** for the production database.

To configure PostgreSQL:
1. Create a PostgreSQL database (Heroku Postgres or another provider).
2. Copy the database URL and add it to:
   - your local `env.py` as `DATABASE_URL`
   - Heroku Config Vars as `DATABASE_URL`

---

### WhiteNoise

This project uses **WhiteNoise** to serve static files in production.

WhiteNoise is enabled in `settings.py` by adding:
- `whitenoise.middleware.WhiteNoiseMiddleware`

and configuring static files storage:
- `whitenoise.storage.CompressedManifestStaticFilesStorage`

---

### Local Development

#### To Clone the Project

1. Go to the GitHub repository.
2. Click **Code** and copy the HTTPS link.
3. In your terminal, run:
   - `git clone <repository-url>`
4. Install dependencies:
   - `pip3 install -r requirements.txt`
5. Create an `env.py` file in the project root and add the required environment variables.

Example `env.py`:

```python
import os

os.environ.setdefault("SECRET_KEY", "your-secret-key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DATABASE_URL", "your-database-url")
os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "your-cloud-name")
os.environ.setdefault("CLOUDINARY_API_KEY", "your-api-key")
os.environ.setdefault("CLOUDINARY_API_SECRET", "your-api-secret")
```

6. Run migrations and start the development server:
   - `python manage.py migrate`
   - `python manage.py runserver`



[Back to contents](#contents)

---

### To Fork the Project

Forking the GitHub repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.

- Log in to GitHub.
- Locate the repository.
- Click to open it.
- The fork button is located on the right side of the repository menu.
- To copy the repository to your GitHub account, click the button.



[Back to contents](#contents)
---

## Credits

### Feedback, Advice and Support

- Richey Malhotra – Code Institute tutor, for guidance and feedback throughout the project  
- Peer support and discussion within the Code Institute Slack community

[Back to contents](#contents)

---

### Learning Help and Resources

- [Code Institute](https://codeinstitute.net/) – Full Stack Web Development course materials and project guidance  
- [Django Documentation](https://docs.djangoproject.com/en/4.2/) – Django framework reference and best practices  
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/) – Authentication and account management  
- [Real Python](https://realpython.com/) – Python and Django tutorials and explanations  
- [W3Schools](https://www.w3schools.com/) – Syntax reference and examples  
- [Stack Overflow](https://stackoverflow.com/) – Community knowledge for troubleshooting and debugging  
- [Heroku Documentation](https://devcenter.heroku.com/) – Deployment and configuration guidance  
- [Cloudinary Documentation](https://cloudinary.com/documentation) – Media storage and delivery

[Back to contents](#contents)

---

### Images

- The homepage background image and category images (*15 Min Meals*, *Meat*, *Fish*, *Vegetarian*) were **AI-generated using [ChatGPT](https://chatgpt.com/)** to maintain a consistent visual style.
- Recipe images are optional and can be uploaded by authenticated users; these images are stored and served using **[Cloudinary](https://cloudinary.com/)**.
- Images were optimised for performance using **[Squoosh](https://squoosh.app/)**.
- All images include descriptive `alt` attributes to support accessibility.

[Back to contents](#contents)

---
