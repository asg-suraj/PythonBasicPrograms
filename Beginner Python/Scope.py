spamGlobal = 42 #global variable

def egge():
    global spamGlobal #make scope of variable global
    spam =44  #local variable
    spamGlobal=44

  

print ('Some Code')
print(spamGlobal)
egge()
print(spamGlobal)







# 1. Code in one function's local scope cannot use variables in any other local scope
# 2. Code in local scope can access global variable
# 3. Code in one function's local scope cannot use variables in another local scope
# 4. Code in one function's local scope cannot use variables in any other local scope
