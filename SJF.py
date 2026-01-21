def find_shortest_job(currentTime, at, bt, v):
    job = -1
    for i in range(len(at)):
        if at[i] <= currentTime and v[i] == 0:
            if job == -1:
                job = i
            elif bt[job] > bt[i]:
                job = i
    return job


print("Enter the PID: ")
pid = eval(input())
print("Enter the AT wrt to PID: ")
at = eval(input())
print("Enter the BT wrt to PID: ")
bt = eval(input())

ct = list()
tat = list()
wt = list()
gt = ['0']

v = [0 for x in range(len(pid))]


print("GIVEN:")
print("PID  AT  BT")
for i in range(len(pid)):
    print(f"{pid[i]}   {at[i]}   {bt[i]}")


# sort for at
for i in range(len(pid)):
    for j in range(len(pid)-1):
        if at[j] > at[j+1]:
            at[j], at[j+1] = at[j+1], at[j]
            bt[j], bt[j+1] = bt[j+1], bt[j]
            pid[j], pid[j+1] = pid[j+1], pid[j]

currentTime = 0
for x in range(len(pid)):
    i = find_shortest_job(currentTime, at, bt, v)
    v[i] = 1
    print(i)
    if at[i] <= currentTime:
        gt.append(pid[i])
        currentTime += bt[i]
        gt.append(str(currentTime))
        ct.append(currentTime)
        tat.append(ct[x] - at[x])
        wt.append(tat[x] - bt[x])
    else:
        gt.append(at[i])
        currentTime = at[i]
        gt.append(pid[i])
        currentTime += bt[i]
        gt.append(str(currentTime))
        ct.append(currentTime)
        tat.append(ct[x] - at[x])
        wt.append(tat[x] - bt[x])

# print(gt)
print("\nGantt Chart: ")
print('--'.join(gt))

print("\nCalculated Times: ")
print("PID  AT  BT  CT  TAT  WT")
for i in range(len(pid)):
    print(f"{pid[i]}   {at[i]}   {bt[i]}  {ct[i]}   {tat[i]}   {wt[i]}")

print("\nAverage WT: ", sum(wt)/len(wt))
print("Average TAT: ", sum(tat)/len(tat))
