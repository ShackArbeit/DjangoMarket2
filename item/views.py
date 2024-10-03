from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Items
from .forms import NewItemForm

def detail(request,pk):
      item=get_object_or_404(Items,pk=pk)
       # 將尚未出售的同種類商品的前三項展示出來並排出當前的產品
      related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
      return render(request,'./detail.html',{
            'item':item,
            'related_items': related_items
      })
# 需要註冊且登入才有權限新增新的產品項目
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

