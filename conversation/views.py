from django.shortcuts import render, get_object_or_404, redirect
from item.models import Items
from .models import Conversation
from django.contrib.auth.decorators import login_required
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):
      item = get_object_or_404(Items, pk=item_pk)

      if item.created_by == request.user:
        return redirect('dashboard:index')
      
      conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
      
      if conversations:
          pass

      if request.method == 'POST':
          form = ConversationMessageForm(request.POST)

          if form.is_valid():
              conversation = Conversation.objects.create(item=item)
              conversation.members.add(request.user)
              conversation.members.add(item.created_by)
              conversation.save()

              conversation_message = form.save(commit=False)
              conversation_message.conversation = conversation
              conversation_message.created_by = request.user
              conversation_message.save()

              return redirect('item:detail', pk=item_pk)
      else:
           form = ConversationMessageForm()
      return render(request, './new.html', {
        'form': form,
        'item': item 
      })
