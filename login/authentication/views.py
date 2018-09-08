from django.shortcuts import render
import pyrebase

config = {
  "apiKey": "AIzaSyDGYMhqucbTLekTaBFumSKbMtX7zLrDNUY",
  "authDomain": "fgapplogin.firebaseapp.com",
  "databaseURL": "https://fgapplogin.firebaseio.com",
  "projectId": "fgapplogin",
  "storageBucket": "fgapplogin.appspot.com",
  "messagingSenderId": "106726536163"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
