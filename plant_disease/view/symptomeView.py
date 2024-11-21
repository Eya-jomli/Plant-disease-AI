from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.Symptome import Symptome
from plant_disease.Model.plant import Plante  # Import the Plante model

# Liste des symptômes (Read - List)
class SymptomeListView(ListView):
    model = Symptome
    template_name = 'symptomes/symptome_list.html'
    context_object_name = 'symptomes'

class FrontOfficeSymptomeListView(ListView):
    model = Symptome
    template_name = 'symptomes/symptome_frontlist.html' 
    context_object_name = 'symptomes_front'  

# Détails d'un symptôme (Read - Detail)
class SymptomeDetailView(DetailView):
    model = Symptome
    template_name = 'symptomes/symptome_detail.html'
    context_object_name = 'symptome'

class SymptomeCreateView(CreateView):
    model = Symptome
    fields = ['nom', 'description', 'plante']  # Include the 'plante' field
    template_name = 'symptomes/symptome_form.html'
    success_url = reverse_lazy('symptome-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plantes'] = Plante.objects.all()  # Add the list of plants to the context
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid. Symptome created:", form.instance)  # Debugging line
        return response

    def form_invalid(self, form):
        print("Form is invalid. Errors:", form.errors)  # Debugging line
        return super().form_invalid(form)

# Mettre à jour un symptôme (Update)
class SymptomeUpdateView(UpdateView):
    model = Symptome
    fields = ['nom', 'description', 'plante']  # Include the 'plante' field
    template_name = 'symptomes/symptome_form.html'
    success_url = reverse_lazy('symptome-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plantes'] = Plante.objects.all()  # Add the list of plants to the context
        return context

# Supprimer un symptôme (Delete)
class SymptomeDeleteView(DeleteView):
    model = Symptome
    template_name = 'symptomes/symptome_confirm_delete.html'
    success_url = reverse_lazy('symptome-list')
