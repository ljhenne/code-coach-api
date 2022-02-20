from fastapi import FastAPI

from core.models import AttemptEvent
from db.manager import save_attempt_event

app = FastAPI()

questions = {}


@app.post("/attempt-events/")
def create_attempt_event(attempt_event: AttemptEvent):
    save_attempt_event(attempt_event)
    print(attempt_event)
