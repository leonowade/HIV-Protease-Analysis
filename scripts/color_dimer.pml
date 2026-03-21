load data/pdb/1idb.pdb
hide all
show cartoon
set ray_shadows, 0
color gray80, chain A
color gray90, chain B
alter (resi 1), b=58.35
alter (resi 2), b=60.90
alter (resi 3), b=28.26
alter (resi 4), b=37.19
alter (resi 5), b=15.16
alter (resi 6), b=24.09
alter (resi 7), b=55.65
alter (resi 8), b=34.35
alter (resi 9), b=12.95
alter (resi 10), b=25.33
alter (resi 11), b=31.90
alter (resi 12), b=43.92
alter (resi 13), b=36.63
alter (resi 14), b=65.66
alter (resi 15), b=56.64
alter (resi 16), b=77.51
alter (resi 17), b=83.20
alter (resi 18), b=91.45
alter (resi 19), b=56.23
alter (resi 20), b=57.07
alter (resi 21), b=70.94
alter (resi 22), b=23.68
alter (resi 23), b=14.31
alter (resi 24), b=11.78
alter (resi 25), b=13.59
alter (resi 26), b=0.00
alter (resi 27), b=0.32
alter (resi 28), b=0.01
alter (resi 29), b=24.98
alter (resi 30), b=37.55
alter (resi 31), b=17.10
alter (resi 32), b=19.13
alter (resi 33), b=41.95
alter (resi 34), b=56.03
alter (resi 35), b=59.17
alter (resi 36), b=60.39
alter (resi 37), b=67.79
alter (resi 38), b=70.59
alter (resi 39), b=92.07
alter (resi 40), b=100.00
alter (resi 41), b=81.65
alter (resi 42), b=68.15
alter (resi 43), b=71.53
alter (resi 44), b=69.79
alter (resi 45), b=66.46
alter (resi 46), b=57.83
alter (resi 47), b=44.50
alter (resi 48), b=41.56
alter (resi 49), b=58.35
alter (resi 50), b=64.44
alter (resi 51), b=58.44
alter (resi 52), b=53.28
alter (resi 53), b=53.48
alter (resi 54), b=32.26
alter (resi 55), b=53.57
alter (resi 56), b=37.11
alter (resi 57), b=45.37
alter (resi 58), b=42.79
alter (resi 59), b=49.37
alter (resi 60), b=44.14
alter (resi 61), b=46.92
alter (resi 62), b=24.05
alter (resi 63), b=27.58
alter (resi 64), b=39.50
alter (resi 65), b=64.16
alter (resi 66), b=47.96
alter (resi 67), b=59.06
alter (resi 68), b=82.08
alter (resi 69), b=49.11
alter (resi 70), b=63.69
alter (resi 71), b=31.34
alter (resi 72), b=44.57
alter (resi 73), b=13.48
alter (resi 74), b=26.17
alter (resi 75), b=34.08
alter (resi 76), b=28.33
alter (resi 77), b=22.38
alter (resi 78), b=32.47
alter (resi 79), b=58.75
alter (resi 80), b=42.88
alter (resi 81), b=44.74
alter (resi 82), b=34.40
alter (resi 83), b=28.56
alter (resi 84), b=19.57
alter (resi 85), b=7.48
alter (resi 86), b=8.00
alter (resi 87), b=7.61
alter (resi 88), b=17.35
alter (resi 89), b=15.17
alter (resi 90), b=12.85
alter (resi 91), b=20.32
alter (resi 92), b=22.61
alter (resi 93), b=22.24
alter (resi 94), b=33.79
alter (resi 95), b=36.43
alter (resi 96), b=23.54
alter (resi 97), b=23.46
alter (resi 98), b=49.31
alter (resi 99), b=55.19
spectrum b, blue_white_red, minimum=0, maximum=100
select top_gears, resi 16+17+18+21+38+39+40+41+43+68
show sticks, top_gears
set stick_radius, 0.3
color yellow, top_gears
orient
set cartoon_transparency, 0.1
bg_color white
