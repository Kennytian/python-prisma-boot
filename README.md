# Python Prisma Boot

## Environment
Normal Linux and macOS
```shell
python -m venv .venv
```

Ubuntu
```
apt-get update && apt install python3.10-venv
```

```shell
source .venv/bin/activate
```

## Setup
### Install dependencies
```shell
pip install -r requirements.txt
```
or

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### Generate database types
```shell
cp .env.example .env
```

```shell
prisma generate
```

## Run
```shell
uvicorn main:app --reload
```

## Database
```shell
prisma db push
```

```shell
prisma db pull
```

## Docker
### Build
```shell
docker build -t python-prisma -f Dockerfile .
```

### Run
```shell
docker rm -f python-app;docker run --env-file .env -p 8123:8000 -d --name python-app python-prisma:latest
```
or

```shell
docker-compose down && docker-compose up -d && docker image prune -f && docker-compose logs -f
```

## Test
```shell
curl http://localhost:8123
```