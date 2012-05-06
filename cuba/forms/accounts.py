# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core import validators
import re
from cuba.models.accounts import UserProxy
from cuba.utils.alias import tran as _
from django import forms
from bootstrap.forms import BootstrapModelForm

class UserCreateForm(BootstrapModelForm):
  class Meta:
    model = UserProxy
    fields = ('username', 'password', 'password2', 'email')

  username = forms.CharField(max_length=30, min_length=5,
                             label=_('用户名'),
                             help_text=_('登录时使用的用户名，请使用字母或字母加数字的组合，不超过30个字符，不少于6个字符'),
                             validators=[validators.RegexValidator(re.compile(r'^\w[\w0-9]+$'))])

  password = forms.CharField(min_length=6, widget=forms.PasswordInput, label=_('密码'))
  password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label=_('确认密码'))
  email = forms.EmailField(label='电子邮件')

  def clean_username(self):
    username = self.cleaned_data['username']
    if UserProxy.objects.filter(username=username).exists():
      raise forms.ValidationError(_('用户名已存在'))
    return username

  def clean_password(self):
    p1 = self.cleaned_data['password']
    p2 = self.data['password2']
    if p1 != p2:
      raise forms.ValidationError(_('两次输入的密码不匹配'))

    return p1

  def save(self, commit=True):
    user = super(UserCreateForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password"])
    if commit:
      user.save()
    return user