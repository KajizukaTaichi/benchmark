import subprocess
import psutil
import time

def execute_command(command):
    start_time = time.time()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = time.time()
    return_code = process.returncode
    execution_time = end_time - start_time
    return stdout, stderr, return_code, execution_time

def get_memory_usage():
    return psutil.Process().memory_info().rss / 1024

def benchmark(name, command):

    # Execute the command
    stdout, stderr, return_code, execution_time = execute_command(command)

    # Get memory usage after command execution
    memory_usage = get_memory_usage()

    print(f"Benchmark of {name}")

    print("Return Code:", return_code)
    print("Execution Time:", execution_time, "seconds")
    print("Memory Usage:", memory_usage, "KB")

if __name__ == "__main__":
    benchmark("Stack", ["stack", "test.stk"])
    benchmark("Stack++", ["stackpp", "test.spp"])
