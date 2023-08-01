<h3 align="center">TelegramCrawler API</h3>

---

<p align="center"> Backend for <a href="https://github.com/Antcating/TelegramCrawler">Telegram Crawler</a> project built with PostgresQL and FastAPI
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This project is an API backend of the [Telegram Crawler](https://github.com/Antcating/TelegramCrawler) project. 
This part is necessary for [Telegram Crawler](https://github.com/Antcating/TelegramCrawler) to operate properly. 

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

Project is built using PostgresQL and FastAPI. There is a Docker container for both of them, so you don't have to setup everything yourself. The only thing, that is needed is [Docker Desktop](https://www.docker.com/products/docker-desktop/) running locally on your machine or install Docker Engine and docker-compose individually. 


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

The container will start with API running locally on `0.0.0.0:8000`. 

You can check it using by going to `0.0.0.0:8000` in your browser. It has to return JSON with Ok row set to true. All possible API calls with descriptions could be seen on the `0.0.0.0:8000/docs`. You can try manually adding new channels or connections and see the response from database.

## ⛏️ Built Using <a name = "built_using"></a>

- [PostgresQL](https://www.postgresql.org/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - API

## ✍️ Authors <a name = "authors"></a>

- [@Antcating](https://github.com/Antcating)
