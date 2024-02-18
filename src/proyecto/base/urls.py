from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro, PaginaDeslogueado
from django.contrib.auth.views import LogoutView

#import views
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('login/', Logueo.as_view(), name='login'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'), # al desloguearse le lleva a la pagina login 
               path('deslogin/', PaginaDeslogueado.as_view(), name='deslogueado'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'), # para que la url sea 127.0.0.1:8000/tarea/num_tarea
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),] 