import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

t= np.arange(393221)
value = np.fromfile('value.dat',dtype=float)
fourier1 = np.fft.ifft(value)
plt.plot(t, fourier1.real, 'b-', t, fourier1.imag, 'r--')



plt.legend(('real', 'imaginary'))
plt.show()

print value
print fourier1
#fourier = Image.fromarray(value.astype('uint8'))
#fourier.show()
