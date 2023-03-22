from django.http import *
from django.shortcuts import render

from shorturl.settings import SITE_ID
from .models import *
from .forms import URLForm, shortener
from django.contrib.redirects.models import Redirect

new_url = ''
old_url = ''

def is_http(url):
    if url[:7] == 'http://' or url[:8] == 'https://':
        return url
    else:
        return 'http://' + url
    pass

def get_url(request):
    
    
    if request.method == 'POST':
        
        form = URLForm(request.POST)
        
        
        
        if form.is_valid():
            global new_url
            global old_url
            
            new_url = is_http(form['new_path'].value())
            old_url = '/' + form['old_path'].value()
            
            redirect = Redirect.objects.create(site_id=1,
                                               old_path = old_url,
                                               new_path = new_url
                                               )
            
            redirect.save()
            return HttpResponseRedirect('/short_url')
        
            

    else:
        
        form = URLForm()

    return render(request, 'shorturl/index.html', {'form': form})

def set_url(request):
    #shorturl = Redirect.objects.get(old_path = new_url)
    return render(request, 'shorturl/short_url.html', {'old_path': new_url, 'new_path': old_url})


def about (request):
    return render(request, 'shorturl/about.html')

def why_shortka (request):
    return render(request, 'shorturl/why_shortka.html')

def pricing (request):
    return render(request, 'shorturl/pricing.html')

def terms (request):
    return render(request, 'shorturl/terms.html')


    



