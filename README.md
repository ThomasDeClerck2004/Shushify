# spotify-shhh
### You can run this script in the background while using Spotify to automatically mute ads.
## Requirements
- Python 3.x
- `spotipy` library
- `pycaw` library
- `python-dotenv` library

## Installation
You can install the required libraries using:
```bash
pip install spotipy pycaw python-dotenv
```

## Setup
1. Create a Spotify Developer account on this url https://developer.spotify.com/dashboard and set up an application to get your `CLIENT_ID` and `CLIENT_SECRET`, use http://127.0.0.1:8000/callback for your "Redirect URIs".
2. Create a `.env` file in the same directory as the script and add the following lines:
```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8000/callback
```
You are done! You can now run the script.