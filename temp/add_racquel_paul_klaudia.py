# -*- coding: utf-8 -*-
# Island survival file: add Racquel-Paul mutual recognition + Klaudia knows
path = '/home/user/Mike and Terri Anne/key_island_survival.md'
with open(path, encoding='utf-8') as f:
    lines = f.read().split('\n')

beats = [
    ('- **Racquel recognizes Paul too:** Racquel recognizes Paul because she was the prostitute who slept with him '
     'at Gotham City. This history comes up between them.'),
    ('- **Klaudia knows about Racquel\u2019s work:** Klaudia knows that Racquel works at a brothel, because they '
     'are best friends who tell each other everything \u2014 they even shared a bedroom when Klaudia\u2019s parents '
     'died.'),
]

found = False
for i, line in enumerate(lines):
    if 'used to visit Gotham City before he had Keagan' in line:
        for k, b in enumerate(beats):
            lines.insert(i + 1 + k, b)
        found = True
        break
assert found, 'Paul-recognizes-Racquel beat not found'

with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('racquel-paul beat added:', 'she was the prostitute who slept with him' in '\n'.join(lines))
print('klaudia-knows beat added:', 'they even shared a bedroom when Klaudia' in '\n'.join(lines))
