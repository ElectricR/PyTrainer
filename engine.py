from repository import Repository

class Engine:

    def __init__(self):
        self.repository = Repository()
        self.progress = self.repository.get_progress()
        self.lesson = self.repository.get_by_oid(self.progress)

    def advance(self):
        self.progress += 1
        self.repository.add_progress()
        self.lesson = self.repository.get_by_oid(self.progress)

    def check(self, answer):
        if answer == self.lesson[3]:
            self.advance()
            return True
        return False

    def get_lesson(self):
        return self.lesson[1:]

    def reset(self):
        self.progress = 1
        self.repository.reset_progress()
        self.lesson = self.repository.get_by_oid(self.progress)


        
