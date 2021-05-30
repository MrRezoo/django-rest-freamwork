from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('one/', views.one, name='one'),
    # path('persons/', views.persons, name='persons'),
    # path('person/<int:person_id>/', views.person, name='person'),
    # path('person_create/', views.person_create, name='person_create'),
]
