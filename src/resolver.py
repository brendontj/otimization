from pulp import *


def define_variables(number_machines, number_jobs, max_time):
    var_dictionary = dict()

    for i in range(1, number_machines+1):
        for j in range(1, number_jobs+1):
            var_dictionary["m"+str(i)+"j"+str(j)] = max_time[i-1]
    return var_dictionary


def resolve(number_machines, number_jobs, time_job, cost_machine, max_time_machine, jobs_per_machines):
    variables_limits = define_variables(number_machines, number_jobs, max_time_machine)
    variables_list = list()

    for k, v in variables_limits.items():
        variables_list.append(LpVariable(k, 0, v))

    problem = LpProblem("NoName", LpMinimize)
    acc = None
    count = 0
    for i in range(len(variables_list)):
        if i != 0 and i % number_jobs == 0:
            problem += acc <= max_time_machine[count]
            count += 1
            acc = None
        acc += variables_list[i]

    if len(max_time_machine) > count:
        problem += acc <= max_time_machine[count]

    el_list = []
    count = 0
    for i in range(len(variables_list)):
        if i != 0 and i % number_jobs == 0:
            count += 1
        el_list.append((variables_list[i], cost_machine[count]))

    problem += LpAffineExpression(el_list)

    for i in range(number_jobs):
        machine_index = 0
        el_list = []
        for j in range(0+i, len(variables_list), number_jobs):
            if (i+1) in jobs_per_machines[machine_index+1]:
                el_list.append((variables_list[j], 1))
            else:
                el_list.append((variables_list[j], 0))
            machine_index += 1

        problem += LpAffineExpression(el_list) == int(time_job[i])

    status = problem.solve(PULP_CBC_CMD(msg=False))

    if status:
        v = problem.variables()
        for i in range(len(v)):
            print(v[i].varValue, end=" ")
            if (i+1) % number_jobs == 0:
                print()
        print(value(problem.objective))
