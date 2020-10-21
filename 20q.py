from z3 import *

# x1, x2, x3, ... represent whether the given question has been answered
# correctly. x1 == 'question 1 is correct'.
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, \
x11, x12, x13, x14, x15, x16, x17, x18, x19, x20 = \
    Bools('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20')
correct = [None] + \
          [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20]
# correct[i] == answer i is correct

x1a, x1b, x1c, x1d, x1e = Bools('x1a x1b x1c x1d x1e')
x2a, x2b, x2c, x2d, x2e = Bools('x2a x2b x2c x2d x2e')
x3a, x3b, x3c, x3d, x3e = Bools('x3a x3b x3c x3d x3e')
x4a, x4b, x4c, x4d, x4e = Bools('x4a x4b x4c x4d x4e')
x5a, x5b, x5c, x5d, x5e = Bools('x5a x5b x5c x5d x5e')
x6a, x6b, x6c, x6d, x6e = Bools('x6a x6b x6c x6d x6e')
x7a, x7b, x7c, x7d, x7e = Bools('x7a x7b x7c x7d x7e')
x8a, x8b, x8c, x8d, x8e = Bools('x8a x8b x8c x8d x8e')
x9a, x9b, x9c, x9d, x9e = Bools('x9a x9b x9c x9d x9e')
x10a, x10b, x10c, x10d, x10e = Bools('x10a x10b x10c x10d x10e')
x11a, x11b, x11c, x11d, x11e = Bools('x11a x11b x11c x11d x11e')
x12a, x12b, x12c, x12d, x12e = Bools('x12a x12b x12c x12d x12e')
x13a, x13b, x13c, x13d, x13e = Bools('x13a x13b x13c x13d x13e')
x14a, x14b, x14c, x14d, x14e = Bools('x14a x14b x14c x14d x14e')
x15a, x15b, x15c, x15d, x15e = Bools('x15a x15b x15c x15d x15e')
x16a, x16b, x16c, x16d, x16e = Bools('x16a x16b x16c x16d x16e')
x17a, x17b, x17c, x17d, x17e = Bools('x17a x17b x17c x17d x17e')
x18a, x18b, x18c, x18d, x18e = Bools('x18a x18b x18c x18d x18e')
x19a, x19b, x19c, x19d, x19e = Bools('x19a x19b x19c x19d x19e')
x20a, x20b, x20c, x20d, x20e = Bools('x20a x20b x20c x20d x20e')

answers = [None]
answers.append(dict(zip(['A','B','C','D','E'], [x1a, x1b, x1c, x1d, x1e])))
answers.append(dict(zip(['A','B','C','D','E'], [x2a, x2b, x2c, x2d, x2e])))
answers.append(dict(zip(['A','B','C','D','E'], [x3a, x3b, x3c, x3d, x3e])))
answers.append(dict(zip(['A','B','C','D','E'], [x4a, x4b, x4c, x4d, x4e])))
answers.append(dict(zip(['A','B','C','D','E'], [x5a, x5b, x5c, x5d, x5e])))
answers.append(dict(zip(['A','B','C','D','E'], [x6a, x6b, x6c, x6d, x6e])))
answers.append(dict(zip(['A','B','C','D','E'], [x7a, x7b, x7c, x7d, x7e])))
answers.append(dict(zip(['A','B','C','D','E'], [x8a, x8b, x8c, x8d, x8e])))
answers.append(dict(zip(['A','B','C','D','E'], [x9a, x9b, x9c, x9d, x9e])))
answers.append(dict(zip(['A','B','C','D','E'], [x10a, x10b, x10c, x10d, x10e])))
answers.append(dict(zip(['A','B','C','D','E'], [x11a, x11b, x11c, x11d, x11e])))
answers.append(dict(zip(['A','B','C','D','E'], [x12a, x12b, x12c, x12d, x12e])))
answers.append(dict(zip(['A','B','C','D','E'], [x13a, x13b, x13c, x13d, x13e])))
answers.append(dict(zip(['A','B','C','D','E'], [x14a, x14b, x14c, x14d, x14e])))
answers.append(dict(zip(['A','B','C','D','E'], [x15a, x15b, x15c, x15d, x15e])))
answers.append(dict(zip(['A','B','C','D','E'], [x16a, x16b, x16c, x16d, x16e])))
answers.append(dict(zip(['A','B','C','D','E'], [x17a, x17b, x17c, x17d, x17e])))
answers.append(dict(zip(['A','B','C','D','E'], [x18a, x18b, x18c, x18d, x18e])))
answers.append(dict(zip(['A','B','C','D','E'], [x19a, x19b, x19c, x19d, x19e])))
answers.append(dict(zip(['A','B','C','D','E'], [x20a, x20b, x20c, x20d, x20e])))


