# FastAPI Todo List API

This is a simple Todo List API built using FastAPI and Pydantic. It allows users to create, list, and retrieve todo items.

## Features

- **Create Todo Item**: Add a new todo item to the list.
- **List Todo Items**: Retrieve a list of todo items, optionally with a limit.
- **Get Todo Item by ID**: Retrieve a specific todo item by its ID.

## Technologies Used

- FastAPI
- Pydantic

### API Endpoints

- **GET /**: Root endpoint, returns a simple greeting message.
- **POST /items**: Create a new todo item.
- **GET /items**: List all todo items, with an optional limit parameter.
- **GET /items/{item_id}**: Get a todo item by its ID.
