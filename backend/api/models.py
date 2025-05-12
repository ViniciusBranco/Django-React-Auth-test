from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """
        Classe para gerar a tabela "Note" no banco de dados.
        Relação: um autor pode gerar muitas notas; cada nota pertence a somente um autor: 1-N
             Se o usuário for deletado, suas notas também serão.
    """
    title = models.CharField(max_length=100) # Campo de texto limitado a 100 caracteres
    content = models.TextField() # Armazena o conteúdo principal da nota, sem limite.
    created_at = models.DateField(auto_now=False, auto_now_add=True) # Data é automaticamente definida quando o registro é criado
    updated_at = models.DateField(auto_now=True, auto_now_add=False) # Data é atualizada automaticamente quando o registro é modificado
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") # Relaciona cada nota com um usuário do sistema
        # Com related_name="notes", acessamos as notas de um usuário através de user.notes

    def __str__(self): # Define como a nota será representada como string
        return self.title # Retorna o título da nota quando o objeto é convertido para string