from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Dragons, Buyers
from .forms import BuyerForm





def index(request):
     dragons = Dragons.objects.all()
     return render(request, "home/index.html", {'dragons': dragons})


def types_of_dragons(request):
     dragons = Dragons.objects.all()
     context = {'dragons': dragons}
     return render(request, "home/dragontipes.html", context)


def buy_dragon(request, dragon_id):
     dragon_get = Dragons.objects.get(pk=dragon_id)
     if request.method == 'POST':
          form = BuyerForm(request.POST)
          if form.is_valid():

               b = Buyers(first_name=form.cleaned_data["name"],
                          last_name=form.cleaned_data["last_name"],
                          cellphone=form.cleaned_data["cellphon"],
                          email=form.cleaned_data["email"],
                          dragon=dragon_get)
               b.save()
               return HttpResponseRedirect(reverse_lazy('index'))
     else:
          form = BuyerForm(request.POST)
     context = {'dragon_get': dragon_get, 'form': form}
     return render(request, "home/buy.html", context)


