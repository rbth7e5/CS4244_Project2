import sys
from pgmpy.readwrite import UAIReader


def read_evid(f_name):
    evidence_file = open(f_name, "r")
    evid = evidence_file.readline().strip().split(" ")
    evid_dict = {}
    for i in range(int(evid[0])):
        evid_dict["var_" + evid[i * 2 + 1]] = evid[i * 2 + 2]
    return evid_dict


def main():
    args = sys.argv[1:]
    model_file = args[0]
    evidence = read_evid(args[1])
    model = UAIReader(model_file)
    print(model.get_domain())
    print(model.get_tables())
    print(evidence)


if __name__ == '__main__':
    main()