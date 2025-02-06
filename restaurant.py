import validators
from typing import Optional

class Restaurant:
    """
    Class representing a restaurant.
    """
    __slots__ = ('_google_url', '_name', '_price_range', '_tags', '_dress_code', '_notes')

    def __init__(self, google_url: str, name: str, price_range: Optional[str],
                 tags: Optional[list[str]], dress_code: Optional[str], notes: Optional[str]):
        """
        Constructor.
        :param google_url: The URL to the restaurant on Google. 
        :param name: The name of the restaurant. 
        :param price_range: The price range of the restaurant. 
        :param tags: List of words describing the restaurant.
        :param dress_code: The dress code, if any.
        :param notes: Any additional notes about the restaurant.
        :raise Exception: If Google URL or name are empty, or if the URL isn't a valid URL.
        """
        if "" in (google_url.strip(), name.strip()):
            raise Exception("Must have non-empty Google URL and restaurant name.")
        elif validators.url(google_url) is not True:
            raise Exception("URL is not valid.")
        self._google_url = google_url
        self._name = name
        self._price_range = price_range
        self._tags = tags
        self._dress_code = dress_code
        self._notes = notes