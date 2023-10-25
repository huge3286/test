## backbone 对比

1. unet + 注意力机制  
注意力模块消耗了90%的计算量
效果较好

2. resnet  
对于一般攻击的效果很好 但是还是不能抗拍照

3. MobileNetV3  
单纯的mobilenet的效果并不好

4. Convnextv2  
效果与Mobilnet并无区别 Convnext是用了大卷积核结构 但没有更好的结果 这应该怎么解释呢  
也许是卷积核还不够大 再看看论文

## 分析
1. 猜测一 使用大卷积核的注意力模块效果很好
    - 可以用带噪声和无噪声的图分别推理一遍 对比推理中间变量的差异从而可以分析出是哪个部分鲁棒性更好

2. 

## 工作计划
1. 试试 ConvnextV2-base
2. 试试 RepLKNet
3. 试试 robust-resnet
    https://github.com/UCSC-VLAA/RobustCNN/blob/main/timm/models/robust_resnet.py
