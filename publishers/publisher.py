import redis
import time
import uuid
import json
import datetime


channel_name = "broker"
name = f"Publisher:[{channel_name}]"
client_UUID = str(uuid.uuid4())

r = redis.Redis(host='redis', port=6379, decode_responses=True)

while True:
    message = f"Test Message {time.time()}"
    payload = dict(
        uu_id=str(uuid.uuid4()), 
        data=message,
        from_publisher=f"{name}-{client_UUID}",
        timestamp=time.time(),
        date=datetime.datetime.now().isoformat()
    )
    print(f"Publisher: {name}-{client_UUID} Sending: {payload}")
    r.publish(channel_name, json.dumps({"name": f"{name}-{client_UUID}", "data": payload}))
    time.sleep(5)
