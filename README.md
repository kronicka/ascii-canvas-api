# ASCII Canvas API

Paint rectangles and flood fill shapes made out of characters on an ASCII canvas.
Spin up the server to manipulate the Canvas through RESTful endpoints and retrieve the modified Canvas back as a JSON.

## Launch the server locally (MacOS)

1. Clone this repository.
2. Install **Python** [3.7.4](https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.6.pkg) (or above).
> **NOTE**: This code has not yet been tested with any versions of Python higher than [3.7.6](https://www.python.org/ftp/python/3.7.6/python-3.7.6-macosx10.6.pkg), but it is likely to work with all stable releases above 3.7.
3. Install **virtualenv** by running this command in the terminal:  
 `pip install virtualenv`
4.  Create a virtual environment in the root of the repo, activate it, and install the required dependencies:  
`virtualenv --python=python3 venv`  
`. venv/bin/activate`  
`pip install -r requirements.txt`  
5. Run the server!  
`python3 app.py`
> **NOTE**: The server runs on 127.0.0.1:5000 by default.

## API Endpoints

These are the endpoints to interact with via the client of your choice.
### Quick Reference
* [**PUT** `/api/v1/canvas/paint`](#paint-a-rectangle) - Modify the Canvas by painting a Rectangle on it.
* [**PUT** `/api/v1/canvas/fill`](#fill-an-area) - Modify the Canvas by filling an Area of points, starting at a specified point.

### Full Reference
#### Paint a Rectangle
**PUT** `/api/v1/canvas/paint`  
**Expected JSON Payload**:  
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

#### Fill an Area
**PUT** `/api/v1/canvas/fill`  
**Expected JSON Payload**:  
```
{
    "x": <int>,
    "y": <int>,
    "fill_symbol": <str of length 1>
}
```

## Stuff left to do
- Implement persistence of the Canvas on application launches [x]
- Implement proper automated tests + API tests                [ ]
- Implement a read-only client + SSE for such client          [ ]
- Add success/failure flags and error message propagation     [ ]
- Reconsider Canvas cropping to be visual only                [ ]
- Elaborate on API responses in the Full Reference doc        [ ]
- Add a Postman collection for the requests                   [ ]
- Put the app in a Docker                                     [ ]
