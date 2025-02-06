import redis
import time
import uuid
import json
import datetime
import pprint


channel_name = "broker"
name = f"Publisher:[{channel_name}]"
client_UUID = str(uuid.uuid4())

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def prepare_message_and_payload(message: str, name: str, client_UUID: str):
    message = f"{message} : {time.time()}"
    payload = dict(
        uu_id=str(uuid.uuid4()), 
        data=message,
        from_publisher=f"{name}-{client_UUID}",
        timestamp=time.time(),
        date=datetime.datetime.now().isoformat()
    )
    return message, payload


while True:
    print(f"Publisher: {name}-{client_UUID} is up and running...")
    message, payload = prepare_message_and_payload(
        message="Prepare Test Message From Publisher", 
        name=name, 
        client_UUID=client_UUID
    )
    print(f"Publisher UUID: {client_UUID}: \n")
    pprint.pprint(payload, indent=2)
    r.publish(channel_name, json.dumps({"NAME": f"{name}", "UUID": f"{client_UUID}", "DATA": payload}))
    time.sleep(5)
