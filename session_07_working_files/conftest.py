from mylib import Config

# INSTANTIATE THE INSTANCE:  READ DATA VALUES FROM FILE,
# AND STORE THEM IN THE INSTANCE (using an internal dict)

conf = Config('pconfig.csv')
print("Initial value of 'db_uname2':", conf.get('db_uname2'))  # Should print 'herbert'

# .get()  RETRIEVES A VALUE BASED ON A KEY (check these against CSV above)
# or None or default value if not found

print(conf.get('db_uname'))        # george
print(conf.get('db_password'))     # password1
print(conf.get('data_query'))      # SELECT this, that FROM ...
print(conf.get('badkey'))          # None
print(conf.get('badkey', 0))       # 0 (default set through .get())

# .set() ADDS A NEW PAIR TO INSTANCE, AND WRITES IT TO THE FILE
# (note that writing to the file will initially blank out the file, which
# may cause it to be empty the next time it is read (which may be
# "ValueError:  not enough values to unpack"); see read_csv_file(self) below

conf.set('db_uname2', 'herbert')
print(conf.get('db_uname2'))       # herbert

# .set() with overwrite=True ALLOWS OVERWRITE OF AN EXISTING KEY (and of course writes to file)
# (note that writing to the file will initially blank out the file, which
# may cause it to be empty the next time it is read (which may be
# "ValueError:  not enough values to unpack"); see read_csv_file(self) below

conf.set('db_uname2', 'gladys', overwrite=True)
print(conf.get('db_uname2'))       # gladys

# WE CAN CONFIRM THE NEW PAIR HAS BEEN WRITTEN TO FILE, BY INSTANTIATING
# A NEW INSTANCE FROM THE SAME FILE AND CHECKING FOR THE KEY

newconf = Config('pconfig.csv')
print(newconf.get('db_uname2'))    # gladys  (confirms that the file has the new value)

# FILENAME AND FILE EXTENSION ARE ALSO STORED IN THE INSTANCE

print(conf.filename)               # pconfig.csv
print(conf.format)                 # csv    (consider os.path.splitext())

# PRINTING THE INSTANCE CALLS THE __str__()  METHOD
# THE STRING RETURNED FROM THIS METHOD IS PRINTED

print(conf)         # this prints the string Config('pconfig.csv')
                    # (consider self.__class__.__name__)