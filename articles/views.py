from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from articles.forms import LivreForm
from .models import Livre

# Create your views here.
# Récupérez tous les livres et afficher dans la page d'accueil
def blogLivre(request):
    allLivre = Livre.objects.all()
    return render(request, "index.html", {'livres': allLivre}) 


# Recupéré les articles envoyer par l'utilisateur depuis le formulaire
def creer_livre(request):
    livres = Livre.objects.all()  # Récupère tous les livres pour les afficher
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.auteur = request.user  # Assurez-vous que l'utilisateur est connecté
            livre.save()
            return redirect('useradmin')  # Redirection après ajout
    else:
        form = LivreForm()  # Formulaire vide pour l'ajout
    return render(request, 'useradmin.html', {'form': form, 'livres': livres})  # Passez le formulaire et les livres au template

# view pour Modifier un article

def modifier_livre(request, id):
    # Récupérer l'objet Livre ou afficher une erreur 404 s'il n'existe pas
    livre = get_object_or_404(Livre, id=id)
    
    # Si la méthode est POST, cela signifie que l'utilisateur a soumis le formulaire
    if request.method == 'POST':
        form_edit = LivreForm(request.POST, request.FILES, instance=livre)
        if form_edit.is_valid():
            form_edit.save()  
            return redirect('useradmin')
    else:
        form = LivreForm(instance=livre)  # Formulaire pré-rempli avec les données du livre

    return render(request, 'modifier_livre.html', {'form': form, 'livre': livre})

# view pour supprimer un livre
def supprimer_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    livre.delete()
    messages.success(request, 'Livre supprimé avec succès!')
    return redirect('useradmin')

# view pour afficher le deatil d'un article
def detail_livre(request, id):
   livre = get_object_or_404(Livre, id=id)
   return render(request, 'detail_article.html', {'livre': livre})