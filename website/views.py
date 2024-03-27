
# views.py

from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, send_from_directory, session, jsonify
import random
from flask_login import login_required, current_user
from sqlalchemy.sql import func  # Import the 'func' module
import json
# from .models import User
from werkzeug.security import generate_password_hash
# from . import db

from datetime import datetime
import datetime as dt

# from .DateToolKit

current_date = dt.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")
current_year = current_date.strftime("%Y")
current_time = datetime.now().strftime("%H:%M")

from .VertexClient import dbORM
from .DateToolKit import clean_date
from . import encrypt

import os
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)

def oppositeTheme(theme):
  if theme == 'light':
    return 'dark'
  else:
    return 'light'

def go_to(screen_id):
  
  User = dbORM.get_all("USER")
  Record = dbORM.get_all("Record")

  def remove_duplicates(original_list):
    duplicates_removed_list = []
    [duplicates_removed_list.append(x) for x in original_list if x not in duplicates_removed_list]
    return duplicates_removed_list

  def getCollectionData():
    
    totals = {}
    for key, value in Record.items():
      if value['_for'] != "NULL":
        if value['_for'] in totals:
          totals[value['_for']] += int(value['amount'])
        else:
          totals[value['_for']] = int(value['amount'])

    return totals

  def getCollectionDataAdvanced():
    
    collection_names = []
    collections = {}


    for k, v in Record.items():
      collection_names.append(Record[f'{k}']['_for'])
      for i, j in collections.items():
        collections[f"{Record[f'{k}']['_for']}"] = [100000, len(dbORM.find_all("Record", "_for", f"{Record[f'{k}']['_for']}"))]

    try:
      collection_names.remove("NULL")
    except:
      pass


    return collections

  def percentageProfitCalc(income, expense):
    # import Math
    return round((((income - expense)/expense) * 100), 2)

  return render_template("dashboard.html",
    ScreenID = screen_id,
    CurrentUser = User[f'{current_user.id}'],
    CurrentDate=clean_date(formatted_date),
    AppTheme=User[f'{current_user.id}']['app_theme'],
    PercentageProfitCalc=percentageProfitCalc,
    SumFunction=sum,
    CurrentYear=current_year,
    AppThemeOpposite=oppositeTheme(User[f'{current_user.id}']['app_theme']),
    Collections=getCollectionData(),
    CollectionsInfo=getCollectionDataAdvanced()
    )


@views.route('/')
def index():
  return render_template("base.html")

@views.route('/home')
def home():
  return render_template("home.html")

@views.route('/dashboard')
def viewDashBoard():
  
  return go_to(screen_id=1)

@views.route('/dashboard/<string:screen_id>')
def goToScreen(screen_id):

  return go_to(screen_id=screen_id)
    
@views.route('/verify-church-passkey', methods=['GET', 'POST'])
def VCPK():
  if request.method == 'POST':
    key = encrypt.encrypter(request.form['passkey'])

    if encrypt.validate_dc(request.form['passkey'], encrypt.decrypter(key)) == True:
      return render_template("signup.html")
    else:
      return render_template("verify-passkey.html", info="Wrong Passkey")
    

  return render_template("verify-passkey.html", info="None")

@views.route('/edit-profile', methods=['POST'])
def editProfile():
  
  if request.form['user_password'] == "":
    

    _ = {
      "name": request.form['user_name'],
      "email": request.form['user_email'],
      "gender": request.form['user_gender']
    }
  else:
    _ = {
      "name": request.form['user_name'],
      "email": request.form['user_email'],
      "gender": request.form['user_gender'],
      "password": generate_password_hash(request.form['user_password'])
    }

  dbORM.update_entry("USER", f"{dbORM.find_one('USER', 'id', str(current_user.id))}", _)
  

  return go_to(screen_id=str(request.form['screen_id']))

@views.route('/add-to-record', methods=['POST'])
def addToRecord():
  
  data_pack = json.loads(request.data)

  _ = {
    'name':  data_pack['name'],
    'amount':  data_pack['amount'],
    '_for':  data_pack['_for'],
    'where':  data_pack['where'],
    'description':  data_pack['description'],
    'timestamp': f'{current_time}',
    'datestamp': f'{current_date}'
  }

  dbORM.add_entry("Record", f"{str(_)}")

  return go_to(screen_id=data_pack['screen'])

@views.route('/change-app-theme', methods=['POST'])
def changeAppTheme():
  data = json.loads(request.data)

  

  dbORM.update_entry("USER", f"{dbORM.find_one('USER', 'id', str(current_user.id))}", {"app_theme": f"{oppositeTheme(data['current_app_theme'])}"})
    

  return jsonify({})

@views.route('/view-collection-record/<string:collection_name>')
def showCollection(collection_name):
  Record = dbORM.get_all("Record")
  User = dbORM.get_all("USER")

  def getCollectionData():
    totals = {}
    for key, value in Record.items():
      if value['_for'] != "NULL":
        if value['_for'] in totals:
          totals[value['_for']] += int(value['amount'])
        else:
          totals[value['_for']] = int(value['amount'])

    return totals

  def getCollectionDataAdvanced(the_collection):
    
    collections = {}

    for key, value in Record.items():
      if the_collection != "NULL":
        if the_collection == value["_for"]:
          collections[value['name']] = [value['amount'], value['datestamp'], value['timestamp']]
        # else:
        #   collections.append(value['name'])


    return collections

  return render_template("collection-page.html",
    CollectionName=collection_name,
    CurrentUser = User[f'{current_user.id}'],
    CurrentDate=clean_date(formatted_date),
    AppTheme=User[f'{current_user.id}']['app_theme'],
    CurrentYear=current_year,
    AppThemeOpposite=oppositeTheme(User[f'{current_user.id}']['app_theme']),
    Collections=getCollectionData(),
    NumberOfPayers=len(dbORM.find_all("Record", "_for", f"{collection_name}")),
    CollectionsInfo=getCollectionDataAdvanced(collection_name)
    )