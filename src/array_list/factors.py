def factors(chosen, current_num=None, numbers=None):
    if chosen == 0:
        return []
    if chosen < 0:
        chosen = abs(chosen)
    if numbers is None:
        numbers = [1]
        current_num = 2
    if current_num == chosen:
        numbers.append(current_num)
        return numbers
    else:
        if chosen % current_num == 0:
            numbers.append(current_num)
        current_num += 1
        return factors(chosen, current_num, numbers)


if __name__ == '__main__':
    print(factors(-12))