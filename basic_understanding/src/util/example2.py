from src.util.common import sumation
import argparse

def main(sum,a,b):
    if sum==1:
        return a+b
    else:
        return a-b

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--sum',"-s",default=1)
    args.add_argument('--a', default=10)
    args.add_argument('--b', default=20)
    parsed_args = args.parse_args()
    print (parsed_args)
    #print(parsed_args.sum)
    #print(parsed_args.a)
    #print(parsed_args.b)
    y = main(int(parsed_args.sum),int(parsed_args.a),int(parsed_args.b))
    print (y)

    #main()