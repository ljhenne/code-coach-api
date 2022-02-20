CREATE TABLE attempt_event(
    id              uuid,
    user_id         uuid,
    event_type      varchar(7),
    question_name   text,
    question_url    text,
    timestamp       timestamptz
);