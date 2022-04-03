judges_count = int(input())

presentation_name = input()
presentation_count=0
avv_sum = 0

while presentation_name != 'Finish':
    avv_score = 0
    for number in range (judges_count):
        grade = float (input())
        avv_score += grade
    avv_score = avv_score/judges_count
    print (f'{presentation_name} - {avv_score:.2f}.')
    avv_sum += avv_score
    presentation_count+=1

    presentation_name = input()

avv_sum /= presentation_count
print (f"Student's final assessment is {avv_sum:.2f}.")