def odd_number_and_mean_finder(l):
    #function that detects odd numbers in a given list input as well as returns mean
    odd_numbers = []
    counter = 0
    for x in l:
        counter += x
        mean  = counter/len(l)
        if (x % 2)!= 0:
            odd_numbers.append(x)
    print(odd_numbers)
    print(mean)

odd_number_and_mean_finder([1, 2, 3, 4, 5, 6, 7, 8, 9])