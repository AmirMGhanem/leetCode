

def switch_no_conditions(n):
    return {5:7,7:5}.get(n,None)


print(switch_no_conditions(5))
print(switch_no_conditions(7))
print(switch_no_conditions(20))
