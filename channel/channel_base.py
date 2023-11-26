from abc import ABC, abstractclassmethod
import logging

from constants import light_speed


class PropagationChannelBase(ABC):
    def __init__(self, fs, fc, **unused_kwargs):
        '''
        :fs: - sampling frequency, Hz
        :fc: - carrier frequency, Hz

        '''
        self.fs = fs
        self.lam = fs / light_speed
        self.fc = fc
        for name, val in unused_kwargs.items():
            logging.warning(f"Unused parameter: (name={name} value={val})")

    @abstractclassmethod
    def process(self, tx_singal, distance, radial_speed):
        pass
