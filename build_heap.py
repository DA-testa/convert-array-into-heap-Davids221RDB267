# python3


def build_heap(data):
    swaps = []
    n=len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    for x in range(n // 2,-1,-1):
        heap(x,n,data,swaps)
    return swaps

def heap(a,n,data,swaps):
    minimalais=a
    y=a*2+1
    if n>y and data[minimalais]<data[y]:
        minimalais=y
        
    b=a*2+2
    
    if data[minimalais]>data[b] and n>b:
        minimalais=b
    
    if a!=minimalais:
        data[a],data[minimalais]=data[minimalais],data[a]
        swaps.append((a,minimalais))
        heap(minimalais,n,data,swaps)
        
        


def main():
    
    try:
        ievadits=input()
        
        if ievadits.startswith('F'):
           testi="tests/"+input()
        
           with open(testi,'r') as ts:
                n=int(ts.readline())
                data = list(map(int, ts.readline().split()))
        elif ievadits.startswith('I'):
            n=int(input())
            data = list(map(int, input().split()))
            
    except Exception as error:
            print("error")
            return
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # output all swaps
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
