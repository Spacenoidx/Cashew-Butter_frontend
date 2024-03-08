# basic Flask functionality

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#necessary database imports, from init and models.py
from . import db
from .models import User

# user session modules
from flask_login import login_user, logout_user, login_required, current_user, LoginManager

# password hashing and checking modules
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)



#Create a new user with this route.
@auth.route("/sign_up", methods=["POST", "GET"])
def sign_up():

    #Routes essentially "work backwards."
    #If someone POST at the sign-up page, AKA tries
    # to make a new account, we check to  see if they already exist.
    # If not, we make a new user.

    #If the person simply loads the page, we present the page.

    if request.method == "POST":

        #Get submitted data from form.

        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        #Query the database for the email and the username, since these must be unique.

        try:
            # Query the database for the email (assuming email is unique)
            email_exists = User.get(User.email == email)
        except User.DoesNotExist:
            email_exists = None

        try:
            # Query the database for the username (assuming username is unique)
            username_exists = User.get(User.username == username)
        except User.DoesNotExist:
            username_exists = None



        if email_exists:
            flash("This email is already in use.", category="error")
        elif username_exists:
            flash("This username is already in use.", category="error")

        # If the email or username are already in use, deny account creation.

        elif password1 != password2:
            flash("Passwords don't match!", category="error")

        # If the password is in use, deny account creation.

        elif len(username) < 2:
            flash("Your username is too short.")
        elif len(password1) < 6:
            flash("Password is too short.", category="error")
        elif len(email) < 4:
            flash("Email is invalid.", category = "error")

        # If all conditions are met, then create a new user.
        else:
            # The password MUST be hashed.
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="pbkdf2:sha256"))
            new_user.save()
            
            login_user(new_user, remember=True)

            # Log the new user in automatically.          
        
            flash("User created!", "message")

            # And send them back to the home page.
            return redirect(url_for("views.home"))

    return render_template("register_page.html", user=current_user)

