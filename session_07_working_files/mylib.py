"""
 mylib.py -- Read a configuration file, write new values or update values to a CSV.

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/27/2024
"""

import csv

class Config:
    """Handles configuration file settings by reading and writing key/value pairs"""

    def __init__(self, filename):
        """Initialize the Config instance and load configuration data."""

        self.filename = filename
        self.format = (filename.split('.')[-1])
        self.params = self.read_csv_file()

    def read_csv_file(self):
        """Read CSV file and return a dictionary of key/value pairs"""

        params = {}
        file = open(self.filename, 'r')
        reader = csv.reader(file)

        rowcounter = 0

        for row in reader:
            rowcounter += 1
            if len(row) != 2:
                raise ValueError(f"File '{self.filename}' appears to be corrupted. "
                                 f"See row {rowcounter}.")
            key, value = row
            params[key] = value

        file.close()
        return params

    def get(self, key, default=None):
        """Return value for a key if it exists, otherwise return None or default"""

        return self.params.get(key, default)

    def set(self, key, value, overwrite=False):
        """Sets new key/value pair, or if the key exists, overwrites with new value"""

        if key in self.params and not overwrite:
            raise KeyError(f'Key "{key}" already exists')

        self.params[key] = value
        self.write_csv_file()

    def write_csv_file(self):
        """Writes new or updated keys/values to the specified configuration file"""

        fh = open(self.filename, 'w', newline='')

        writer = csv.writer(fh)

        for key, value in self.params.items():
            writer.writerow([key, value])

        fh.close()

    def __str__(self):
        """Returns the configuration instance as a string-formatted filename"""

        return f"Config('{self.filename}')"