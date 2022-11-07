import time
def deb():
    n = 0
    while True:
        time.sleep(1)
        print('abcd')
        time.sleep(1)
        print('efgh')
        n+=1
        print(n)
        if n==10:
            break
