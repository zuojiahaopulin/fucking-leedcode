def prime_num(N):
    result = []
    if N <= 0:
        print []
    if N == 1:
        print [1]
    else:
        result = [1]
        for num in range(2, N+1):
            i = 2
            while(i*i <= num):
                if num % i == 0:
                    break
                else:
                    i += 1
            if i*i > num:
                result.append(num)
        print result
        
if __name__ == "__main__":
    prime_num(100)
