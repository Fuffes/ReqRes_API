from enum import Enum


class EnumList(Enum):

    @classmethod
    def list(cls):
        '''
        may help to get the list with values(i'm not sure)
        '''
        return list(map(lambda c: c.value, cls))
