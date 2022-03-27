import numpy as np

def mandelbrot(z_n_minus_one, constant):
    z_n = z_n_minus_one * z_n_minus_one + constant
    return z_n

initial_z = 0 + 0j
iterations = 6
constant = 0.5 + 0.1j

z_n_minus_one = initial_z

for i in range(iterations):
    z_n = mandelbrot(z_n_minus_one, constant)
    print(z_n)
    z_n_minus_one = z_n


complex_numbers = [0.2+0.2j,-0.3+0.2j,-0.6+0.4j,-1.3+0.1j,-1.7+0.1j,0.2-0.2j,-0.3-0.2j,-0.6-0.4j,-1.3-0.1j,-1.7-0.1j]


for item in complex_numbers:
    iterations = 0
    initial_z = 0 + 0j
    constant = item

    z_n_minus_one = initial_z

    while iterations < 100:
        z_n = mandelbrot(z_n_minus_one, constant)

        if np.absolute(z_n) > 100:
            print(iterations)
            break
        else:
            iterations += 1
            z_n_minus_one = z_n

    if iterations == 100:
        print('P')
