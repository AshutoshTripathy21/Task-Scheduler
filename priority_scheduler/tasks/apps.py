from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    def ready(self):
        # Importing the management command to register it
        from .management.commands import send_task_notifications