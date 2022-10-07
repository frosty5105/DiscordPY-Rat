from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
    return "faysal is cool"

def run():
  app.run(host='0.0.0.0',port=5000) 

def awake():  
    t = Thread(target=run)
    t.start()