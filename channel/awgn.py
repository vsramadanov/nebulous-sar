import numpy as np

from constants import light_speed
from .channel_base import PropagationChannelBase


class AwgnChannel(PropagationChannelBase):
    def __init__(self, noise_psd, **other_args):
        '''
        :noise_psd: noise power spectrum density, V/Hz

        '''
        super().__init__(**other_args)
        self.noise_psd = noise_psd

    def process(self, tx_singal, range, radial_speed) -> (int, np.array):
        '''
        :tx_signal: transmitted signal
        :range: distance from radar to target, m
        :radial_speed: radial target speed, m/s

        returns:

        '''
        samples_offset = int(np.floor(2 * range / light_speed * self.fs))

        range_offset = samples_offset / self.fs * light_speed
        phase_offset = 2 * np.pi * (2 * range - range_offset) / self.lam
        phase_rotator = np.exp(-1j * phase_offset)

        fading_factor = 1 / range ** 4

        sigma = self.noise_psd * self.fs

        return samples_offset, tx_singal * fading_factor * phase_rotator \
            + sigma * np.random.randn(*tx_singal.shape)
