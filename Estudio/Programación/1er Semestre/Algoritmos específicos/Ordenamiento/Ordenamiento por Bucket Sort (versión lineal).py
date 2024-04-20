def bucket_sort(lista):
    min_val = min(lista)
    max_val = max(lista)
    bucket_range = (max_val - min_val) / len(lista)
    n = len(lista)
    buckets = [[] for _ in range(n)]
    for num in lista:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(sorted(bucket))
    return sorted_list
