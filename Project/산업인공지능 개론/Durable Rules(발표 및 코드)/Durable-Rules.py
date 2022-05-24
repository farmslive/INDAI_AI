from durable.lang import *

with ruleset('투약기'):
    #1
    @when_all(c.first << (m.predicate == '투약기가') & (m.object == '동작하지 않는다.'),
              (m.predicate == '투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 전원(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '투약기 전원을', 'object': '올린다' })
    #2
    @when_all(c.first << (m.predicate == '투약기가') & (m.object == '동작하지 않는다.'),
              (m.predicate == '투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 쇼트(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '투약기의', 'object': '차단기를 확인한다'})
    #3
    @when_all(c.first << (m.predicate == '투약기가'') & (m.object == '오동작 한다.'),
              (m.predicate == '오동작 투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 접지(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '투약기의', 'object': '접지를 확인한다'})
    #4
    @when_all(c.first << (m.predicate == '투약기가') & (m.object == '오동작 한다.'),
              (m.predicate == '투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 센서(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '센서의', 'object': '설치를 확인한다'})
    #5
    @when_all(c.first << (m.predicate == '투약기가') & (m.object == '약품이 투여되지 않는다.'),
              (m.predicate == '투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 투여(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '배관의', 'object': '압력을 확인한다'})
    #6
    @when_all(c.first << (m.predicate == '투약기가') & (m.object == '약품의 투여량이 다르다.'),
              (m.predicate == '투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 비율(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '투약비율을', 'object': '확인한다'})
   #7
    @when_all(c.first << (m.predicate == '투약기가') & (m.object == '약품의 투여량이 다르다.'),
              (m.predicate == '투약기의') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def 튜브(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '튜브번호를', 'object': '확인한다'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


assert_fact('투약기', { 'subject': '전원 문제일경우', 'predicate': '투약기가', 'object': '동작하지 않는다.' })
assert_fact('투약기', { 'subject': '전원 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })
assert_fact('투약기', { 'subject': '쇼트 문제일경우', 'predicate': '투약기가', 'object': '동작하지 않는다.' })
assert_fact('투약기', { 'subject': '쇼트 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })
assert_fact('투약기', { 'subject': '접지 문제일경우', 'predicate': '투약기가', 'object': '오작동 한다.' })
assert_fact('투약기', { 'subject': '접지 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })
assert_fact('투약기', { 'subject': '센서 문제일경우', 'predicate': '투약기가', 'object': '오작동 한다.' })
assert_fact('투약기', { 'subject': '센서 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })
assert_fact('투약기', { 'subject': '투여 문제일경우', 'predicate': '투약기가', 'object': '약품이 투여되지 않는다.' })
assert_fact('투약기', { 'subject': '투여 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })
assert_fact('투약기', { 'subject': '비율 문제일경우', 'predicate': '투약기가', 'object': '약품의 투여량이 다르다.' })
assert_fact('투약기', { 'subject': '비율 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })
assert_fact('투약기', { 'subject': '튜브 문제일경우', 'predicate': '투약기가', 'object': '약품의 투여량이 다르다.' })
assert_fact('투약기', { 'subject': '튜브 문제일경우', 'predicate': '투약기의', 'object': '문제해결 방법이다.' })




Fact: 전원 문제일경우 투약기가 동작하지 않는다.
Fact: 전원 문제일경우 투약기 전원을 올린다
Fact: 전원 문제일경우 투약기의 문제해결 방법이다.
Fact: 쇼트 문제일경우 투약기가 동작하지 않는다.
Fact: 쇼트 문제일경우 투약기 전원을 올린다
Fact: 쇼트 문제일경우 투약기의 문제해결 방법이다.
Fact: 접지 문제일경우 투약기가 오작동 한다.
Fact: 접지 문제일경우 투약기의 문제해결 방법이다.
Fact: 센서 문제일경우 투약기가 오작동 한다.
Fact: 센서 문제일경우 투약기의 문제해결 방법이다.
Fact: 투여 문제일경우 투약기가 약품이 투여되지 않는다.
Fact: 투여 문제일경우 배관의 압력을 확인한다
Fact: 투여 문제일경우 투약기의 문제해결 방법이다.
Fact: 비율 문제일경우 투약기가 약품의 투여량이 다르다.
Fact: 비율 문제일경우 튜브번호를 확인한다
Fact: 비율 문제일경우 투약비율을 확인한다
Fact: 비율 문제일경우 투약기의 문제해결 방법이다.
Fact: 튜브 문제일경우 투약기가 약품의 투여량이 다르다.
Fact: 튜브 문제일경우 튜브번호를 확인한다
Fact: 튜브 문제일경우 투약비율을 확인한다
Fact: 튜브 문제일경우 투약기의 문제해결 방법이다.


