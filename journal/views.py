import markdown
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Journal
from django.db.models import Q

@login_required
def home(request):

    user = request.user

    search_query = request.GET.get('search', '')

    user_journals = Journal.objects.filter(user=user)
    public_journals = Journal.objects.filter(is_public=True).exclude(user=user)

    if search_query:
        user_journals = user_journals.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
        public_journals = public_journals.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )

    journals = user_journals | public_journals  

    journals = journals.order_by('-created_at')

    return render(request, 'home.html', {'journals': journals, 'search_query': search_query})

@login_required
def create_journal(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_public = request.POST.get('is_public') == 'on'

        Journal.objects.create(
            title=title,
            content=content,
            user=request.user,
            is_public=is_public
        )
        return redirect('journal:home') 
    return render(request, 'create_journal.html')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("journal:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def delete_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    if journal.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this journal.")
    journal.delete()
    return redirect('journal:home')

@login_required
def edit_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)

    if journal.user != request.user:
        return redirect('journal:home')

    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        journal.title = title
        journal.content = content
        journal.save()

        return redirect('journal:view_journal', journal.id)

    return render(request, 'journal/edit_journal.html', {'journal': journal})

@login_required

def view_journal(request, journal_id):

    journal = get_object_or_404(Journal, id=journal_id)

   
    if not journal.is_public and journal.user != request.user:
        return HttpResponseForbidden("You are not allowed to view this journal.")


    md = markdown.Markdown()
    journal_content_html = md.convert(journal.content)


    return render(request, 'view_journal.html', {
        'journal': journal,
        'journal_content_html': journal_content_html
    })