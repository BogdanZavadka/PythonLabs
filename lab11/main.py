import re
from zipfile import ZipFile


def main():
    with ZipFile("log.zip") as zip_file:
        zip_file.extractall()
    log_file = open('log.txt', 'r')
    logs_list = log_file.read().split("\n")
    regex = re.compile(
        ".*\\[\\d{2}/\\w{3}/\\d{4}:((02:((19:[3-5]\\d)|"
        "([2-5]\\d:[0-5]\\d)))|(0[3-9]:[0-5]\\d:[0-5]\\d)|"
        "(10:[0-5]\\d:[0-5]\\d)|(11:0\\d:[0-2]\\d)).*\"GET.*\" [2-3]\\d{2}.*"
    )
    found_matches = 0
    for i in range(len(logs_list)):
        match = re.match(regex, logs_list[i])
        if match:
            print(match.group())
            found_matches += 1
    print("Matches found: ", found_matches)


if __name__ == '__main__':
    main()
