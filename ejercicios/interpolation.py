a = 'the number {0} have been interpolated'.format(1.23)
b = 'the number {0} have been interpolated'.replace('{0}',str(1.23))
c = 'the number {0} have been interpolated'.replace('{0}','1.23')
d = 'the numbers {0} and {1} have been interpolated'.format('1.23', 9.9999)
e = 'the numbers {0} and {1} have been interpolated'.format('1.23', 9.9999)

one = 'the number {0:>10} have been formated '.format(123)
one = 'the number {0:<10} have been formated '.format(123)
one = 'the number {0:010} have been formated '.format(123)
one = 'the number {0:+} have been formated '.format(123)
one = 'the number {0:-} have been formated '.format(123)
one = 'the number {0: } have been formated '.format(123)

one = 'the number {0:b} have been formated '.format(123)
one = 'the number {0:c} have been formated '.format(123)
one = 'the number {0:d} have been formated '.format(123)
one = 'the number {0:o} have been formated '.format(123)
one = 'the number {0:x} have been formated '.format(123)

one = 'the number {0:+#016b} have been formated '.format(123)

print(a)
print(b)
print(c)
print(d)
print(e)

print(one)
