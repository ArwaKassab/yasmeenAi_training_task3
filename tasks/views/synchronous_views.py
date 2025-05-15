from time import perf_counter
from asgiref.sync import async_to_sync, sync_to_async
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from tasks.models import Task
from tasks.serializers.task_serializers import TaskSerializer
from django.utils.timezone import now

class TaskSyncView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        start = perf_counter()
        result = self.run_sync(request.user)
        duration = perf_counter() - start

        # أضيف زمن التنفيذ للبيانات
        result["execution_time_seconds"] = f"{duration:.4f}"

        return Response(result)

    def run_sync(self, user):
        today = now().date()

        completed_tasks = list(Task.objects.filter(user=user, is_completed=True))
        incomplete_tasks = list(Task.objects.filter(user=user, is_completed=False))
        completed_today = list(Task.objects.filter(user=user, is_completed=True, created_at__date=today))
        incomplete_today = list(Task.objects.filter(user=user, is_completed=False, created_at__date=today))
        completed_count = Task.objects.filter(user=user, is_completed=True, created_at__date=today).count()
        incomplete_count = Task.objects.filter(user=user, is_completed=False, created_at__date=today).count()

        completed_tasks_serialized = TaskSerializer(completed_tasks, many=True).data
        incomplete_tasks_serialized = TaskSerializer(incomplete_tasks, many=True).data
        completed_today_serialized = TaskSerializer(completed_today, many=True).data
        incomplete_today_serialized = TaskSerializer(incomplete_today, many=True).data

        return {
            "completed_tasks": completed_tasks_serialized,
            "incomplete_tasks": incomplete_tasks_serialized,
            "completed_today": completed_today_serialized,
            "incomplete_today": incomplete_today_serialized,
            "count_completed_today": completed_count,
            "count_incomplete_today": incomplete_count,
        }
