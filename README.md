# [Easy Eats Kitchen](https://easy-eats-kitchen-c0e4478907ac.herokuapp.com/)

Developer: Jolanta Djatlova ([jolantadjatlova](https://github.com/jolantadjatlova))

Easy Eats Kitchen is a full-stack web application that allows users to browse, search, and filter recipes, while registered users can create, edit, and delete their own recipes.

The application focuses on clean UX design, accessibility, and secure authentication, providing a simple and practical solution for everyday meal planning with full CRUD functionality.


### Contents

- [UX](#ux)
  - [The 5 Planes of UX](#the-5-planes-of-ux)
    - [1. Strategy](#1-strategy)
    - [2. Scope](#2-scope)
    - [3. Structure](#3-structure)
    - [4. Skeleton](#4-skeleton)
    - [5. Surface](#5-surface)
  - [User Goals](#user-goals)
    - [Visitor Goals](#visitor-goals)
    - [Authenticated User Goals](#authenticated-user-goals)
    - [Administrator Goals](#administrator-goals)
  - [User Stories](#user-stories)
    - [Visitor Stories](#visitor-stories)
    - [Authenticated User Stories](#authenticated-user-stories)
    - [Administrator Stories](#administrator-stories)

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
    - [Global Features](#global-features)
    - [Home Page](#home-page)
    - [Recipes Page](#recipes-page)
    - [Recipe Detail Page](#recipe-detail-page)
    - [Add Recipe Page](#add-recipe-page)
    - [Authentication Pages](#authentication-pages)
    - [Error Pages](#error-pages)
  - [Future Enhancements](#future-enhancements)

- [Data Model & Relationships](#data-model--relationships)
- [CRUD Functionality](#crud-functionality)
- [Security Features](#security-features)
- [Technologies Used](#technologies-used)

- [Testing](#testing)
  - [Bugs](#bugs)
  - [Responsiveness Test](#responsiveness-test)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
  - [User Story Testing](#user-story-testing)
  - [Form Validation Testing](#form-validation-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Browser Testing](#browser-testing)

- [Deployment](#deployment)
  - [To Deploy the Project](#to-deploy-the-project)
  - [To Fork the Project](#to-fork-the-project)
  - [To Clone the Project](#to-clone-the-project)

- [Credits](#credits)
  - [Feedback, Advice and Support](#feedback-advice-and-support)
  - [Learning Help and Resources](#learning-help-and-resources)
  - [Images](#images)

- [Final Tidy-Up](#final-tidy-up)

## UX

[Back to contents](#contents)

---

### The 5 Planes of UX

[Back to contents](#contents)

---

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
- Create an account to save, manage, and share personal recipes.
- Access the website seamlessly across mobile, tablet, and desktop devices.

##### Project Goals
- Build a full-stack Django application demonstrating CRUD functionality.
- Implement user authentication to support personalised features.
- Apply UX best practices, including intuitive navigation and responsive design.
- Use consistent styling and clear typography to support readability and usability.


[Back to contents](#contents)

---

#### 2. Scope

##### Functional Requirements
- Users can browse a list of recipes without needing to create an account.
- Users can view individual recipe detail pages containing ingredients and method steps.
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


[Back to contents](#contents)

---

#### 3. Structure

##### Interaction Design
The website follows a simple and intuitive user flow focused on recipe discovery and management. Public users can browse, search, and filter recipes, while authenticated users can access additional features such as creating and managing their own recipes. Clear UI feedback is provided throughout user interactions.

##### Information Architecture
Content is organised into clear sections including the homepage, recipe listings, recipe detail pages, and user account functionality. Categories are used to group recipes and support easy navigation. A consistent layout is maintained across all pages using Bootstrap’s grid system.

##### Navigation Layout
A persistent navigation bar provides access to key areas of the site, including Home, Categories, and user-specific options. The navigation collapses into a mobile-friendly menu on smaller screens to ensure usability across devices.

##### User Flow
Users arrive on the homepage and can immediately browse or search for recipes. Authenticated users are able to add and manage recipes, while public users can continue browsing without registering.


[Back to contents](#contents)

---

#### 4. Skeleton

Wireframes were used to plan page layout, navigation placement, and content hierarchy before visual styling was applied. Key interface elements such as the navigation bar, search functionality, recipe cards, and forms were positioned to ensure clarity and ease of use across different screen sizes.

The wireframes created can be viewed in the [Wireframes](#wireframes) section.



[Back to contents](#contents)

---

#### 5. Surface



[Back to contents](#contents)

---

### User Goals

#### Public Users
- To browse and view recipes without needing to create an account.
- To search and filter recipes in order to quickly find suitable meal ideas.
- To explore recipe content and read comments before deciding to register.

#### Authenticated Users
- To create an account and log in securely to access additional features.
- To create, edit, and manage personal recipes in one place.
- To interact with other users by leaving comments and sharing cooking tips.
- To receive clear feedback when performing actions such as creating, editing, or deleting content.



[Back to contents](#contents)

---

### User Stories

#### Public Users
- As a public user, I want to browse a list of recipes and view individual recipe details so that I can find inspiration and cook a meal.  
- As a public user, I want to filter recipes by category so that I can quickly find recipes that suit my preferences.  
- As a public user, I want to search for recipes by keyword so that I can locate specific dishes quickly.

#### Authenticated Users
- As an authenticated user, I want to create an account so that I can create and manage my own recipes.  
- As an authenticated user, I want to log in to my account so that I can access recipe management features.  
- As an authenticated user, I want to create new recipes so that I can save and share my own recipes.  
- As an authenticated user, I want to edit my own recipes so that I can update ingredients or method steps when needed.  
- As an authenticated user, I want to delete my own recipes so that I can remove recipes I no longer want.  
- As an authenticated user, I want to leave comments on recipes so that I can share feedback and tips with other users.



[Back to contents](#contents)

---

## Design Choices



[Back to contents](#contents)

---

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

[Back to contents](#contents)

---

### Typography

- The **Playfair Display** typeface is used for headings to create a warm, recipe-style aesthetic that reflects the home-cooking theme of the project.  
- **Lato** is used for body text and navigation due to its clean, simple letterforms, ensuring good readability across different screen sizes.  
- Varying font weights are used to establish clear visual hierarchy between headings, navigation elements, and content text.  
- This typography pairing supports a welcoming and approachable interface while keeping the layout clear and easy to navigate.


[Back to contents](#contents)

---

### Colour Scheme

The colour palette was designed using [Coolors](https://coolors.co/) and inspired by the *Easy Eats Kitchen* hero imagery and overall food theme. It combines warm, earthy tones with soft neutral colours to create a natural and welcoming feel that reflects home cooking and fresh ingredients. Accent colours are used to highlight interactive elements while keeping the interface calm and easy to navigate.

![Easy Eats Kitchen Colour Palette](docs/easy-eats-palette.png)

![Easy Eats Kitchen Contrast Grid](docs/easy-eats-contrast-grid.png)



[Back to contents](#contents)

---

### Images



[Back to contents](#contents)

---

### Responsiveness



[Back to contents](#contents)
## Agile Development Process

[Back to contents](#contents)

---

### Planning Tools & Workflow



[Back to contents](#contents)

---

#### GitHub Projects (Kanban)



[Back to contents](#contents)

---

#### GitHub Issues



[Back to contents](#contents)

---

#### MoSCoW Prioritization



[Back to contents](#contents)

---

### Images



[Back to contents](#contents)

---

### Responsiveness



[Back to contents](#contents)

---

## Features

[Back to contents](#contents)

---

### Existing Features



[Back to contents](#contents)

---

### Future Enhancements



[Back to contents](#contents)

---

## Data Model & Relationships


[Back to contents](#contents)

---

## CRUD Functionality



[Back to contents](#contents)

---

## Security Features


[Back to contents](#contents)

---

## Technologies Used



[Back to contents](#contents)

---

## Testing

[Back to contents](#contents)

---

### Bugs


[Back to contents](#contents)

---

### Responsiveness Test



[Back to contents](#contents)

---

### Code Validation

[Back to contents](#contents)

---

#### HTML


[Back to contents](#contents)

---

#### CSS


[Back to contents](#contents)

---

#### JavaScript



[Back to contents](#contents)

---

### User Story Testing



[Back to contents](#contents)

---

### Form Validation Testing


[Back to contents](#contents)

---

### Lighthouse Testing



[Back to contents](#contents)

---

### Browser Testing


[Back to contents](#contents)

---

## Deployment

[Back to contents](#contents)

---

### To Deploy the Project



[Back to contents](#contents)

---

### To Fork the Project



[Back to contents](#contents)

---

### To Clone the Project



[Back to contents](#contents)

---

## Credits

[Back to contents](#contents)

---

### Feedback, Advice and Support



[Back to contents](#contents)

---

### Learning Help and Resources



[Back to contents](#contents)

---

### Images



[Back to contents](#contents)

---

## Final Tidy-Up



[Back to contents](#contents)