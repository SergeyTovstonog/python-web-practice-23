from celery import Celery
from tasks import add, multiply, priority_add, long_task
from celery_conf import app

# Normal task
result = add.delay(4, 4)
print(result.get())

long_task_result = long_task.delay()
# print(long_task_result.get())

# Priority task
priority_result = priority_add.apply_async((10, 10), priority=9)
print(priority_result.get())

# Long-running task
