# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def get_binary(N, bin_):
    """get the binary number"""
    if N > 1:
        get_binary(N//2, bin_=bin_)
    bin_.append(N%2) 
    return ''.join(str(x) for x in bin_)
    
def solution(N):
    # write your code in Python 3.6
    bin_ = get_binary(N, bin_=[])
    all_len_ = [0]
    len_ = 0 
    gap = False
    for i in bin_:
        if int(i) == 1:
            if not len_:
                gap = True
            else:
                all_len_.append(len_)
                len_ = 0
                gap = True
        elif int(i) == 0 and gap:
            len_ += 1
    return max(all_len_)
