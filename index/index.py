def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print_list(cities) 