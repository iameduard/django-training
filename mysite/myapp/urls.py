from django.urls import path, re_path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	re_path(r'^searchform/$',views.search_book),
	re_path(r'^searchform/$',views.search_book),
	re_path(r'^searchform/search/$',views.book_response),
	re_path(r'^contact/$',views.contact),

]