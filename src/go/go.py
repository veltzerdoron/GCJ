import argparse
import importlib
import traceback
import sys
import os

__version__ = "1.1"


def execute(command, phase):
    """ executes a command inside a phase """

    try:
        print(phase)
        input("EXECUTE : " + command)
        return os.system(command)
    except Exception as e:
        print("SOMETHING WENT WRONG IN " + phase + " : " + str(e))


def run_input(folder, problem, src, size, index, interact="N"):
    """
        run the problem solver on a given input size

    :param folder: path to src and data folder
    :param problem: the problem letter ('A'-'Z')
    :param src: file which implements the problem's solution algorithm
    :param size: LARGE or SMALL problem input data
    :param index: index of the problem
    :param interact: should we perform this in an interactive mode
    :return: boolean representing success for the algorithm
    """

    filename = folder + problem + "-" + size + "-" + index
    input_filename = filename + ".in"
    output_filename = filename + ".out"
    source_filename = folder + problem + ".py"

    input_name = "PROBLEM " + problem + "'s " + size.upper() + " INPUT"
    phase = "DOWNLOADING " + input_name + "'s OUTPUT"
    if interact.upper() != 'N':
        execute(command="codejam -d -p " + problem + " -t " + size + " | xargs -I % mv % " + input_filename,
                phase=phase)
    else:
        print("NOT " + phase + " (INTERACT OFF)")

    try:
        # open input and output files
        input_file = open(input_filename, 'r')
        output_file = open(output_filename, 'w')

    except Exception as e:
        print("SOMETHING WENT WRONG WHILE OPENING THE INPUT/OUTPUT FILES! " + str(e))
        return False

    try:
        # run the code
        print("RUNNING " + problem.upper() + " PY CODE ON " + input_name)
        p, m = src.rsplit('.', 1)
        src_module = __import__(p, globals=globals(), fromlist=m)
        importlib.reload(src_module)
        src_class = getattr(src_module, m)
        src_class.solve(input_file, output_file)

        # printout the resulting output
        with open(output_filename, 'r') as output_file:
            print(output_file.read())

    except Exception as e:
        print(traceback.format_exc())
        print("SOMETHING WENT WRONG WHILE RUNNING THE CODE! " + str(e))
        return False

    try:
        # close Input and output
        input_file.close()
        output_file.close()

    except Exception as e:
        print("SOMETHING WENT WRONG WHILE CLOSING THE FILES! " + str(e))
        return False

    phase = "UPLOADING " + input_name + "'s OUTPUT"
    if interact.upper() != 'N':
        return (execute(
            command="codejam -s -p " + problem + " -t " + size + " -o " + output_filename + " -f " + source_filename,
            phase=phase) == 0)
    else:
        print("NOT " + phase + " (INTERACT OFF)")
        return True


def run_example(folder, problem, src):
    """
        run the problem solver on the example files

    :param folder: folder for the contest's stage
    :param problem: letter representing the problem
    :param src: the source file
    """
    # open example output file
    example_filename = folder + problem + "-definition-0.example"
    example_name = "PROBLEM " + problem + "'s EXAMPLE"

    # run the code till the solver's output equals the example's output or an explicit command is given to ignore
    passed = False
    skip = False
    while not passed:
        answer = input("RUN " + example_name + "?(YES/No/Skip): ")
        if answer.upper() == "N":
            # try to submit anyway (without passing the comparison)
            passed = True
        elif answer.upper() == "S":
            # skip question to the next one
            passed = True
            skip = True
        else:
            # run the solver on the example input (no interaction so this always returns true)
            run_input(folder, problem, src, "definition", "0")

            # compare the output file to the example output
            output_filename = folder + problem + "-definition-0.out"
            if (execute("diff -b " + output_filename + " " + example_filename,
                        "COMPARING " + example_name) == 0):
                # if files are equal
                print("EXAMPLE MATCHES OUTPUT")
                passed = True
            else:
                print("EXAMPLE DOESN'T MATCH OUTPUT")

    return skip


def run_stage():
    """ runs the entire stage with repeats according to the passed arguments """

    parser = argparse.ArgumentParser(
        description="A script that's runs a single stage in the google code jam contest",
        epilog="")
    parser.add_argument("ID", help='Google''s URL parameter defining the stage')
    parser.add_argument("contest", help='Master folder for the stage (usually year)')
    parser.add_argument("stage", help='Name of the stage to be run')
    parser.add_argument("problems", type=list, default=[chr(ord('A') + i) for i in range(3)],
                        help="List of problems to be solved, defaults to ABC")
    parser.add_argument('-i', '--interact', choices=['Y', 'N', 'S'], default='Y',
                        help="fully interact ('Y') just submit ('S') or have no interaction ('N') with the site")
    parser.add_argument('-v', '--version', action='version', version='%(prog) {version}'.format(version='__version__'))

    args = parser.parse_args(args=sys.argv[1:])

    code = args.ID
    contest = args.contest
    stage = args.stage
    interact = args.interact
    problems = args.problems

    print("STARTING CONTEST WITH ARGUMENTS " + str(args))

    phase = "INITIALIZING STAGE " + stage.upper()
    if interact == "Y":
        # this must not fail
        if (execute(command="codejam -i -c " + code,
                    phase=phase) == 1):
            raise Exception("FAILED LOGGING IN (EXITING)")
    else:
        print("NOT " + phase + " (INTERACT OFF)")

    # Output and Input folders
    folder = "../../src/" + contest + "/" + stage + "/"

    # keep done problems for skip interaction
    problems_done = set()
    while problems_done != set(problems):  # compare using a set
        # loop on range problems
        for problem in problems:  # keep the problems ordered in a list
            while problem not in problems_done:
                # get the problem letter
                problem_name = "PROBLEM " + problem

                # build module path
                src = "src." + contest + "." + stage + "." + problem

                # special treatment for example stage
                input("PROCESS " + problem_name + "'s EXAMPLE (WRITE SOURCE CODE IN FILE - " + "..\\" +
                      contest + "\\" + stage + "\\" + problem + ".py" + ")")
                if run_example(folder, problem, src):
                    break

                # repeat for all sizes
                sizes = ["small", "large"]
                successes = set()
                while successes != sizes:
                    # if not all sizes work find a size that doesn't work
                    for size in sizes:
                        if size not in successes:
                            break

                    # ask whether to run the algorithm on the input
                    problem_input = problem_name + "'s " + size.upper() + " INPUT"
                    answer = input("PROCESS " + problem_input + " (YES/No/0-9/Skip): ")
                    if answer == 'N':
                        break
                    if answer == 'S':
                        successes.add(size)
                        continue
                    if answer.isdigit() and len(answer) == 1:
                        index = int(answer)
                    else:
                        index = '0'
                    if run_input(folder, problem, src, size, index, interact):
                        successes.add(size)

                if successes != sizes:
                    for size in sizes:
                        problem_input = problem_name + "'s " + size.upper() + " INPUT"
                        if size not in successes:
                            print("SKIPPED " + problem_input)
                        else:
                            print("SOLVED " + problem_input)
                else:
                    # report problem solution and add to done list
                    print("SOLVED " + problem_name)
                    problems_done.add(problem)

    input("FINISHED STAGE " + stage)
    sys.exit(0)


if __name__ == "__main__":
    run_stage()
