# https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif


def quicksort(ar):
    if len(ar) < 2:
        return ar
    lt, eq, rt = [], [], []
    for item in ar:
        if item < ar[0]:
            lt.append(item)
        elif item > ar[0]:
            rt.append(item)
        else:
            eq.append(item)
    sub = quicksort(lt) + eq + quicksort(rt)
    print(*sub)
    return(sub)

ar = [5, 8, 1, 3, 7, 9, 2]
quicksort(ar)