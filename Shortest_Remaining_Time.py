arrival_input = input("Enter Arrival Time (Seperate by Spaces): ")
burst_input = input("Enter Burst Time (Seperate by Spaces): ")

arrival_time = list(map(int, arrival_input.split()))
burst_time = list(map(int, burst_input.split()))

num = len(arrival_time)

# Initializing variables
completion_time = [0] * num
waiting_time = [0] * num
turnaround_time = [0] * num
normalized_tr = [0] * num
remaining_time = burst_time[:]  # To track remaining burst time for each process
complete = 0
current_time = 0
min_remaining_time = float('inf')
shortest = 0
check = False

# Loop until all processes are complete
while complete != num:
    # Find the process with the minimum remaining time at the current time
    for i in range(num):
        if (arrival_time[i] <= current_time and remaining_time[i] < min_remaining_time and remaining_time[i] > 0):
            min_remaining_time = remaining_time[i]
            shortest = i
            check = True

    if not check:
        current_time += 1
        continue

    # Process the shortest job
    remaining_time[shortest] -= 1
    min_remaining_time = remaining_time[shortest]

    if min_remaining_time == 0:
        min_remaining_time = float('inf')

    # If a process is fully executed
    if remaining_time[shortest] == 0:
        complete += 1
        check = False

        finish_time = current_time + 1
        completion_time[shortest] = finish_time

        # Calculate waiting time
        waiting_time[shortest] = (finish_time - burst_time[shortest] - arrival_time[shortest])

        if waiting_time[shortest] < 0:
            waiting_time[shortest] = 0

    current_time += 1

# Calculate turnaround time and normalized turnaround time
for i in range(num):
    turnaround_time[i] = burst_time[i] + waiting_time[i]
    normalized_tr[i] = turnaround_time[i] / burst_time[i]

# Calculating averages
sum_wt = sum(waiting_time)
sum_tr = sum(turnaround_time)
sum_ntr = sum(normalized_tr)
avg_wt = sum_wt / num
avg_tr = sum_tr / num
avg_ntr = sum_ntr / num

# Print the header
print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Waiting Time':<15}{'Completion Time':<20}{'Turnaround Time':<20}{'Normalized TAT':<20}")
print("-" * 115)

# Print the details for each process
for i in range(num):
    print(f"{i + 1:<10}{arrival_time[i]:<15}{burst_time[i]:<15}{waiting_time[i]:<15}{completion_time[i]:<20}{turnaround_time[i]:<20}{normalized_tr[i]:<20.2f}")

# Print the averages
print("-" * 115)
print(f"{'Averages':<10}{'':<15}{'':<15}{avg_wt:<15.2f}{'':<20}{avg_tr:<20.2f}{avg_ntr:<20.2f}")