
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# from . __init__ import initialize_app
# app = initialize_app()


# from flask_login import UserMixin, LoginManager

# FL_Login = LoginManager(app)
# FL_Login.login_view = 'auth.login'

# from .VertexClient import dbORM

# class UserClass:
#     def __init__(self, id):
#         self.id = id

#     @staticmethod
#     def is_authenticated():
#         return True

#     @staticmethod
#     def is_active():
#         return True

#     @staticmethod
#     def is_anonymous():
#         return False

#     def get_id(self):
#         return self.id


#     @FL_Login.user_loader
#     def load_user(id):
#         try:
#             u = dbORM.find_one("User", "id", id)
#             if not u:
#                 return None
#             return UserClass(id=dbORM.get_all("User")[f'{u}']['id'])
#         except:
#             anonymous = {
#                 "0": {
#                     "id": "0", 
#                     "email": "NULL", 
#                     "password": "NULL", 
#                     "name": "NULL", 
#                     "age": "NULL", 
#                     "description": "NULL", 
#                     "userType": "seller", 
#                     "niche": "NULL", "username": "NULL", 
#                     "intrests": "NULL", 
#                     "store_link": "NULL", 
#                     "is_verified_account": "NULL", 
#                     "identification_document": "Notes.txt", "identification_document_path": "NULL", 
#                     "is_pro_user": "False", 
#                     "profile_picture": "&begin;#9a33d0<->#e4e707&end;", 
#                     "user_theme": "light", 
#                     "profileViewCount": "NULL"
#                 }
#             }
#             return UserClass(id=anonymous['0']['id'])

# @auth.route("/login", methods=['GET', 'POST']) 
# def login():
#     User = dbORM.get_all("User")

#     if request.method == 'POST':
#         email = request.form.get('user_email')
#         password = request.form.get('user_password')

#         user = dbORM.find_one("User", "email", email)
#         if user and check_password_hash(User[f'{user}']['password'], password):
#             # flash("Logged in successfully.", category='Success')

#             t_user = UserClass(id=f'{user}')

#             login_user(t_user, remember=True)

#             # flash("What do you think of VidBuy?", category='Prompt')

#             return redirect(url_for('views.dashboard'))
#         else:
#             flash("Incorrect password or email. Please try again.", category="Error occurred")

#     return render_template('login.html')

# @auth.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     flash("Logged out successfully.", category='Success')
#     return redirect(url_for('auth.login'))

# @auth.route("/signup", methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form.get('user_name')
#         email = request.form.get('user_email')
#         age = request.form.get("user_age")
#         password1 = request.form.get('user_password')
#         password2 = request.form.get('user_password_confirm')

#         bio = request.form.get('user_bio')
#         niche = request.form.get('user_niche')

#         user = dbORM.find_one("User", 'email', email)

#         if user:
#             flash("Email is already taken. Please use a different email.", category='Error occurred')
#         elif len(email) < 4:
#             flash('Invalid email: Email must be at least 4 characters long.', category='Error occurred')
#         elif len(name) < 2:
#             flash('Invalid name: Name must be at least 2 characters long.', category='Error occurred')
#         elif password1 != password2:
#             flash('Passwords do not match. Please re-enter your password.', category='Error occurred')
#         elif len(password1) < 8:
#             flash('Password is too short. It must be at least 8 characters long.', category='Error occurred')
#         else:
#             hashed_password = generate_password_hash(password1)
#             new_user = {
#                 'email': email,
#                 'name': name,
#                 'password': hashed_password,
#                 'age': age,
#                 'description': bio,
#                 'niche': niche,
#                 'username': generate_username(name),
#                 "userType": "seller",
#                 'store_link': createStoreLink(username=generate_username(name)),
#                 'is_verified_account': "False",
#                 'profileViewCount': "0",
#                 "is_pro_user": "False",
#                 "profile_picture": f"&begin;{randomColor()[0]}<->{randomColor()[1]}&end;",
#                 "user_theme": "light"
#             }

#             # for key, details in new_user.items():
#             dbORM.add_entry("User", f"{encrypter(str(new_user))}")

#             flash('Account created successfully.', category='Success')

#             t_user = UserClass(id=dbORM.find_one("User", 'email', email))

#             login_user(t_user, remember=True)

#             new_store = {
#                 'name': f"{generate_username(name)} Store",
#                 'description': bio,
#                 'user_id': f"{current_user.id}",
#                 'socials': "[]"
#             }
#             # for key, details in new_store.items():
#             dbORM.add_entry("Store", f"{encrypter(str(new_store))}")

#             return redirect(url_for('views.dasboard'))

#     return render_template("signup.html")

    