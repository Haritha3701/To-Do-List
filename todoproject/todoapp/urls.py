from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from todoapp import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('delete/<int:task_id>/', views.delete_task, name="deletepage"),
    path('update/<int:task_id>/', views.update, name="updatepage"),
    path('cvhome/', views.Tasklistview.as_view(), name="cvhome"),
    path('cvdetail/<int:pk>/', views.Taskdetailview.as_view(), name="cvdetail"),
    path('cvupdate/<int:pk>/', views.Taskupdateview.as_view(), name="cvupdate"),
    path('cvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name="cvdelete"),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
