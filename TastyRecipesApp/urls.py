from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from TastyRecipesApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("TastyRecipesApp.web.urls")),
    path('recipe/', include("TastyRecipesApp.recipes.urls")),
    path('profile/', include("TastyRecipesApp.profiles.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)