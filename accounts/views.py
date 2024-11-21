# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Pour afficher un message de succès (optionnel)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter.")
            return redirect('login')  # Redirection vers la page de connexion
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



