from scipy import signal
import numpy as np


def get_plot_data(fs_hz, number_coeffs, f_low_hz, f_high_hz, rp, rs, f_type, design):
    if f_type == 'lowpass':
        Wn = f_low_hz
    elif f_type == 'highpass':
        Wn = f_high_hz
    else:
        Wn = [f_low_hz, f_high_hz]
    if design not in ['cheby1', 'cheby2', 'ellip']:
        rp = None
        rs = None
    b, a = signal.iirfilter(number_coeffs,
                            Wn,
                            rp=rp,
                            rs=rs,
                            btype=f_type,
                            ftype=design,
                            output='ba',
                            fs=fs_hz)
    worN = np.logspace(0, 4, num=1024)*(fs_hz/2)/1e4
    frequency_hz, h = signal.freqz(b, a,
                                   worN=worN,
                                   fs=fs_hz,
                                   include_nyquist=False)
    _, gd_samples = signal.group_delay((b, a),
                                       w=worN,
                                       fs=fs_hz)
    amplitude_dB = 20 * np.log10(abs(h))
    angle_deg = np.unwrap(np.angle(h))*(180/np.pi)
    return frequency_hz, amplitude_dB, angle_deg, gd_samples
