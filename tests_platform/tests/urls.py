from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router dla API
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'results', views.ResultViewSet)

# Konfiguracja głównych ścieżek
urlpatterns = [
    path('', views.main_page, name='main_page'),  # Strona główna HTML
    path('api/', include(router.urls)),  # Wszystkie ścieżki API
]
