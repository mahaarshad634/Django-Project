from django import forms
from . models import userr,post

# class Post(forms.Form):
#     title=forms.CharField()
#     blog=forms.CharField()


# class person(forms.Form):
#     name=forms.CharField()
#     roll=forms.IntegerField()

class student_registration(forms.ModelForm):
    class Meta:
        model = userr
        fields= ['name','username','password']
        labels= {'name':'Enter name','username':'Enter username','password':'Enter password'}

class Postt(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

class posttt(forms.ModelForm):
    class Meta: 
        model = post
        fields = [ 'title','description','image']
        labels = { 'title': 'Enter title','description':'Enter description' , 'image':'Enter image'}