
from django.forms import ModelForm, TextInput
#from .models import Shorturl
from django.contrib.redirects.models import Redirect
import secrets
#from .models import Redirect

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shortener ():
    
    short = ''
    
    for i in range(8):
        short += secrets.choice(letters)
    
    return short


class URLForm(ModelForm):
    
    
    shortener = shortener()
    
    class Meta:
        model = Redirect
        
        fields = ['old_path', 'new_path'] 
            
        widgets = {
            "new_path": TextInput(attrs = {'placeholder': 'Enter your URL', 'class':'input-text'}),
            
            "old_path": TextInput(attrs = {'type': 'hidden', 'value': shortener, 'id': shortener}),
            #"site_id": TextInput(attrs = {'type': 'hidden', 'value': 34}),
        }