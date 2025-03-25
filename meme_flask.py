#!/bin/python3

# Importing necessary libraries
from flask import Flask, render_template  # Flask is a web framework used to build web applications.
import requests  # Requests is a Python library to make HTTP requests to APIs.
import json  # JSON module is used to handle JSON data (i.e., parsing and converting).

# Initialize the Flask web application.
app = Flask(__name__)  # Flask is a web framework, and we create an app instance using Flask.

def get_meme():
    # Function to fetch a meme from the meme API.

    # URL pointing to the meme API that fetches meme data from the "dankmemes" subreddit.
    # This URL could be dynamic if you want to fetch memes from other subreddits.
    url = "https://meme-api.com/gimme/dankmemes"  # Fetches a random meme from the dankmemes subreddit.

    # Sends a GET request to the URL and fetches the response data.
    response = json.loads(requests.request("GET", url).text)  # Sends a GET request to the meme API and parses the JSON response.

    # Extracting the URL of the large version of the meme image from the response.
    meme_large = response["preview"][-2]  # Accessing the second last element in the 'preview' list, which is the large version of the meme image.

    # Extracting the subreddit name from the response data.
    subreddit = response["subreddit"]  # The name of the subreddit where the meme was sourced from.

    # Return the meme image URL and subreddit name to be used later.
    return meme_large, subreddit  # This will be used in the rendering of the HTML template.

# This is the route for the homepage of the web application.
@app.route("/")  
def index():
    # The function associated with the "/" route, which is triggered when the user visits the homepage.

    # Call the get_meme function to fetch the meme URL and subreddit.
    meme_pic, subreddit = get_meme()  # Calling the get_meme function to get the meme data.

    # Rendering the HTML template named "meme_index.html" and passing the meme data (meme picture URL and subreddit name) to it.
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)  # This renders the template and passes the meme data to it.

# Start the Flask web server, making it accessible to all devices on the network.
app.run(host="0.0.0.0", port=80)  # Running the Flask app on all available network interfaces, on port 80.
