import redis
import uuid
import pprint

channel_name = "broker"
name = f"Subscriber:[{channel_name}]"
client_UUID = str(uuid.uuid4())

def message_handler(message):
    print(f"Message Received:\n")  # Debugging line
    pprint.pprint(message, indent=2)


r = redis.Redis(host='redis', port=6379, decode_responses=True)
p = r.pubsub()
p.subscribe(**{channel_name: message_handler})

print(f"Subscribed to {channel_name}...")  # Debugging line

for message in p.listen():  # Listen for new messages
    print(f"Subscribed ID: {name}-{client_UUID}\n")  # Debugging line
    print(f"Message Received : \n")
    