seconds_1 = int(input())
hours = seconds_1 // 3600
minutes = (seconds_1 % 3600) // 60
seconds = (seconds_1 % 3600) % 60
print(f"{hours}:{minutes}:{seconds}")
