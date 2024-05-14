# Apex Tracker to get rank, stats, news, map rotation and more!

## Local development
1. Create and activate Python virtual environment
   ```python
   python -m venv venv
   source venv/bin/activate #This works on Mac/Linux. 
   venv/scripts/activate # This works on Windows.
   ```
2. Install requirements
   ```python
   pip install -r requirements.txt
   ```
3. Create an api key file (make sure you have an API key from https://apexlegendsapi.com/)
   ```shell
   echo 'key = "api_key_here"' > apiKey.py
   ```