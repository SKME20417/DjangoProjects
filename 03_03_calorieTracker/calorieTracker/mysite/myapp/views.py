from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):
    if request.method=="POST":
        food_consumed = request.POST['food_consumed']
        consumed = Food.objects.get(name = food_consumed)
        user = request.user.id
        consume = Consume(user = user, food_consumed = consumed)
        consume.save()
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user = request.user.id)
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food':consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(pk = id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('index')
    return render(request, 'myapp/delete.html')