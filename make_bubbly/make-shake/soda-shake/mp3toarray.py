# -*- coding: utf-8 -*-
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

# 音楽データの読み込み
sound = AudioSegment.from_file("soda-sound.mp3", "mp3")

# NumPy配列に返還
data = np.array(sound.get_array_of_samples())

# ステレオ音声から片方を抽出
x = data[::sound.channels]

print(x)

'''# グラフ化
plt.plot(x[50000:250000])
plt.grid()
plt.show()'''

np.save("soda-array",x[50000:250000],fix_imports=True)
