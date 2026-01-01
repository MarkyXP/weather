from app.database.db import Location_Metadata
import app.location.details as location
from app.location import llm

def add(location_name : str):
    """
    
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