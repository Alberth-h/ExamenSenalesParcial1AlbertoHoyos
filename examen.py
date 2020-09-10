import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate


frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia941 = SinSignal(freq=941, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

#para el 2
wave_697_2 = frecuencia697.make_wave(duration=1, start=0, framerate=44100)
wave_1336_2 = frecuencia1336.make_wave(duration=1, start=0, framerate=44100)

#para el 3
wave_697_3 = frecuencia697.make_wave(duration=1, start=1, framerate=44100)
wave_1477_3 = frecuencia1477.make_wave(duration=1, start=1, framerate=44100)

#para el 8
wave_852_8 = frecuencia852.make_wave(duration=1, start=2, framerate=44100)
wave_1336_8 = frecuencia1336.make_wave(duration=1, start=2, framerate=44100)

#para el 0
wave_941_0 = frecuencia941.make_wave(duration=1, start=3, framerate=44100)
wave_1336_0 = frecuencia1336.make_wave(duration=1, start=3, framerate=44100)


wave_sonido2 = wave_697_2 + wave_1336_2
wave_sonido3 = wave_697_3 + wave_1477_3
wave_sonido8 = wave_852_8 + wave_1336_8
wave_sonido0 = wave_941_0 + wave_1336_0

wave_sonido = wave_sonido2 + wave_sonido3 + wave_sonido8 + wave_sonido0

wave_sonido.write("output.wav")