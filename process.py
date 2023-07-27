import json
import sys

def process_ipc_benchmarks(results1, results2):
    for r in results1:
        if r["Benchmark"] == "One way IPC microbenchmarks":
            ipc_benchmarks_1 = r["Results"]
    for r in results2:
        if r["Benchmark"] == "One way IPC microbenchmarks":
            ipc_benchmarks_2 = r["Results"]

    assert len(ipc_benchmarks_1) == len(ipc_benchmarks_2)

    print(f"|IPC Benchmark|Direction|IPC length|In same VSpace|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|")
    print(f"|-------------|---------|----------|--------------|-------------------|---------------------|-----------------|--------------------|------|")
    for i in range(len(ipc_benchmarks_1)):
        name1 = ipc_benchmarks_1[i]["Function"]
        direction1 = ipc_benchmarks_1[i]["Direction"]
        mean1 = ipc_benchmarks_1[i]["Mean"]
        stddev1 = round(ipc_benchmarks_1[i]["Stddev"], 2)
        in_same_vspace1 = ipc_benchmarks_1[i]["Same vspace?"]
        ipc_length1 = ipc_benchmarks_1[i]["IPC length"]

        name2 = ipc_benchmarks_2[i]["Function"]
        direction2 = ipc_benchmarks_2[i]["Direction"]
        mean2 = ipc_benchmarks_2[i]["Mean"]
        stddev2 = round(ipc_benchmarks_2[i]["Stddev"], 2)
        in_same_vspace2 = ipc_benchmarks_2[i]["Same vspace?"]
        ipc_length2 = ipc_benchmarks_2[i]["IPC length"]

        assert name1 == name2
        assert direction1 == direction2
        assert in_same_vspace1 == in_same_vspace1
        assert ipc_length1 == ipc_length2

        # Now we want to print the difference comparing all the results of the
        # second file to the first.
        mean_diff = mean1 - mean2
        mean_perc_diff = (1 - mean1 / mean2) * 100
        print(f"|{name1}|{direction1}|{ipc_length1}|{in_same_vspace1}|{mean1}|{stddev1}|{mean2}|{stddev2}|{round(mean_perc_diff, 2)}%|")
        # print(f"IPC function: {name1}, direction: {direction1}")
        # print(f"Mean: {mean1} -> {mean2}: {round(mean_perc_diff, 2)}%")
        # print(f"Standard deviation 1: {round(stddev1, 1)}, standard deviation 2: {round(stddev2, 1)}")

    print("\n")


def process_regular(results1, results2, benchmark):
    for r in results1:
        if r["Benchmark"] == benchmark:
            ipc_benchmarks_1 = r["Results"]
    for r in results2:
        if r["Benchmark"] == benchmark:
            ipc_benchmarks_2 = r["Results"]

    assert ipc_benchmarks_1 is not None
    assert ipc_benchmarks_2 is not None
    assert len(ipc_benchmarks_1) == len(ipc_benchmarks_2)

    print(f"|Benchmark|Priority|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|")
    print(f"|---------|--------|-------------------|---------------------|------------------|--------------------|------|")

    for i in range(len(ipc_benchmarks_1)):
        prio = ipc_benchmarks_1[i]["Prio"]
        stddev1 = round(ipc_benchmarks_1[i]["Stddev"], 2)
        stddev2 = round(ipc_benchmarks_2[i]["Stddev"], 2)
        mean1 = ipc_benchmarks_1[i]["Mean"]
        mean2 = ipc_benchmarks_2[i]["Mean"]
        mean_diff = mean1 - mean2
        mean_perc_diff = (1 - mean1 / mean2) * 100
        print(f"|{benchmark}|{prio}|{mean1}|{stddev1}|{mean2}|{stddev2}|{round(mean_perc_diff, 2)}%|")

    print("\n")


def print_benchmark_names(results):
    for r in results:
        print(r["Benchmark"])


def process(results1_file, results2_file):
    with open(results1_file, "r") as f:
        results1 = json.loads(f.read())
    with open(results2_file, "r") as f:
        results2 = json.loads(f.read())

    process_ipc_benchmarks(results1, results2)
    process_regular(results1, results2, "Signal to thread of higher prio")
    process_regular(results1, results2, "Signal to process of higher prio")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 process.py [RESULTS 1] [RESULTS 2]")
        exit(1)

    process(sys.argv[1], sys.argv[2])
