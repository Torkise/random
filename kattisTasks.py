# Kodetest Whitson
def problemOne(N):
    baseHundred = N // 100
    if (baseHundred == 0):
        return 99
    if (N % 100 < 49):
        return (baseHundred*100)-100 + 99
    else:
        return (baseHundred*100) + 99

def problemTwo(N, solutions):
    print("N =", N)
    if N in solutions.keys():
        val = solutions.get(N)
        print('Solution: ' + '4 ' + val[0] + ' 4 ' + val[1] + ' 4 ' + val[2] + ' 4')
        return eval('4' + val[0] + '4' + val[1] + '4' + val[2] + '4')
    else:
        return "no solution"

# Creating possible anwsers for task 2 
operator = ['+', '-', '*', '/']
solutions = {}
for a in operator:
    for b in operator:
        for c in operator:
            num = eval('4' + a + '4' + b + '4' + c + '4')
            if (num >= 0 and int(num) == float(num)):
                solutions[int(num)] = [a, b, c]  
print(solutions.keys())

print("_____________Task 1__________")
print(problemOne(10))
print(problemOne(249))
print(problemOne(10000))
print("____________________________________")


print("___________Task2___________________")
print(problemTwo(5,solutions))
print(problemTwo(9,solutions))
print(problemTwo(0,solutions))
print(problemTwo(7,solutions))
print(problemTwo(11,solutions))
print(problemTwo(24,solutions))