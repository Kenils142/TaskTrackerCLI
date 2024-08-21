# Task Tracker CLI
Project repos for [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

This is simple task tracker for CLI.

Task Tacker CLI, version 1.0.0

Note that in this CLI Application | is equal to OR.
so if you see --help | -h it means either you can use --help or -h.
Any of the two will work. 

Angle bracket (< >) are for you to understand that you need to provide some input there 
you dont have to write those brackets, they arent part of command.


To add task to tracker use command:
> task-cli.py --add | -a <"task-description">

To update task description of a task, use command:
> task-cli.py --update | -u <task-id> <"new-description">

To delete a task from the tracker, use command:
> task-cli.py --delete | -d <task-id>

To change status of a task, use command:
> task-cli.py --mark-as | -m <"incomplete" | "in-progress" | "done">

To view all the tasks in traker, use command:
> task-cli.py --list | -l

To view tasks based on their status, use command:
> task-cli.py --list | -l <"incomplete" | "in-progress" | "done">
