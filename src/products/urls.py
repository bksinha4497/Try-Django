from django.urls import path
from .views import (
	product_detail_view,
	product_create_view,
	raw_product_create_view,
	render_initial_data,
	dynamic_lookup_view,
	product_delete_view,
	product_query_set,
	)



app_name='products'
urlpatterns = [
	
    path('',product_detail_view),
    path('create/',product_create_view),
    path('initial/',render_initial_data),
    path('rawcreate/',raw_product_create_view),
    path('<int:id>/',dynamic_lookup_view,name='product-detail'),
    path('<int:id>/delete/',product_delete_view,name='product_delete'),
    path('query/',product_query_set),
   
]
