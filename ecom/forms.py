from django import forms
from django.contrib.auth.models import User
from . import models
from django.utils.translation import ugettext_lazy

from .models import Comment, Customer, News


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30, label=ugettext_lazy('Имя'))
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), label=ugettext_lazy('Сообщение'))


class InformationForm(forms.Form):
    name = forms.CharField(label="Ваше имя", min_length=2, max_length=100)
    city = forms.CharField(label="Ваш город", min_length=2, max_length=100)
    job = forms.CharField(label="Ваш род занятий", min_length=2, max_length=100)
    gender = forms.ChoiceField(label="Ваш пол",
                             choices=[('1', 'Мужской'), ('2', 'Женский')],
                             widget=forms.RadioSelect, initial=1)
    notice = forms.BooleanField(label="Получать новости от сайта", required=False)
    email = forms.CharField(label='Ваш email', min_length=7)
    message = forms.CharField(label='Коротко о себе', widget = forms.Textarea(attrs={'rows': 12, 'cols': 20}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'image')
        labels = {'title': "Заголовок", 'content': "Текст", 'image': "Картинка"}
