# -*- coding: utf-8 -*-

from django import forms

from noticias.models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta():
        model = Noticia
        exclude = ('pub_date',)

class ContactenosForm(forms.Form):
    email = forms.EmailField(label="Email")
    name = forms.CharField(label="Nombre")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea())