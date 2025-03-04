from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import ItemsForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

# def index(request):
#     allitems = Items.objects.all()
#     # template = loader.get_template('food/index.html')
#     context = {
#         "allitems" : allitems,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request,'food/index.html', context)

class IndexClassView(ListView):
    model = Items
    template_name = 'food/index.html'
    context_object_name = 'allitems'
    


def about(request):
    return HttpResponse("This is about my website")

# def details(request,id):
#     # return HttpResponse("This is item no/id:%s" %id)
#     item = Items.objects.get(pk=id)
#     context = {
#         'item' : item,
#     }
#     return render(request, "food/detail.html", context)

class FoodDetailView(DetailView):
    model = Items
    template_name = 'food/detail.html'
    
# def create_item(request):
#     form = ItemsForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item-form.html', {'form':form})

class CreateItemView(CreateView):
    model = Items
    fields = ['name', 'desc', 'quntity' ,'price', 'image']
    template_name = 'food/item-form.html'
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    






def update_item(request, id):
    item = Items.objects.get(id = id)
    form = ItemsForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, "food/item-form.html",{'form':form, 'item':item})

    

def delete_item(request, id):
    item = Items.objects.get(pk = id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item':item})

