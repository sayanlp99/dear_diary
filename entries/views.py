from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.order_by("-date_posted")
    context = {'entries' : entries}
    return render(request, 'entries/index.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    context = {'form':form}
    return render(request, 'entries/add.html', context)

def delete_entry(request, id):
    item_to_delete = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        item_to_delete.delete()
        return redirect('home')
    return render(request, 'entries/index.html', {'item_to_delete': item_to_delete})

def show_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    context = {'entry': entry}
    return render(request, 'entries/show.html', context)

def edit_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = EntryForm(instance=entry)
    context = {'form': form, 'entry': entry}
    return render(request, 'entries/show.html', context)