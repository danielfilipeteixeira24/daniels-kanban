import uuid

class Kanban:
    """
    This is a class for a "kanban". A "kanban" corresponds to a
    ticket or a post-it in a Kanban board.
    """
    def __init__(self, name, priority="7", color="blue"):
        self.id = uuid.uuid4()
        self.name = name
        self.priority = priority
        self.color = color
    
    def getId(self):
        """
        Returns a string with the ID of the Kanban.
        """

        return str(self.id)

class Queue:
    """
    Class for a Queue on a Kanban Board.
    A Queue has:
    - A "name" that defines what is the queue. (acts as ID)
    - A list of the active Kanbans.
      """
    def __init__(self, name):
        """
        """

        self.name = name
        self.kanbans = []

    def addKanban(self, kanban):
        """
        Add a new Kanban card to the queue.
        """
        self.kanbans.append(kanban)

    def removeKanban(self, kanban):
        """
        Removes a Kanban card from the queue.
        """
        self.kanbans.remove(kanban)

    def printKanbans(self):
        print("Queue " + self.name + ":")
        for kanban in self.kanbans:
            print(kanban.name)


class Board:
    """
    Class for a Kanban board.
    Each board will have one backlog queue, and at least one
    non-backlog queue.
    """
    def __init__(self):
        """
        Empty constructor.
        """
        self.backlog = Queue("Backlog")
        self.queues = []
    
    def addNewKanban(self, kanban):
        self.backlog.addKanban(kanban)

    def printKanbans(self):
        self.backlog.printKanbans()
        for queue in self.queues:
            queue.printKanbans()