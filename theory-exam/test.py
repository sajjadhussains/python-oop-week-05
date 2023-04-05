# names=['hatim','katim','satim']
# id=[1,2,3,4]
# for i, j in zip(range(len(names)), range(len(id))):
#     print(i, ",", j)
# def check_anagram(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#     else:
#         length=len(str1)
#         print(length)
#         for i in range(length):
#             print(str1[i])
#             if str1[i] not in str2:
#                 # print(str1[i])
#                 return False
#         return True

# print(check_anagram('shuov','shuvo'))
# check_anagram('shuv','shuvo')
def dp( l1 , l2): 
    def p ( ll1 , ll2 , n ) : 
        return ll1[n] * ll2[n] 
    r = 0 
    for i in range ( len ( l1 ) ) : 
      r += p ( l1 , l2 , i ) 
    return r 


print (dp ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ))

