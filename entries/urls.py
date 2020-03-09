"""dear_diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views 
from .views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView, home_screen_view


urlpatterns = [
    path('', home_screen_view, name='home'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>/update', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete', EntryDeleteView.as_view(), name='entry-delete'),

]
