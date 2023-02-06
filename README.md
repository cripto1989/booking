# Booking project

1. [Requirements](#requirements)
2. [Configuration](#configuration)
    * [Installing dependencies](#installing-dependencies)
    * [Running project](#running-project)
3. [Endpoints](#endpoints)
    * [Create a room](#create-a-room)
    * [Delete a room](#delete-a-room)
    * [Create an event](#create-an-event)
    * [List all events](#list-all-events)
    * [Create a booking](#create-a-booking)
    * [Cancel a booking](#cancel-a-booking)
4. [Running tests](#running-tests)

## Requirements
- Python 3.9.16
- Sqlite
- Pyenv

## Configuration
Feel free to use wathever tools to manage a virtual environment such as pipenv, pyenv-virtualenv, poetry and so on. For this project pyenv was used.

### Installing dependencies
After activating a virtualenv use the next command to install all dependency package
```
pip install -r requirements/requirements.txt -r requirements/requirements-test.txt
```

### Running project
For running the project just execute the next command
```
python manage.py runserver
```

## Endpoints
All available endpoints

### Create a room
`POST /api/v1.0/room/` 
```json
{
    "capacity": "15"
}
```

### Delete a room
`DELETE /api/v1.0/room/delete/d39ffa6f-5adf-4e2e-bd38-161a334b4ca3/`

### Create an event
`POST /api/v1.0/event/` 
```json
{    
    "room": "e975dbec-96fa-4a9d-b50d-8819fedcaec5",
    "type": "Public"
}
```

### List all events
`GET /api/v1.0/events/`

### Create a booking
`POST /api/v1.0/booking/` 
```json
{    
    "event": "4d8651f5-ffc2-4c6c-ba09-5a9690c76f32"    
}
```

### Cancel a booking
`DELETE /api/v1.0/booking/cancel/ec85b4e2-7b8c-49c7-9f03-546c4f49b760/`

## Running tests
```
pytest
```