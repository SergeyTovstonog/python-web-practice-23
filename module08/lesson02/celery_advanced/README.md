`celery -A celery_conf worker --loglevel=info --queues=priority,celery`
`celery -A celery_conf beat --loglevel=info`