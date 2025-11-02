"""Debug string splitting"""

test_str = 'LO1: Create HTML pages\nLO2: Style with CSS\nLO3: Add JavaScript interactivity'
print('Original:', repr(test_str))

lines = test_str.split('\n')
print('Split result:', lines)
print('Length:', len(lines))

for i, line in enumerate(lines):
    print(f'  [{i}]: {repr(line)}')

# Test with replace
lines2 = test_str.replace('\r\n', '\n').split('\n')
print('\nWith replace:')
for i, line in enumerate(lines2):
    print(f'  [{i}]: {repr(line)}')

# Test zip
ic_str = 'IC1: HTML5 tags and structure\nIC2: CSS selectors and properties\nIC3: JavaScript basics and DOM'
ic_lines = ic_str.split('\n')

print('\nZip result:')
for i, (lo, ic) in enumerate(zip(lines, ic_lines)):
    print(f'  Pair {i}: LO={lo} | IC={ic}')
