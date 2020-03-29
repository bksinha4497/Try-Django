from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kargs):
	
	return render(request,"home.html",{})


def contact_view(request,*args,**kargs):
	
	return render(request,"contact.html",{})

def about_view(request,*args,**kargs):
	my_context= {
		"title":"This is capfirst",
		"my_text" :"This is about us",
		"This_is_true":True,
		"my_number":123,
		"my_list":['abc',122,123,124],
		"my_html":"<h3>Render HTML using template filter safe</h3>",

	}
	
	return render(request,"about.html",my_context)

def social_view(request,*args,**kargs):
	
	return HttpResponse("<h1>Social Page</h1>")