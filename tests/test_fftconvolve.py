from pydevtips.fftconvolve import RFFTConvolve, FFTConvolve
import numpy as np


# create random signal
n = 1000
signal = np.random.randn(n)

# create filter
filter = np.random.randn(n)

# reference output
fft_naive = np.convolve(signal, filter, mode="full")


def test_rfft():

    # create object
    rfft_convolver = RFFTConvolve(filter=filter, length=len(signal))

    # convolve
    rfft_out = rfft_convolver(signal)

    # check results
    assert np.allclose(rfft_out, fft_naive)


def test_fft():

    # create object
    fft_convolver = FFTConvolve(filter=filter, length=len(signal))

    # convolve
    fft_out = fft_convolver(signal)

    # check results
    assert np.allclose(fft_out, fft_out)
