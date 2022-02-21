# Code Coach API

## Running the server

```bash
uvicorn main:app --reload
```

## The lifecycle of a question attempt

Six event types:

* start
* test
* fail
* success
* stop
* abandon

### Start

Opens a new problem attempt.

### Test

Triggered when the user runs the code using whatever test functionality the site provides.

### Fail

Triggered when the user hits submit but the attempt was unsuccessful.

### Success

Triggered when the user hits submit adn the attempt was successful.

Stops the timer.

### Abandon

When the user leaves the page, either by closing the tab, or navigating away.

Stops the timer.
