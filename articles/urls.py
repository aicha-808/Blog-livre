from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import blogLivre, creer_livre, detail_livre, modifier_livre, supprimer_livre

urlpatterns = [
    path('', blogLivre, name='accueil'),  # URL racine
    path("useradmin/", creer_livre, name='useradmin'),
    path('livre/modifier/<int:id>/', modifier_livre, name='modifier_livre'),
    path('supprimer_livre/<int:id>/', supprimer_livre, name='supprimer_livre'),
    path('detail_livre/<int:id>/', detail_livre, name='detail_livre' )
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
