def flatten_lists(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, list) and not isinstance(x, (str, bytes)):
            for sub_x in flatten_lists(x):
                yield sub_x
        else:
            yield x