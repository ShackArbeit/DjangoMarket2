from django.shortcuts import render,redirect
from item.models import Items,Category
from .forms import SignupForm

# 將從 item app 裡面所定義的 Category,Items models 拿過來用
def index(request):
      items=Items.objects.filter(is_sold=False)[0:6]
      categories=Category.objects.all()
      return render(request,'./index.html',{
            'categories':categories,
            'items':items
      })

def contact(request):
      return render(request,'./contact.html')

def signup(request):
      if request.method=='POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('/login/')
      else:
        form = SignupForm()
      return render(request,'./signup.html',{
            'form':form
      })
