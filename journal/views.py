from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Journal

@login_required
def home(request):
    # Get the logged-in user
    user = request.user

    # Query for user's journals and public journals by others
    user_journals = Journal.objects.filter(user=user)
    public_journals = Journal.objects.filter(is_public=True).exclude(user=user)

    # Combine the queries
    journals = user_journals.union(public_journals).order_by('-created_at')

    return render(request, 'home.html', {'journals': journals})

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
        return redirect('journal:home')  # Ensure 'homepage' matches the name in your URL patterns.
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
    # Get the journal entry or 404 if not found
    journal = get_object_or_404(Journal, id=journal_id)

    # Optionally, you can restrict access to only the user who created the journal or allow all users
    if not journal.is_public and journal.user != request.user:
        return HttpResponseForbidden("You are not allowed to view this journal.")

    return render(request, 'view_journal.html', {'journal': journal})