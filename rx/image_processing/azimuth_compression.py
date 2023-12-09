from abc import ABC, abstractclassmethod
from dataclasses import dataclass

import numpy as np
from scipy.signal import correlate

from constants import light_speed


class AzimuthCompressor(ABC):

    def __init__(self, **unused_args):
        super().__init__(**unused_args)

    @abstractclassmethod
    def process(
            self,
            range_compressed_signal: np.array,
            image: np.array) -> np.array:
        pass


@dataclass(frozen=True)
class ConvolutionAzimuthCompressorParams:
    strobe: np.array


class ConvolutionAzimuthCompressor(AzimuthCompressor):

    def __init__(self, params: ConvolutionAzimuthCompressorParams):

        super().__init__()
        self.__generate_azimuth_reference()

    def process(
            self,
            range_compressed_signal: np.array,
            image: np.array) -> np.array:

        azimuth_bin, rx_len = range_compressed_signal.shape
        for idx in range(rx_len):
            image[::, idx] = correlate(
                image[::, idx], self.azimuth_ref[::, idx], mode='same')

        return image

    def __generate_azimuth_reference(self):

        range_bins = (np.arange(rx_start, rx_start +
                      rx_len) + .5) / fs * light_speed
        Y0 = (np.arange(0, azimuth_base) - azimuth_base // 2) * lam / 4
        range_diff = np.zeros((azimuth_base, rx_len))
        for idx, y0 in enumerate(Y0):
            range_diff[idx, ::] = np.sqrt(range_bins**2 + y0**2) - X0
        self.azimuth_ref = np.exp(2j * np.pi * range_diff / lam)
