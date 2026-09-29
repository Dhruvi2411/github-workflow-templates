def greet(func):
    
    def new_check():       
        print("Hello----")
        func()
        print("Bbyy...")
    
    return new_check
    
@greet
def test():
    print("Conversation...")

test()


def print_val(num):
    
    for i in range(num):
        yield i
        
ans = print_val(100000)
print(next(ans))
print(next(ans))
print(next(ans))
print(next(ans))
print(next(ans))
