# test
only for test

# 目标拆解

## 应付检查
1. 制作webUI  
    - streamlit
2. 转 ONNX -> tensorrt  
    - torch.onnx.export

## 提升检测准确率
1. 新的噪声模型
2. 鲁棒性更好的模型


## 提升检测速度
1. 轻量化的BackBone（水印模型+关键点检测模型）


# 工作计划
1. 测试新的噪声模型
2. 设计一个大卷积核+轻量化的Backbone提升模型鲁棒性
3. 训练后量化 提升推理速度
4. tensorrt部署 c++封装成SDK
