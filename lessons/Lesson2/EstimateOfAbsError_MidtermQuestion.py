#plug in the last two points or x values like x3 and x2 and the amount of significant figures in the question he wants

def EstimateOfAbsError(x3, x2, SignificantFigures):
    #x3 = -7.624
    #x2 = -7.84
    #SignificantFigures = 1

    #answer = abs(x3-x2)
    #rounded_answer = round(answer, SignificantFigures)
    rounded_answer = round(abs(x3-x2), SignificantFigures)
    print(rounded_answer)
    return rounded_answer