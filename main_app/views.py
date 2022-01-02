from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Stock, Client, Order
from django.views.generic import ListView, DetailView
from .forms import OrderForm
# from .forms import orderForm
import uuid 
import boto3
# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('templates/home.html')
    else:
      error_message = 'Invalid Signup, try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registrations/signup.html', context)

@login_required
def stocks_index(request):
  stocks = Stock.objects.filter(user=request.user)
  return render(request, 'stocks/index.html', {'stocks':stocks})

@login_required
def stocks_detail(request, stock_id):
  stock = Stock.objects.get(id=stock_id)
  #toys_stock_doesnt_have = Toy.objects.exclude(id__in = stock.toys.all().values_list('id'))
  #order_form = orderForm()
  return render(request, 'stocks/detail.html', { 'stock': stock})

class StockCreate(CreateView):
  model = Stock
  fields = ['name','ticker','purchase_price','volume']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def add_order(request, stock_id):
  form = OrderForm(request.POST)
  if form.is_valid():
    new_order = form.save(commit=False)
    new_order.stock_id = stock_id
    new_order.save()
  return redirect('stocks_detail', stock_id=stock_id)

class StockUpdate(UpdateView):
  model = Stock
  fields = ['name', 'ticker','purchase_price','volume']

class StockDelete(DeleteView):
  model = Stock


class ClientList(ListView):
  model = Client

class ClientDetail(DetailView):
  model = Client

class ClientCreate(CreateView):
  model = Client
  fields = '__all__'

class ClientUpdate(UpdateView):
  model = Client
  fields = '__all__'

class ClientDelete(DeleteView):
  model = Client
  success_url='/clients/'




  