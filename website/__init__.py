from flask import Flask, redirect, render_template
from .models import db, User



def create_app():
   app = Flask(__name__)

   app.config["SECRET_KEY"] = "helloworld"


   with app.app_context():
       db.init("test.db")

   from . import auth
   from . import views  

   app.register_blueprint(auth.auth)
   app.register_blueprint(views.views)

   return app