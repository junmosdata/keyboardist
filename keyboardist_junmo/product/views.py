from django.shortcuts import render
from django.views.generic import *
from product.models import *

from product.forms import ProductSearchForm
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.
class ProductLV(ListView):
    model = Product
    
class ProductDV(DetailView):
    model = Product
    
class SearchFV(FormView):
    form_class = ProductSearchForm
    template_name = 'product/product_search.html'
    
    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        product_list = Product.objects.filter(Q(title__icontains=searchWord) |
                                              Q(content__icontains=searchWord)).distinct()
        
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = product_list
        
        return render(self.request, self.template_name, context)

# LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('title', 'price', 'image', 'content')
    success_url = reverse_lazy('product:index')
    
    def form_valid(self, form):
        
        print(form)
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
# LoginRequiredMixin -> 로그인한 사용자가 아니면 로그인 페이지로 이동
# object_list -> 현재 로그인한 사용자가 작성한 Post
class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'product/product_change_list.html'
    
    def get_queryset(self):
        return Product.objects.filter(owner = self.request.user)
    
# OwnerOnlyMixin -> 작성자만이 수정할 수 있도록
class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Product
    fields = ('title', 'price', 'image', 'content')
    success_url = reverse_lazy('product:index')
    
# OwnerOnlyMixin -> 작성자만이 삭제할 수 있도록
class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')