＊音声認識＊

ターミナルで以下を実行

$ cd speech-recognition/sample

$ sudo modprobe snd-pcm-oss

$ julius -C ~/Portable_Drinkbar/speech-recognition/julius-4.4.2/julius-kits/grammar-kit-v4.1/hmm_mono.jconf -nostrip -input mic -gram ~/Portable_Drinkbar/speech-recognition/sample/drink -module &

(これでjuliusサーバーが立ち上がる)

別端末を立ち上げて、speech-recognition/sampleで、

$ python test.py

を実行
