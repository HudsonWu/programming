# -*- coding: utf-8 -*-

import re

namePattern = re.compile(r'(Windows 7 With SP1.*?)[ ]*?<')
ed2kPattern = re.compile(r' href="(ed2k://.*?)" .*?>(.*?)</a>')
shaPattern = re.compile(r'(SHA1:.*?)<')
name_list = []
ed2k_list = []
sha_list = []

result_file = open('result.txt', 'w')

with open("source.html", encoding="utf-8") as pattern_file:
    for pattern in pattern_file:
        if namePattern.search(pattern):
            name_result = namePattern.search(pattern).groups()[0]
            name_list.append(name_result)
        if ed2kPattern.search(pattern):
            ed2k_result = ed2kPattern.search(pattern).groups()
            ed2k_list.append(ed2k_result)
        if shaPattern.search(pattern):
            sha_result = shaPattern.search(pattern).groups()[0]
            sha_list.append(sha_result)
    pattern_file.close()

name_list.remove('Windows 7 With SP1 64位英文家庭普通版')
name_list.remove('Windows 7 With SP1 64位简体中文家庭普通版')

if len(ed2k_list) == len(sha_list) == len(name_list):
    for i in range(len(ed2k_list)):
        result_file.write(str(name_list[i]) + '\n' + \
                          "+ name: " + str(ed2k_list[i][1]) + '\n' + \
                          "+ ed2k: " + str(ed2k_list[i][0]) + '\n' + \
                          "+ " + str(sha_list[i]) + '\n\n')

result_file.close()
