n = int(input())
positive = []
negative = []
positive_count =0
negative_sum = 0
for _ in range (n):
    number = int(input())
    if number >=0:
        positive.append(number)
        positive_count += 1
    else:
        negative.append(number)
        negative_sum += number

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")