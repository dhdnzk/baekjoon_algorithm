raw_data = str(input())

set = set()

for start_idx in range(0, len(raw_data)):

    for end_idx in range(start_idx + 1, len(raw_data) + 1):
        sub_str = raw_data[start_idx:end_idx]

        set.add(sub_str)


print(len(set))

