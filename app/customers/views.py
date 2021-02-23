from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from customers.models import Customer

class CustomerListView(generic.ListView):
    model = Customer
    paginate_by = 10

class CustomerDetailView(generic.DetailView):
    model = Customer

class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'

class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'

class CustomerDetele(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer')


def index(request):
    return render(request, 'index.html', {})
