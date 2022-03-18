from app import app
from flask import request, redirect, session
from app.controllers import authController

@app.route('/signup', methods=['POST'])
def signUp():
    if request.method == 'GET':
        print("melihat semua user")
    elif request.method == 'POST':
        return authController.signUp()

@app.route('/signin', methods=['POST'])
def signIn():
    return authController.signIn()

@app.route('/user/<id>', methods=['GET', 'PUT'])
def userDetails(id):
    if(request.method == 'GET'):
        return authController.getUser(id)
    if(request.method == 'PUT'):
        return authController.updateUser(id)