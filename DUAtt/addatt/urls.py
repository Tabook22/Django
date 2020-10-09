from django.urls import path, include

urlpatterns = [
    Path('',views.homepage, name="homepage")