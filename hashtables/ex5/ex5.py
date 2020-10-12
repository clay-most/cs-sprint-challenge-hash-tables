# Your code here
directory = {}


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []

    for file in files:
        # targeting the last portion of the file path after the final "/"
        file_name = file.split("/")[-1]
        if file_name not in directory:
            directory[file_name] = [file, ]
        else:
            directory[file_name].append(file)
    for query in queries:
        if query in directory:
            for each in directory[query]:
                result.append(each)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
