## Nudge API Documentation

This API documentation provides an overview of the Nudge API, including the supported requests, base URL, API endpoints, payload structure, and descriptions of each endpoint's functionality.

# DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

### Base URL
The base URL for the Nudge API is: `/api/v3/app`

### Nudge Object Data Model
The Nudge object represents a user-created nudge for an event. Here is the data model for the Nudge object:

- `event_id` (integer): The ID of the event associated with the nudge.
- `article\event`(Choose field): this feild is to select between article or event
- `title` (string): The title of the nudge.
- `image` (file): An image file that serves as the cover for the nudge.
- `scheudle_on time` (timestamp): The time at which the user wants to send the nudge.
- `description` (string): A description of the nudge.
- `icon` (file): An icon for the nudge.
- `invitation` (string): A one-line invitation for the nudge.
- `preview`:to check  the invitation.
- `publish`:to print the invitation

### Endpoints

#### Retrieve a Nudge
- Request Type: GET
- Endpoint: `/nudges/<int:id>/`
- Description: Retrieves a specific nudge by ID.

#### List Nudges
- Request Type: GET
- Endpoint: `/nudges`
- Description: Retrieves a list of all nudges.

#### Create a Nudge
- Request Type: POST
- Endpoint: `/nudges`
- Payload:
  - `event_id` (integer, required): The ID of the event associated with the nudge.
  - `title` (string, required): The title of the nudge.
  - `image` (file, required): An image file that serves as the cover for the nudge.
  - `send_time` (timestamp, required): The time at which the user wants to send the nudge.
  - `description` (string, required): A description of the nudge.
  - `icon` (file, optional): An icon for the nudge.
  - `invitation` (string, optional): A one-line invitation for the nudge.
- Description: Creates a new nudge.

#### Update a Nudge
- Request Type: PUT
- Endpoint: `/nudges/:nudge_id`
- Payload: Same as the create payload
- Description: Updates an existing nudge by ID.

#### Delete a Nudge
- Request Type: DELETE
- Endpoint: `/nudges/:nudge_id`
- Description: Deletes a specific nudge by ID.

### Example API Usage

#### Retrieve a Nudge
- Request: GET `/api/v3/app/nudges/1`
- Response: 200 OK
  ```json
  {
    "id": 1,
    "event_id": 46,
    "title": "Sample Nudge",
    "image": "https://127.0.0.1:8000/nudge_image.jpg",
    "send_time": "2023-05-12T10:00:00Z",
    "description": "This is a sample nudge description.",
    "icon": "https://127.0.0.1:8000/nudge_icon.png",
    "invitation": "Join us for an exciting event!"
  }
  ```

#### List Nudges
- Request: GET `/api/v3/app/nudges`
- Response: 200 OK
  ```json
  [
    {
    "id": 1,
    "event_id": 46,
    "title": "Sample Nudge",
    "image": "https://127.0.0.1:8000/nudge_image.jpg",
    "send_time": "2023-05-12T10:00:00Z",
    "description": "This is a sample nudge description.",
    "icon": "https://127.0.0.1:8000/nudge_icon.png",
    "invitation": "Join us for an exciting event!"
  },
  {
    "id": 2,
    "event_id": 456,
    "title": "Sample Nudge",
    "image": "https://127.0.0.1:8000/nudge_image.jpg",
    "send_time": "2023-05-12T10:00:00Z",
    "description": "This is a sample nudge description.",
    "icon": "https://127.0.0.1:8000/nudge_icon.png",
    "invitation": "Join us for an exciting event!"
  }]
  ```

  # CURD operations

  - `create`:used to create a data
  - `update`:updating the previous stored data
  - `read`: used to read the stored data
  - `delete`: delete the stored data
  
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `nudges`, so we will use the following URLS - `/nudges/` and `/nudges/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`nudges` | GET | READ | Get all movies
`nudges/:id` | GET | READ | Get a single movie
`nudges`| POST | CREATE | Create a new movie
`nudges/:id` | PUT | UPDATE | Update a movie
`nudges/:id` | DELETE | DELETE | Delete a movie


     