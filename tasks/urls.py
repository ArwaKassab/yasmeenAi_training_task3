from django.urls import path
from tasks.views import task_views ,scatter_gather_views

urlpatterns = [
    path('', task_views.TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', task_views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('<int:pk>/toggle-status/', task_views.TaskToggleStatusView.as_view(), name='task-toggle-status'),
    path('scatter-gather/', scatter_gather_views.TaskAsyncParallelView.as_view(), name='task-scatter-gather'),
    path('no-scatter-gather/', scatter_gather_views.TaskSyncView.as_view(), name='task-scatter-gather'),
]
