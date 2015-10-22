import webbrowser


# Define the movie class and method for showing trailers
class Movie():
    """This class provides a way to store movie related information as well as a method for opening a movie trailer."""
    

    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, value_to_my_brain):
        """Inits the Movie class with title, storyline, poster image, and url to the video trailer.""" 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.value_to_my_brain = value_to_my_brain

    def show_trailer(self):
        """Opens up the video trailer in a browser window."""
        
        webbrowser.open(self.trailer_youtube_url)

