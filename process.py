class Process():
    def __init__(self, id, at, bt):
        self.at = at
        self.bt = bt
        self.id = id
        self.ct = None
        self.tat = None
        self.wt = None

def print_process(processes, mode = 0):
    print(f"{'PID':<5} {'AT':<5} {'BT':<5}", end="")
    if mode == 1:
        print(f" {'CT':<5} {'TAT':<5} {'WT':<5}", end="")
    print()

    print("-" * (35 if mode == 1 else 15))

    for p in processes:
        print(f"{p.id:<5} {p.at:<5} {p.bt:<5}", end="")
        if mode == 1:
            ct = p.ct if p.ct is not None else "-"
            tat = p.tat if p.tat is not None else "-"
            wt = p.wt if p.wt is not None else "-"
            print(f" {ct:<5} {tat:<5} {wt:<5}", end="")
        print()


def print_averages(process_list):
    n = len(process_list)
    total_wt = sum(p.wt for p in process_list)
    total_tat = sum(p.tat for p in process_list)

    print(f"\nAvg WT = {total_wt / n:.2f}, Avg TAT = {total_tat / n:.2f}")