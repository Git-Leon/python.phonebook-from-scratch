# Created by Leon Hunter at 9:54 AM 10/23/2020
class Person(object):

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name