# answers[i][x] == answer[i] is x

s = Solver()

# Exactly one choice per question.
def ExactlyOneTrue(s,a,b,c,d,e):
    s.add(And(Or(a, b, c, d, e),
              Or(Not(a), Not(b)),
              Or(Not(a), Not(c)),
              Or(Not(a), Not(d)),
              Or(Not(a), Not(e)),
              Or(Not(b), Not(c)),
              Or(Not(b), Not(d)),
              Or(Not(b), Not(e)),
              Or(Not(c), Not(d)),
              Or(Not(c), Not(e)),
              Or(Not(d), Not(e))))
ExactlyOneTrue(s, x1a, x1b, x1c, x1d, x1e)
ExactlyOneTrue(s, x2a, x2b, x2c, x2d, x2e)
ExactlyOneTrue(s, x3a, x3b, x3c, x3d, x3e)
ExactlyOneTrue(s, x4a, x4b, x4c, x4d, x4e)
ExactlyOneTrue(s, x5a, x5b, x5c, x5d, x5e)
ExactlyOneTrue(s, x6a, x6b, x6c, x6d, x6e)
ExactlyOneTrue(s, x7a, x7b, x7c, x7d, x7e)
ExactlyOneTrue(s, x8a, x8b, x8c, x8d, x8e)
ExactlyOneTrue(s, x9a, x9b, x9c, x9d, x9e)
ExactlyOneTrue(s, x10a, x10b, x10c, x10d, x10e)
ExactlyOneTrue(s, x11a, x11b, x11c, x11d, x11e)
ExactlyOneTrue(s, x12a, x12b, x12c, x12d, x12e)
ExactlyOneTrue(s, x13a, x13b, x13c, x13d, x13e)
ExactlyOneTrue(s, x14a, x14b, x14c, x14d, x14e)
ExactlyOneTrue(s, x15a, x15b, x15c, x15d, x15e)
ExactlyOneTrue(s, x16a, x16b, x16c, x16d, x16e)
ExactlyOneTrue(s, x17a, x17b, x17c, x17d, x17e)
ExactlyOneTrue(s, x18a, x18b, x18c, x18d, x18e)
ExactlyOneTrue(s, x19a, x19b, x19c, x19d, x19e)
ExactlyOneTrue(s, x20a, x20b, x20c, x20d, x20e)

# (1) The first question whose answer is A is:
#     (A) 1  (B) 2  (C) 3  (D) 4  (E) 5
s.add(x1 == Or(x1a,
               And(x1b,x2a,Not(x1a)),
               And(x1c,x3a,Not(x1a),Not(x2a)),
               And(x1d,x4a,Not(x1a),Not(x2a),Not(x3a)),
               And(x1e,x5e,Not(x1a),Not(x2a),Not(x3a),Not(x4a))))

# (2) The next question with the same answer as this one is:
#     (A) 4  (B) 6  (C) 8  (D) 10  (E) 12
s.add(x2 == Or(And(x2a,Not(x3a),x4a),
               And(x2b,Not(x3b),Not(x4b),Not(x5b),x6b),
               And(x2c,Not(x3c),Not(x4c),Not(x5c),Not(x6c),Not(x7c),x8c),
               And(x2d,Not(x3d),Not(x4d),Not(x5d),Not(x6d),Not(x7d),Not(x8d),
                   Not(x9d),x10d),
               And(x2e,Not(x3e),Not(x4e),Not(x5e),Not(x6e),Not(x7e),Not(x8e),
                   Not(x9e),Not(x10e),Not(x11e),x12e)))

# (3) The only two consecutive questions with identical answers are questions:
#     (A) 15 and 16  (B) 16 and 17  (C) 17 and 18  (D) 18 and 19  (E) 19 and 20
def same_answer(i,j):
    return Or(And(answers[i]['A'],answers[j]['A']),
              And(answers[i]['B'],answers[j]['B']),
              And(answers[i]['C'],answers[j]['C']),
              And(answers[i]['D'],answers[j]['D']),
              And(answers[i]['E'],answers[j]['E']))
