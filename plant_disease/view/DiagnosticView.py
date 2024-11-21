from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.Diagnostic import Diagnostic  # Assurez-vous que ce chemin est correct


# Liste des diagnostics (Read - List)
class DiagnosticListView(ListView):
    model = Diagnostic
    template_name = 'diagnostics/diagnostic_list.html'
    context_object_name = 'diagnostics'


# Détails d'un diagnostic (Read - Detail)
class DiagnosticDetailView(DetailView):
    model = Diagnostic
    template_name = 'diagnostics/diagnostic_detail.html'
    context_object_name = 'diagnostic'


# Créer un diagnostic (Create)
class DiagnosticCreateView(CreateView):
    model = Diagnostic
    fields = ['plante', 'maladie', 'traitement', 'notes']
    template_name = 'diagnostics/diagnostic_form.html'
    success_url = reverse_lazy('diagnostic-list')


# Mettre à jour un diagnostic (Update)
class DiagnosticUpdateView(UpdateView):
    model = Diagnostic
    fields = ['plante', 'maladie', 'traitement', 'notes']
    template_name = 'diagnostics/diagnostic_form.html'
    success_url = reverse_lazy('diagnostic-list')


# Supprimer un diagnostic (Delete)
class DiagnosticDeleteView(DeleteView):
    model = Diagnostic
    template_name = 'diagnostics/diagnostic_confirm_delete.html'
    success_url = reverse_lazy('diagnostic-list')




# Liste des diagnostics (Read - List)
class DiagnosticListViewFront(ListView):
    model = Diagnostic
    template_name = 'diagnostics/diagnosticF_list.html'
    context_object_name = 'diagnostics'


# Détails d'un diagnostic (Read - Detail)
class DiagnosticDetailViewFRONT(DetailView):
    model = Diagnostic
    template_name = 'diagnostics/diagnosticF_detail.html'
    context_object_name = 'diagnostic'







