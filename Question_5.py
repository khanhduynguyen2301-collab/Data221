import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 < 0 or radiusOfCircle2 < 0:
        return "Invalid input, the input must be positive."
    areaOfCircle1 = math.pi * (radiusOfCircle1**2)
    areaOfCircle2 = math.pi * (radiusOfCircle2**2)

    larger = max(areaOfCircle1, areaOfCircle2)
    smaller = min(areaOfCircle1, areaOfCircle2)

    areaCoveragePercentage = (smaller / larger) * 100
    return f"{areaCoveragePercentage} %"

print(circleAreaCoverage(3, 5))
