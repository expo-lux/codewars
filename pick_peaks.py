def is_plateau(arr: list):
    val = arr[0]
    for item in arr:
        if item < val:
            return True
        elif item > val:
            return False
    return False


def pick_peaks(arr):
    pos, peaks = [], []
    if arr:
        prev = arr[0]
        for i, value in enumerate(arr[1:-1]):
            j = i + 1
            nexx = arr[j + 1]
            if value > prev and value > nexx:
                pos.append(j)
                peaks.append(value)
            elif value > prev and value == nexx:
                if is_plateau(arr[j:]):
                    pos.append(j)
                    peaks.append(value)
            prev = value
    return {'pos': pos, 'peaks': peaks}

arr = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]
arr = []
print(pick_peaks(arr))
