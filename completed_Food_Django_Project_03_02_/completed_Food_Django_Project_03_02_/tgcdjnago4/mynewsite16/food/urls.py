from django.urls import path
from . import views

# namespacing
app_name = 'food'

urlpatterns = [
    path("", views.IndexClassView.as_view(), name= "index"),
    path("about/", views.about, name= "about"),
    #localhost/food/1
    path("<int:pk>/", views.FoodDetailView.as_view(), name="detail"),
    #add item
    path("add/", views.CreateItemView.as_view(), name= "create_item"),
    path('update/<int:id>/', views.update_item, name="update"),
    path('delete/<int:id>/', views.delete_item, name="delete"),
]
