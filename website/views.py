from os import name
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# Naming our main blueprint "views".

views = Blueprint ('views', __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":

        email = request.form['email']

        from website import db
        from .models import User
        db.connect()
        User.create_table()
        
    
        User.create(email=email)

        db.commit()
        return "Thanks!"

        
    else:
        return render_template("home.html")   

@views.route("/user_search", methods=["POST", "GET"])
def user_lookup_page():
    if request.method == "POST":

        user_id = request.form['user_id']

        return redirect ( url_for ("views.user_lookup_result", user_id = user_id))
    else:
        return render_template("user_lookup.html")

# This view is the result page of the search view accessed above. The view above passes along the user's entry as user_id 
# and if a result is present, it will render in the template below.
    
@views.get('/users/<int:user_id>')
def user_lookup_result(user_id):
    from website import db
    from .models import User
    db.connect()
    # new user variable accesses the table with User.select()
    user = User.select().where(User.id == user_id).get()
    print(f"{user} is the number just entered!!!")

    return render_template("user_lookup_results.html", user = user )
    

@views.route('/submit_horse', methods=["POST", "GET"])
def submit_horse():
    if request.method == "POST":
        horse_Name = request.form["horse_Name"]
        horse_Gender = request.form["horse_Gender"]

        from website import db
        from .models import Horse
        db.connect()
        Horse.create_table()
        
    
        Horse.create(name=horse_Name, gender = horse_Gender)

        db.commit()

        flash('You successfully submitted a horse!', "message")

        return render_template("submit_horse.html")     
    else:    
        return render_template("submit_horse.html")

@views.route("/horse_table")

def horse_table():
    from website import db
    from .models import Horse
    db.connect()
    # new user variable accesses the table with User.select()
    horses = Horse.select()

    for horse in horses:
        print(horse)

    return render_template("horse_table.html", horses = horses )

@views.route("/claim_horse/<horse_name>", methods=["POST", "GET"])

def claim_horse(horse_name):
    from website import db
    from .models import Horse
    db.connect()

    # Use .get() instead of .select().where() if you expect only one result
    db_horse = Horse.get(Horse.name == horse_name)

    # Access the 'name' attribute of the retrieved Horse object
    return f"Hi!, {db_horse.name}"
