# AdventofCode2023
Advent 2023

Day 1:

Straight forward for part 1, part 2 required realizing that reading comprehension is hard and overlapping numbers still parse correctly sevenine = 79 and not 7ine

Day 2:

Mostly a Parsing problem, how well can you parse the input and keep track.  Use RE again.

Day 3:

brute forcing part 2 as you can iterate the valid configurations <- Dumb way to do it
already parsed the numbers and know the numbers next to gear, just track the gears with exactly two numbers. Duh.

Day 4:

That's a lot of scratchers, just multiply loop through to count.

Day 5:

Need to calculate intervals

Day 6:

Gimme problem, super easy and can brute force, even though it's parabolas calculations.  Could have done half the work once you found the peak.  Oh yeah, learned to use python's progressbar2 for fancy graphics.  https://medium.com/pythoniq/progress-bars-in-python-with-progressbar2-da77838077a9

Day 7:

Use classes that's it.  Straight forward

Day 8:

Use Linked lists mostly.  Step 2, figure out distances of all starts A to stops Z and find Least common multiple of the distances.

Day 9:

Python list.append does all the work as well as [::-1]

Day 10:

Numpy abuse, need to implement ray tracing algorithm for each [y, x] count transitions between bounderies, odd = inside, even = outside we're in a closed loop.


Day 11:

Spent time implementing galaxy expansion with numpy and np.insert.  Threw it all away for part2 to just implement fancy manhatten distance.  Calculate crossings and then just subtract the crossings from abs(x1-x2) and multiply it by galaxy crossing expansion coefficient.


Unfinished:


Day 5 part 2, need to write the range class to track ranges