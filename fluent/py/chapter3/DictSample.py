DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
d1 = dict(DIAL_CODES)
print('Dictionary 1 Keys : ', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('Dictionary 2 Keys : ', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
print('Dictionary 3 Keys : ', d3.keys())
print(d1 == d2 == d3)