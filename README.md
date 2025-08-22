# Shushify
### You can run this script in the background while using Spotify to automatically mute ads.
## Requirements
- Python 3.x
- A Spotify account
- A Spotify Developer account
- A Code Editor (like VSCode, PyCharm, etc.)
- `spotipy` library
- `pycaw` library
- `python-dotenv` library

## Setup 
First you will need to create a virtual environment (optional but recommended) do this in your terminal of your project directory:
```bash
python -m venv venv
venv\Scripts\Activate  # On Windows
```
Note: you need to install python first.

If you get the error UnauthorizedAccess you might need to change the execution policy in a PowerShell terminal (run as administrator):
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
```

You can now install the required libraries in your environment using:
```bash
pip install spotipy pycaw python-dotenv
```

## Installation
1. Create a Spotify Developer account on this url https://developer.spotify.com/dashboard and set up an application to get your `CLIENT_ID` and `CLIENT_SECRET`, use http://127.0.0.1:8000/callback for your "Redirect URIs" during setup.
2. Update the already existing .env-example file in the project directory with your `CLIENT_ID` and `CLIENT_SECRET` and rename it to `.env` it should look like this:
```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8000/callback
```
Note: Replace `your_spotify_client_id` and `your_spotify_client_secret` with the values from your Spotify Developer application.