s.add(x3 == Or(
    And(x3a, same_answer(15, 16),
        *[Not(same_answer(i,i+1)) for i in range(1,20) if i != 15]),
    And(x3b, same_answer(16, 17),
        *[Not(same_answer(i,i+1)) for i in range(1,20) if i != 16]),
    And(x3c, same_answer(17, 18),
        *[Not(same_answer(i,i+1)) for i in range(1,20) if i != 17]),
    And(x3d, same_answer(18, 19),
        *[Not(same_answer(i,i+1)) for i in range(1,20) if i != 18]),
    And(x3e, same_answer(19, 20),
        *[Not(same_answer(i,i+1)) for i in range(1,20) if i != 19])))

# 4. The answer to this question is the same as the answers to questions:
#    (A) 10 and 13  (B) 14 and 16  (C) 7 and 20  (D) 1 and 15  (E) 8 and 12
s.add(x4 == Or(And(x4a,x10a,x13a),
               And(x4b,x14b,x16b),
               And(x4c,x7c,x20c),
               And(x4d,x1d,x15d),
               And(x4e,x8e,x12e)))

# 5. The answer to question 14 is:
#    (A) B  (B) E  (C) C  (D) A  (E) D
s.add(x5 == Or(And(x5a,x14b),
               And(x5b,x14e),
               And(x5c,x14c),
               And(x5d,x14a),
               And(x5e,x14d)))

# 6. The answer to this question is:
#    (A) A  (B) B  (C) C  (D) D  (E) none of the above
s.add(x6 == True)

# 7. The answer that appears most often (possibly tied) is:
#    (A) A  (B) B  (C) C  (D) D  (E) E
def ToInt(x):
    return If(x,1,0)
def answer_sum(ans):
    return reduce(lambda x,y : x+y,
                  map(lambda i: ToInt(answers[i][ans]), range(1,21)))
s.add(x7 == Or(And(x7a,
                   answer_sum('A') >= answer_sum('B'),
                   answer_sum('A') >= answer_sum('C'),
                   answer_sum('A') >= answer_sum('D'),
                   answer_sum('A') >= answer_sum('E')),
               And(x7b,
                   answer_sum('B') >= answer_sum('A'),
                   answer_sum('B') >= answer_sum('C'),
                   answer_sum('B') >= answer_sum('D'),
                   answer_sum('B') >= answer_sum('E')),
               And(x7c,
                   answer_sum('C') >= answer_sum('A'),
                   answer_sum('C') >= answer_sum('B'),
                   answer_sum('C') >= answer_sum('D'),
                   answer_sum('C') >= answer_sum('E')),
               And(x7d,
                   answer_sum('D') >= answer_sum('A'),
                   answer_sum('D') >= answer_sum('B'),
                   answer_sum('D') >= answer_sum('C'),
                   answer_sum('D') >= answer_sum('E')),
               And(x7e,
                   answer_sum('E') >= answer_sum('A'),
                   answer_sum('E') >= answer_sum('B'),
                   answer_sum('E') >= answer_sum('C'),
                   answer_sum('E') >= answer_sum('D'))))

# 8. Ignoring those that occur equally often, the answer that appears least
#    often is:
#    (A) A  (B) B  (C) C  (D) D  (E) E
s.add(x8 == Or(And(x8a,
                   answer_sum('A') <= answer_sum('B'),
                   answer_sum('A') <= answer_sum('C'),
                   answer_sum('A') <= answer_sum('D'),
                   answer_sum('A') <= answer_sum('E')),
               And(x8b,
                   answer_sum('B') <= answer_sum('A'),
                   answer_sum('B') <= answer_sum('C'),
                   answer_sum('B') <= answer_sum('D'),
                   answer_sum('B') <= answer_sum('E')),
               And(x8c,
                   answer_sum('C') <= answer_sum('A'),
                   answer_sum('C') <= answer_sum('B'),
                   answer_sum('C') <= answer_sum('D'),
                   answer_sum('C') <= answer_sum('E')),
               And(x8d,
                   answer_sum('D') <= answer_sum('A'),
                   answer_sum('D') <= answer_sum('B'),
                   answer_sum('D') <= answer_sum('C'),
                   answer_sum('D') <= answer_sum('E')),
               And(x8e,
                   answer_sum('E') <= answer_sum('A'),
                   answer_sum('E') <= answer_sum('B'),
                   answer_sum('E') <= answer_sum('C'),
                   answer_sum('E') <= answer_sum('D'))))

