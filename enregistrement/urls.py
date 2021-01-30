from django.urls import path

from .views import *

app_name = 'enregistrement'

urlpatterns = [
    path('etudiant/add/', EtudiantCreateView.as_view(), name='etudiant-add'),
    path('etudiant/list/', EtudiantListView.as_view(), name='etudiant-list'),
    path('etudiant/<int:pk>/delete/',
         EtudiantDeleteView.as_view(), name='etudiant-delete'),
    path('etudiant/<int:pk>/update/',
         EtudiantUpdateView.as_view(), name='etudiant-update'),
    path('enseignant/add/', EnseignantCreateView.as_view(), name='enseignant-add'),
    path('enseignant/list/', EnseignantListView.as_view(), name='enseignant-list'),
    path('enseignant/<int:pk>/delete/',
         EnseignantDeleteView.as_view(), name='enseignant-delete'),
    path('enseignant/<int:pk>/update/',
         EnseignantUpdateView.as_view(), name='enseignant-update'),
    path('encadrement/add/', EncadrementCreateView.as_view(), name='encadrement-add'),
    path('encadrement/list/', EncadrementListView.as_view(), name='encadrement-list'),

    path('encadrement/<int:pk>/delete/',
         EncadrementDeleteView.as_view(), name='encadrement-delete'),
    path('encadrement/<int:pk>/update/',
         EncadrementUpdateView.as_view(), name='encadrement-update'),


    path('soutenance/add/', SoutenanceCreateView.as_view(), name='soutenance-add'),
    path('soutenance/list/', SoutenanceListView.as_view(), name='soutenance-list'),


    path('jury/add/', JuryCreateView.as_view(), name='jury-add'),
    path('jury/list/', JuryListView.as_view(), name='jury-list'),
]
