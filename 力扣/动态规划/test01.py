ways = []
def main(n):

    if n==0:
        ways.append(1)
    else:
        if n>=2:
            main(n-1)
            main(n-2)
        else:
            main(n - 1)
    return ways


n=eval(input())
print(len(main(n)))

