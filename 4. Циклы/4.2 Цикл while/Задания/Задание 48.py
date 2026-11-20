start_sum = float(input())
target_sum = float(input())
percent = float(input())
month = 0
while start_sum <= target_sum:
    month += 1
    start_sum += start_sum * (percent / 100 / 12)
    print(f"{month} - {start_sum:.2f}")