from django.urls import path
from empleados.views import (
    delete_emp,
    edit_emp,
    show_emp,
    create_emp,
)

urlpatterns = [
    path("", show_emp, name="empleados"),
    path("<int:id>/", edit_emp, name="empleado"),
    path("borrar/<int:id>/", delete_emp, name="delete_emp"),
    path("nuevo/", create_emp, name="nuevo_emp"),
]