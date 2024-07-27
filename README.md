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
    git clone https://github.com/ilevk/solar-backend-fastapi-advanced.git
    cd solar-backend-fastapi-advanced
    ```

2. **Set up a virtual environment:**
    - You can use any virtual environment tools.
    ```sh
    conda create --name solar python=3.12
    conda activate solar
    ```

3. **Install dependencies:**

    ```sh
    pip install poetry
    poetry install
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the necessary environment variables. For example:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

To run the application, use the following command:

```sh
$ uvicorn app.main:app --reload
```

# Project Structure
Here is an overview of the project structure:

```
solar-backend-fastapi/
├── app/
│   ├── clients/
│   ├── core/
│   ├── main.py
│   ├── models/
│   │   └── schemas/
│   ├── routers/
│   └── services/
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
└── start.sh
```

- app/clients/: Contains client code for external services.
- app/core/: Core utilities like configuration and logging.
- app/main.py: Entry point of the application.
- app/models/: Data models and schemas.
- app/routers/: API route definitions.
- app/services/: Business logic and service layer.

## Configuration
Configuration is managed using environment variables. You can set these variables in a .env file in the root directory.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
