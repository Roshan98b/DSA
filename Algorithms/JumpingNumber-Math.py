def bfs(n, i, result):
    queue = [i]
    while (len(queue) != 0):
        num = queue.pop()
        if num<n:
            result.append(num)
            ld = num%10
            if ld == 0:
                queue.append((num*10) + (ld+1))
            elif ld == 9:
                queue.append((num*10) + (ld-1))
            else:
                queue.append((num*10) + (ld+1))
                queue.append((num*10) + (ld-1))

def j_num(n):
    if n <= 9:
        return [i for i in range(n+1)]
    result = [0]
    for i in range(1,10):
        bfs(n, i, result)
    return result

if __name__ == "__main__":
    n = 125
    jn = j_num(n)
    print(max(jn))