import asyncio
from time import perf_counter
from asgiref.sync import async_to_sync, sync_to_async
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from tasks.models import Task
from tasks.serializers.task_serializers import TaskSerializer
from django.utils.timezone import now

class TaskAsyncParallelView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        start = perf_counter()
        result = async_to_sync(self.run_scatter_gather)(request.user)
        duration = perf_counter() - start

        # أضيف زمن التنفيذ للبيانات
        result["execution_time_seconds"] = f"{duration:.4f}"

        return Response(result)

    async def run_scatter_gather(self, user):
        today = now().date()

        @sync_to_async
        def get_completed_tasks():
            return list(Task.objects.filter(user=user, is_completed=True))

        @sync_to_async
        def get_incomplete_tasks():
            return list(Task.objects.filter(user=user, is_completed=False))

        @sync_to_async
        def get_completed_tasks_today():
            return list(Task.objects.filter(user=user, is_completed=True, created_at__date=today))

        @sync_to_async
        def get_incomplete_tasks_today():
            return list(Task.objects.filter(user=user, is_completed=False, created_at__date=today))

        @sync_to_async
        def count_completed_today():
            return Task.objects.filter(user=user, is_completed=True, created_at__date=today).count()

        @sync_to_async
        def count_incomplete_today():
            return Task.objects.filter(user=user, is_completed=False, created_at__date=today).count()

        results = await asyncio.gather(
            get_completed_tasks(),
            get_incomplete_tasks(),
            get_completed_tasks_today(),
            get_incomplete_tasks_today(),
            count_completed_today(),
            count_incomplete_today(),
        )

        (completed_tasks, incomplete_tasks,
         completed_today, incomplete_today,
         completed_count, incomplete_count) = results

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
