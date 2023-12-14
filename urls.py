from django.urls import path, include

urlpatterns = [
    path('stocks/', include('stocks.urls')), # Assuming 'stocks' is the app name
]
