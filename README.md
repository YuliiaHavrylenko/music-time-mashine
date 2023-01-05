<h1 align="center">Music Time Machine</h1>

## Description
This script allows you to create a playlist of popular songs from a specific date using the Billboard Hot 100 chart. Simply enter a date and the script will use the requests and BeautifulSoup libraries to scrape song titles from the chart, search for those songs on Spotify using the spotipy library, and add them to a private playlist on your Spotify account. This is a fun way to "travel back in time" and discover the music that was popular on a specific date.

### About the project.
- The requests library, which is used to send a GET request to the Billboard website to retrieve the Hot 100 chart data for a given date
- The BeautifulSoup library, which is used to parse the chart data and extract the song titles
- The spotipy used to authorize the user's Spotify account and interact with the Spotify API.


## Project setup
To set up and run this script, you will need to do the following:

1. Install the required libraries:

- requests
- beautifulsoup4
- spotipy
You can install these libraries using pip, the Python package manager. For example:

```
pip install requests beautifulsoup4 spotipy
```

1. Obtain a Spotify developer account and create a new app. This will give you a CLIENT_ID and CLIENT_SECRET that you will need to use to authorize the user's Spotify account.

2. Replace the placeholder values for CLIENT_ID and CLIENT_SECRET in the script with your own values.

3. Set the OAUTH_AUTHORIZE_URL to the URL of your app. This is the URL that the user will be redirected to after authorizing the app.

4. Run the script using a Python interpreter. The user will be prompted to enter a date in the format "YYYY-MM-DD" and will be directed to the Spotify website to authorize the app. After authorizing the app, the script will scrape the Billboard chart for the given date, search for the songs on Spotify, and create a private playlist with the results. The playlist will be added to the user's Spotify account.