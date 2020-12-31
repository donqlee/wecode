lst=[]
num = range(1,50)
def even_num_finder(num):
    for i in num:
        if i%2==0:
            lst.append(i)
    return lst