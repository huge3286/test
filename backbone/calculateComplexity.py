import torchvision.models as models
import torch
from ptflops import get_model_complexity_info

from replknet import create_RepLKNet31B

with torch.cuda.device(0):
    net = create_RepLKNet31B(small_kernel_merged=False)
    net.eval()
    # net = torch.compile(net)
    macs, params = get_model_complexity_info(net, (3, 224, 224), as_strings=True, print_per_layer_stat=True, verbose=True)
    print("{:<30}  {:<8}".format("Computational complexity: ", macs))
    print("{:<30}  {:<8}".format("Number of parameters: ", params))
