def  job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x[2], reverse=True) 
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * (max_deadline + 1)
    total_profit = 0

    for  job in jobs:
        job_id, deadline, profit = job
        for j in range(min(deadline, max_deadline), 0, -1):
            if schedule[j] == -1:
                schedule[j] = job_id
                total_profit += profit
                break
    scheduled_jobs = [job for job in schedule if job != -1]
    print("Optimal Job Sequence:", scheduled_jobs)
    print("Maximum Profit:", total_profit)

n = int(input("Enter number of jobs: "))
jobs = []  
print("Enter job details in format: JobID Deadline Profit")
for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append((job_id, int(deadline), int(profit)))
job_scheduling(jobs, n)

'''
 Job Scheduling – Theory
🎯 Goal:
Schedule jobs in such a way that:

Each job takes 1 unit of time

No two jobs overlap

Each job has:

A deadline (by when it must be done)

A profit (earned if job is completed before the deadline)

🟢 Objective: Maximize total profit by selecting and scheduling the most profitable jobs before their deadlines.
An array of n jobs. Each job has:

An id (Job identifier)

A deadline (latest time slot by which it must be completed)

A profit (earned if job is done within deadline)

Step-by-step:
Sort all jobs in decreasing order of profit.

Find the maximum deadline to determine how many time slots are needed.

Create a slot array of size equal to max deadline, initialized as empty.

Iterate through sorted jobs and for each job:

Try to place it in the latest available time slot before its deadline.

If a slot is free, schedule the job there.

Collect and return scheduled jobs and total profit.
Time Complexity:

Sorting jobs: O(n log n)

Scheduling: O(n × d) where d = max deadline

Space Complexity:

O(d) for slot array
'''