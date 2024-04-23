import pickle

from model import Board

class BoardRepository:
    def __init__(self, filename):
        """
        Constructor with the filename to load the 
        board and the model.
        """

        self.filename = filename

    def loadBoard(self):
        board = Board()
        
        try:
            with open(self.filename, mode="rb") as file:
                board = pickle.load(file)
        except:
            # Do nothing.
            pass

        return board

    def saveBoard(self, board):
        with open(self.filename, mode="wb") as file:
            pickle.dump(board, file)

    