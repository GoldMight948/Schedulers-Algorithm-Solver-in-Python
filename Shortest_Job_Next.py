arrival_input=input("Enter Arrival Time (Seperate by Spaces):")
burst_input=input("Enter Burst Time (Seperate by Spaces):")

arrival_time=list(map(int,arrival_input.split()))
burst_time=list(map(int,burst_input.split()))

processes=sorted(zip(arrival_time,burst_time))#,key=lambda x:x[0])
print(processes)

num=len(processes)
completion_time=[0]*num
waiting_time=[0]*num
turnaround_time=[0]*num
normalized_tr=[0]*num
current_time=0

#Completion,Waiting,Turnaround,Normalized for 1st Process
arrival,burst=processes[0]
if current_time < arrival:
    current_time=arrival
completion=0
completion=current_time+burst
completion_time[0]=completion

#Waiting
waiting=completion-arrival-burst
waiting_time[0]=waiting

#Turnaround
turnaround=waiting+burst
turnaround_time[0]=turnaround

#Normalized Turnaround
ntr=turnaround/burst
normalized_tr[0]=ntr

processes.pop(0)

processes=sorted(processes,key=lambda x:x[1])
num=len(processes)

completion=0
waiting=0
turnaround=0
ntr=0
current_time=completion_time[0]

for i in range(num):
    arrival,burst=processes[i]
    completion=current_time+burst
    current_time=completion
    completion_time[i+1]=completion

for i in range(num):
    arrival,burst=processes[i]
    waiting=completion_time[i+1]-arrival-burst
    waiting_time[i+1]=waiting

for i in range(num):
    arrival,burst=processes[i]
    turnaround=waiting_time[i+1]+burst
    turnaround_time[i+1]=turnaround

for i in range(num):
    arrival,burst=processes[i]
    ntr=turnaround_time[i+1]/burst
    normalized_tr[i+1]=ntr

sum_wt=sum(waiting_time)
sum_tr=sum(turnaround_time)
sum_ntr=sum(normalized_tr)
print(sum_wt," ",sum_tr," ",sum_ntr," ")
num=num+1
avg_wt=(sum_wt/num)
avg_tr=(sum_tr/num)
avg_ntr=(sum_ntr/num)
print(avg_wt)

# Print the header
print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Waiting Time':<15}{'Completion Time':<20}{'Turnaround Time':<20}{'Normalized TAT':<20}")
print("-" * 115)

# Print the details for each process
for i in range(num):
    print(f"{i+1:<10}{arrival_time[i]:<15}{burst_time[i]:<15}{waiting_time[i]:<15}{completion_time[i]:<20}{turnaround_time[i]:<20}{normalized_tr[i]:<20.2f}")

# Print the averages
print("-" * 115)
print(f"{'Averages':<10}{'':<15}{'':<15}{avg_wt:<15.2f}{'':<20}{avg_tr:<20.2f}{avg_ntr:<20.2f}")