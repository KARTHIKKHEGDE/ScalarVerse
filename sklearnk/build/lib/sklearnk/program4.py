def hill_climbing(func, start, step=0.01, max_iter=1000):
    x = start

    for _ in range(max_iter):
        f_x = func(x)
        f_right = func(x + step)
        f_left = func(x - step)

        if f_right > f_x and f_right >= f_left:
            x += step
        elif f_left > f_x:
            x -= step
        else:
            break

    return x, func(x)


if __name__ == '__main__':
    # ---- User input ----
    while True:
        try:
            func_str = input("\nEnter a function of x: ")
            func = lambda x: eval(func_str)
            func(0)   # test
            break
        except:
            print("Invalid function. Try again.")

    while True:
        try:
            start = float(input("\nEnter starting value: "))
            break
        except:
            print("Enter a valid number.")

    maxima, max_value = hill_climbing(func, start)

    print("The maxima is at x =", maxima)
    print("The maximum value obtained is", max_value)
