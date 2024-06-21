from celery import Celery
import tasks

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

app.conf.task_routes = {
    'tasks.priority_add': {'queue': 'priority'},
}

app.conf.task_queues = {
    'priority': {
        'exchange': 'priority',
        'routing_key': 'priority',
        'queue_arguments': {'x-max-priority': 10},
    },
}
app.set_default()
app.conf.task_default_priority = 5
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'
app.conf.accept_content = ['json']
