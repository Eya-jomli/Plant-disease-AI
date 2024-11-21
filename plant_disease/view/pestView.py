from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.pest import Pest


# Liste des ravageurs (Read - List)
class PestListView(ListView):
    model = Pest
    template_name = 'pests/pest_list.html'
    context_object_name = 'pests'


# Détails d'un ravageur (Read - Detail)
class PestDetailView(DetailView):
    model = Pest
    template_name = 'pests/pest_detail.html'
    context_object_name = 'pest'


# Créer un ravageur (Create)
class PestCreateView(CreateView):
    model = Pest
    fields = ['nom', 'type', 'description', 'image', 'plantes']
    template_name = 'pests/pest_form.html'
    success_url = reverse_lazy('pest-list')


# Mettre à jour un ravageur (Update)
class PestUpdateView(UpdateView):
    model = Pest
    fields = ['nom', 'type', 'description', 'image', 'plantes']
    template_name = 'pests/pest_form.html'
    success_url = reverse_lazy('pest-list')


# Supprimer un ravageur (Delete)
class PestDeleteView(DeleteView):
    model = Pest
    template_name = 'pests/pest_confirm_delete.html'
    success_url = reverse_lazy('pest-list')


# Liste des ravageurs (Read - List) pour le front-office
class FrontOfficePestListView(ListView):
    model = Pest
    template_name = 'pests/front_pest_list.html'  # Nouveau chemin de template
    context_object_name = 'pests'


# Détails d'un ravageur (Read - Detail) pour le front-office
class FrontOfficePestDetailView(DetailView):
    model = Pest
    template_name = 'pests/front_pest_detail.html'  # Nouveau chemin de template
    context_object_name = 'pest'





