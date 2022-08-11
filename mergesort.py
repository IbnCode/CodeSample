def mergesort(L):

    if len(L) <= 1:
        return
    mid1 = len(L)//3
    mid2 = 2*len(L)//3
    left, mid, right = L[:mid1], L[mid1:mid2] , L[mid2:]

    #Mergesort core
    mergesort(left)
    mergesort(mid)
    mergesort(right)
    temp = merge_three(left, mid, right)
    for i in range(len(temp)):
        L[i] = temp[i]

def merge_three(left, mid, right):
    L = []
    i = j = k = 0
    while i < len(left) or k < len(right) or j < len(mid):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L = L + merge(mid[j:],right[k:])
            break
        elif j >= len(mid):
            L = L + merge(left[i:],right[k:])
            break
        elif k >= len(right):
            L = L + merge(left[i:],mid[j:])
            break
        else:
            if left[i] >= mid[j]:
                if mid[j] >= right[k]:
                    L.append(right[k])
                    k += 1
                else:
                    L.append(mid[j])
                    j += 1
            else:
                if left[i] >= right[k]:
                    L.append(right[k])
                    k += 1
                else:
                    L.append(left[i])
                    i += 1
    return L



def merge(left, right):
    L = []
    i = j = 0
    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,10000))
    return L

def testCreateArray(): #test function for testing in-place and multi-pivot algorithms, can print the array later to terminal
    def testAux():
        a = []
        for i in range(300):
            j = create_random_list(i*500 + 500)
            x = timeit.default_timer()
            mergesort(j) #insert sorting function here
            y = timeit.default_timer()
            a.append(y-x)
        return a
    n = testAux() #making different tests
    m = testAux()
    x = testAux()
    test = []
    for i in range(300):
        test.append((n[i]+m[i]+x[i])/3) #adding the mean of all tests (to print later)
    return test
