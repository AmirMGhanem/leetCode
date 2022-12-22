

def switch_no_condition(n):
    return {5:7,7:5}.get(n,None)

def switch_numbers(n):
    return (n + 2) % 7


print(switch_numbers(5))
print(switch_numbers(7))
print(switch_numbers(20))
