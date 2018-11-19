from django.shortcuts import render,request,redirect
from django.contrib.auth import autenticate,login
from django.contrib.auth.decorators import login_required

def register_account(request)

    if request.method == 'POST' or request.method == 'PUT':
        