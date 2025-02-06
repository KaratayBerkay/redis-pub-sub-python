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
