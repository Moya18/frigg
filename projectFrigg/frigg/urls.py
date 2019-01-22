from django.urls import path

from . import views

app_name = 'frigg'
urlpatterns = [
    path('', views.index, name='index'),
    path('fillQuoteForm/', views.fillQuoteForm, name = 'fill_quote_form'),
    path('createQuote/', views.createQuote, name = 'create_quote'),
    path('getQuotes/', views.getQuotes, name = 'get_quote'),
    path('fillClientForm/', views.fillClientForm, name = 'fill_client_form'),
    path('createClient/', views.createClient, name = 'create_client'),
    path('approveQuote/', views.approveQuote, name = 'approve_quote'),
    path('getJobs/', views.getJobs, name = 'get_job'),
]
