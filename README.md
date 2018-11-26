# captcha_check
# author: DYBOY

### 项目简介：
利用 `captcha` 库生成的图形验证码，并对其进行内容识别。首先通过对验证码图片进行一个“`灰度`”处理，使之变为灰度图，灰度图有利于去除杂色，便于提高模型精度，提升训练速度。训练过程中，使用了`三层CNN`，最终的准确率最高可达到`98.75%`


### 运行环境：
- python3.6
- tensorflow 1.10 (运行时，缺少什么就安装对应包 例如安装tensorflow：pip3 install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple )
- windows 10 家庭版


### USAGE:
- 训练模型：python3 model_train.py
- 测试模型：python3 model_test.py

### 效果：

[![预测](https://upload-images.jianshu.io/upload_images/6661013-0740ed1f4da0e286.png "预测")](https://upload-images.jianshu.io/upload_images/6661013-0740ed1f4da0e286.png "预测")

### 项目介绍文章地址：
- https://blog.dyboy.cn/program/100.html
	

### 训练过程记录：

``` shell
[root@VM_96_17_centos captcha]# /usr/local/bin/python3.6 model_train.py 
2018-11-26 09:29:57.038117: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2018-11-26 09:29:57.408852: W tensorflow/core/framework/allocator.cc:122] Allocation of 41943040 exceeds 10% of system memory.
2018-11-26 09:29:57.451278: W tensorflow/core/framework/allocator.cc:122] Allocation of 41943040 exceeds 10% of system memory.
2018-11-26 09:29:57.498523: W tensorflow/core/framework/allocator.cc:122] Allocation of 41943040 exceeds 10% of system memory.
2018-11-26 09:29:57.525206: W tensorflow/core/framework/allocator.cc:122] Allocation of 41943040 exceeds 10% of system memory.
2018-11-26 09:29:57.566340: W tensorflow/core/framework/allocator.cc:122] Allocation of 41943040 exceeds 10% of system memory.
Mon Nov 26 09:30:03 2018  step: 0  accuracy: 0.1
Mon Nov 26 09:33:47 2018  step: 100  accuracy: 0.1175
Mon Nov 26 09:37:29 2018  step: 200  accuracy: 0.1
Mon Nov 26 09:41:11 2018  step: 300  accuracy: 0.095
Mon Nov 26 09:44:53 2018  step: 400  accuracy: 0.1
Mon Nov 26 09:48:32 2018  step: 500  accuracy: 0.105
Mon Nov 26 09:52:11 2018  step: 600  accuracy: 0.0575
Mon Nov 26 09:55:50 2018  step: 700  accuracy: 0.09
Mon Nov 26 09:59:30 2018  step: 800  accuracy: 0.105
Mon Nov 26 10:03:10 2018  step: 900  accuracy: 0.085
Mon Nov 26 10:06:50 2018  step: 1000  accuracy: 0.0875
Mon Nov 26 10:10:31 2018  step: 1100  accuracy: 0.09
Mon Nov 26 10:14:11 2018  step: 1200  accuracy: 0.08
Mon Nov 26 10:17:51 2018  step: 1300  accuracy: 0.0825
Mon Nov 26 10:21:31 2018  step: 1400  accuracy: 0.135
Mon Nov 26 10:25:11 2018  step: 1500  accuracy: 0.18
Mon Nov 26 10:28:51 2018  step: 1600  accuracy: 0.31
Mon Nov 26 10:32:31 2018  step: 1700  accuracy: 0.4225
Mon Nov 26 10:36:09 2018  step: 1800  accuracy: 0.4625
Mon Nov 26 10:39:49 2018  step: 1900  accuracy: 0.4925
Mon Nov 26 10:43:28 2018  step: 2000  accuracy: 0.5475
Mon Nov 26 10:47:07 2018  step: 2100  accuracy: 0.58
Mon Nov 26 10:50:46 2018  step: 2200  accuracy: 0.6725
Mon Nov 26 10:54:25 2018  step: 2300  accuracy: 0.69
Mon Nov 26 10:58:06 2018  step: 2400  accuracy: 0.735
Mon Nov 26 11:01:46 2018  step: 2500  accuracy: 0.735
Mon Nov 26 11:05:27 2018  step: 2600  accuracy: 0.745
Mon Nov 26 11:09:07 2018  step: 2700  accuracy: 0.825
Mon Nov 26 11:12:46 2018  step: 2800  accuracy: 0.7675
Mon Nov 26 11:16:26 2018  step: 2900  accuracy: 0.8425
Mon Nov 26 11:20:05 2018  step: 3000  accuracy: 0.825
Mon Nov 26 11:23:43 2018  step: 3100  accuracy: 0.855
Mon Nov 26 11:27:23 2018  step: 3200  accuracy: 0.8425
Mon Nov 26 11:31:02 2018  step: 3300  accuracy: 0.8375
Mon Nov 26 11:34:41 2018  step: 3400  accuracy: 0.8575
Mon Nov 26 11:38:20 2018  step: 3500  accuracy: 0.8475
Mon Nov 26 11:41:59 2018  step: 3600  accuracy: 0.8775
Mon Nov 26 11:45:38 2018  step: 3700  accuracy: 0.8825
Mon Nov 26 11:49:17 2018  step: 3800  accuracy: 0.9025
Mon Nov 26 11:52:57 2018  step: 3900  accuracy: 0.8625
Mon Nov 26 11:56:37 2018  step: 4000  accuracy: 0.92
Mon Nov 26 12:00:17 2018  step: 4100  accuracy: 0.8925
Mon Nov 26 12:03:56 2018  step: 4200  accuracy: 0.9075
Mon Nov 26 12:07:35 2018  step: 4300  accuracy: 0.91
Mon Nov 26 12:11:15 2018  step: 4400  accuracy: 0.92
Mon Nov 26 12:14:54 2018  step: 4500  accuracy: 0.915
Mon Nov 26 12:18:36 2018  step: 4600  accuracy: 0.9275
Mon Nov 26 12:22:16 2018  step: 4700  accuracy: 0.9375
Mon Nov 26 12:25:56 2018  step: 4800  accuracy: 0.905
Mon Nov 26 12:29:36 2018  step: 4900  accuracy: 0.915
Mon Nov 26 12:33:17 2018  step: 5000  accuracy: 0.945
Mon Nov 26 12:36:56 2018  step: 5100  accuracy: 0.9475
Mon Nov 26 12:40:35 2018  step: 5200  accuracy: 0.9375
Mon Nov 26 12:44:15 2018  step: 5300  accuracy: 0.9675
Mon Nov 26 12:47:57 2018  step: 5400  accuracy: 0.945
Mon Nov 26 12:51:37 2018  step: 5500  accuracy: 0.96
Mon Nov 26 12:55:16 2018  step: 5600  accuracy: 0.93
Mon Nov 26 12:58:56 2018  step: 5700  accuracy: 0.9
Mon Nov 26 13:02:36 2018  step: 5800  accuracy: 0.9425
Mon Nov 26 13:06:15 2018  step: 5900  accuracy: 0.9275
Mon Nov 26 13:09:54 2018  step: 6000  accuracy: 0.9225
Mon Nov 26 13:13:34 2018  step: 6100  accuracy: 0.945
Mon Nov 26 13:17:13 2018  step: 6200  accuracy: 0.945
Mon Nov 26 13:20:52 2018  step: 6300  accuracy: 0.9475
Mon Nov 26 13:24:32 2018  step: 6400  accuracy: 0.9675
Mon Nov 26 13:28:13 2018  step: 6500  accuracy: 0.95
Mon Nov 26 13:31:51 2018  step: 6600  accuracy: 0.9375
Mon Nov 26 13:35:30 2018  step: 6700  accuracy: 0.9475
Mon Nov 26 13:39:09 2018  step: 6800  accuracy: 0.95
Mon Nov 26 13:42:49 2018  step: 6900  accuracy: 0.96
Mon Nov 26 13:46:29 2018  step: 7000  accuracy: 0.955
Mon Nov 26 13:50:09 2018  step: 7100  accuracy: 0.9425
Mon Nov 26 13:53:48 2018  step: 7200  accuracy: 0.9625
Mon Nov 26 13:57:27 2018  step: 7300  accuracy: 0.94
Mon Nov 26 14:01:10 2018  step: 7400  accuracy: 0.97
Mon Nov 26 14:04:52 2018  step: 7500  accuracy: 0.9675
Mon Nov 26 14:08:31 2018  step: 7600  accuracy: 0.9575
Mon Nov 26 14:12:11 2018  step: 7700  accuracy: 0.96
Mon Nov 26 14:15:51 2018  step: 7800  accuracy: 0.9425
Mon Nov 26 14:19:31 2018  step: 7900  accuracy: 0.965
Mon Nov 26 14:23:11 2018  step: 8000  accuracy: 0.9725
Mon Nov 26 14:26:51 2018  step: 8100  accuracy: 0.9825
Mon Nov 26 14:30:32 2018  step: 8200  accuracy: 0.975
Mon Nov 26 14:34:11 2018  step: 8300  accuracy: 0.9625
Mon Nov 26 14:37:49 2018  step: 8400  accuracy: 0.9775
Mon Nov 26 14:41:29 2018  step: 8500  accuracy: 0.955
Mon Nov 26 14:45:09 2018  step: 8600  accuracy: 0.9675
Mon Nov 26 14:48:47 2018  step: 8700  accuracy: 0.96
Mon Nov 26 14:52:27 2018  step: 8800  accuracy: 0.9625
Mon Nov 26 14:56:06 2018  step: 8900  accuracy: 0.9525
Mon Nov 26 14:59:45 2018  step: 9000  accuracy: 0.9575
Mon Nov 26 15:03:24 2018  step: 9100  accuracy: 0.9675
Mon Nov 26 15:07:02 2018  step: 9200  accuracy: 0.9725
Mon Nov 26 15:10:41 2018  step: 9300  accuracy: 0.9575
Mon Nov 26 15:14:19 2018  step: 9400  accuracy: 0.97
Mon Nov 26 15:17:57 2018  step: 9500  accuracy: 0.9775
Mon Nov 26 15:21:36 2018  step: 9600  accuracy: 0.9775
Mon Nov 26 15:25:14 2018  step: 9700  accuracy: 0.97
Mon Nov 26 15:28:53 2018  step: 9800  accuracy: 0.98
Mon Nov 26 15:32:32 2018  step: 9900  accuracy: 0.9825
Mon Nov 26 15:36:10 2018  step: 10000  accuracy: 0.9775
Mon Nov 26 15:39:48 2018  step: 10100  accuracy: 0.97
Mon Nov 26 15:43:26 2018  step: 10200  accuracy: 0.9575
Mon Nov 26 15:47:05 2018  step: 10300  accuracy: 0.9625
Mon Nov 26 15:50:42 2018  step: 10400  accuracy: 0.9675
Mon Nov 26 15:54:21 2018  step: 10500  accuracy: 0.9725
Mon Nov 26 15:57:59 2018  step: 10600  accuracy: 0.9825
Mon Nov 26 16:01:39 2018  step: 10700  accuracy: 0.9825
Mon Nov 26 16:05:18 2018  step: 10800  accuracy: 0.985
Mon Nov 26 16:08:57 2018  step: 10900  accuracy: 0.9625
Mon Nov 26 16:12:38 2018  step: 11000  accuracy: 0.965
Mon Nov 26 16:16:18 2018  step: 11100  accuracy: 0.97
Mon Nov 26 16:19:58 2018  step: 11200  accuracy: 0.9875
Mon Nov 26 16:23:37 2018  step: 11300  accuracy: 0.98
Mon Nov 26 16:27:17 2018  step: 11400  accuracy: 0.9625
Mon Nov 26 16:30:58 2018  step: 11500  accuracy: 0.975
Mon Nov 26 16:34:39 2018  step: 11600  accuracy: 0.985
Mon Nov 26 16:38:18 2018  step: 11700  accuracy: 0.9775
Mon Nov 26 16:41:58 2018  step: 11800  accuracy: 0.9825
Mon Nov 26 16:45:38 2018  step: 11900  accuracy: 0.98
Mon Nov 26 16:49:18 2018  step: 12000  accuracy: 0.9825
Mon Nov 26 16:52:57 2018  step: 12100  accuracy: 0.985
Mon Nov 26 16:56:36 2018  step: 12200  accuracy: 0.98
Mon Nov 26 17:00:15 2018  step: 12300  accuracy: 0.9725
Mon Nov 26 17:03:54 2018  step: 12400  accuracy: 0.955
Mon Nov 26 17:07:35 2018  step: 12500  accuracy: 0.97
Mon Nov 26 17:11:14 2018  step: 12600  accuracy: 0.9775
Mon Nov 26 17:14:53 2018  step: 12700  accuracy: 0.985
...
```
