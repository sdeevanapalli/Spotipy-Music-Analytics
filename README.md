# Spotipy Music Application

## Overview
This is a Python application that utilizes the Spotipy API to interact with Spotify's music data. It allows users to perform various tasks such as checking current playback, accessing top tracks of artists, managing playlists, and more.

## Features
- Current Playback: Check what's currently playing.
- Top 10 Songs of any Artist: Discover the top tracks of any artist.
- Artists You Follow: View a list of artists you follow on Spotify.
- Your Top Artist Plays: See your top played artists.
- Your Live Devices: View and manage your live Spotify devices.
- Personal Information: View your Spotify profile information.
- Play Music: Search and play any song available on Spotify.
- Your Top Songs: See your top played songs.

## Requirements
- Python 3.x
- Spotipy library (install using `pip install spotipy`)
- dotenv library (install using `pip install python-dotenv`)

## Getting Started
1. Clone this repository to your local machine.

2. Create a Spotify Developer Account:
    - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
    - Log in with your Spotify account or sign up if you don't have one.
    - Create a new app and note down the `CLIENT_ID` and `CLIENT_SECRET`.

3. Set Up Environment Variables:
    - Create a `.env` file in the root directory of the project.
    - Add the following lines to the `.env` file:
        ```
        CLIENT_ID=<your-client-id>
        CLIENT_SECRET=<your-client-secret>
        ```
    - Replace `<your-client-id>` and `<your-client-secret>` with the respective values obtained from the Spotify Developer Dashboard.

4. Install Dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Run the Application:
    ```
    python app.py
    ```

6. Follow the prompts to interact with the application.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.
