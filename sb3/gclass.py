class GenericData(object): #pylint: disable=too-few-public-methods
    """A hunk of random API data
    that is not widely used enough to deserve its own class.
    """
    def __init__(self, *_, **data):
        """Initialize the data by copying kwargs to __dict__"""
        self.__dict__.update(data)

    def __repr__(self):
        """Represent some GenericData."""
        return (self._repr(self)
                if callable(getattr(self, "_repr", ""))
                else getattr(self, "_repr", ""))

    __str__ = __repr__

    def __getitem__(self, key):
        """Get an attribute like a dict item."""
        return self.__dict__.__getitem__(key)

    def __setitem__(self, key, val):
        """Set an attribute like a dict item."""
        return self.__dict__.__setitem__(key, val)

    def __delitem__(self, key):
        """Del an attribute like a dict item."""
        return self.__dict__.__delitem__(key)

class NameRepr(GenericData):
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"

_define = lambda name: type(name, (NameRepr,), {}) # makes subclass of GenericData-like
