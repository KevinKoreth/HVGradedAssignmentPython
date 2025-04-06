```
This endpoint retrieves the configuration data in JSON format. The configuration data is parsed from the `config.ini` file and saved as `database.json`. If the `database.json` file is not found, an error message is returned.

Example Response:
{
    "Database": {
        "host": "localhost",
        "port": "3306",
        "username": "admin",
        "password": "secret"
    },
    "Server": {
        "address": "192.168.0.1",
        "port": "8080"
    }
}
```

## How to Run the Server

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
    ```bash
    pip install flask
    ```
3. Navigate to the directory containing `run.py`:
    ```bash
    cd <DIRECTORY>/config_management
    ```
4. Start the server by executing:
    ```bash
    python run.py
    ```
5. Access the endpoint by visiting `http://127.0.0.1:5000/config` in your web browser or using a tool like `curl` or Postman.
```
