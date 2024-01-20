## Getting Started

### Setting up the Server (modify script)
Default location for files to get saved at is `/tmp/simple-fileserver/`
Update `SAVE_FILEPATH` in `main.py` to update this

### Running the Server:
 - Switch to server directory:
   ```
   cd server
   ```
 - Create a virtual environment
   ```
   virtualenv venv
   ```
 - Activate virtual environment
   ```
   source venv/bin/activate
   ```
 - Install requirements
   ```
   pip install -r requirements.txt
   ```
 - Start uvicorn server
   ```
   uvicorn main:app --host 0.0.0.0
   ```

### Setting up the Client (modify script)

 - Update `HOSTNAME` with the HOSTNAME or IP Address.

### Setting up virtual env (needs to be done once)
 - Switch to client directory:
   ```
   cd client
   ```
 - Create a virtual environment
   ```
   virtualenv venv
   ```
 - Activate virtual environment
   ```
   source venv/bin/activate
   ```
 - Install requirements
   ```
   pip install -r requirements.txt
   ```

### Running the Client
 - Activate virtual environment (if you haven't already done so)
   ```
   source venv/bin/activate
   ```
 - Run script
   ```
   python client.py [Path To File/Directory]
   ```

### Running tests
 - Switch to tests directory
   ```
   cd tests
   ```
 - Create a virtual environment for running tests (one time only)
   ```
   virtualenv venv
   ```
 - Activate virtual environment for running tests
   ```
   source venv/bin/activate
   ```
 - Install requirements
   ```
   pip install -r ../server/requirements.txt
   pip install -r ../client/requirements.txt
   pip install pytest
   ```
 - Run pytest
   ```
   pytest
   ```
   To see console output on passing tests run:
   ```
   pytest -s
   ```
