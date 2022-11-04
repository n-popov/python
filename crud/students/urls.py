from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_handler),
    path('all/', all_students),
    path('add_student/', add_student),
    path('delete_student/<int:student_id>/', delete_student),
    path('update_student/', update_student),
]