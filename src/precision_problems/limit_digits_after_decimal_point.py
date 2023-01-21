def limit_digits_after_decimal_point(arr):
    length = len(arr)
    neg_cnt = 0
    pos_cnt = 0
    zero_cnt = 0
    for i in arr:
        if i < 0:
            neg_cnt += 1
        elif i == 0:
            zero_cnt += 1
        else:
            pos_cnt += 1
    print("%.6f" % (pos_cnt / length))
    print("%.6f" % (neg_cnt / length))
    print("%.6f" % (zero_cnt / length))
