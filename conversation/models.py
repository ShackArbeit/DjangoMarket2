from django.db import models
from django.contrib.auth.models import User
from item.models import Items

class Conversation(models.Model):
#  每個 Conversation 都關聯到一個 Items 實例，也就是說，每個對話都圍繞著某個特定的
#  商品或項目（Items 模型中的一個實例）如果有多個 Conversation（對話）與同一個   
#  Items 關聯，那麼這就是一對多的關係，即 一個 Items 可以有多個 Conversation，但
#  每個 Conversation 只能對應到一個 Items。
# 當我們設置 related_name='conversations'，這表示：從 Items 模型的角度來看，可以
#  通過 conversations 這個名稱來查詢該商品（Items）相關的所有對（Conversation）。
      item=models.ForeignKey(Items,related_name='conversations',on_delete=models.CASCADE)
      members = models.ManyToManyField(User, related_name='conversations')
      created_at = models.DateTimeField(auto_now_add=True)
      modified_at = models.DateTimeField(auto_now=True)
      class Meta:
          ordering = ('-modified_at',)

class ConversationMessage(models.Model):
      conversation=models.ForeignKey(Conversation,related_name='messages', on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
