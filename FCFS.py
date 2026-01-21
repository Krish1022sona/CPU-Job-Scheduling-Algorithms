'''
Sample Input:
['P1', 'P2', 'P3', 'P4'] 
[0, 2, 4, 5]
[7, 4, 1, 4]
'''


def minindex(l):
    mini = 0
    for i in range(len(l)):
        if (l[i] < l[mini]):
            i = mini

    return mini


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


print("GIVEN:")
print("PID  AT  BT")
for i in range(len(pid)):
    print(f"{pid[i]}   {at[i]}   {bt[i]}")

for i in range(len(pid)):
    for j in range(len(pid)-1):
        if at[j] > at[j+1]:
            at[j], at[j+1] = at[j+1], at[j]
            bt[j], bt[j+1] = bt[j+1], bt[j]
            pid[j], pid[j+1] = pid[j+1], pid[j]

currentTime = 0
for i in range(len(pid)):
    if at[i] <= currentTime:
        gt.append(pid[i])
        currentTime += bt[i]
        gt.append(str(currentTime))
        ct.append(currentTime)
        tat.append(ct[i] - at[i])
        wt.append(tat[i] - bt[i])
    else:
        gt.append(at[i])
        currentTime = at[i]
        gt.append(pid[i])
        currentTime += bt[i]
        gt.append(str(currentTime))
        ct.append(currentTime)
        tat.append(ct[i] - at[i])
        wt.append(tat[i] - bt[i])

# print(gt)
print("\nGantt Chart: ")
print('--'.join(gt))

print("\nCalculated Times: ")
print("PID  AT  BT  CT  TAT  WT")
for i in range(len(pid)):
    print(f"{pid[i]}   {at[i]}   {bt[i]}  {ct[i]}   {tat[i]}   {wt[i]}")

print("\nAverage WT: ", sum(wt)/len(wt))
print("Average TAT: ", sum(tat)/len(tat))
