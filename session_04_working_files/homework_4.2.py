"""
 homework_4.2.py -- Sum up bytes by user id from a log file

 Author: Mary Kidd (kiddmary@gmail.com)
 Last Revised: 11/9/2024
"""

import re

user_bytes = {}

counter = 0

with open('access_log.txt') as fh:

    for line in fh:

        match_netid = re.search(r'~([A-Za-z]{2,3}\d+)', line)
        match_bytes = re.search(r'\s(\d+)$', line)

        if match_netid and match_bytes:
            counter += 1
            username = match_netid.group(1)
            bytes_used = int(match_bytes.group(1))

            if username in user_bytes:
                user_bytes[username] += bytes_used
            else:
                user_bytes[username] = bytes_used

filtered_usernames = [username for username in user_bytes if user_bytes[username] > 10000000]
sorted_usernames = sorted(filtered_usernames, key=user_bytes.get, reverse=True)

print(f'{counter} matches found (both user id and end-of-line bytes found on the line)')

for username in sorted_usernames:
    print(f'{username}: {user_bytes[username]}')