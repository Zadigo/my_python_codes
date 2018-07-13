from django.forms import forms, widgets
from django.forms import EmailField, CharField, FileField, URLField, ImageField, ChoiceField
from books.choices import STARS

class TestForm(forms.Form):
    nom = CharField(widget=widgets.TextInput(attrs={'placeholder':'Nom'}))
    prenom = CharField(widget=widgets.TextInput(attrs={'placeholder':'Prenom'}))
    email = EmailField(widget=widgets.TextInput(attrs={'placeholder':'Email'}))
    password = CharField(widget=widgets.PasswordInput(attrs={'placeholder':'Password'}))
    facebook = URLField(widget=widgets.URLInput(attrs={'placeholder':'Facebook link'}))
    pic = ImageField(max_length=20, allow_empty_file=True)
    picture = FileField()
    another = ChoiceField(choices=STARS)
