from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from core.constants import EventType
from core.helpers import to_camel


class AttemptEvent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    user_id: str

    event_type: EventType
    question_name: str
    question_url: str
    timestamp: datetime

    class Config:
        alias_generator = to_camel
