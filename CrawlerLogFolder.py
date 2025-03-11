def minOperations(logs):
    def process_logs(logs, depth, index):
        if index == len(logs):
            return depth
        operation = logs[index]
        if operation == "../":
            new_depth = max(0, depth - 1)
        elif operation == "./":
            new_depth = depth
        else:
            new_depth = depth + 1
        return process_logs(logs, new_depth, index + 1)

    return process_logs(logs, 0, 0)

logs = ["d1/","d2/","../","d21/","./"]
print(minOperations(logs))

logs = ["d1/","d2/","./","d3/","../","d31/"]
print(minOperations(logs))

logs = ["d1/","../","../","../"]
print(minOperations(logs))
