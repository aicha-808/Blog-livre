from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import blogLivre, creer_livre, detail_livre, liste_articles, modifier_livre, supprimer_livre, telecharger_pdf

urlpatterns = [
    path('', blogLivre, name='accueil'),  # URL racine
    path("useradmin/", creer_livre, name='useradmin'),
    path("articles/", liste_articles, name='liste_articles'),
    path('livre/modifier/<int:id>/', modifier_livre, name='modifier_livre'),
    path('supprimer_livre/<int:id>/', supprimer_livre, name='supprimer_livre'),
    path('detail_livre/<int:id>/', detail_livre, name='detail_livre' ),
    path('telecharger_pdf/<int:id>/', telecharger_pdf, name='telechargerpdf')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
