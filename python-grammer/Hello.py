def pr():
    print("Hello Python")


def weather(temperature):
    if temperature > 30:
        print('it\'s hot today')
    else:
        print('not bad')


def do_work(times):
    for time in range(times):
        print('work {}'.format(time))


pr()
weather(35)
do_work(5)
