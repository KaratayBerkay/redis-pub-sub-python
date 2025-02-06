# Redis Docker Setup and Usage

1 Publisher and 5 subcriber Pub/sub Redis

### Running Redis Container

```bash
# Start All Publishers and Subscribers via docker
docker compose up -d --build
```

## Requirements

- Docker
- Python
- Redis-py package (`pip install redis`)

## Additional Commands

```bash
# Stop All container
docker compose down
```

## Notes

- Default Redis port is 6379
- No authentication is set by default
- Data is not persisted by default

## Outputs

Output: redis-server

```python
2025-02-06 17:40:23 1:C 06 Feb 2025 14:40:23.009 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
2025-02-06 17:40:23 1:C 06 Feb 2025 14:40:23.009 _ Redis version=7.4.2, bits=64, commit=00000000, modified=0, pid=1, just started
2025-02-06 17:40:23 1:C 06 Feb 2025 14:40:23.009 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
2025-02-06 17:40:23 1:M 06 Feb 2025 14:40:23.012 _ monotonic clock: POSIX clock_gettime
2025-02-06 17:40:23 1:M 06 Feb 2025 14:40:23.015 _ Running mode=standalone, port=6379.
2025-02-06 17:40:23 1:M 06 Feb 2025 14:40:23.016 _ Server initialized
2025-02-06 17:40:23 1:M 06 Feb 2025 14:40:23.017 _ Ready to accept connections tcp
```

Output: redis-publisher

```python
2025-02-06 17:40:26 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': 'f3faadea-69a9-43ed-abb8-10a8d10400b7', 'data': 'Test Message 1738852826.0965672', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852826.0966303, 'date': '2025-02-06T14:40:26.096639'}
2025-02-06 17:40:31 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': '6de0a586-9027-40ae-98b1-535029d1d76b', 'data': 'Test Message 1738852831.1154695', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852831.1155615, 'date': '2025-02-06T14:40:31.115565'}
2025-02-06 17:40:36 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': '1f3ea67a-93d1-4d96-8e17-56f3d1d95ca1', 'data': 'Test Message 1738852836.1214228', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852836.1215355, 'date': '2025-02-06T14:40:36.121539'}
2025-02-06 17:40:41 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': '19fb816e-7d0c-4a29-a6cb-94a1b2ccbf49', 'data': 'Test Message 1738852841.1274476', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852841.12754, 'date': '2025-02-06T14:40:41.127544'}
2025-02-06 17:40:46 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': '92545a19-66fa-4e99-b72d-2f4b29252def', 'data': 'Test Message 1738852846.135932', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852846.1360197, 'date': '2025-02-06T14:40:46.136023'}
2025-02-06 17:40:51 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': 'db79021e-ae82-4076-a4b0-a08f44ea31c1', 'data': 'Test Message 1738852851.141963', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852851.1420588, 'date': '2025-02-06T14:40:51.142062'}
2025-02-06 17:40:56 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': '65082a1f-c79d-4073-80aa-4304d29bd48d', 'data': 'Test Message 1738852856.1479404', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852856.1480284, 'date': '2025-02-06T14:40:56.148032'}
2025-02-06 17:41:01 Publiher: Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055 Sending: {'uu_id': '7a097980-a06c-4375-844a-ccd5629604ab', 'data': 'Test Message 1738852861.1539502', 'from_publisher': 'Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055', 'timestamp': 1738852861.1540413, 'date': '2025-02-06T14:41:01.154045'}
```

Output: redis-subscriber1

