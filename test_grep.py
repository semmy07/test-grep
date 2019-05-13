import re
import sys


if __name__ == '__main__':
    params = sys.argv

    file_path = params[-1]
    search_text = params[-2].strip('"')
    exclude = '-v' in params

    try:
        with open(file_path) as file:
            for line in file.readlines():
                found_text = re.search(search_text, line)

                if exclude and not found_text:
                    print(line.rstrip())
                elif not exclude and found_text:
                    print(line.rstrip())
    except Exception as e:
        print('There was an exception!\n{}'.format(e))
