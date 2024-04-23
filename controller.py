from model import Kanban, Board
from repository import BoardRepository

class Controller:
    """
    Workflows:
    1. Add new Kanban card (add to Backlog).
    2. Move Kanban cards between different queues.
    3. Remove Kanban.
    4. Edit Kanban.
    
    Regarding the Setup of queues:
    1. Add queues.
    2. Move queues.
    3. Edit queues.
    4. Delete queues.
    """

    filename = "model.txt"

    def __init__(self):
        self.repository = BoardRepository(self.filename)
        self.board = self.repository.loadBoard()

    def createKanban(self, name):
        kanban = Kanban(name)
        self.board.addNewKanban(kanban)
        self.repository.saveBoard(self.filename)

    def saveBoard(self):
        self.repository.saveBoard(self.filename)

    def printKanbans(self):
        self.board.printKanbans()