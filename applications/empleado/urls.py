from django.urls import path


def desde_emp(selft):
    print("Alo Empleado")


urlpatterns = [
    path('empleado/', desde_emp),
]
