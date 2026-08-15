# -*- coding: utf-8 -*-
path = '/home/user/Mike and Terri Anne/key_island_survival.md'
with open(path, encoding='utf-8') as f:
    lines = f.read().split('\n')

beats = [
    ('- **They cannot bury Uncle Paul:** The kids have no shovels to dig the ground, so they have to leave Uncle '
     'Paul\u2019s body on the sand.'),
    ('- **Moving to the other side of the island:** Langston Siobhan asks Keagan and Virgil to go to the other side '
     'of the island \u2014 away from Uncle Paul\u2019s body \u2014 and they agree. They use their rowboat to cross '
     'to the other side.'),
    ('- **Langston Siobhan goes quiet:** Langston Siobhan becomes very quiet, and the boys are very nervous for '
     'her.'),
]

found = False
for i, line in enumerate(lines):
    if 'Langston Siobhan turns seven, and Keagan turns eight' in line:
        for k, b in enumerate(beats):
            lines.insert(i + 1 + k, b)
        found = True
        break
assert found, 'birthdays beat not found'

with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('beats added:', all('leave Uncle Paul\u2019s body on the sand' in '\n'.join(lines),
                          'use their rowboat' in '\n'.join(lines),
                          'boys are very nervous for her' in '\n'.join(lines)))
