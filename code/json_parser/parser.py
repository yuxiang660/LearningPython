import json
import os


if __name__ == "__main__":
    CASE_LIST_KEY = "case_list"
    ENV_KEY = "env"
    ENV_PATH_KEY = "path"
    ENV_CUSTOM_KEY = "custom"
    TEST_ROOT_KEY = "test_root"
    TEST_RESULT_ROOT_KEY = "test_result_root"
    LOG_FILE_KEY = "log_file"

    with open("config.json", 'r') as f:
        data = json.load(f)

    case_list = data[CASE_LIST_KEY]
    env_path = data[ENV_KEY][ENV_PATH_KEY]
    env_custom = data[ENV_KEY][ENV_CUSTOM_KEY]
    test_root = data[TEST_ROOT_KEY]
    test_result_root = data[TEST_RESULT_ROOT_KEY]
    log_file = data[LOG_FILE_KEY]

    print(case_list)
    print(env_path)
    print(env_custom)
    print(test_root)
    print(test_result_root)
    print(log_file)

    print(json.dumps(data, indent=4))
