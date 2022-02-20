from core import StrEnum


class EventType(StrEnum):
    ABANDON = "abandon"
    FAIL = "fail"
    START = "start"
    STOP = "stop"
    SUCCESS = "success"
    TEST = "test"
