from process import *


def find_highest_priority_job(process_list, current_time):
    idx = -1
    min_pr = float('inf')

    for i in range(len(process_list)):
        p = process_list[i]
        if p.at <= current_time and p.rt > 0:
            if p.pr < min_pr:
                min_pr = p.pr
                idx = i
            elif p.pr == min_pr and idx != -1:
                if p.id < process_list[idx].id:
                    idx = i
    return idx


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
    p.rt = bt
    process_list.append(p)

for i in range(n):
    for j in range(i, n-1):
        if process_list[j].at > process_list[j+1].at:
            process_list[j], process_list[j +
                                          1] = process_list[j+1], process_list[j]

current_time = 0
completed = 0
gantt = []

while completed != n:
    i = find_highest_priority_job(process_list, current_time)

    if i != -1:
        p = process_list[i]

        if not gantt or gantt[-1] != p.id:
            gantt.append(current_time)
            gantt.append(p.id)

        p.rt -= 1
        current_time += 1

        if p.rt == 0:
            completed += 1
            p.ct = current_time
            p.tat = p.ct - p.at
            p.wt = p.tat - p.bt
    else:
        if not gantt or gantt[-1] != "Idle":
            gantt.append(current_time)
            gantt.append("Idle")
        current_time += 1

gantt.append(current_time)

print("\nGantt Chart:")
print("-".join(map(str, gantt)))

print("\nCalculated Times:")
header = f"{'PID':<5} {'AT':<5} {'BT':<5} {
    'PR':<5} {'CT':<5} {'TAT':<5} {'WT':<5}"
print(header)
print("-" * len(header))
for p in process_list:
    print(f"{p.id:<5} {p.at:<5} {p.bt:<5} {
          p.pr:<5} {p.ct:<5} {p.tat:<5} {p.wt:<5}")

print_averages(process_list)
