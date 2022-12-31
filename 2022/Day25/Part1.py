with open("input.txt") as f:
    numbers = [line.strip() for line in f.read().split('\n')]


def convert_to_decimal(snafu: str) -> int:
    decimal = 0
    for i, c in enumerate(list(snafu[::-1])):
        match c:
            case '=' if i == 0: decimal += -2
            case '-' if i == 0: decimal += -1
            case '1' if i == 0: decimal += 1
            case '2' if i == 0: decimal += 2
            case '=' if i > 0: decimal += -2 * (5**i)
            case '-' if i > 0: decimal += -1 * (5**i)
            case '1' if i > 0: decimal += 5**i
            case '2' if i > 0: decimal += 2 * (5**i)
    return decimal


def convert_to_snafu(number: int) -> str:
    snafu_decimal = []
    snafu = []

    while number > 4:
        new_number = int(number / 5)
        snafu_decimal.append(number - new_number * 5)
        number = new_number
    snafu_decimal.append(number)

    for i, n in enumerate(snafu_decimal):
        match n:
            case 0:
                snafu.append('0')
            case 1:
                snafu.append('1')
            case 2:
                snafu.append('2')
            case 3:
                snafu.append('=')
                if len(snafu_decimal) - 1 == i:
                    snafu.append('1')
                else:
                    snafu_decimal[i + 1] += 1
            case 4:
                snafu.append('-')
                if len(snafu_decimal) - 1 == i:
                    snafu.append('1')
                else:
                    snafu_decimal[i + 1] += 1
            case 5:
                snafu.append('0')
                if len(snafu_decimal) - 1 == i:
                    snafu.append('1')
                else:
                    snafu_decimal[i + 1] += 1

    return ''.join(snafu)[::-1]


answer = 0
for n in numbers:
    answer += convert_to_decimal(n)

print(convert_to_snafu(answer))

