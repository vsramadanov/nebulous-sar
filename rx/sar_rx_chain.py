import importlib
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class RxChainParams:
    strobe: np.array
    range_compressor: dict
    azimuth_compressor: dict
    noise_figure: float
    noise_temperature: float


class RxChain:

    def __init__(self, params: RxChainParams) -> None:

        self.params = params

        range_compressor_lib = importlib.import_module(
            'image_processing.range_compressor')
        azimuth_compressor_lib = importlib.import_module(
            'image_processing.azimuth_compressor')

        range_compressor_type = getattr(
            range_compressor_lib, params.range_compressor['type'])
        azimuth_compressor_type = getattr(
            azimuth_compressor_lib, params.azimuth_compressor['type'])

        self.range_compressor = range_compressor_type(
            params.range_compressor['args'])
        self.azimuth_compressor = azimuth_compressor_type(
            params.azimuth_compressor['args'])

    def process(self, delays: np.array, echos: np.array):

        strobe = self.params.strobe
        rx_signal = np.zeros(strobe[1] - strobe[0])

        num_echos, echo_len = echos.shape
        for idx in range(num_echos):
            echo = echos[idx, ::]
            delay = delays[idx]
            end = min(delay + echo_len, strobe[1])
            rx_signal[idx, delay:end] = rx_signal[idx, delay:end] + echo

        # TODO: add receiver noise

        # Image processing
