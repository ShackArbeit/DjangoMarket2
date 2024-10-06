from django import forms
from .models import Items

INPUT_CLASS='w-full py-4 px-6 rounded-xl border-2 border-purple-900'

# 新增產品的 Form 表單
class NewItemForm(forms.ModelForm):
      class Meta:
            model=Items
            fields=('category','name','description','image','price',)

            widgets={
                  'category': forms.Select(attrs={
                        'class':INPUT_CLASS
                  }),
                  'name': forms.TextInput(attrs={
                        'class':INPUT_CLASS
                  }),
                   'description': forms.Textarea(attrs={
                        'class':INPUT_CLASS
                  }),
                  'price': forms.TextInput(attrs={
                        'class':INPUT_CLASS
                  }),
                  'image': forms.FileInput(attrs={
                        'class':INPUT_CLASS
                  }),
            }

# 創建產品後的可修改產品的表單
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            })
        }