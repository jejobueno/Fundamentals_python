
def list_manipulation(list,command,location,value = 0):
    if command == "remove" and location == "end":
        return list.pop(-1)
    if command == "remove" and location == "beginning":
        return list.pop(0)
    if command == "add" and location == "beginning":
        return [value] + list
    if command == "add" and location == "end":
        return list + [value]
        
print(f' list_manipulation([1,2,3],"remove","end") -> print out: {list_manipulation([1,2,3],"remove","end")}')
print(f' list_manipulation([1,2,3],"remove","beginning") -> print out: {list_manipulation([1,2,3],"remove","beginning")}')
print(f' list_manipulation([1,2,3],"add","beginning",20) -> print out: {list_manipulation([1,2,3],"add","beginning",20)}')
print(f' list_manipulation([1,2,3],"add","end",30) -> print out: {list_manipulation([1,2,3],"add","end",30)}')