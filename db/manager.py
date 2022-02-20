import psycopg2.extras

from core.helpers import load_query
from core.models import AttemptEvent


def save_attempt_event(attempt_event: AttemptEvent):
    query = load_query("save_attempt_event")
    conn_params = dict(
        dbname="",
        user="",
        password="",
        host="",
        port="5432"
    )
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cur:
            query_params = {
                attempt_event.user_id,
                attempt_event.event_type,
                attempt_event.question_name,
                attempt_event.question_url
            }
            cur.execute(query, query_params)
            return cur.fetch_all()
