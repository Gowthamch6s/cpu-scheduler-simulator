processes = [
    {"pid": "P1", "arrival_time": 0, "burst_time": 5, "priority": 2},
    {"pid": "P2", "arrival_time": 1, "burst_time": 3, "priority": 1},
    {"pid": "P3", "arrival_time": 2, "burst_time": 8, "priority": 3},
]


def fcfs_scheduling(processes):
    processes = sorted(processes, key=lambda x: x["arrival_time"])

    current_time = 0
    schedule = []

    for process in processes:
        start_time = max(current_time, process["arrival_time"])
        completion_time = start_time + process["burst_time"]

        turnaround_time = completion_time - process["arrival_time"]
        waiting_time = turnaround_time - process["burst_time"]

        schedule.append({
            "pid": process["pid"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "completion_time": completion_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time
        })

        current_time = completion_time

    return schedule


def priority_scheduling(processes):
    processes = sorted(processes, key=lambda x: x["arrival_time"])

    current_time = 0
    completed = []
    schedule = []

    while len(completed) < len(processes):
        available_processes = []

        for process in processes:
            if process["arrival_time"] <= current_time and process not in completed:
                available_processes.append(process)

        if len(available_processes) == 0:
            current_time += 1
            continue

        selected_process = min(available_processes, key=lambda x: x["priority"])

        start_time = current_time
        completion_time = start_time + selected_process["burst_time"]

        turnaround_time = completion_time - selected_process["arrival_time"]
        waiting_time = turnaround_time - selected_process["burst_time"]

        schedule.append({
            "pid": selected_process["pid"],
            "arrival_time": selected_process["arrival_time"],
            "burst_time": selected_process["burst_time"],
            "priority": selected_process["priority"],
            "completion_time": completion_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time
        })

        current_time = completion_time
        completed.append(selected_process)

    return schedule


def round_robin_scheduling(processes, time_quantum):
    queue = []
    schedule = []
    current_time = 0

    remaining_time = {}
    completion_time = {}

    processes = sorted(processes, key=lambda x: x["arrival_time"])

    for process in processes:
        remaining_time[process["pid"]] = process["burst_time"]

    queue.append(processes[0])

    visited = set()
    visited.add(processes[0]["pid"])

    while queue:
        current_process = queue.pop(0)
        pid = current_process["pid"]

        start_time = current_time

        if remaining_time[pid] > time_quantum:
            current_time += time_quantum
            remaining_time[pid] -= time_quantum
        else:
            current_time += remaining_time[pid]
            remaining_time[pid] = 0
            completion_time[pid] = current_time

        end_time = current_time

        schedule.append({
            "pid": pid,
            "start_time": start_time,
            "end_time": end_time
        })

        for process in processes:
            if process["arrival_time"] <= current_time and process["pid"] not in visited:
                queue.append(process)
                visited.add(process["pid"])

        if remaining_time[pid] > 0:
            queue.append(current_process)

    final_result = []

    for process in processes:
        pid = process["pid"]
        turnaround_time = completion_time[pid] - process["arrival_time"]
        waiting_time = turnaround_time - process["burst_time"]

        final_result.append({
            "pid": pid,
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "completion_time": completion_time[pid],
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time
        })

    return schedule, final_result


def print_results(title, results):
    print(f"\n{title}")
    print("-" * 75)
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    print("-" * 75)

    total_waiting_time = 0
    total_turnaround_time = 0

    for item in results:
        print(
            f"{item['pid']}\t"
            f"{item['arrival_time']}\t"
            f"{item['burst_time']}\t"
            f"{item['completion_time']}\t\t"
            f"{item['turnaround_time']}\t\t"
            f"{item['waiting_time']}"
        )

        total_waiting_time += item["waiting_time"]
        total_turnaround_time += item["turnaround_time"]

    average_waiting_time = total_waiting_time / len(results)
    average_turnaround_time = total_turnaround_time / len(results)

    print("-" * 75)
    print("Average Waiting Time:", round(average_waiting_time, 2))
    print("Average Turnaround Time:", round(average_turnaround_time, 2))


def print_execution_order(schedule):
    print("\nExecution Order")
    print("-" * 35)

    for item in schedule:
        print(f"{item['pid']} runs from {item['start_time']} to {item['end_time']}")


print("Processes:")
for process in processes:
    print(process)

fcfs_result = fcfs_scheduling(processes)
print_results("FCFS Scheduling Results", fcfs_result)

priority_result = priority_scheduling(processes)
print_results("Priority Scheduling Results", priority_result)

print("\nRound Robin Scheduling")
time_quantum = 2

rr_schedule, rr_result = round_robin_scheduling(processes, time_quantum)

print_execution_order(rr_schedule)
print_results("Round Robin Final Results", rr_result)