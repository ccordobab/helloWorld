from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name='pages/home.html'

class AboutPageView(TemplateView):
    template_name='pages/about.html'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context.update({
           "title": "About us - Online Store",
           "subtitle": "About us",
           "description": "This is an about page ...",
           "author": "Developed by: Your Name",
        })
       return context
    

class ContactPageView(TemplateView):
    template_name='pages/contact.html'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context.update({
           "title": "Contact us - Online Store",
           "subtitle": "Contact us",
           "description": "Thanks for reaching out, a Cloud9 employee will be available ",
           "email": "Cloud9@mail.com",
           "address": "563412 13th street east",
           "phone":"893503934849",
        })
       return context
    

# start of something premade

class Product:
   products = [
      {"id":"1", "name":"TV", "description":"Best TV", 'price':'200'},
      {"id":"2", "name":"iPhone", "description":"Best iPhone", 'price':'300'},
      {"id":"3", "name":"Chromecast", "description":"Best Chromecast",'price':'100'},
      {"id":"4", "name":"Glasses", "description":"Best Glasses",'price':'50'},
    ]
   

class ProductIndexView(View):
   template_name = 'products/index.html'
   
   def get(self, request):
      viewData = {}
      viewData["title"] = "Products - Online Store"
      viewData["subtitle"] = "List of products"
      viewData["products"] = Product.products
      return render(request, self.template_name, viewData)


class ProductShowView(View):
   template_name = 'products/show.html'
   
   def get(self, request, id):
      viewData = {}
      try:
         product = Product.products[int(id)-1]
      except:
         return render(request,'products/errorFile.html')
      
      viewData["title"] = product["name"] + " - Online Store"
      viewData["subtitle"] = product["name"] + " - Product information"
      viewData["product"] = product
      viewData["pprice"]=int(product["price"])
         
      return render(request, self.template_name, viewData)
   

class ProductForm(forms.Form):
   name = forms.CharField(required=True)
   price = forms.FloatField(required=True)

   def clean_price(self):
      price = self.cleaned_data.get('price')
      if price < 0:
         raise forms.ValidationError("the price cannot be negative")
      return price


class ProductCreateView(View):
   template_name = 'products/create.html'

   def get(self, request):
      form = ProductForm()
      viewData = {}
      viewData["title"] = "Create product"
      viewData["form"] = form
      return render(request, self.template_name, viewData)
   
   def post(self, request):
      form = ProductForm(request.POST)
      if form.is_valid():
         return redirect('creation')
      else:
         viewData = {}
         viewData["title"] = "Create product"
         viewData["form"] = form
         return render(request, self.template_name, viewData)

class CreationCompletedView(TemplateView):
   template_name = 'products/creationCompleted.html'

#end of the premade