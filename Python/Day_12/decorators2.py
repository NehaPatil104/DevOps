# Manually calling decorator

# def divide(x,y):       
#     print(x/y)         
# def outer_div(func): # func = divide       
#     def inner(x,y):        
#         if(x<y):    
#             x,y = y,x    
#         return func(x,y)         
#     return inner    
# divide1 = outer_div(divide)   # => inner(x,y)
# divide1(6,4) # => inner(2, 4)   

# using syntactic annotator

def outer_div(func):    
    def inner(x,y):        
        if(x<y):    
           x,y = y,x    
        return func(x,y)         
    return inner    
   
@outer_div    # divide = outer_div(divide) => inner
def divide(x,y):      
     print(x/y)    

divide(2, 22) # => inner(2, 22) => return divide(22, 2)