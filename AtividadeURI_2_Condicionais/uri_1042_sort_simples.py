def main():
    num_1, num_2, num_3 = map(int, input().split())

    if num_1 < num_2 < num_3:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'\
            .format(num_1,num_2,num_3,num_1,num_2,num_3))
    elif num_1 < num_3 < num_2:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'\
            .format(num_1,num_3,num_2,num_1,num_2,num_3))
    elif num_2 < num_1 < num_3:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'\
            .format(num_2,num_1,num_3,num_1,num_2,num_3))
    elif num_2 < num_3 < num_1:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'\
            .format(num_2,num_3,num_1,num_1,num_2,num_3))
    elif num_3 < num_1 < num_2:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'\
            .format(num_3,num_1,num_2,num_1,num_2,num_3))
    elif num_3 < num_2 < num_1:
        print('{}\n{}\n{}\n\n{}\n{}\n{}'\
            .format(num_3,num_2,num_1,num_1,num_2,num_3))


if __name__ == '__main__':
    main()
