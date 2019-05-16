import re
import sys

from sre_constants import error


def validate_params(params):
    if len(params) < 3:
        print('ERROR! You should enter at least 2 arguments')
        return False, False
    elif len(params) > 4:
        print('ERROR! You should enter maximum 4 arguments')
        return False, False
    elif len(params) == 4:
        if not params[1] == '-v':
            print('ERROR! Unrecognized option: {}'.format(params[1]))
            return False, False
        return True, True
    return True, False


def main():
    params = sys.argv

    is_valid, exclude = validate_params(params)

    if not is_valid:
        return

    file_path = params[-1]
    search_text = params[-2].strip('"')

    try:
        compiled_text = re.compile(search_text)
        with open(file_path, 'r') as file:
            for line in file:
                found_text = compiled_text.search(line)

                if exclude and not found_text:
                    print(line.rstrip())
                elif not exclude and found_text:
                    print(line.rstrip())
    except error:
        print('ERROR! Wrong regular expression')
    except FileNotFoundError:
        print('ERROR! No such file or directory: {}'.format(file_path))


if __name__ == '__main__':
    main()
