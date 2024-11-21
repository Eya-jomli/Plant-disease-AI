from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.traitement import Traitement


# Liste des traitements (Read - List)
class TraitementListView(ListView):
    model = Traitement
    template_name = 'traitements/traitement_list.html'
    context_object_name = 'traitements'


# Détails d'un traitement (Read - Detail)
class TraitementDetailView(DetailView):
    model = Traitement
    template_name = 'traitements/traitement_detail.html'
    context_object_name = 'traitement'


 
# Créer un traitement (Create)
class TraitementCreateView(CreateView):
    model = Traitement
    fields = ['nom', 'description', 'méthode', 'maladie']
    template_name = 'traitements/traitement_form.html'
    success_url = reverse_lazy('traitement-list')


# Mettre à jour un traitement (Update)
class TraitementUpdateView(UpdateView):
    model = Traitement
    fields = ['nom', 'description', 'méthode', 'maladie']
    template_name = 'traitements/traitement_form.html'
    success_url = reverse_lazy('traitement-list')


# Supprimer un traitement (Delete)
class TraitementDeleteView(DeleteView):
    model = Traitement
    template_name = 'traitements/traitement_confirm_delete.html'
    success_url = reverse_lazy('traitement-list')




# List of Traitements (Read - List)
class TraitementListViewFRONT(ListView):
    model = Traitement
    template_name = 'traitementfront/traitementf_list.html'
    context_object_name = 'traitements'


# Detail of a Traitement for FRONT (Read - Detail)
class TraitementDetailViewFRONT(DetailView):
    model = Traitement
    template_name = 'traitementfront/traitementf_detail.html'
    context_object_name = 'traitement'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diagnostics'] = self.object.diagnostics.all()
        return context

