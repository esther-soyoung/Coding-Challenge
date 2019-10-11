from datetime import datetime
import sys
from collections import OrderedDict

def solution(m, musicinfos):
    m_ = sharp(m)
    ret = '(None)'
    for i in musicinfos:
        j = played(i)  # (duration, name, played notes)
        if m_ in j[2]:
            if ret == '(None)':
                ret = j
            else:  # tie
                ret = max(ret, j, key = lambda x : x[0])

    if ret != '(None)':
        ret = ret[1]
    return ret


''' Input: string of notes
    Return: replace C#, D#, F#, G#, A# with c, d, f, g, a
'''
def sharp(str_notes):
    ret = ''
    for i in range(len(str_notes) - 1):
        if str_notes[i] == '#':
            continue
        if str_notes[i+1] == '#':
            ret += str_notes[i].lower()
        else:
            ret += str_notes[i]
    if str_notes[-1] != '#':
        ret += str_notes[-1]
    return ret


''' Input: single line of musicinfo
    Return: (duration, name, notes)  //notes actually played in radio
'''
def played(musicinfo_single):
    s = musicinfo_single.split(',')
    duration = datetime.strptime(s[1], '%H:%M') - datetime.strptime(s[0], '%H:%M')
    duration = duration.seconds//60
    name = s[2]
    notes = sharp(s[3])

    num_played = duration // len(notes)  # whole song
    rest_played = duration % len(notes)  # rest
    ret = ''
    for i in range(num_played):
        ret += notes
    ret += notes[:rest_played]

    return (duration, name, ret)




if __name__ == "__main__":
    m = ['ABCDEFG', 'CC#BCC#BCC#BCC#B', 'ABC']
    musicinfos = [["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]]
    for i in range(len(m)):
        print(solution(m[i], musicinfos[i]))
