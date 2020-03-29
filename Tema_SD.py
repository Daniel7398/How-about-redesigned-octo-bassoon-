import time
import random

f = open("Date.in", 'r')
g = open("Date.out", 'w')


v = []
SD = f.readlines()
t = int(SD[0][0])
def mediana_din_3(Q, p, q):
    mij = (p + q - 1) // 2
    a = Q[p]
    b = Q[mij]
    c = Q[q]
    if a <= b <= c:
        return b
    if c <= b <= a:
        return b
    if a <= c <= b:
        return c
    if b <= c <= a:
        return c
    return a

def pivot_mediana(A):
    if len(A) < 5:
        return sorted(A)[len(A) // 2]
    subliste = [sorted(A[i:i + 5]) for i in range(0, len(A), 5)]
    mediane = [sl[len(sl) // 2] for sl in subliste]
    return pivot_mediana(mediane)


def quickSort(w, tip):
    L = []
    E = []
    G = []

    if len(w) <= 1:
        return w
    else:
        if tip == 1:
            pivot = mediana_din_3(w, 0, len(v) - 1)
        else:
            pivot = pivot_mediana(v)
        for i in w:
            if i < pivot:
                L.append(i)
            elif i > pivot:
                G.append(i)
            else:
                E.append(i)
        L = quickSort(L, tip)
        G = quickSort(G, tip)
        return L + E + G

def countsort(w):
    m = max(w)
    fr = [0 for i in range(10 ** 6)]
    for x in w:
        fr[x] += 1

    rez = []
    for i in range(10 ** 6):
        while fr[i] > 0:
            rez.append(i)
            fr[i] -= 1

    return rez


def bubblesort(w):
    s = w
    p = 0
    while p == 0:
        p = 1
        for i in range(len(w) - 1):
            if w[i] > w[i + 1]:
                a = w[i]
                w[i] = w[i + 1]
                w[i + 1] = a
                p = 0
    return s

def interclasare(wst, wdr):
    i = j = 0
    rez = []
    while i < len(wst) and j < len(wdr):
        if wst[i] < wdr[j]:
            rez.append(wst[i])
            i = i + 1
        else:
            rez.append(wdr[j])
            j = j + 1
    rez.extend(wst[i:])
    rez.extend(wdr[j:])
    return rez


def mergesort(w):
    if len(w) <=1:
        return w
    else:
        mij = len(w) // 2
        wst = mergesort(w[:mij])
        wdr = mergesort(w[mij:])
        return interclasare(wst, wdr)

def radixsort_offset(x, y, z):
    bit = ((2 ** z) - 1) << y * z
    buckets = [[] for a in range(2 ** z)]
    for num in x:
        bit_offset = (num & bit) >> y * z
        buckets[bit_offset].append(num)
    w=[]
    for x in buckets:
        for y in x:
            w.append(y)
    return w


def radix_sort(w, p):
    maxim = max(w)
    biti = 0
    while (maxim):
        biti += 1
        maxim = maxim >> 1

    if biti % p == 0:
        bit_maxim = biti // p
    else:
        bit_maxim = (biti // p) + 1
    x = w
    for i in range(bit_maxim):
        x = radixsort_offset(x, i, p)
    return x

def test(w):
    ok = 1
    for i in range(0, len(w) - 1):
        if w[i] > w[i + 1]:
            ok = 0
    if ok == 0:
        g.write("Nu este sortat.")
    else:
        g.write("Este sortat.")

def generator(n, maxim):
    lista = []
    for x in range(n):
        nr = random.randint(0, maxim + 1)
        lista.append(nr)
    return lista

tst=0
while tst < t:
    intrare = SD[tst + 1].split()
    n = int(intrare[0])
    maxim = int(intrare[1])
    w = generator(n, maxim)

    g.write('Testul ' + str(tst + 1) + ':\n')
    g.write('valoare maxima este ' + str(maxim) + ' nr. maxim de elemente este ' + str(n) + '\n')

    start_time = time.time()
    sol = quickSort(w, 1)
    g.write('Quicksort cu mediana din 3: ')
    test(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = quickSort(w, 2)
    g.write('Quicksort cu mediana medianelor: ')
    test(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')


    if maxim < 10 ** 6:
        start_time = time.time()
        sol = countsort(w)
        g.write('Countsort: ')
        test(sol)
    else:
        start_time = time.time()
        g.write('Countsort: ')
        g.write('Nu se poate sorta')
    g.write("  %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    if n <= 3000:
        sol = bubblesort(w)
        g.write('Bubble Sort: ')
        test(sol)
    else:
        g.write('Bubble Sort: ')
        g.write("Nu se poate sorta")
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = mergesort(w)
    g.write('Mergesort: ')
    test(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = radix_sort(w, 8)
    g.write('Radixsort in baza 256: ')
    test(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = radix_sort(w, 1)
    g.write('Radixsort in baza 2: ')
    test(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')


    start_time = time.time()
    sol.sort()
    g.write("Sortare implicita Python: ")
    test(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')
    g.write('\n')
    g.write('\n')
    tst += 1
f.close()

