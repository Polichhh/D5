from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
   title = forms.CharField(min_length=5)

   class Meta:
       model = Post
       fields = ['title', 'postCategory', 'text']

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       title = cleaned_data.get("title")

       if title is not None and len(title) < 5:
           raise ValidationError({
               "title": "Название не может быть менее 5 символов."
           })

       if text == title:
           raise ValidationError(
               "Наполнение не должно быть идентично названию."
           )
       return cleaned_data


class NewsForm(forms.ModelForm):
   title = forms.CharField(min_length=5)

   class Meta:
       model = Post
       fields = ['title', 'postCategory', 'text']

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       title = cleaned_data.get("title")

       if title is not None and len(title) < 5:
           raise ValidationError({
               "title": "Название не может быть менее 5 символов."
           })

       if text == title:
           raise ValidationError(
               "Наполнение не должно быть идентично названию."
           )
       return cleaned_data

class ArticleForm(forms.ModelForm):
   title = forms.CharField(min_length=5)

   class Meta:
       model = Post
       fields = ['title', 'postCategory', 'text']

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       title = cleaned_data.get("title")

       if title is not None and len(title) < 5:
           raise ValidationError({
               "title": "Название не может быть менее 5 символов."
           })

       if text == title:
           raise ValidationError(
               "Наполнение не должно быть идентично названию."
           )
       return cleaned_data