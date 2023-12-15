## Getting Started

### Setting up the Server (modify script)
Default location for files to get saved at is `/tmp/simple-fileserver/`
Update `SAVE_FILEPATH` in `main.py` to update this

### Running the Server:
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
- Update `FILENAME` with path to filename.  Can be relative if in the CWD, or full path otherwise.
- Update `HOSTNAME` with the HOSTNAME or IP Address.

### Running the Client
`python client.py`