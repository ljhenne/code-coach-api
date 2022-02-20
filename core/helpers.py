def load_query(query_name: str) -> str:
    filepath = f"db/queries/{query_name}.sql"
    with open(filepath, "r") as f:
        return f.read()


def to_camel(string: str) -> str:
    string_parts = string.split("_")
    first = string_parts[0]
    remaining = "".join([word.capitalize() for word in string_parts])
    return first + remaining
