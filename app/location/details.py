import wikipedia


def get_details(location: str):
    """
    Gets some information about a location (from wiki)

    Args:
        location: The name of the location to search for.

    Returns:
        A string containing details about the location.

    Usage:
    >>> get_details("Melbourne")
    '...Flinders Street station...'
    """
    location_page_name = wikipedia.search(f"{location}")
    if not location_page_name:
        raise ValueError(f"Could not find information about {location}")
    location_page = wikipedia.page(location_page_name[0])
    content = location_page.content
    lat, long = [float(v) for v in location_page.coordinates]
    return content, lat, long


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
