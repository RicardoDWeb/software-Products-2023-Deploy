from django.urls import path
from . import views

app_name = 'cadcli'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('cadastrar_cliente', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('consultar_todos_clientes', views.consultar_todos_clientes, name='consultar_todos_clientes'),
    path('alterar_cliente', views.alterar_cliente, name='alterar_cliente'),
    path('alterar_um_cliente/<int:pk>/', views.alterar_um_cliente, name='alterar_um_cliente'),
    path('excluir_cliente', views.excluir_cliente, name='excluir_cliente'),
    path('excluir_um_cliente/<int:pk>/', views.excluir_um_cliente, name='excluir_um_cliente'),
    path('pagina_de_sucesso', views.pagina_de_sucesso, name='pagina_de_sucesso'),
    path('pagina_exclusao_sucesso/', views.pagina_exclusao_sucesso, name='pagina_exclusao_sucesso'),

    # Outras URLs do aplicativo
]
