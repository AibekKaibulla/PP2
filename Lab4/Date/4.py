from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 30, 0)
date2 = datetime(2024, 2, 11, 10, 45, 0) 

difference = date2 - date1

difference_seconds = difference.total_seconds()

print("Difference between the two dates in seconds:", difference_seconds)