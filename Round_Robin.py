# Input Phase
arrival_input = input("Enter Arrival Time (Separated by Spaces): ")  # Input arrival time
burst_input = input("Enter Burst Time (Separated by Spaces): ")  # Input burst time
time_quantum = int(input("Enter Time Quantum: "))  # Input time quantum for Round Robin

# Convert inputs to lists
arrival_time = list(map(int, arrival_input.split()))  # Convert arrival times to list
burst_time = list(map(int, burst_input.split()))  # Convert burst times to list

# Make a copy of the burst time for remaining burst time tracking
remaining_time = burst_time[:]

# Number of processes
num = len(arrival_time)

# Initialize lists
completion_time = [0] * num  # To store completion time of each process
waiting_time = [0] * num  # To store waiting time for each process
turnaround_time = [0] * num  # To store turnaround time for each process
normalized_tr = [0] * num  # To store normalized turnaround time
current_time = 0  # Track the current system time

# Process Queue (list of indices of processes in order of arrival)
process_queue = [i for i in range(num)]  # Start with all processes in arrival order

while process_queue:
    i = process_queue.pop(0)  # Take the first process in the queue
    arrival = arrival_time[i]
    
    # If the process arrives after the current time, skip forward to when it arrives
    if current_time < arrival:
        current_time = arrival

    # Process the current job for a time quantum or less if it can finish
    executed_time = min(time_quantum, remaining_time[i])
    remaining_time[i] -= executed_time
    current_time += executed_time

    # If the process has finished executing, calculate completion time
    if remaining_time[i] == 0:
        completion_time[i] = current_time
        turnaround_time[i] = completion_time[i] - arrival_time[i]  # TAT = Completion - Arrival
        waiting_time[i] = turnaround_time[i] - burst_time[i]  # WT = TAT - Burst
        # No need to add it back to the queue if finished
    else:
        # If the process is not finished, add it back to the end of the queue
        process_queue.append(i)

# Calculate Normalized Turnaround Time and averages
for i in range(num):
    normalized_tr[i] = turnaround_time[i] / burst_time[i]  # Normalized TAT = TAT / Burst

# Calculate Averages
avg_waiting_time = sum(waiting_time) / num
avg_turnaround_time = sum(turnaround_time) / num
avg_normalized_tr = sum(normalized_tr) / num

# Print Results
print("\nProcess Results:")
print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Completion Time':<20}{'Waiting Time':<15}{'Turnaround Time':<20}{'Normalized TAT':<20}")
print("-" * 115)

for i in range(num):
    print(f"{i+1:<10}{arrival_time[i]:<15}{burst_time[i]:<15}{completion_time[i]:<20}{waiting_time[i]:<15}{turnaround_time[i]:<20}{normalized_tr[i]:<20.2f}")

# Print Averages
print("-" * 115)
print(f"{'Averages':<10}{'':<15}{'':<15}{'':<20}{avg_waiting_time:<15.2f}{avg_turnaround_time:<20.2f}{avg_normalized_tr:<20.2f}")
