Please note: There are 2 branches created for this capstone project - 'initial' and 'fancy'.
For the 'initial' branch, it should have all the files that fulfill the assignment objectives for the capstone project.
For the 'fancy' branch, I wanted to incorporate the html templates to the endpoints and test its functionality.

To grade the assignment files in the 'initial' branch, perform the following at the project directory before running the server:
    git checkout intial

To grade the assignment files in the 'fancy' branch, perform the following at the project directory before running the server:
    git checkout fancy

The localhost is 127.0.0.1:8000 and this project uses MySQL as the local back-end database (at Port 3306), which resides on your machine.
Please configure your MySQL settings at the project's settings.py file accordingly.
A guide on populating your database (for the Menu table) will be provided at the last section of this readme file.

The following endpoints are available for testing using the 'POST' method with JSON:
/auth/users                     ["username", "password", "email" (optional)]
/auth/token/login               ["username", "password"]
/restaurant/api-token-auth      ["username", "password"] (Note: This is functionally the same as /auth/token/login)
/restaurant/menu                ["title", "price", "inventory"]
/restaurant/book                ["name", "no_of_guests", "bookingDate"] (authentication token required)

Note: "bookingDate" should be in the format of "%Y-%M-%DT%H:%M" when using JSON. For example, "2023-02-07T12:30".

The following endpoints are available for testing using the 'GET' method:
/restaurant/                    (static content)
/restaurant/about               (static content)
/restaurant/menu
/restaurant/bookings            (authentication token required)

The following endpoints require authentication token:
/restaurant/book
/restaurant/bookings

For unit testing, please run the following command at the project directory:
    python manage.py test tests

Populating the Menu table
-------------------------
When checking out the 'fancy' branch, I've prepared images to display alongside its name and price. 
The images will only show up if the 'title' of the menu item matches the image filename. 
Here are the 'title' labels and images I've used for my project:
    Grilled Fish
    Grilled Pork Chop
    New York Steak
    Chicken Kebab
    Spaghetti alle Vongole

