class RockGuitar:
    def __init__(self, guitarist="", guitar=""):
        self.guitarist = guitarist
        self.guitar = guitar

    def set_entry(self, guitarist, guitar=""):
        self.guitarist = guitarist
        self.guitar = guitar

    def __str__(self):
        return "{:<20s} {:<20s}".format(self.guitarist, self.guitar)
