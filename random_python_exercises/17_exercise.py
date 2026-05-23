def judge_circle(moves: str) -> bool:
    counterUD, counterRL = 0, 0
    for index, value in enumerate(moves):
        match value:
            case "U":
                counterUD -=1
            case "D":
                counterUD +=1
            case "R":
                counterRL -=1
            case "L":
                counterRL +=1
    return not counterUD and not counterRL

print(judge_circle("UD"))
print(judge_circle("RRDD"))
print(judge_circle("LL"))
print(judge_circle("RR"))
print(judge_circle("DURDLDRRLL"))