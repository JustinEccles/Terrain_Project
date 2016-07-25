README.TXT
Terrain Generation References:
  http://flafla2.github.io/2014/08/09/perlinnoise.html
  http://zach.in.tu-clausthal.de/teaching/cg2_08/literatur/simplexnoise.pdf
  http://www.decarpentier.nl/scape-procedural-basics
  https://www.reddit.com/r/proceduralgeneration/
  
Blender Reference:
  https://github.com/a1studmuffin/SpaceshipGenerator
  
Poster Resources:
  http://i.stack.imgur.com/NQqLa.jpg
  
  
  Perlin Noise:
  How it Works:

  The algorithm starts with a “seed”, a word or number, and returns a matrix of semi-random values between -1 and 1.
 
  These values flow smoothly between one another that creates a consistent curve when graphed. 

  This is necessary for generating a “height map,” the digital equivalent of a topographical map.
  
  
  
  Examples of Rendered Images:
  Project Description:

  We used an algorithm called Perlin Noise to generate semi-random values. 

  These value are then sent to our custom 2D renderer, that converts lower values into colors associated with oceans and higher values to colors associated with land masses. 

  We can also send the values to a 3D modeling software, such as Blender, and use them to raise or lower points on a mesh to make a 3D model.
  
  
  
  Problems:

  Initially, we could only add values to the first row of our matrix. We quickly discovered we made an error with our counting, so it skipped all rows but the first.

  We tried to implement a heat map created by a sin wave, but the map would have hard cutoffs between colors instead of smooth transitions.
  
  Future Improvements:

  Add a working heat and moisture map to determine different colors for the land masses, such as prairies or mountains with snow peaks.

  Have the program automatically export the matrix to a 3D renderer and construct the mesh without user input.


