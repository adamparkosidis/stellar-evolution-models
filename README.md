# Stellar Evolution models using MESA

## Description

This is end extended analysis of stellar evolution models. In this project we create models of different mass and analyse the key points of their evolution.
There is an extended analysis in `Stellar_evolution_and structere_MESA_project.pdf` which aims to explain the underling physics and mechanisms that govern the evolution of single stars in the mass regime of interest.

## [MESA](https://docs.mesastar.org/en/release-r22.05.1/) 

To produce the data contained in /workplace/runs  [MESA Release 12778](https://zenodo.org/record/3698354#.Y1KO6vxBxH4) and [MESA SDK](http://user.astro.wisc.edu/~townsend/static.php?ref=mesasdk#Download) were used. There are [Other dependencies](http://user.astro.wisc.edu/~townsend/static.php?ref=mesasdk#Linux_.01Intel.01)  necessary for the code to run properly. Finally [mesaPlot](https://github.com/rjfarmer/mesaplot) is used to read MESA ouput files  

How to: [Install the MESASDK](http://www.astro.wisc.edu/~townsend/static.php?ref=mesasdk#Installation) and [MESA install instructions](http://mesa.sourceforge.net/prereqs.html#set-your-environment-variables)



## Code Overview

1) Time evolution of the central abundances for a massive star

We compute a MESA model of a $15 M_{\odot}$ star and probe the evolution until the end of helium burning. We plot:

1. The central H and He mass fraction as a function of time for the duration of the main sequence and comment on your plot.

2. The central C, N & O mass fraction as a function of time for the duration of the main sequence and comment on your plot.

Note that H, He, C and O are standard outputs, but we add N.

3. The central He, C, and O abundance as a function of time zooming in on the central helium burning phase and comment on your plot.


2) A Hertzsprung-Russell diagram from 1 to 12 $M_{\odot}$ We pick five masses M = [12, 7, 5, 3, 1] $M_{\odot}$ with solar metallicity. We evolve these models until they reach the end of the main sequence.
We:

1. Plot the evolutionary track in an Hertzsprung-Russel diagram (excluding the pre-main sequence). We also, add lines of constant radii in fractions of R⊙.

2. We explain what a Hertzsprung-Russell diagram is. We pick ick at least one of our chosen masses and a compute it again at Z/Z⊙ = 0.01, add it/them to the plot, and 
explain qualtatively why there are differences between stars at $Z/Z_{\odot} = 1$ and $Z/Z_{\odot} = 0.01$.

3. Pick one of the five masses (we picked the one with $M=5 M_{\odot}) and we evolve that system again, but now until the end of core helium burning. We make a new Hertzsprung-Russel diagram and add labels to mark key features in the evolutionary tracks. We include the following

(a) Start of H burning (or zero-age main sequence)
(b) End of the main sequence (as marked by the start of the overall contraction at the end of central H burning)
(c) Onset of H-shell burning
(d) The location where the star starts to ascend the giant branch
(e) Central ignition of helium burning
(f) The location where the star spends most of the helium burning phase
(g) Central exhaustion of helium.
(h) End of the evolutionary track. Note that the end of the evolutionary track probably coincides
with the central exhausting of helium.

4. Apart from the pre-main sequence contraction, there are two other phases where the star contracts. We analyse these phases.

5. The Main sequence spans from A-B. We indicate the letters (from the previous question) that mark the following phases:

(a) Evolution across the Hertzsprung gap
(b) Ascend of the (first) giant branch
(c) blue loop
(d) Ascend of the Asymptotic Giant Branch

7. We stopped the track at central helium exhaustion. We also speculate how will the evolution of a star of this mass
continue andt its final.


3) Evolution in the central temperature - density plane. Another very important diagnostic diagram is the (central) temperature - density plane.
We:

1. Evolve a 15 $M_{\odot}$ and plot the central temperature versus the central density in a log-log plot.

2. Plot the approximate boundary lines between regions where

(a) radiation pressure dominates
(b) electrons behave like a classical ideal gas
(c) electrons behave line a degenerate gas
(d) electrons behave relativistic degenerate gas.

3. Mark on the track where (a) central hydrogen burning is taking place. (b) central helium burning
is taking place. 

4. Discuss if the center of the star is degenerate when H ignites in the center, when He ignites in the center or if the center of the star is ever degenerate
