#coding=utf-8
'''
Mnsit原始数据集为字符格式，将数据集转换为cvs格式，
后续代码都会在cvs文件的基础上进行编写，这样大家看代码也能清楚很多
代码由以下网址提供，表示感谢。
https://pjreddie.com/projects/mnist-in-csv/

该py文件属于一个补充，不使用也不影响后续算法的实践。
转换后的CVS文件在Mnist文件夹中
'''
def convert(imgf, labelf, outf, n):
    with open(imgf, "rb") as f:
        o = open(outf, "w")
        l = open(labelf, "rb")

        f.read(16)
        l.read(8)
        images = []

        for _ in range(n):
            image = [ord(l.read(1))]
            image.extend(ord(f.read(1)) for _ in range(28*28))
            images.append(image)

        for image in images:
            o.write(",".join(str(pix) for pix in image)+"\n")
    o.close()
    l.close()

if __name__ == '__main__':
    convert(".\Mnist\\t10k-images.idx3-ubyte", ".\Mnist\\t10k-labels.idx1-ubyte",
            ".\Mnist\\mnist_test.csv", 10000)
    convert(".\Mnist\\train-images.idx3-ubyte", ".\Mnist\\train-labels.idx1-ubyte",
            ".\Mnist\mnist_train.csv", 60000)