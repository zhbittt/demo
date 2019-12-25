import json
import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from . import models
from django.forms import Form
from django.forms import fields
from django.forms import widgets
from django.db.models import Q
from django.db.utils import IntegrityError


class LoginForm(Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名', 'id': 'username'})
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码', 'id': 'password'})
    )
