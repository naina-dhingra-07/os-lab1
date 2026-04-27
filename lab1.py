class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# INPUT
def take_input():
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        pid = f"P{i+1}"
        at = int(input(f"Enter Arrival Time for {pid}: "))
        bt = int(input(f"Enter Burst Time for {pid}: "))
        processes.append(Process(pid, at, bt))

    return processes


# DISPLAY
def display(processes):
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


# FCFS
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0

    gantt = []

    for p in processes:
        if time < p.at:
            time = p.at

        start = time
        time += p.bt

        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        gantt.append((p.pid, start, time))

    return gantt


# SJF (Non-preemptive)
def sjf(processes):
    processes_copy = processes[:]
    completed = []
    time = 0

    gantt = []

    while processes_copy:
        available = [p for p in processes_copy if p.at <= time]

        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda x: x.bt)
        processes_copy.remove(shortest)

        start = time
        time += shortest.bt

        shortest.ct = time
        shortest.tat = shortest.ct - shortest.at
        shortest.wt = shortest.tat - shortest.bt

        completed.append(shortest)
        gantt.append((shortest.pid, start, time))

    return completed, gantt


# AVERAGES
def averages(processes):
    avg_tat = sum(p.tat for p in processes) / len(processes)
    avg_wt = sum(p.wt for p in processes) / len(processes)
    return avg_tat, avg_wt


# GANTT CHART
def print_gantt(gantt):
    print("\nGantt Chart:")
    for p in gantt:
        print(f"| {p[0]} ", end="")
    print("|")

    print("0", end="")
    for p in gantt:
        print(f"\t{p[2]}", end="")
    print()


# MAIN
processes = take_input()

# FCFS
fcfs_list = [Process(p.pid, p.at, p.bt) for p in processes]
fcfs_gantt = fcfs(fcfs_list)

print("\n--- FCFS ---")
display(fcfs_list)
print_gantt(fcfs_gantt)

avg_tat, avg_wt = averages(fcfs_list)
print(f"Average TAT: {avg_tat}")
print(f"Average WT: {avg_wt}")


# SJF
sjf_list = [Process(p.pid, p.at, p.bt) for p in processes]
sjf_result, sjf_gantt = sjf(sjf_list)

print("\n--- SJF ---")
display(sjf_result)
print_gantt(sjf_gantt)

avg_tat, avg_wt = averages(sjf_result)
print(f"Average TAT: {avg_tat}")
print(f"Average WT: {avg_wt}")