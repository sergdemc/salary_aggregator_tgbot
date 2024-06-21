# RLT Salary Aggregator Bot
Telegram Bot for salary aggregation: Asyncio, Aiogram, MongoDB, and Docker.

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.9 or higher installed:

```bash
>> python --version
Python 3.12.4
```

#### Docker

The project uses Docker to run the database. To install Docker use its [official instruction](https://docs.docker.com/get-docker/).

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
git clone git@github.com:sergdemc/salary_aggregator_tgbot.git && cd salary_aggregator_tgbot
```

Then you have to install all necessary dependencies in your virtual environment:

```bash
make install
```

## Usage

For start the application you need to create `.env` file in the root directory of the project. You can use `.env.example` as a template.

Start MongoDB in the Docker container and load data to DB by running:
```bash
make load-data
```

Start Bot by running:
```bash
make start-bot
```

_The bot will be available in Telegram_

Input data format:
```
{
    "dt_from": "2022-09-01T00:00:00",
    "dt_upto": "2022-12-31T23:59:00",
    "group_type": "month"
}
```

Stop the service by running
```bash
make stop
```

## Tests

To run tests, use the command:
```bash
make test
```

More commands are available in the `Makefile`.