# TODO: kind of unclear whether I include or exclude 9 here in each sum...
# 9. The sum of all question numbers whose answers are correct and the same as
#    this one is in the range:
#    (A) 59 to 62, inclusive
#    (B) 52 to 55, inclusive
#    (C) 44 to 49, inclusive
#    (D) 61 to 67, inclusive
#    (E) 44 to 53, inclusive
def qnum_sum(ans):
    return reduce(lambda x,y : x+y,
                  map(lambda i: If(answers[i][ans], i, 0), range(1,21)))
s.add(x9 == Or(And(x9a, qnum_sum('A') >= 59, qnum_sum('A') <= 62),
               And(x9b, qnum_sum('B') >= 52, qnum_sum('B') <= 55),
               And(x9c, qnum_sum('C') >= 44, qnum_sum('C') <= 49),
               And(x9d, qnum_sum('D') >= 61, qnum_sum('D') <= 67),
               And(x9e, qnum_sum('E') >= 44, qnum_sum('E') <= 53)))

# 10. The answer to question 17 is:
#     (A) D  (B) B  (C) A  (D) E  (E) wrong
s.add(x10 == Or(And(x10a, x17d),
                And(x10b, x17b),
                And(x10c, x17a),
                And(x10d, x17e),
                And(x10e, Not(x17))))

# 11. The number of questions whose answer is D is:
#     (A) 2  (B) 3  (C) 4  (D) 5  (E) 6
s.add(x11 == Or(And(x11a, answer_sum('D') == 2),
                And(x11b, answer_sum('D') == 3),
                And(x11c, answer_sum('D') == 4),
                And(x11d, answer_sum('D') == 5),
                And(x11e, answer_sum('E') == 6)))

# 12. The number of OTHER questions with the same answer as this
#     one is the same as the number of questions with answer:
#     (A) B  (B) C  (C) D  (D) E  (E) none of the above
s.add(x12 == Or(And(x12a, answer_sum('A') - 1 == answer_sum('B')),
                And(x12b, answer_sum('B') - 1 == answer_sum('C')),
                And(x12c, answer_sum('C') - 1 == answer_sum('D')),
                And(x12d, answer_sum('D') - 1 == answer_sum('E')),
                And(x12e,
                    answer_sum('A') - 1 != answer_sum('B'),
                    answer_sum('B') - 1 != answer_sum('C'),
                    answer_sum('C') - 1 != answer_sum('D'),
                    answer_sum('D') - 1 != answer_sum('E'))))

# 13. The number of questions whose answer is E is:
#     (A) 5  (B) 4  (C) 3  (D) 2  (E) 1
s.add(x13 == Or(And(x13a, answer_sum('E') == 5),
                And(x13b, answer_sum('E') == 4),
                And(x13c, answer_sum('E') == 3),
                And(x13d, answer_sum('E') == 2),
                And(x13e, answer_sum('E') == 1)))

# 14. There is no answer that appears exactly:
#     (A) two times
#     (B) three times
#     (C) four times
#     (D) five times
#     (E) none of the above
def no_answer_sum(x):
    return And(answer_sum('A') != x,
               answer_sum('B') != x,
               answer_sum('C') != x,
               answer_sum('D') != x,
               answer_sum('E') != x)
s.add(x14 == Or(And(x14a, no_answer_sum(2)),
                And(x14b, no_answer_sum(3)),
                And(x14c, no_answer_sum(4)),
                And(x14d, no_answer_sum(5)),
                And(x14e,
                    Not(no_answer_sum(2)),
                    Not(no_answer_sum(3)),
                    Not(no_answer_sum(4)),
                    Not(no_answer_sum(5)))))

def answer_in_model(m, i):
    if m[answers[i]['A']]: return 'A'
    if m[answers[i]['B']]: return 'B'
    if m[answers[i]['C']]: return 'C'
    if m[answers[i]['D']]: return 'D'
    if m[answers[i]['E']]: return 'E'
    raise Exception('No answer for %s!' % i)

print s.check()
m = s.model()
for i in range(1,21):
    print '%s: %s' % (i,answer_in_model(m,i))
