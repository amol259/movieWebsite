import webbrowser as wb
"""
    Movie Class that stores a title, a poster image, and a youtube trailer
"""
class Movie():
    def __init__(self,title,poster_image_url,trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
        #Opens Youtube Trailer in browser when called 
    def show_trailer(self):
        wb.open(self.trailer_youtube_url)
