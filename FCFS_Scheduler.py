arrival_input=input("Enter Arrival Time (Seperated by spaces):") #input arrival time 
burst_input=input("Enter Burst Times (Seperated by spaces):") #input burst time

arrival_time=list(map(int,arrival_input.split())) #split arrival times in a list
burst_time=list(map(int,burst_input.split()))# split burst time in a list

processes=list(zip(arrival_time,burst_time)) #make a list of arrival,burst time in the format of [arrival,burst]
processes.sort(key=lambda x:x[0]) #make pairs of arrival and burst time using keys

num=len(arrival_time) #number of processes
completion_time=[0]*num #completion time list
current_time=0 #current time

for i in range(num):
    arrival,burst=processes[i]  #define arrival and burst time
    start_time=max(current_time,arrival) #starts the time with whichever is greater
    completion=start_time+burst #calculates completion time
    current_time=completion #increments the current time after each process
    completion_time[i]=completion #make a completion time array

waiting_time=[0]*num #waiting time list

for i in range (num):
    arrival,burst=processes[i] #define arrival and burst time
    comp=completion_time[i] #define completion time
    waiting=comp-arrival-burst #calculates waiting time
    waiting_time[i]=waiting #append/input waiting time in a list

turnaround_time = [0]*num #turnaround time list

for i in range (num):
    arrival,burst=processes[i] #define arrival and burst time
    wait=waiting_time[i] #define waiting time
    turnaround=wait+burst #calculates turnaround time
    turnaround_time[i]=turnaround #append/input turnaround time in a list

normalized_tr = [0]*num #normalized turnaround time

for i in range(num):
    arrival,burst=processes[i] #define arrival and burst time
    tr=turnaround_time[i] #define turnaround time
    ntr=(tr/burst) #calculates normalized turnaround time
    normalized_tr[i]=ntr #append/input normalized turnaround time in a list

for i in range (num):
    print("Arrival Time:",arrival_time[i], #prints Arrival Time
          " Burst Time:",burst_time[i], #prints Burst time
          " Waiting Time:",waiting_time[i], #prints Waiting Time
          " Completion Time:",completion_time[i], #prints Completion Time
          " Turnaround Time:",turnaround_time[i], #prints Turnaround Time
          " Normalized Turnaround Time:",normalized_tr[i]) #prints Normalized Turnaround Time
