# Simple Books API

The scope of this application is to test the functionalities of the Simple Books API.

The documentation can be found visiting the [Simple Books API Documentation page](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md).

The API is available at `https://simple-books-api.glitch.me`

## Prerequisites 
To run the application, you need python 3.11, venv and pip to be installed. 

The libraries used are requests (version 2.31), pytest (version 7.4.3), pytest-html (version 4.1.1). 
To install them, run the Terminal command:
```commandline
pip install -r requirements.txt
```

## Running the tests

The tests can be found in the _test_ fonder.
To run any test, you can run the corresponding file.

## Generating the report

To generate the report, run the Terminal command: 
```commandline
pytest --html=report.html
```