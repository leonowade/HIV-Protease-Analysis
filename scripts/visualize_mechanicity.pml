# 1. Load the mapped PDB file
load results/1hhp_mechanicity_mapped.pdb

# 2. Make it look professional
bg_color white
show cartoon
hide lines

# 3. Apply the Mechanicity Heatmap
# Everything red is a high-flex, low-mutation "Gear"
spectrum b, blue_white_red, minimum=10, maximum=400

# 4. Highlight the "Master Gears" (Flaps and Hinges)
# Tips: 48-52, Hinges: 38-42
select gears, resi 38-42+48-52
show sticks, gears
set stick_radius, 0.2
color yellow, gears

# 5. Add a surface for a professional look
# We'll make it transparent so we can see the "skeleton" inside
set transparency, 0.5
show surface

# 6. Set the view for the best angle
orient