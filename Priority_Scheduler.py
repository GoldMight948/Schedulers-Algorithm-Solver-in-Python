# Input Phase
arrival_input = input("Enter Arrival Time (Separated by spaces): ")  # Input arrival time
burst_input = input("Enter Burst Times (Separated by spaces): ")  # Input burst time
priority_input = input("Enter Priority (Separated by spaces): ")  # Input priority for each process

# Convert inputs to lists
arrival_time = list(map(int, arrival_input.split()))  # Split arrival times into a list
burst_time = list(map(int, burst_input.split()))  # Split burst times into a list
priority = list(map(int, priority_input.split()))  # Split priority into a list

# Combine arrival, burst, and priority into a list of tuples (arrival, burst, priority)
processes = list(zip(arrival_time, burst_time, priority))

# Sort processes by priority (smaller value means higher priority), if equal, sort by arrival time
processes.sort(key=lambda x: (x[2], x[0]))  # Sort by priority first, then arrival time

# Number of processes
num = len(arrival_time)

# Initialize lists
completion_time = [0] * num
current_time = 0  # Track the current time in the system

# Scheduling based on priority
for i in range(num):
    arrival, burst, priority = processes[i]  # Define arrival, burst time, and priority for each process
    start_time = max(current_time, arrival)  # Process starts at the current time or after it arrives
    completion = start_time + burst  # Calculate the completion time
    current_time = completion  # Move the current time forward after the process completes
    completion_time[i] = completion  # Record completion time for each process

# Waiting Time Calculation
waiting_time = [0] * num  # Initialize waiting time list
for i in range(num):
    arrival, burst, priority = processes[i]  # Get process details
    comp = completion_time[i]  # Get completion time
    waiting = comp - arrival - burst  # Waiting time = Completion time - Arrival time - Burst time
    waiting_time[i] = waiting  # Store waiting time

# Turnaround Time Calculation
turnaround_time = [0] * num  # Initialize turnaround time list
for i in range(num):
    arrival, burst, priority = processes[i]  # Get process details
    wait = waiting_time[i]  # Get waiting time
    turnaround = wait + burst  # Turnaround time = Waiting time + Burst time
    turnaround_time[i] = turnaround  # Store turnaround time

# Normalized Turnaround Time Calculation
normalized_tr = [0] * num  # Initialize normalized turnaround time list
for i in range(num):
    arrival, burst, priority = processes[i]  # Get process details
    tr = turnaround_time[i]  # Get turnaround time
    ntr = tr / burst  # Normalized Turnaround Time = Turnaround time / Burst time
    normalized_tr[i] = ntr  # Store normalized turnaround time

# Calculate Averages
sum_wt = sum(waiting_time)  # Total waiting time
sum_tr = sum(turnaround_time)  # Total turnaround time
sum_ntr = sum(normalized_tr)  # Total normalized turnaround time

avg_wt = sum_wt / num  # Average waiting time
avg_tr = sum_tr / num  # Average turnaround time
avg_ntr = sum_ntr / num  # Average normalized turnaround time

# Output Results
print("\nProcess Results:")
print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority':<10}{'Waiting Time':<15}{'Completion Time':<20}{'Turnaround Time':<20}{'Normalized TAT':<20}")
print("-" * 120)

for i in range(num):
    arrival, burst, priority = processes[i]  # Get process details
    print(f"{i+1:<10}{arrival:<15}{burst:<15}{priority:<10}{waiting_time[i]:<15}{completion_time[i]:<20}{turnaround_time[i]:<20}{normalized_tr[i]:<20.2f}")

# Output Averages
print("-" * 120)
print(f"{'Averages':<10}{'':<15}{'':<15}{'':<10}{avg_wt:<15.2f}{'':<20}{avg_tr:<20.2f}{avg_ntr:<20.2f}")
