"""Plylist exceptions."""


class UnknownFormatException(Exception):
    """Raised if playlist format cannot be determined."""

    pass


class UnsupportedFormatException(Exception):
    """Raised if playlist format is not supported."""

    pass


class PlaylistReadError(Exception):
    """Raised if playlist file cannot be read."""

    pass
