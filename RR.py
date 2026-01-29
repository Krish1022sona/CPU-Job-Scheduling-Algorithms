from process import *

n = int(input("Enter The Number of Processes: "))
q = int(input("Enter Time Quantum: "))
print("Enter PID AT BT")
process_list = []

for i in range(n):
    input_l = input().split()
    pid = input_l[0]
    at = int(input_l[1])
    bt = int(input_l[2])

    p = Process(pid, at, bt)
    p.rt = p.bt
    process_list.append(p)

for i in range(n):
    for j in range(i, n - 1):
        if process_list[j].at == process_list[j + 1].at:
            if process_list[j].id > process_list[j + 1].id:
                process_list[j], process_list[j + 1] = process_list[j + 1], process_list[j]
        elif process_list[j].at > process_list[j + 1].at:
            process_list[j], process_list[j + 1] = process_list[j + 1], process_list[j]


current_time = 0
completed = 0
gantt = []
ready_queue = []
arrival_index = 0 # To track which processes have been added to the queue

if process_list[0].at > 0:
    gantt.append("0")
    gantt.append("Idle")
    current_time = process_list[0].at

while arrival_index < n and process_list[arrival_index].at <= current_time:
    ready_queue.append(process_list[arrival_index])
    arrival_index += 1

while completed < n:
    if not ready_queue:
        if arrival_index < n:
            gantt.append(str(current_time))
            gantt.append("Idle")
            current_time = process_list[arrival_index].at

            while arrival_index < n and process_list[arrival_index].at <= current_time:
                ready_queue.append(process_list[arrival_index])
                arrival_index += 1
        continue

    p = ready_queue.pop(0)

    if not gantt or gantt[-1] != str(current_time):
        gantt.append(str(current_time))
    gantt.append(p.id)

    exec_time = min(q, p.rt)

    p.rt -= exec_time
    current_time += exec_time

# put new process in ready que
    while arrival_index < n and process_list[arrival_index].at <= current_time:
        ready_queue.append(process_list[arrival_index])
        arrival_index += 1

    # put cur process in ready que (if not finished)
    if p.rt > 0:
        ready_queue.append(p)
    else:
        completed += 1
        p.ct = current_time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

gantt.append(str(current_time))

print("\nGantt Chart:")
print("-".join(gantt))

print("\nCalculated Times:")
print_process(process_list, 1)

print_averages(process_list)