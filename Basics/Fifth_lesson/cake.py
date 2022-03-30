widght=int(input())
lenght=int(input())
whole_cake=widght*lenght

sum_of_taken_piece=0

while True:
    pieces_taken=input()
    if pieces_taken=="STOP":
        print(f"{whole_cake} pieces are left." )
        break
    whole_cake-=int(pieces_taken)
    if whole_cake<= 0:
        print(f"No more cake left! You need {sum_of_taken_piece - whole_cake} pieces more.")
        break
