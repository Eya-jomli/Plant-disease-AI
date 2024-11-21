from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.Symptome import Symptome
from plant_disease.Model.prevention import prevention  # Ensure correct import path



# Liste des mesures préventives (Read - List)
class PreventionListView(ListView):
    model = prevention
    template_name = 'preventions/prevention_list.html'
    context_object_name = 'preventions'

class FrontPreventionListView(ListView):
    model = prevention
    template_name = 'preventions/front_prevention_list.html'  # Adjust the template name
    context_object_name = 'preventions'

    def get_queryset(self):
        # Get the symptom ID from the query parameters
        symptom_id = self.request.GET.get('symptome_id')
        return prevention.objects.filter(symptômes_connexes_id=symptom_id)
# Détails d'une mesure préventive (Read - Detail)
class PreventionDetailView(DetailView):
    model = prevention
    template_name = 'preventions/prevention_detail.html'
    context_object_name = 'prevention'

# Créer une mesure préventive (Create)
class PreventionCreateView(CreateView):
    model = prevention
    fields = ['nom', 'description', 'symptômes_connexes']
    template_name = 'preventions/prevention_form.html'
    success_url = reverse_lazy('prevention-list')  # Adjust URL name as needed

# Mettre à jour une mesure préventive (Update)
class PreventionUpdateView(UpdateView):
    model = prevention
    fields = ['nom', 'description', 'symptômes_connexes']
    template_name = 'preventions/prevention_form.html'
    success_url = reverse_lazy('prevention-list')

# Supprimer une mesure préventive (Delete)
class PreventionDeleteView(DeleteView):
    model = prevention
    template_name = 'preventions/prevention_confirm_delete.html'
    success_url = reverse_lazy('prevention-list')