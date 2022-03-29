    import math
    tournaments_number=int(input())
    initial_points=int(input())
    total_points=0
    final_points=0
    average_points=0
    percent_win_tour=0
    winned_tours=0
    for i in range(tournaments_number):
        position=input()
        if position=="W":
            total_points+=2000
            winned_tours+=1
        elif position=="F":
            total_points+=1200
        elif position== "SF":
            total_points+=720
    final_points= total_points + initial_points
    average_points=total_points/tournaments_number
    percent_win_tour=winned_tours/tournaments_number*100
    print (f"Final points: {final_points}")
    print (f"Average points: {math.floor(average_points)}")
    print(f"{percent_win_tour:.2f}%")

