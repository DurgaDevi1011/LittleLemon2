# LittleLemon its a web application 

##Setup:
py -m  pip install Django
py -m pip install djangorestframework
py -m pip install djoser
py -m pip install mysqlclient
py manage.py migrate

##Create dataBase in MySql server and then create required databases;

1. CREATE TABLE menu(
id INT AUTO_INCREMENT,
tittle VARCHAR(255),
price decimal(10,2),
inventory INT,
PRIMARY KEY(id)
);


2. CREATE TABLE booking(
id INT AUTO_INCREMENT,
name VARCHAR(255),
no_of_guests INT,
bookingdate DATETIME,
PRIMARY KEY(id)
);

API URLs
http://127.0.0.1:8000/restaurant/api-token-auth/ 
http://127.0.0.1:8000/restaurant/menu/menu-items/
http://127.0.0.1:8000/restaurant/menu/menu-items/14
http://127.0.0.1:8000/restaurant/booking/tables/
http://127.0.0.1:8000/restaurant/booking/


Djoser:
http://127.0.0.1:8000/auth/users/ (users can also be registered through post method)
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/users/confirm/
http://127.0.0.1:8000/auth/users/resend_activation/
http://127.0.0.1:8000/auth/users/set_password/
http://127.0.0.1:8000/auth/users/reset_password/
http://127.0.0.1:8000/auth/users/reset_password_confirm/
http://127.0.0.1:8000/auth/users/set_username/
http://127.0.0.1:8000/auth/users/reset_username/
http://127.0.0.1:8000/auth/users/reset_username_confirm/

Djoser TOKEN:
http://127.0.0.1:8000/auth/token/login/