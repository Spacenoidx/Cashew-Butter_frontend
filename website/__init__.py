from flask import Flask, redirect, render_template
from .models import Horse, db, User
from flask_login import LoginManager



def create_app():
   app = Flask(__name__)

   app.config["SECRET_KEY"] = "helloworld"

    # database initialized and created in one move upon app creaton.
   with app.app_context():
       db.init("test.db")
       User.create_table()
       Horse.create_table()

   from . import auth
   from . import views  

   app.register_blueprint(auth.auth)
   app.register_blueprint(views.views)
   
   login_manager = LoginManager()
   login_manager.login_view = "auth.login"
   login_manager.init_app(app)
   
   # Uses a Session to store the given the ID of a user.
   @login_manager.user_loader
   def load_user(id):
    try:
        return User.get(User.id == int(id))
    except User.DoesNotExist:
        return None

#Return the entire app.
   return app