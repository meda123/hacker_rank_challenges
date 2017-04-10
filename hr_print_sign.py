
# Takes in a num and returns a string "Higher than zero", "Lower than zero", 
# "Exactly zero" based on the number 

def print_sign(num):
    # Compose your function here.
    if num > 0:
        return "Higher than zero"
    if num == 0:
        return "Exactly zero"
    if num < 0:
        return "Lower than zero"
        
input_num = int(raw_input())
print print_sign(input_num)