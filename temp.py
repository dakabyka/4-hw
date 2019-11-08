import numpy as np
import matplotlib.pyplot as plt

code = np.array([1, 1, 1, -1, 1], dtype=np.int8)

length = 3 #в дз 5

code_signal = np.repeat(code, length)
#plt.plot(np.concatenate([code_signal, -code_signal]), 'x') #посылаем 1 и -1
plt.grid()

# 1 -> 1, -1 -> 0

def str2bits(s):
    byte_str = s.encode(encoding='ascii')
    byte_array = np.frombuffer(byte_str, dtype=np.uint8)
    bits = np.unpackbits(byte_array)
    return bits

print(str2bits('a'), list(b'a'))

def bits2signal(bits):
    data = 2 * np.asarray(bits, dtype=float) - 1
    return np.outer(data, code_signal).reshape(-1) #внешнее произведение

def func(signal, sigma=1):
    obs = signal + np.random.normal(scale=sigma, size=signal.size)
    return obs
def decode(y):
    conv = np.convolve(y, code_signal[::-1], mode='same')
    return conv

bits = str2bits('a')
signal = bits2signal(bits)
y = func(signal, sigma=1)
decoded = decode(y)
print(y)
plt.plot(decoded, label='convolved')
plt.plot(y, label='obs')
plt.legend()
#plt.figure()
#plt.plot(np.convolve(code_signal, code_signal[::-1], mode='full'))

#достать биты из свернутого сигнала

def bit2str(bits):
    bits = np.asarray(bits, dtype=np.uint8)
    byte_array = np.packbites(bits)
    byte_str = byte_array.tobytes()
    s = byte_str.decode(encoding='ascii')
    return s
