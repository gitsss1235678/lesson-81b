def MaxActivities(arr, n):
    selected = []
    Activity.sort(key=lambda x: x[1])
    i = 0
    selected.append(arr[i])

    for i in range(1, n):
        '''If this activity has start time greater than or equal to the finish time of previously selected activity, then select it'''
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected

if __name__ == '__main__':
    Activity = [[3, 7], [2, 0], [6, 8], [1,7], [7, 5], [2, 3]]
    n = len(Activity)
    selected = MaxActivities(Activity, n)
    print("Following activities are selected : ")
    print(selected[0], end = "")
    for i in range (1, len(selected)):
        print(",", end = "")
        print(selected[i], end = "")