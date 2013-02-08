#-*-coding:utf-8-*-
import sys

input = open(sys.argv[1]).readlines()

#解放のコツは初期値は００で決まりで「今の座標」－「次の座標」をため続けてそれを最後に比較するでいいと思う