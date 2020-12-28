#!/usr/bin/env python

import sys

from resolver import *


def read_in():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())
    return lines
    

def resolve_machines_jobs(data):
    number_machines = None
    number_jobs = None

    for ind in data:
        if ind != ' ' and number_jobs is None:
            number_jobs = ind
        elif ind != ' ' and number_jobs is not None:
            number_machines = ind

    return int(number_jobs), int(number_machines)


def resolve_cost_max_time_machine(data, number_machines):
    cost_machine = list()
    max_time_machine = list()

    for i in range(number_machines):
        cost_and_max_time_per_machine = data[i].split(' ')
        cost_machine.append(int(cost_and_max_time_per_machine[0]))
        max_time_machine.append(int(cost_and_max_time_per_machine[1]))
    return cost_machine, max_time_machine


def resolve_jobs_machine(data):
    mj = dict()
    ind_to_use = 0
    count = 0
    for i in range(len(data)):
        if i == ind_to_use:
            count += 1
            mj[count] = list()
            ind_to_use = ind_to_use + int(data[i]) + 1
        else:
            mj[count].append(int(data[i]))
    return mj


def resolve_input(data):
    number_jobs, number_machines = resolve_machines_jobs(data[0])
    time_job = list()
    cost_machine, max_time_machine = resolve_cost_max_time_machine(data[number_jobs+1:], number_machines)

    for i in range(number_jobs):
        time_job.append(data[i+1])

    jobs_per_machines = resolve_jobs_machine(data[1+number_jobs+number_machines:])
    return {
        'n_machines': number_machines,
        'n_jobs': number_jobs,
        't_job': time_job,
        'c_machine': cost_machine,
        'm_t_machine': max_time_machine,
        'j_m': jobs_per_machines
    }


def main():
    lines = read_in()
    data_inputed = resolve_input(lines)
    resolve(
        data_inputed['n_machines'],
        data_inputed['n_jobs'],
        data_inputed['t_job'], 
        data_inputed['c_machine'], 
        data_inputed['m_t_machine'],
        data_inputed['j_m'])


if __name__ == "__main__":
    main()
