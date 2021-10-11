from django import forms
from django.db.models.enums import Choices
from django.forms import fields
from django.forms.widgets import Widget
from django.utils.regex_helper import Choice
from django.forms import widgets
from blogapp.models import Post,Catagory

cho=Catagory.objects.all().values_list('name','name')
choice_list=[]
for items in cho:
    choice_list.append(items)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','catagory','body','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'aman','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'catagory':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }