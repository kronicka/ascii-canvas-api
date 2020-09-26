from app import strict_redis


def event_stream():
    """
    Set up a pub/sub event stream with Redis.
    """
    stream = strict_redis.pubsub()
    stream.subscribe('canvas_changes')

    for message in stream.listen():
        if message['type'] == 'message':
            data = f'data: {message["data"].decode("utf-8")}\n\n'
            yield data
