from process import *


# to print with priority
def print_priority_table(process_list):
    print("\nCalculated Times:")
    header = f"{'PID':<5} {'AT':<5} {'BT':<5} {'PR':<5} {'CT':<5} {'TAT':<5} {'WT':<5}"
    print(header)
    print("-" * len(header))

    for p in process_list:
        print(f"{p.id:<5} {p.at:<5} {p.bt:<5} {p.pr:<5} {p.ct:<5} {p.tat:<5} {p.wt:<5}")



n = int(input("Enter The Number of Processes: "))
print("Enter PID AT BT PR")
process_list = []

for i in range(n):
    input_l = input().split()
    pid = input_l[0]
    at = int(input_l[1])
    bt = int(input_l[2])
    pr = int(input_l[3])

    p = Process(pid, at, bt)
    p.pr = pr
    process_list.append(p)

for i in range(n):
    for j in range(i, n - 1):
        if process_list[j].at > process_list[j + 1].at:
            process_list[j], process_list[j + 1] = process_list[j + 1], process_list[j]


current_time = 0
completed = 0
gantt = []
is_completed = [False] * n

if process_list[0].at > 0:
    gantt.append("0")
    gantt.append("Idle")
    current_time = process_list[0].at

while completed < n:
    ready_queue = []
    for i in range(n):
        if process_list[i].at <= current_time and not is_completed[i]:
            ready_queue.append((i, process_list[i]))

    if not ready_queue:
        next_arrival = float('inf')
        for p in process_list:
            if p.at > current_time:
                next_arrival = min(next_arrival, p.at)

        gantt.append(str(current_time))
        gantt.append("Idle")
        current_time = next_arrival
        continue


    idx, p = min(ready_queue, key=lambda x: x[1].pr)

    if not gantt or gantt[-1] != str(current_time):
        gantt.append(str(current_time))
    gantt.append(p.id)

    current_time += p.bt

    is_completed[idx] = True
    completed += 1

    p.ct = current_time
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt

gantt.append(str(current_time))


print("\nGantt Chart:")
print("-".join(gantt))

print_priority_table(process_list)

print_averages(process_list)