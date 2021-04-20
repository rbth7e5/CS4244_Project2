import sys
from pgmpy.readwrite import UAIReader
import cnfgen
import math

F = cnfgen.CNF()
params_to_weights = dict()


def read_evid(f_name):
    evidence_file = open(f_name, "r")
    evid = evidence_file.readline().strip().split(" ")
    evid_dict = {}
    for i in range(int(evid[0])):
        evid_dict["var_" + evid[i * 2 + 1]] = evid[i * 2 + 2]
    return evid_dict


def generate_binary_array(num):
    if num == 0:
        return []

    def binary_add(binary_arr):
        copy_list = binary_arr.copy()
        start = len(copy_list) - 1
        while copy_list[start]:
            copy_list[start] = False
            start = start - 1
        copy_list[start] = True
        return copy_list
    init = [False for _ in range(num)]
    result = [init]
    for i in range(int(math.pow(2, num) - 1)):
        init = binary_add(init)
        result.append(init)
    return result


def table_to_cnf(table):
    ind_format = "i{var_name}"
    param_format = "q{param_name}"
    num_variables = len(table[0])
    variables = table[0]
    weights = table[1]
    if num_variables == 1:
        var = variables[0]
        ind_name = ind_format.format(var_name=var)
        param_name = param_format.format(param_name=var)
        F.add_clause([(False, ind_name), (True, param_name)])
        F.add_clause([(True, ind_name), (False, param_name)])
        params_to_weights[param_name] = weights[1]
    else:
        binary_array = generate_binary_array(num_variables - 1)
        last_var = variables[-1]
        last_ind_name = ind_format.format(var_name=last_var)
        for i, arr in enumerate(binary_array):
            param_name = param_format.format(param_name="".join(["True" if val else "False" for val in arr]) + "".join(variables))
            indicators_arr = [(not val, ind_format.format(var_name=variables[i])) for i, val in enumerate(arr)]
            F.add_clause(indicators_arr + [(False, last_ind_name)] + [(True, param_name)])
            F.add_clause(indicators_arr + [(True, last_ind_name)] + [(False, param_name)])
            params_to_weights[param_name] = weights[i*2+1]


def main():
    args = sys.argv[1:]
    model_file = args[0]
    evidence = read_evid(args[1])
    model = UAIReader(model_file)
    tables = model.get_tables()
    for table in tables:
        table_to_cnf(table)


if __name__ == '__main__':
    main()
