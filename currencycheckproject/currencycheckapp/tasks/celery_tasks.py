from celery import shared_task

@shared_task
def your_celery_task():
    print("Executing example task...")

    # Your task logic here
    
    print("Example task completed.")