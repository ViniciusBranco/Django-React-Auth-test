from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# Class Based Views

class CreateUserView(generics.CreateAPIView):
    # CreateAPIView fornece apenas o método HTTP POST
    queryset = User.objects.all() # acessa todos os usuários do sistema
    serializer_class = UserSerializer # define o serializador desta classe
    permission_classes = [AllowAny] # Define as permissões necessárias para acessar a view
        # permite que qualquer usuário (mesmo não autenticado) acesse a view
        # Apropriado para registro de novos usuários


class NoteListCreate(generics.ListCreateAPIView):
    # ListCraeteAPIView fornece automaticamente endpoints GET (listar) e POST (criar)
    # Responde a requisições DELETE em /api/notes/
    serializer_class = NoteSerializer    # Usa NoteSerializer para conversão de dados
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    # Esta configuração garante a segurança dos dados, 
    # impedindo que usuários acessem ou modifiquem notas de outros usuários.

    # sobrescrição de métodos de ListCraeteAPIView
    def get_queryset(self):
        # Trata requisições GET
        # reconhece o usuário
        # Retorna apenas as notas pertencentes ao usuário atual
        user = self.request.user 
        return Note.objects.filter(author=user) # Retorna um QuerySet filtrado por autor
    
    def perform_create(self, serializer): 
        # Trata requisições POST
        # se o serializador estiver válido...
        # Define automaticamente o campo author como o usuário atual
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)




class NoteDelete(generics.DestroyAPIView):
    # NoteDelete fornece funcionalidade específica para operações de exclusão via HTTP DELETE
    # Responde a requisições DELETE em /api/notes/<id>/
    serializer_class = NoteSerializer       # Usa NoteSerializer para conversão de dados
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    # Esta configuração garante a segurança dos dados, 
    # impedindo que usuários acessem ou modifiquem notas de outros usuários.

    # sobrescrição de métodos de NoteDelete
    def get_queryset(self):
        # Trata requisições GET
        # reconhece o usuário
        # Deleta apenas as notas pertencentes ao usuário atual
        user = self.request.user 
        return Note.objects.filter(author=user) # Retorna um QuerySet filtrado por autor
    