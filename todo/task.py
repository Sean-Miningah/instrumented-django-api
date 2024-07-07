from celery import shared_task

@shared_task
def send_completion_email(username, user_email):
  
  # sending email function should be here 
  print('Task completed:', username)
  