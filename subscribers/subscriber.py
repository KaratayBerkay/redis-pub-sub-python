import redis
import uuid

channel_name = "broker"
name = f"Subscriber:[{channel_name}]"
client_UUID = str(uuid.uuid4())

def message_handler(message):
    print(f"Received: {dict(message)}")  # Debugging line


r = redis.Redis(host='redis', port=6379, decode_responses=True)
p = r.pubsub()
p.subscribe(**{channel_name: message_handler})

print(f"Subscribed to {channel_name}...")  # Debugging line

for message in p.listen():  # Listen for new messages
    print(f"Message Read From: {name}-{client_UUID} Received: {message}")  # Debugging line