#!/usr/bin/python3
"""M3U playlist handling."""

# stdlib imports
from random import shuffle
from re import match
from os import linesep
from os.path import expanduser

# internal imports
from handrit.exceptions import PlaylistReadError

# external imports
# :^)


EXT_M3U_HEADER = "#EXTM3U"


class M3UPlaylist(object):
    """Playlist class for m3u format."""

    def __init__(self, path=None, entries=None):
        """Init method."""
        self.extm3u = False
        self.entries = entries

        assert not (path and entries), \
            "path and entries supplied, choose one only"

        if path:
            # Read playlist from supplied path
            self.path = path
            self.read(path)
            self.new_file = False
        else:
            self.new_file = True

    def __len__(self):
        """Return number of songs in playlist."""
        return len(self.entries)

    def __getitem__(self, key):
        """Allow access to playlist entries via key."""
        return self.entries[key]

    def __setitem__(self, key, item):
        """Assign `item` to `key`."""
        self.entries[key] = item

    def __contains__(self, item):
        """Check if entry is in playlist."""
        return item in self.entries

    def __add__(self, other):
        """Append two playlists."""
        if not isinstance(other, M3UPlaylist):
            raise TypeError("only instances of type {} can be added".format(
                type(self)))
        return M3UPlaylist(entries=self.entries + other.entries)

    def _parse(self, playlist):
        """Parse playlist in m3u format."""
        entries = []
        if match(r"^#EXTM3U", playlist.readline()):
            self.extm3u = True
        else:
            playlist.seek(0)
        for line in playlist:
            if not match(r"^#", line):
                entries.append(line.strip(' \n\t\r'))
        self.entries = entries

    def _add_entries(self, file_paths, position=None):
        """Add multiple entries to playlist."""
        if position:
            self.entries[position:position] = file_paths
        else:
            self.entries.extend(file_paths)

    def _add_entry(self, file_path, position=None):
        """Add entry to playlist."""
        if position:
            self.entries.insert(position, file_path)
        else:
            self.entries.append(file_path)

    def save(self, path):
        """Save playlist in m3u format."""
        lines = map(lambda x: "".join(x, linesep), self.entries)
        if self.extm3u and self.new_file:
            lines.insert(0, "".join(EXT_M3U_HEADER, linesep))
        with open(path, 'w+') as f:
            f.writelines(lines)

    def remove_duplicates(self):
        """Remove duplicate paths."""
        # XXX: Uh oh... this will destroy the sort order
        self.entries = list(set(self.entries))

    def add(self, file_paths, position=None):
        """Add file(s) to playlist."""
        if isinstance(file_paths, str):
            self._add_entry(file_paths, position)
        else:
            self._add_entries(file_paths, position)

    def index(self, needle):
        """Return index of file in playlist. Does not match line number."""
        return self.entries.index(needle)

    def shuffle(self):
        """Shuffle playlist order."""
        # Note that the only way to restore the original order is to read the
        # playlist file again.
        shuffle(self.entries)

    def read(self, path):
        """Read playlist file."""
        self.new_file = False
        path = expanduser(path)
        try:
            with open(path, 'r') as f:
                self._parse(f)
        except Exception as e:
            raise PlaylistReadError(e)
