from abc import ABC, abstractclassmethod
from dataclasses import dataclass

import numpy as np
from scipy.signal import correlate


class RangeCompressor(ABC):

    def __init__(self, config):
        pass

    @abstractclassmethod
    def process(self, rx_signal: np.array, image: np.array) -> np.array:
        pass


@dataclass(frozen=True)
class ConvolutionRangeCompressorParams:
    reference: np.array


class ConvolutionRangeCompressor(RangeCompressor):

    def __init__(self, params: ConvolutionRangeCompressorParams):
        super().__init__()

    def process(self, rx_signal: np.array, image: np.array) -> np.array:

        azimuth_bin, range_bin = rx_signal.shape
        for idx in range(azimuth_bin):
            image[idx, ::] = correlate(
                rx_signal[idx, ::], self.ref_signal, mode='same')

        return image
