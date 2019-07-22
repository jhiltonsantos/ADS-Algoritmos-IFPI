def main():
    tweet = input()

    if len(tweet)>140:
        print('MUTE')
    else:
        print('TWEET')


main()