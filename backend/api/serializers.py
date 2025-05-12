from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer): # Cria serializador para User
    class Meta: # configuração do serializador
        model = User # informa que o modelo Django User será serializado para JSON
        fields = ["id", "username", "password"] # informa quais campos serão serializados
        # Embora a senha possa ser escrita, ela nunca pode ser retornada nas respostas da API!
        # Com 'write_only':True, a senha não será incluída quando os dados do usuário forem serializados (convertidos para JSON/lidos)
        extra_kwargs = {"password": {"write_only": True}} # Isso é uma medida de segurança importante para evitar que senhas sejam expostas nas respostas da API
            # Garante que a senha seja definido automaticamente pelo backend

    def create(self, validated_data):
        """
        Sobrescrição do comportamento padrão de criação de usuário 
        do Django REST Framework.

        * Recebe dados validados (validated_data)
            - Dados já validados pelo serializador
            - Contém campos como username e password (e o id, claro)
        
        * Cria usuário com segurança
            - Usa create_user() do Django ao invés de create()
            - create_user() aplica hash na senha automaticamente
            - O operador ** desempacota o dicionário de dados
        
        * Retorna o usuário criado
            - Objeto User criado é retornado para o DRF

        Nota:   Sem este método customizado, as senhas seriam salvas em texto puro, 
                o que seria um risco de segurança.
        """
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer): # Cria serializador para Note
    class Meta: # configuração do serializador
        model = Note # informa que o modelo Django Note será serializado para JSON
        fields = ["id", "title", "content", "created_at", "updated_at", "author"] # informa quais campos serão serializados
        extra_kwargs = {"author": {"read_only": True}} # Previne que um usuário crie notas em nome de outro usuário
            # Garante que o autor seja definido automaticamente pelo backend.
            # Sem esta configuração, qualquer cliente da API poderia potencialmente modificar 
            # o autor de uma nota, comprometendo a segurança e confiabilidade do sistema.