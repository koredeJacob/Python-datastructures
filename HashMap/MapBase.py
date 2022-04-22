from msvcrt import kbhit
from typing import MutableMapping


class MapBase(MutableMapping):
    
    class _Item:
        __slots__='_key','_value'
        
        def __init__(self,k,v):
            self._key=k
            self._value=v
        
        def __eq__(self, other) -> bool:
            return self._key==other._key
        
        def __lt__(self,other):
            return self._key<other._key
        def __ne__(self,other) -> bool:
            return not(self._key==other._key)
        