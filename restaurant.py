from typing import Optional

class Restaurant:
    """
    Class representing a restaurant.
    """
    __slots__ = ('_google_url', '_name', '_price_range', '_tags', '_dress_code', '_notes')

    def __init__(self, google_url: Optional[str], name: Optional[str], price_range: Optional[str],
                 tags: Optional[list[str]], dress_code: Optional[str], notes: Optional[str]):
        """
        Constructor.
        :param google_url: The URL to the restaurant on Google. 
        :param name: The name of the restaurant. 
        :param price_range: The price range of the restaurant. 
        :param tags: List of words describing the restaurant.
        :param dress_code: The dress code, if any.
        :param notes: Any additional notes about the restaurant.
        """
        self._google_url = google_url
        self._name = name
        self._price_range = price_range
        self._tags = tags
        self._dress_code = dress_code
        self._notes = notes