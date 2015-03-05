# Fermi-Pasta-Ulam Problem
Simulation of the Fermi-Pasta-Ulam problem.

More about this topic at [Wikipedia](https://en.wikipedia.org/wiki/Fermi%E2%80%93Pasta%E2%80%93Ulam_problem)

# Requirements

* numpy
* matplotlib => 1.4.2

If you want to save your animation as a mp4-video you also need to install a moviewriter.
Recommended is 'avconv'.

# It's all about force
In the Fermi-Pasta-Ulam problem non-linear terms in the resilience are examined. The following formular shows the implemented resilience with a quadratic and cubic term. k is always equals 1 and alpha respectivly beta can be changed manually in the program.

![force](http://www.sciweavers.org/tex2img.php?eq=F%20%3D%20k%20%28%20%5CDelta%20x_1%20-%20%20%5CDelta%20x_2%20%29%20%2B%20%20%5Calpha%20%28%20%5CDelta%20x_1%5E2%20-%20%20%5CDelta%20x_2%5E2%20%29%20%2B%20%20%5Cbeta%20%28%20%5CDelta%20x_1%5E3%20-%20%20%5CDelta%20x_2%5E3%20%29%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

If you want to have a non-harmonic force, just set alpha or beta to a value > 0

# Example
Here is one example with Alpha = 0 and Beta = 0.3

![init_mode=1](https://raw.githubusercontent.com/libeanim/fpu-problem/master/example/im_a0_b0.3_1.gif)

The [mp4-video](https://raw.githubusercontent.com/libeanim/fpu-problem/master/example/im_a0_b0.3_1.mp4) is much more fluent.

# Troubleshoot
You need an up-to-date matplotlib package! In Linux the ffmpg library is depricated and libav (avconv) is used instead. Former matplotlib versions may have some problems with this.

(This only affects saving your animation in a mp4 file. The live animation should work anyways)
