from django.conf import settings
from django.urls import path,include

from .views import ModelSave
from django.conf.urls.static import static


urlpatterns = [
    path('mldb/',ModelSave.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)