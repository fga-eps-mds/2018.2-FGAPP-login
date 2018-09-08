class User(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'email', 'password'):
            setattr(self, field, kwargs.get(field, None))