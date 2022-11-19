import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except KeyError:
        print('Conversion failed')
        x = -1
    except TypeError:
        print('Conversion failed')
        x = -1
    return x


# result = convert(("one two three seven").split())
# print(result)  # 1237
# result = convert(("around one two three seven").split())
# print(result)  # 1237
# result = convert(("655").split())
# print(result)  # 1237


# =======================================================================

# def convert(s):
#     x = -1
#     try:
#         number = ''
#         for token in s:
#             number += DIGIT_MAP[token]
#         x = int(number)
#     except (KeyError, TypeError) :
#         print('Conversion failed')
#     return x
#
#
# result = convert(("one two three seven 677").split())
# print(result)  # 1237

# =======================================================================
import sys
def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f'Conversion error: {e!r}', file=sys.stderr)
    return -1

result = convert(("one two three seven 677").split())
print(result)  # 1237





