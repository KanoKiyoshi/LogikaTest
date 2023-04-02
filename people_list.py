#from people import People

class people_list:
    def __init__(self):
        self.people_list = []
    
    def add(self, obj:People):
        self.people_list.append(obj)
    
    def get_all(self, flag):
        if flag == 'json':
            