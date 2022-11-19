# Idea is to create an application for selling old staff

1. Install Flask
   $ python3 -m pip install flask

2. To run flask server for Mac
   !!! You should be in the folder where your file is located
   $ export FLASK_APP=app.py
   $ export FLASK_ENV=development
   $ flask run


$ pip freeze > requirements.txt


3. Take a look again Chapter 4 - video 7 about reCAPTCHA and implement it
4. update a link for jQuery - copy the link from the official web site








Требования:
1. Should be used POST method for sending FORMs 
FOR ME - MAKE IT WITH GET METHOD 
   
2. Flash message after adding a new Item should be blue coloure
FOR ME - current implementation is green
detailes here - https://getbootstrap.com/docs/5.0/components/alerts/
search in app.py file for "flash"
3. decimal value for PRICE field in the "New Item" form
4. Add description for validation user's inputs on the "New Item" form
5. for Form on a main page, should be used a POST method 
FOR ME - current implementation and correct implementation is GET
6. testing for uploading files - type, size
inlcuding security test for file name - prohibided or allowed
   
7. reCAPTHCA feature is implemented on NEW_TEM form - to prevent a spam
8. The is use the Rub currency
FOR ME - in current implementation is Dollar currency
9. Mark required fields for better UI/UX


