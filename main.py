from core.baseapp import baseApp
from data_model import book
from view.view_book import ViewBook

class MainApp(baseApp):
    def __init__(self):
        self.books = []
        self.inputbook = []
        self.viewbook = []
        baseApp.__init__(self)

class ViewBook (book) :
    def __init__(self):
        vbook = ViewBook (self, book)
        vbook.list_book()


if __name__ == "__main__":
    app = MainApp()
    app.run()

def list_book(self):
    return self.list_book
def add_book(self):
    return self.add_book()