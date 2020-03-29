from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
# Create your views here.
from .forms import ProductForm,RawProductForm




def product_create_view(request):
	
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductForm()

	context = { 
			'form':form
		}
	return render(request,"products/product_create.html",context)



def raw_product_create_view(request):
	my_form = RawProductForm() ## security issue in GET
	if request.method =='POST':
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			#now the data is good
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
		else :
			print(my_form.errors)
	context = { 	
			'form':my_form
		}
	return render(request,"products/product_create.html",context)



def product_detail_view(request):
	obj=Product.objects.get(id=1)
	# context ={
	# 	'title': obj.title,
	# 	'description': obj.description,
	# 	'price': obj.price,
	# }
	context = { 
			'object':obj,
		}
	return render(request,"products/product_detail.html",context)

def render_initial_data(request):
	initial_data={
		'title':'my awesome title'
		}
	obj=Product.objects.get(id=1)	
	form=ProductForm(request.POST or None,initial=initial_data,instance=obj)
	if form.is_valid():
		form.save()
	context={
		'form':form
	}
	return render(request,"products/product_create.html",context)


def dynamic_lookup_view(request,id):
		
	#obj=Product.objects.get(id=my_id)
	obj=get_object_or_404(Product,id=id)
	context={
		'obj':obj
	}
	return render(request,"products/product_create.html",context)

def product_delete_view(request,id):
		
	#obj=Product.objects.get(id=my_id)
	obj=get_object_or_404(Product,id=id)
	obj.delete()
	return redirect ('../../')
	context={
		'obj':obj
	}
	return render(request,"products/product_create.html",context)

def product_query_set(request):
	queryset=Product.objects.all()
	context={
		'object_list':queryset
	}
	return render(request,"products/query-set.html",context)

