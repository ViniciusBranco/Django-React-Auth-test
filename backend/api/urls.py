from django.urls import path
from . import views


urlpatterns = [
    # Define uma rota para api/notes/
    path('notes/', views.NoteListCreate.as_view(), name='note-list'),

    # Define uma rota para deletar notas específicas em api/notes/delete/<int:pk>
    path('notes/delete/<int:pk>', views.NoteDelete.as_view(), name='delete-note'),
    # O <int:pk> é um parâmetro na URL que captura um número inteiro (ID da nota)
]
