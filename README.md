# Operating System Resource Manager

A Python-based CPU scheduling simulator that demonstrates how an operating system manages processes using different scheduling algorithms.

This project implements:

- First Come First Serve (FCFS)
- Priority Scheduling
- Round Robin Scheduling
- Waiting Time calculation
- Turnaround Time calculation
- Average performance comparison
- Round Robin execution order tracking

## Project Overview

Operating systems use CPU scheduling algorithms to decide which process should run next.  
This project simulates that behavior using Python.

Each process contains:

- Process ID
- Arrival Time
- Burst Time
- Priority

The simulator calculates important performance metrics such as:

- Completion Time
- Turnaround Time
- Waiting Time
- Average Waiting Time
- Average Turnaround Time

## Technologies Used

- Python 3

No external libraries are required.

## Scheduling Algorithms

### 1. FCFS Scheduling

First Come First Serve executes processes in the order they arrive.

Example:

```text
P1 -> P2 -> P3