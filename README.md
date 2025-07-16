# Docker watch setup example

## Setup

### Prerequisites:
- docker
- uv

### Local

#### Setup the project's venv (for syntax highlighting in IDE)
```sh
uv venv
```

#### Install dependencies
```sh
uv sync
```

### Docker

#### Run in Docker:
```sh
docker compose up --build --watch -d
```
`docker` - uses docker

`compose` - indicates, that we want to set up multiple containers at once acording to [the compose file](docker-compose.yml)

`up` - means, we want to run containers

`--bulid` - builds the images, it is needed when running for the first time or after some changes

`--watch` - enables watch acording to the config in [the compose file](docker-compose.yml)

`-d` - also known as `--detach`, after this command, docker does not print logs in terminal and runs in background, thus making our terminal free

#### Stop docker
```sh
docker compose stop
```

#### Kill all containers 
preserves volumes, thus data from volumes remains intact (in this example these kind of data are postgres tables)
```sh
docker compose down
```

#### Kill all containers with volumes (removes all data from volumes)

> [!CAUTION]
> Use this command if you are 100% sure you want to delete the database

```sh
docker compose down -v
```
