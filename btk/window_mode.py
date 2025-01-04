from enum import Enum


class WindowMode(Enum):
    """
    RENDER  : Use Render Window (Don't have Always On Top but is sizable)\n
    PREF    : Use Preference Window (Have Always On Top but is not sizable)
    NEW     : Open a new window (Can't do much more)
    """

    RENDER = 0
    PREF = 1
    NEW = 2
