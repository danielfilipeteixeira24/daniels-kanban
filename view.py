from controller import Controller

if __name__=="__main__":
    controller = Controller()
    controller.createKanban("New Kanban")
    controller.printKanbans()