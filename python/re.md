# 正则表达式

## re.sub

```
>>> import re
>>> s = '100 BROAD ROAD APT. 3'
>>> # \b，匹配一个单词边界，使用\b表达一个独立的词
>>> re.sub(r'\bROAD\b', 'RD.', s)
'100 BROAD RD. APT. 3'
>>> re.sub('\\bROAD\\b', 'RD.', s)
'100 BROAD RD. APT. 3'
>>> re.sub('([^aeiou])y$', r'\1ies', 'vacancy')
'vacancies'
```

## re.search

罗马数字：
```
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
```

```
>>> pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
>>> pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
>>> re.search(pattern, 'MMDCLXVI')
<_sre.SRE_Match object at 0x008EEB48>
```

### 松散正则表达式

```
>>> import re
>>> pattern = '''
    ^                 # beginning of string
    M{0,3}            # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3}   # hudreds - 900(CM), 400(CD), 0-300(0 to 3 Cs),
                      # or 500-800(D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})  # tens - 90(XC), 40(XL), 0-30(0 TO 3 Xs),
                      # or 50-80(L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})  # ones - 9(IX), 4(IV), 0-3(0 to 3 Is),
                      # or 5-8(V, followed by 0 to 3 Is)
    $                 # end of string
    '''
>>> # 如果要使用松散正则表达式，需要传递一个叫re.VERBOSE的参数
>>> re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE)
<_sre.SRE_Match object at 0x008EEB48>
```

## re.compile

```
>>> # \d匹配所有0-9的数字，\D匹配除了数字外的所有字符
>>> phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
>>> phonePattern.search('work 1-(800) 555.1212#1234').groups()
('800', '555', '1212', '1234')
```

```
>>> phonePattern = re.compile('''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
>>> phonePattern.search('work 1-(800) 555.1212#1234').groups()
('800', '555', '1212', '1234')
```
