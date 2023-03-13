
def main():
    answer=input('What time is it?')
    time=convert(answer)
    if time >= 7 and time <=8:
        print('Breakfast time')
    elif time >= 12 and time <=13:
        print('Meal time')
    elif time >= 18 and time <=19:
        print('Dinner time')


def convert(time):
    hours, minutes = time.split(":")
    newhour= float(int(hours) + int(minutes)/int(60))
    return newhour


if __name__ == "__main__":
    main()