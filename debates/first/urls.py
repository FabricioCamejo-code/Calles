from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('', views.home, name='home'),
    path('paises/', views.lista_paises, name='paises'),
    path('ciudades/<int:pais_id>/', views.ciudades, name='ciudades'),
    path('calles/<int:ciudad_id>/', views.calles, name='calles'),
    path('votar/<int:calle_id>/', views.votar, name='votar'),
    path('gracias/', views.gracias, name='gracias'),
    path('listado_votos/', views.listado_votos, name='listado_votos'),
    path('detalles_calle/<int:calle_id>/', views.detalle_calle, name='detalles_calle'),
    path('media/<path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('confirmar-voto/<str:confirmation_token>/', views.confirmar_voto, name='confirmar_voto'),
    path('ingresar-datos-votante/<str:token>/', views.ingresar_datos_votante, name='ingresar_datos_votante'),
    path('ingresar-datos-votante/<str:token>/<int:calle_id>/', views.ingresar_datos_votante, name='ingresar_datos_votante'),
    path('procesar_voto/<str:token>/', views.procesar_voto, name='procesar_voto'),
    path('error/', views.error_page, name='error'),
    

]

handler404 = 'first.views.error_404'
handler500 = 'first.views.error_500'

# la siguiente línea se utiliza para servir archivos estáticos durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)