#GovRptWordCloudv2.py
import jieba
import wordcloud
import imageio
#from scipy.misc import imread
mask = imageio.imread("E:/pythontest/chapter7/fivestart.png")
excludes = { }
f = open("E:/pythontest/chapter7/关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("grwordcloudm.png")


