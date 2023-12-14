from django.urls import include, path

urlpatterns = [
    # ... other project url patterns ...
    path('stocks/', include('yahoo_api_app.urls')),
]