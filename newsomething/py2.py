

def search(L, e):
    print(L, e,)

    def bin_search(L, e, max, min):
    

        if max == min:
            if L[max] == e:
                return True
            else:
                return False
        
        mid = round((max+min)/2)

        print(f"max = {max}, min = {min}, mid = {mid}")

        if L[mid] == e:
            return True
        else:
            if e<L[mid]:
                max = mid - 1
                return bin_search(L, e, max, min)
            else:
                min = mid + 1
                return bin_search(L, e, max, min)
                


    

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, len(L)-1, 0)

    

print(search([1,3,4,6,8,9,11], 3))
