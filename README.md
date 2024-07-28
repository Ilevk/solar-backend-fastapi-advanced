# Solar Backend FastAPI Advanced

Welcome to the Solar Backend FastAPI project! This project is designed to provide backend services for a LLM chat application using Upstage Solar API.
This repository contains simple RAGs for using the Layout Analysis, Embedding, and Chat features of the Upstage API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This is an example project for developing an Upstage Solar API service based on FastAPI.

## Features

- FastAPI for building APIs
- Integration with OpenAI for using Upstage Solar API
- Configuration management
- Error handling and logging
- Modular structure for scalability

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

    ```sh
    $ git clone https://github.com/ilevk/solar-backend-fastapi-advanced.git
    $ cd solar-backend-fastapi-advanced
    ```

2. **Set up a virtual environment:**
    - You can use any virtual environment tools.
    ```sh
    $ conda create --name solar python=3.12
    $ conda activate solar
    ```

3. **Install dependencies:**

    ```sh
    $ pip install poetry, pre-commit
    $ pre-commit install
    $ poetry install
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the necessary environment variables. For example:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Install Docker:**

    We will use Docker to run a ChromaDB instance. so you need to install docker, docker-compose.

    Follow the instructions on the [Official Docker website, Install Docker Engine](https://docs.docker.com/engine/install/) to install Docker on your machine.

    Follow the instructions on the [Official Docker website, Install Docker Compose](https://docs.docker.com/compose/install/) to install Docker Compose on your machine.

6. **Run ChromaDB for Vector Search**

    Run a ChromaDB instance using docker-compose:

    ```sh
    $ git clone https://github.com/chroma-core/chroma

    $ docker-compose up -d # start the ChromaDB instance
    $ docker-compose down  # stop the ChromaDB instance
    ```

## Usage

To run the application, use the following command:

```sh
$ uvicorn app.main:app --host {host} --port {port}
```

# Project Structure
Here is an overview of the project structure:

```
.
├── app
│   ├── clients
│   │   ├── open_ai.py
│   │   └── upstage.py
│   ├── core
│   │   ├── config.py
│   │   └── db.py
│   ├── models
│   │   └── schemas
│   │       └── document.py
│   ├── routers
│   ├── services
│   │   └── embedding.py
│   └── main.py
├── .pre-commit-config.yaml
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
└── start.sh
```

## FastAPI app
This directory contains the main application code.

- ### clients
  Contains client classes for interacting with external APIs.
  - `open_ai.py`: Client for interacting with the OpenAI API.
    - chat, stream_chat.
  - `upstage.py`: Client for interacting with the Upstage API.
    - embedding, layout_anlaysis.

- ### core
  Contains core functionalities and configurations.
  - `errors`: Custom error classes and handlers.
  - `config.py`: Configuration settings for the application, including environment variables.
  - `dependencies.py`: Dependency injection for FastAPI.
  - `db.py`: ChromaDB connection and setup.
  - `lifespan.py`: Application lifecycle events, such as startup and shutdown.
  - `logger.py`: Setup for logging.

- ### models
  Contains Pydantic models and schemas used for data validation and serialization.
  - chat, document, embedding, etc.

- ### routers
  Contains the API route definitions.
    - `chat.py`: Routes for chat operations.
    - `embedding.py`: Routes for embedding operations.

- ### services
  Contains business logic and service classes.
  - `embedding.py`: Services related to embedding operations.
  - `chat.py`: Services related to chat operations.
  - `service_factory.py`: Factory class for creating service instances.

- `main.py`: The entry point of the application. It initializes the FastAPI app and includes the application lifecycle events.

## Configuration
Configuration is managed using environment variables. You can set these variables in a .env file in the root directory.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Configuration
Configuration is managed using environment variables. You can set these variables in a .env file in the root directory.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
