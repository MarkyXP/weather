"""Business logic that connects between the Details, Database, and LLM
to add a location to the system

This module contains the following functions:
- `add(location)` - Adds the location to the database
"""


from app.database.db import Location_Metadata
import app.location.details as location
from app.location import llm

def add(location_name : str) -> int:
    """
    Checks the database if the location_name already exists, if it doesn't
    it uses wiki & an LLM to get landmarks & the lat/long of the location,
    and stores them in the database.

    Args:
        location_name (str): Name of the place (e.g. 'Melbourne')

    Returns:
        The ID of the location in the database

    Raises:
        ValueError if the location is already in the database.
    
    Usage:
        >>> add('Melbourne')
        1
    """
    location_name = location_name.strip()
    existing_location = Location_Metadata.select().where(
        Location_Metadata.name_lower == location_name.lower()
    )
    # assert existing_location, ValueError("Location already exists")
    details, lat, long = location.get_details(location_name)
    landmarks = llm.get_landmarks(location_name, details)
    # lat, long = llm.get_lat_long(details)
    loc = Location_Metadata.create(
        name_lower = location_name.lower().strip(),
        name = location_name,
        wiki_data = details,
        landmarks = landmarks,
        lat = lat,
        long = long
    )
    return loc.id

if __name__ == "__main__":
    from app.database.db import setup
    setup()
    import doctest
    doctest.testmod(
        verbose=True,
        optionflags=doctest.ELLIPSIS
    )