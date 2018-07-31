
happy_hardcore_acts = {
    'DJ Paul Elstak':       ('Dutch',   'Life is like a dance'),
    'Dune':                 ('German',  'Hardcore vibes'),
    'Scooter':              ('German',  'Hyper Hyper'),
    'Tokyo Ghetto Pussy':   ('German',  'I kiss your lips'),
    'Party Animals':        ('Dutch',   'Aquarius'),
    'Technohead':           ('Dutch',   'I wanna be hippy')
}

# for act, (nationality, info) in happy_hardcore_acts.items():
#     print(act, info)

# for act, (nationality, hit) in happy_hardcore_acts.items():
#     if nationality != 'German':
#         continue
#     if not act.startswith('D'):
#         continue
#     if 'vibes' not in hit:
#         continue
#     print('%s was a %s act, and their big hit was %s' %(act, nationality, hit))
#
for act, (nationality, hit) in happy_hardcore_acts.items():
    if nationality == 'Australian':
        print('Australian act found!')
        break
        print('%s wsa a %s act, and their big hit was %s' % (act,nationality,hit))
    else:
        print('No German act found!')
