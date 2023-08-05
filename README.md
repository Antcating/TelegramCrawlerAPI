<h3 align="center">TelegramCrawler API</h3>

---

<p align="center"> Backend for <a href="https://github.com/Antcating/TelegramCrawler">Telegram Crawler</a> project built with PostgresQL and FastAPI
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Configs](#configs)
- [ToDo](#todo)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This project is an API backend of the [Telegram Crawler](https://github.com/Antcating/TelegramCrawler) project. 
This part is necessary for [Telegram Crawler](https://github.com/Antcating/TelegramCrawler) to operate properly. 
It contains several preset table in PostgresQL for storing Telegram Channels, Connections between them and the Queue mechanism.
Also included configured FastAPI with appropriate CRUD for all essential features of [Telegram Crawler](https://github.com/Antcating/TelegramCrawler).

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

Project is built using PostgresQL and FastAPI. There is a Docker container for both of them, so you don't have to setup everything yourself. In particular, for this project we will need docker-compose. You can install full [Docker Desktop](https://www.docker.com/products/docker-desktop/) bundle with docker-compose already built into it or install Docker Engine and docker-compose individually. 


### Installing

Make sure, that Docker is installed and running on your machine. 

Clone this project:

```
git clone https://github.com/Antcating/TelegramCrawlerAPI.git
```
Go to the project directory:

```
cd TelegramCrawlerAPI
```
And run docker-compose to start up the project:
```
docker-compose up
```

## ⭐ Usage <a name="usage"></a>

The container will start with API running locally on `127.0.0.1:8000`. 

You can check it using by going to `127.0.0.1:8000` in your browser. It has to return JSON with Ok row set to true. All possible API calls with descriptions could be seen on the `127.0.0.1:8000/docs`. You can try manually adding new channels or connections and see the response from database.

## 📖 Configs <a name="configs"></a>

There are several places where you can change some configs of the project. 
- In `docker-compose.yml` you can change your Postgres username (POSTGRES_USER), password (POSTGRES_PASSWORD) and name of the database (POSTGRES_DB). **If you change any of this rows, you have to update `config.ini` file with updated data using the pattern shown in `config.ini` file**
- `config.ini` also contains row named `DATE`. This row is used to analyze connections before and after specific `DATE`. For example, my use-case: analyzing connections between channel before and after beginning of full-blown russian invasion in Ukraine. You can set this DATE to whatever you want and it will reflect in `TelegramConnections` table. All connections before the break would have `0` in the `type` column of the table and all connections after the break would have `1`. 
If you want to disable this feature - set the `DATE` to `1/1/1970`, so that all the connections would be considered and after the break and their `type` column would always be set to `1`.

## ToDo <a name="todo"></a>

- Write wiki for CRUD
- Write front-end for the Database using API 

## ⛏️ Built Using <a name = "built_using"></a>

- [PostgresQL](https://www.postgresql.org/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - API

## ✍️ Authors <a name = "authors"></a>

- [@Antcating](https://github.com/Antcating)
