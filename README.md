# ASCII Canvas API

Paint rectangles and flood fill shapes made out of characters on an ASCII canvas.
Spin up the server to manipulate the Canvas through RESTful endpoints and retrieve the modified Canvas back as a JSON.


## Launch the server in a Docker

1. Clone this repository.
2. Install the latest version of [Docker](https://docs.docker.com/get-docker/).
> **NOTE**: Docker Compose is included in Docker Desktop for MacOS and Windows, but may require additional installs for Linux or alternative cases. See [this page](https://docs.docker.com/compose/install/) for additional info.
3. Run the app by running this command in the root of the repo:  
`docker-compose up` (use `-d` to run in the background)
> **NOTE**: The server runs on `localhost:1337` by default and should be accessible from a browser.


That's it!

## Launch the server locally (MacOS)

1. Clone this repository.
2. Install **Python** [3.7.4](https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.6.pkg) (or above).
> **NOTE**: This code has not yet been tested with any versions of Python other than 3.7.4, 3.7.6, and [3.8.5](https://www.python.org/downloads/release/python-385/), but it is likely to work with all stable releases above 3.7.
3. Install **virtualenv** by running this command in the terminal:  
 `pip install virtualenv`
4.  Create a virtual environment in the root of the repo, activate it, and install the required dependencies:  
`virtualenv --python=python3 venv`  
`. venv/bin/activate`  
`pip install -r requirements.txt`  
5. Install and run Redis:  
`brew install redis`  
`redis-server` (use `--daemonize yes` to run in the background)  
5. Run the server!  
`python3 app.py`  
> **NOTE**: The server runs on `localhost:1337` by default and should be accessible from a browser.

That's it!

## API Endpoints

These are the endpoints to interact with via the client of your choice.  
A Postman Collection for the following is available in `resources` directory.  
### Quick Reference
* [**PUT** `/api/v1/canvas/paint`](#paint-a-rectangle) - Modify the Canvas by painting a Rectangle on it.
* [**PUT** `/api/v1/canvas/fill`](#fill-an-area) - Modify the Canvas by filling an Area of points, starting at a specified point.

### Full Reference
#### Paint a Rectangle
**PUT** `/api/v1/canvas/paint`  
**Expected JSON Request Payload Format**:  
```
{
    "x": <int>,
    "y": <int>,
    "width": <int>,
    "height": <int>,
    "fill_symbol": <str of length 1: optional>,
    "outline_symbol": <str of length 1: optional>
}
```  
**Sample Request Payload**:
``` 
{
    "x": 0,
    "y": 0,
    "width": 2,
    "height": 2,
    "fill_symbol": "+"
}
```  
**Successful Response Example**:  
The current Canvas with a `width = 2` and `height = 2` rectangle at `(0, 0)`, filled with `+` symbol, assuming previously empty Canvas:  
```
{
    "data": [
        ["+", "+", " ", " ", ...],
        ["+", "+", " ", " ", ...],
        [" ", " ", " ", " ", ...],
        ...
    ],
    "errors": null
} 
```  

#### Fill an Area
**PUT** `/api/v1/canvas/fill`  
**Expected JSON Payload Format**:  
```
{
    "x": <int>,
    "y": <int>,
    "fill_symbol": <str of length 1>
}
```
**Sample Request Payload**:
``` 
{
    "x": 2,
    "y": 5,
    "fill_symbol": "-"
}
```  
**Successful Response Example**:  
The current Canvas, fully filled with `-`, assuming previously empty Canvas:  
```
{
    "data": [
        ["-", "-", "-", "-", ...],
        ["-", "-", "-", "-", ...],
        ["-", "-", "-", "-", ...],
        ...
    ],
    "errors": null
} 
```  
## Running Tests
### Running tests locally
Running tests locally can be done via running the following command in the root of the repo:  
`python3 -m pytest`  
> **NOTE**: This is assuming the server was set up correctly, and the virtualenv is activated.
### Running tests in a Docker
Running test with the Docker set up can be done via running the following command:  
`docker exec -it canvas_api python3 -m pytest`
> **NOTE**: This is assuming the server was set up correctly, using Docker, and the `canvas_api` container is running.
