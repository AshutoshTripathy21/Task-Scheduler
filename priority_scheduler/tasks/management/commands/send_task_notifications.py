from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.core.mail import send_mail
from tasks.models import Task

class Command(BaseCommand):
    help = 'Send notifications for tasks with approaching deadlines'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Recipient email address')

    def handle(self, *args, **options):
        recipient_email = options['email']

        # Define notification criteria (e.g., tasks with deadlines within 24 hours)
        deadline_threshold = timezone.now() + timezone.timedelta(days=1)
        
        # Query tasks needing notifications
        tasks_needing_notifications = Task.objects.filter(
            deadline__lte=deadline_threshold,
            completed=False
        )

        for task in tasks_needing_notifications:
            # Compose email content
            subject = f'Approaching Deadline: {task.title}'
            message = f'Task "{task.title}" is due on {task.deadline}. Priority: {task.priority}'
            
            # Send email notification
            send_mail(subject, message, 'exampleflask365@outlook.com', [recipient_email])
            
            self.stdout.write(self.style.SUCCESS(f'Notification sent for task: {task.title}'))
