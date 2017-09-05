import webbrowser
# code based off of the website mini-project from the Udacity nanodegree


class Movie():
        def __init__(self, movie_title, poster_image,
                     trailer_youtube):
            # Constructor
            self.title = movie_title
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            # display the trailer in a new window
            webbrowser.open(self.trailer_youtube_url)
