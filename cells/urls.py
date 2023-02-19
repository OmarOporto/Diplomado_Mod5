from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"cells", views.cellsViewSet)
router.register(r"prisoner", views.prisonerViewSet)
router.register(r"guards", views.guardsViewSet)

urlpatterns = [
    path('conctact/<str:name>', views.contact, name='index'),
    #path('categorias', views.categorias, name='categorias'),
    path('categorias/cantidad/',views.categoria_count),
    path('guards/onMorning/',views.guards_onMorinng),
    path('', include(router.urls))
]