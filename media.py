import webbrowser
# Here we declare the Movie class


class Movie():
    # init function defines movies class variables
    def __init__(self, movie_title, movie_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.movie_line = movie_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show trailers function open webbrowser with youtube trailer link
    def show_trailer(self):
        webbrowser.open(self.trailer)
