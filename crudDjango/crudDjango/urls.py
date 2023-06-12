from django.urls import path
from appCRUD import views

urlpatterns = [
    #rota, view responsável, nome de referencia
    path('',views.home,name='home'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('listagem',views.listagem,name='listagemUsuarios')
]
