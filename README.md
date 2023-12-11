### Getting Started

Default location for files to get saved at is `/tmp/simple-fileserver/`
Update `SAVE_FILEPATH` in `main.py` to update this

Running the Server:
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
