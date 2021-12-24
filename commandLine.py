import sys
def areaRect(len,brd):
    return len*brd

def main():
    if (len(sys.argv)==3):
        length=float(sys.argv[1])
        breadth=float(sys.argv[2])
        area = areaRect(length, breadth)
        print("area of rectangle is",area)
    else:
        print("unexpected number of command line arguments")
        
if __name__=='__main__':
    main()
      