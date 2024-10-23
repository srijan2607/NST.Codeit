'''After her lecture, Priya Ma'am gave her students 
n
n post-class questions to solve. However, her students, being a bit lazy, decided to choose only k questions (where 
1
≤
k
≤
5
1≤k≤5) out of the 
n
n questions. Your task is to determine how many distinct ways the students can select exactly k k questions from the given n n questions.'''


n,k = map(int,input.split())
num = 1
for i in range(0,k):
    num *= (n - i)
den = 1 
for i in range(1, k + 1):
    den *= i
print( num // den)
        
