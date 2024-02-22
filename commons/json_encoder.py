from json import JSONEncoder


class ObjectJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
