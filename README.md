# sunride-avionics-application

Lots of code has been hashed out but left in INTENTIONALLY to show that this was done without AI. This took time with a good couple iterations to fully nail down so I hope you can see the progression and my thought proccess by an actual human.

Coupple of assumptions were made as i produced this code ill try to list all of them here and my rationalle behind some of my choices. You can find mini explainaitions via my comments throughout the code but the overarching descisions as to why ive coded the solution in the way i have will be found here.

1. I chose to code in python because it is by far my best language. I do have experience coding in C and i feel i would have been able to produce a solutin in that language but still chose to do it in python as i feel i can be more succinct and produce a cleaner "higher order" solution in Py.

2. I assumed the data being fed from the sensors was base 10 already converted from binary into thier decimal equivilents. Not entirley sure if i was supposed to make it that way but i hope you can apreciate it showing my ability to convert between different numerical bases even if it wasn't part of the brief.

3. Initially wanted to encode timestamps into the 32 bits and decided to compress the time into 4 bits which would get recycled every 1000ms. Then realised that i could skip the timestamping entirley and rely on the 100ms cadence of the encoding programme.

4. Majority of compression comes from reducing 32bit accel down into 15 bits. I googled what an average range of G's might look like through the course of a flight and figures ranged from 10g-20g. Furthermore i found that most accelerometers give a range of +-16g's so just assumed that as the working range for the acceleration data. Have to accept some loss of precision due to reduction from 32bits --> 15bits but still have abount 3dp of precision with 15 bits between [-16g,+16] so i think it was an acceptable loss.


Thank you hope you like my code!
