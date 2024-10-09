# 1.11:  Use csv.writer to selectively write columns to a CSV.  Loop through the list of lists and
# write only the company and country columns to the file.  Include the header.  Close the file, then
# look for newfile4.csv in the session directory.

rows = [
         [ 'company', 'state/province', 'country' ],
         [ 'Acme', 'Caliornia', 'US' ],
         [ 'Bento', 'Toledo', 'SP' ],
         [ 'OuiOui', 'Bourges', 'FR' ],
         [ 'Beta', 'New York', 'US' ]
       ]

fname = '../newfile4.csv'

wfh = open(fname, 'w', newline='')
writer = csv.writer(wfh)


