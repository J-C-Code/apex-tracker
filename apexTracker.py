import sys
from functions import *
# Modules above

command = sys.argv[1].lower()

if command == "rank":
    username = sys.argv[-1]
    getRank(username)
elif command == "stats":
    username = sys.argv[-1]
    getStat(username)
elif command == "news":
    news()
elif command == "map":
    map()
else:
    print('Unknown error, make sure you\'re using "rank" or "stats"')
