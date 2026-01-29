from process import *


def find_shortest_job(process_list, current_time):
    idx = -1
    min_rt = float('inf')

    for i in range(len(process_list)):
        p = process_list[i]
        if p.at <= current_time and p.rt > 0:
            if p.rt < min_rt:
                min_rt = p.rt
                idx = i
            elif p.rt == min_rt:
                if p.at < process_list[idx].at:
                    idx = i

    return idx



n = int(input("Enter The Number of Processes: "))
print("Enter PID AT BT")
process_list = []

for i in range(n):
    input_l = input().split()
    pid = input_l[0]
    at = int(input_l[1])
    bt = int(input_l[2])
    p = Process(pid, at, bt)
    p.rt = bt
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

if process_list[0].at > 0:
    gantt.append("Idle")
    current_time = process_list[0].at

while completed != n:
    i = find_shortest_job(process_list, current_time)

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
        gantt.append(current_time)
        gantt.append("Idle")
        current_time += 1

gantt.append(current_time)


print("\nGantt Chart:")
print("-".join(map(str, gantt)))

print("\nCalculated Times:")
print_process(process_list, 1)

print_averages(process_list)