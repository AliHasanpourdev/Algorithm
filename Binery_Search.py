def binery_search(l, k) :
    if len(l)==0 :
        return False
    else :
        left = 0
        right = len(l)-1
        mid = int((left+right)/2)
        if l[mid]==k :
            return True
        elif l[mid]<k :
            return binery_search(l[mid+1:], k)
        else :
            return binery_search(l[:mid], k)
        

def main() :
    l = list(map(float, input("please enter your list seperated by space : ").split(" ")))
    k = float(input("please enter the number for find : "))
    print(binery_search(l, k))


if __name__ == "__main__" :
    main()