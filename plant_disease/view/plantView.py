from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  plant_disease.Model.plant import Plante
from plant_disease.Model.typePlant import TypePlante 
from django.shortcuts import render, get_object_or_404

# Liste des plantes (Read - List)
class PlanteListView(ListView):
    model = Plante
    template_name = 'plantes/plante_list.html'
    context_object_name = 'plantes'

# Détails d'une plante (Read - Detail)
class PlanteDetailView(DetailView):
    model = Plante
    template_name = 'plantes/plante_detail.html'
    context_object_name = 'plante'

# Créer une plante (Create)
class PlanteCreateView(CreateView):
    model = Plante
    fields = ['nom', 'description', 'image', 'type_plante']
    template_name = 'plantes/plante_form.html'
    success_url = reverse_lazy('plante-list')

# Mettre à jour une plante (Update)
class PlanteUpdateView(UpdateView):
    model = Plante
    fields = ['nom', 'description', 'image', 'type_plante']
    template_name = 'plantes/plante_form.html'
    success_url = reverse_lazy('plante-list')

# Supprimer une plante (Delete)
class PlanteDeleteView(DeleteView):
    model = Plante
    template_name = 'plantes/plante_confirm_delete.html'
    success_url = reverse_lazy('plante-list')


def plantes_by_type(request, type_plante_id):
    # Retrieve the specified TypePlante
    type_plante = get_object_or_404(TypePlante, id=type_plante_id)
    
    # Get all plants with this type
    plantes = Plante.objects.filter(type_plante=type_plante)
    
    context = {
        'type_plante': type_plante,
        'plantes': plantes
    }
    
    return render(request, 'type_plante/plantes_by_type.html', context)