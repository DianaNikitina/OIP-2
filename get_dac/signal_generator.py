import numpy as np
import time
 
def get_sin_wave_amplitude(freq, t):
    return (np.sin(2 * np.pi * freq * t) + 1.0) / 2.0
 
def get_triangle_wave_amplitude(freq, t):
    
    period = 1.0 / freq
    phase = (t % period) / period 
    
    
    if phase < 0.5:
        return 2 * phase          
    else:
        return 2 - 2 * phase      
 
def get_sawtooth_wave_amplitude(freq, t):
   
    period = 1.0 / freq
    phase = (t % period) / period
    return phase  
 
def get_meander_wave_amplitude(freq, t):
    
    period = 1.0 / freq
    phase = (t % period) / period
    return 1.0 if phase < 0.5 else 0.0
 
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0 / sampling_frequency)