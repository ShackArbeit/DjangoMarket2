from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Items

@login_required
def dashboard(request):
      items=Items.objects.filter(created_by=request.user)
      return render(request,'./dashboard.html',{
            'items':items
      })

