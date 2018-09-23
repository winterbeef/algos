
def divsub(num, div, times=0):    
    # term case
    if num < div:
        # num = remainder
        return "q:{}, r:{}".format(times, num) 
    
    else:
        times += 1
        # 1, 2
        divsub(num-div, div, times)

        

# min q : 0
# max q : num

# 1 < x < num
# bin search 


# left  = [0, 31/2]
# right = [31/2+1, 31]
# 
# candidate * div =?= num
#   > 
#   = q:candidate, r:0
#   < 

# 31, 5
# try cand = 31/2 (15)
# (15 * div) ? = 31
# <
# ==
# >



# need num div!!
def bindiv(num, div, target):
    
    if num * div == target:
        return "q: {} r: {}".format(num, 0)
    
    elif num * div > target:
        num <<= 1
        bindiv(num, div, target)
    
    elif num < div:
        
    
    else:
        num >>= 1
        bindiv(num, div, target)


        
