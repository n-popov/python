try:
    print(open(input()).read().lower().split().count(input().lower()))
except:
    print(0)
