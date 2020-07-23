import json

def parse_log(log_file):
    with open(log_file, 'r') as f:
        print(f.read())
        return True

if __name__ == "__main__":
    with open('input.json', 'r') as f:
        data = json.load(f)
    log_files = {}
    run_times = {}
    key1 = 'log_file'
    key2 = 'run_time'
    key3 = 'pass'
    for test_name in data:
        test_info = data[test_name]
        log_files[test_name] = test_info[key1]
        run_times[test_name] = test_info[key2]

    print(log_files)
    print(run_times)

    output = {}
    for test_name, log_file in log_files.items():
        log = {}
        log[key1] = log_file
        log[key2] = run_times[test_name]
        log[key3] = parse_log(log_file)
        output[test_name] = log

    with open('output.json.log', 'w') as f:
        json.dump(output, f, indent=4)
