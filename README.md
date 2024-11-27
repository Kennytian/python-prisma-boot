# Python Prisma Boot

## Environment
```shell
python -m venv .venv
```
```shell
source .venv/bin/activate
```
```shell
touch .gitignore requirements.txt
```

## Dependencies

```shell
cat <<EOF > requirements.txt
fastapi
uvicorn
pydantic
prisma
EOF
```

## Setup
```shell
pip3 install -r requirements.txt
```
```shell
prisma init --datasource-provider postgresql
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
prisma generate
```