```python
2025-02-06 17:40:26 Subscribed to broker...
2025-02-06 17:40:26 Message Read From: Subscriber:[broker]-0e96c77d-b79e-4315-9ef1-b9386927ac0b Received: {'type': 'subscribe', 'pattern': None, 'channel': 'broker', 'data': 1}
2025-02-06 17:40:26 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "f3faadea-69a9-43ed-abb8-10a8d10400b7", "data": "Test Message 1738852826.0965672", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852826.0966303, "date": "2025-02-06T14:40:26.096639"}}'}
2025-02-06 17:40:31 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "6de0a586-9027-40ae-98b1-535029d1d76b", "data": "Test Message 1738852831.1154695", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852831.1155615, "date": "2025-02-06T14:40:31.115565"}}'}
2025-02-06 17:40:36 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "1f3ea67a-93d1-4d96-8e17-56f3d1d95ca1", "data": "Test Message 1738852836.1214228", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852836.1215355, "date": "2025-02-06T14:40:36.121539"}}'}
2025-02-06 17:40:41 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "19fb816e-7d0c-4a29-a6cb-94a1b2ccbf49", "data": "Test Message 1738852841.1274476", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852841.12754, "date": "2025-02-06T14:40:41.127544"}}'}
2025-02-06 17:40:46 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "92545a19-66fa-4e99-b72d-2f4b29252def", "data": "Test Message 1738852846.135932", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852846.1360197, "date": "2025-02-06T14:40:46.136023"}}'}
2025-02-06 17:40:51 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "db79021e-ae82-4076-a4b0-a08f44ea31c1", "data": "Test Message 1738852851.141963", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852851.1420588, "date": "2025-02-06T14:40:51.142062"}}'}
2025-02-06 17:40:56 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "65082a1f-c79d-4073-80aa-4304d29bd48d", "data": "Test Message 1738852856.1479404", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852856.1480284, "date": "2025-02-06T14:40:56.148032"}}'}
```

Output: redis-subscriber2

```python
2025-02-06 17:40:25 Subscribed to broker...
2025-02-06 17:40:25 Message Read From: Subscriber:[broker]-bb625b1a-69cb-48cd-b0f8-d3aeac95b905 Received: {'type': 'subscribe', 'pattern': None, 'channel': 'broker', 'data': 1}
2025-02-06 17:40:26 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "f3faadea-69a9-43ed-abb8-10a8d10400b7", "data": "Test Message 1738852826.0965672", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852826.0966303, "date": "2025-02-06T14:40:26.096639"}}'}
2025-02-06 17:40:31 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "6de0a586-9027-40ae-98b1-535029d1d76b", "data": "Test Message 1738852831.1154695", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852831.1155615, "date": "2025-02-06T14:40:31.115565"}}'}
2025-02-06 17:40:36 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "1f3ea67a-93d1-4d96-8e17-56f3d1d95ca1", "data": "Test Message 1738852836.1214228", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852836.1215355, "date": "2025-02-06T14:40:36.121539"}}'}
2025-02-06 17:40:41 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "19fb816e-7d0c-4a29-a6cb-94a1b2ccbf49", "data": "Test Message 1738852841.1274476", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852841.12754, "date": "2025-02-06T14:40:41.127544"}}'}
2025-02-06 17:40:46 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "92545a19-66fa-4e99-b72d-2f4b29252def", "data": "Test Message 1738852846.135932", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852846.1360197, "date": "2025-02-06T14:40:46.136023"}}'}
2025-02-06 17:40:51 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "db79021e-ae82-4076-a4b0-a08f44ea31c1", "data": "Test Message 1738852851.141963", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852851.1420588, "date": "2025-02-06T14:40:51.142062"}}'}
2025-02-06 17:40:56 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "65082a1f-c79d-4073-80aa-4304d29bd48d", "data": "Test Message 1738852856.1479404", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852856.1480284, "date": "2025-02-06T14:40:56.148032"}}'}
2025-02-06 17:41:01 Received: {'type': 'message', 'pattern': None, 'channel': 'broker', 'data': '{"name": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "data": {"uu_id": "7a097980-a06c-4375-844a-ccd5629604ab", "data": "Test Message 1738852861.1539502", "from_publisher": "Publisher:[broker]-1841dba0-6dcf-4f6f-a714-6edc6f5e1055", "timestamp": 1738852861.1540413, "date": "2025-02-06T14:41:01.154045"}}'}
```
