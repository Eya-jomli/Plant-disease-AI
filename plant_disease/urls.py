from django.urls import path
from . import views

from  plant_disease.view import TypeView, plantView, MaladieView, pestView , TraitementView, causeView, ControlProductView, symptomeView, preventionView, chatbotView , DiagnosticView 
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import dashboard_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('predict/', views.predict, name='predict'),  # Predict page URL
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('backoffice/', views.backoffice_view, name='backoffice'),
    # *************
  path('typePlantes/', TypeView.TypePlanteListView.as_view(), name='typePlantes-list'),
    path('typePlantes/front', TypeView.TypePlanteListViewFront.as_view(), name='typePlantes-list-front'),
    path('typePlantes/<int:pk>/', TypeView.TypePlanteDetailView.as_view(), name='typePlantes-detail'),
    path('typePlantes/create/', TypeView.TypePlanteCreateView.as_view(), name='typePlantes-create'),
    path('typePlantes/<int:pk>/update/', TypeView.TypePlanteUpdateView.as_view(), name='typePlantes-update'),
    path('typePlantes/<int:pk>/delete/', TypeView.TypePlanteDeleteView.as_view(), name='typePlantes-delete'),
    path('generate_description/', TypeView.generate_description, name='generate-description'), 
    #**********************
    path('plantes/type/<int:type_plante_id>/', plantView.plantes_by_type, name='plantes-by-type'),
    path('plantes/', plantView.PlanteListView.as_view(), name='plante-list'),
    path('plantes/<int:pk>/', plantView.PlanteDetailView.as_view(), name='plante-detail'),
    path('plantes/create/', plantView.PlanteCreateView.as_view(), name='plante-create'),
    path('plantes/<int:pk>/update/', plantView.PlanteUpdateView.as_view(), name='plante-update'),
    path('plantes/<int:pk>/delete/', plantView.PlanteDeleteView.as_view(), name='plante-delete'),


    #*********url pest*************
    path('pests/', pestView.PestListView.as_view(), name='pest-list'),
    path('pests/<int:pk>/', pestView.PestDetailView.as_view(), name='pest-detail'),
    path('pests/create/', pestView.PestCreateView.as_view(), name='pest-create'),
    path('pests/<int:pk>/update/', pestView.PestUpdateView.as_view(), name='pest-update'),
    path('pests/<int:pk>/delete/', pestView.PestDeleteView.as_view(), name='pest-delete'),
 # URLs pests pour le front-office
    path('pests/front/', pestView.FrontOfficePestListView.as_view(), name='front-pest-list'),
    path('pests/front/<int:pk>/', pestView.FrontOfficePestDetailView.as_view(), name='front-pest-detail'),




     #*********url ControlProduct*************
    path('control-products/', ControlProductView.ControlProductListView.as_view(), name='controlproduct-list'),
    path('control-products/<int:pk>/', ControlProductView.ControlProductDetailView.as_view(), name='controlproduct-detail'),
    path('control-products/create/', ControlProductView.ControlProductCreateView.as_view(), name='controlproduct-create'),
    path('control-products/<int:pk>/update/', ControlProductView.ControlProductUpdateView.as_view(), name='controlproduct-update'),
    path('control-products/<int:pk>/delete/', ControlProductView.ControlProductDeleteView.as_view(), name='controlproduct-delete'),
    
 # URLs ControlProduct pour le front office
    path('control-products/front', ControlProductView.FrontOfficeControlProductListView.as_view(), name='front-controlproduct-list'),
    path('control-products/front/<int:pk>/', ControlProductView.FrontOfficeControlProductDetailView.as_view(), name='front-controlproduct-detail'),


      # Maladie URLs
    path('maladies/', MaladieView.MaladieListView.as_view(), name='maladie-list'),
    path('maladies/<int:pk>/', MaladieView.MaladieDetailView.as_view(), name='maladie-detail'),
    path('maladies/create/', MaladieView.MaladieCreateView.as_view(), name='maladie-create'),
    path('maladies/<int:pk>/update/', MaladieView.MaladieUpdateView.as_view(), name='maladie-update'),
    path('maladies/<int:pk>/delete/', MaladieView.MaladieDeleteView.as_view(), name='maladie-delete'),
    path('maladies/', MaladieView.MaladieListView.as_view(), name='maladie-list'),
     # Front-office URLs
    path('maladiesFront/', MaladieView.MaladieListFrontView.as_view(), name='Maladies'),
    path('maladiesFront/<int:pk>/', MaladieView.MaladieDetailfrontView.as_view(), name='maladie-detailfront'),



      # Cause URLs

    path('causes_maladie/', causeView.CauseMaladieListView.as_view(), name='cause_maladie-list'),
    path('causes_maladie/<int:pk>/', causeView.CauseMaladieDetailView.as_view(), name='cause_maladie-detail'),
    path('causes_maladie/create/', causeView.CauseMaladieCreateView.as_view(), name='cause_maladie-create'),
    path('causes_maladie/<int:pk>/update/', causeView.CauseMaladieUpdateView.as_view(), name='cause_maladie-update'),
    path('causes_maladie/<int:pk>/delete/', causeView.CauseMaladieDeleteView.as_view(), name='cause_maladie-delete'),

    path('traitements/', TraitementView.TraitementListView.as_view(), name='traitement-list'),
    path('traitements/<int:pk>/', TraitementView.TraitementDetailView.as_view(), name='traitement-detail'),
    path('traitements/create/', TraitementView.TraitementCreateView.as_view(), name='traitement-create'),
    path('traitements/update/<int:pk>/', TraitementView.TraitementUpdateView.as_view(), name='traitement-update'),
    path('traitements/delete/<int:pk>/', TraitementView.TraitementDeleteView.as_view(), name='traitement-delete'),
     path('front/traitements/', TraitementView.TraitementListViewFRONT.as_view(), name='traitementf-list'),  
    path('front/traitements/<int:pk>/', TraitementView.TraitementDetailViewFRONT.as_view(), name='traitementf-detail'),  


     # URLs for Diagnostic
    path('diagnostics/', DiagnosticView.DiagnosticListView.as_view(), name='diagnostic-list'),
    path('diagnostic/<int:pk>/', DiagnosticView.DiagnosticDetailView.as_view(), name='diagnostic-detail'),
    path('diagnostic/create/', DiagnosticView.DiagnosticCreateView.as_view(), name='diagnostic-create'),
    path('diagnostic/<int:pk>/update/', DiagnosticView.DiagnosticUpdateView.as_view(), name='diagnostic-update'),
    path('diagnostic/<int:pk>/delete/', DiagnosticView.DiagnosticDeleteView.as_view(), name='diagnostic-delete'),
     path('front/diagnostics/', DiagnosticView.DiagnosticListViewFront.as_view(), name='diagnosticF-list'),  
    path('front/diagnostics/<int:pk>/', DiagnosticView.DiagnosticDetailViewFRONT.as_view(), name='diagnosticF-detail'),  


     # URLs for Symptôme
    path('symptomes/', symptomeView.SymptomeListView.as_view(), name='symptome-list'),  
    path('symptomes/front', symptomeView.FrontOfficeSymptomeListView.as_view(), name='symptome_frontlist'),
    path('symptomes/<int:pk>/', symptomeView.SymptomeDetailView.as_view(), name='symptome-detail'),  # Detail view
    path('symptomes/add/', symptomeView.SymptomeCreateView.as_view(), name='symptome-create'),  # Create view
    path('symptomes/<int:pk>/edit/', symptomeView.SymptomeUpdateView.as_view(), name='symptome-update'),  # Update view
    path('symptomes/<int:pk>/delete/', symptomeView.SymptomeDeleteView.as_view(), name='symptome-delete'),  # Delete view
  # URLs for Prevention
    path('preventions/', preventionView.PreventionListView.as_view(), name='prevention-list'),  # List view
    path('preventions/front',preventionView.FrontPreventionListView.as_view(), name='front-prevention-list'), 
    path('preventions/<int:pk>/', preventionView.PreventionDetailView.as_view(), name='prevention-detail'),  # Detail view
    path('preventions/add/', preventionView.PreventionCreateView.as_view(), name='prevention-create'),  # Create view
    path('preventions/<int:pk>/edit/', preventionView.PreventionUpdateView.as_view(), name='prevention-update'),  # Update view
    path('preventions/<int:pk>/delete/', preventionView.PreventionDeleteView.as_view(), name='prevention-delete'),  # Delete view

    
    path('chatbot/', chatbotView.chat_interface, name='chat_interface'),  # GET request for the chat interface
    path('chatbot/api/', chatbotView.chat, name='chatbot_api'),  # POST request for handling chat messages

    #*********user*************
     path('register/', accounts_views.register, name='register'),
     path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', next_page='plante-list'), name='login'),
     path('logout_client/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout_client'),


]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    