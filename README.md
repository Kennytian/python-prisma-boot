# Python Prisma Boot

## 1. Environment
### 1.1 Create .venv
General Linux 
```shell
python -m venv .venv
```

macOS
```shell
python3 -m venv .venv
```

Ubuntu
```
apt-get update && apt install python3.10-venv
```
### 1.2 Activate
```shell
source .venv/bin/activate
```

## 2. Setup
### 2.1 Install dependencies
```shell
pip install -r requirements.txt
```

or

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### 2.2 Generate database types
```shell
cp .env.example .env
```

```shell
prisma generate
```

## 3. Run
```shell
uvicorn main:app --reload
```

## 4. Database
```shell
prisma db push
```

```shell
prisma db pull
```

## 5. Docker
### 5.1 Build
```shell
docker build -t python-prisma -f Dockerfile .
```

### 5.2 Run
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
