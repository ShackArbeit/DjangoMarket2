from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Items,Category
from django.db.models import Q
from .forms import NewItemForm,EditItemForm



def items(request):
    query=request.GET.get('query','')
    items=Items.objects.filter(is_sold=False)
    category_id=request.GET.get('category',0)
    categories=Category.objects.all()

    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
    if category_id:
        items = items.filter(category_id=category_id)

    return render(request,'./items.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })



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

    return render(request, './ItemForm.html', {
        'form': form,
        'title': '新增新產品',
    })

# 需要註冊且登入才可以刪除產品
@login_required
def delete(request,pk):
    item=get_object_or_404(Items,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, './ItemForm.html', {
        'form': form,
        'title': '編輯修改產品',
    })