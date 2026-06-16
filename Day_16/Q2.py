arr = [1, 2, 2, 3, 3, 3, 4]

max_freq = 0
element = arr[0]

for i in arr:
    freq = arr.count(i)
    if freq > max_freq:
        max_freq = freq
        element = i

print("Maximum frequency element:", element)
print("Frequency:", max_freq)