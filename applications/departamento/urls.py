from django.urls import path


def desde_dep(selft):
    print("Alo Departamento")


urlpatterns = [
    path('departamento/', desde_dep),
]
