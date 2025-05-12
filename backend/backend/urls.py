from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


"""
TokenObtainPairView é a view responsável por criar um novo par de tokens (access + refresh)
    Quando um usuário faz login, esta view:
        Recebe username e password via POST
        Valida as credenciais
        Retorna dois tokens:
        access_token: token de curta duração para autenticação
        refresh_token: token de longa duração para obter novos access tokens

TokenRefreshView é a view responsável por renovar tokens de acesso expirados
    Funcionamento:
        Recebe um refresh_token válido via POST
        Valida o refresh token
        Retorna um novo access_token
"""
# Em resumo:
# O access token é usado para autenticar requisições
# O refresh token permite renovar o access token sem necessidade de novo login


urlpatterns = [
    # URL para acesso ao painel administrativo do Django
    path('admin/', admin.site.urls), # Requer autenticação de superusuário: python manage.py createsuperuser
    
    # Endpoint para registro de novos usuários
    path('api/user/register/', CreateUserView.as_view(), name="register"), # Permite criar novos usuários sem autenticação (AllowAny em api.views)

    # Endpoint para login/autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),

    # Endpoint para renovar tokens de acesso
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),

    # Fornece interface de navegação da API
    path('api-auth/', include('rest_framework.urls')),

    # Inclui endpoint para listar, adicionar e deletar notas
    path('api/', include('api.urls')),
]
