
>[!tip] 压缩视频 
>[[视频和音频]]

参考资料 : [FFmpeg压片教程](https://www.bilibili.com/video/BV1sL411x7ix/?spm_id_from=333.337.search-card.all.click&vd_source=036ef261e6800ac6f6a743a8d5dce899)

## 一些视频理论基础 

我们参加的视频格式 例如 mp4 ,kmp 这些都是容器,h264,av1才是视频的编码格式,类似于瓶装可乐和罐装可乐,改变容器并不会改变其内容.所以大部分视频都可以简单的格式转换. 

我们的重点肯定是视频编码格式,因为它才是真正影响视频质量的. 


## 参数解析

| 参数解析 | 参数作用 | example |
| ---- | ---- | ---- |
| -i | input file name |  |
| -vf fps=30,scale=1920:1080 |  |  |
| -c:v libx265 |  |  |

## 常用功能 

| 功能       | 命令                                            | 补充            |
| -------- | --------------------------------------------- | ------------- |
| 提取视频封面   | `ffmpeg -i input.mp4 -frames 1 output.jpg`    | 其实可以将视频转为gif的 |
| 进行H265编码 | `ffmpeg -i input.mp4 -c:v libx265 output.mp4` | 其实就已经足够了不是吗   |

其实使用这里两个基本上就足够了. 


## 惊人的H265 

大部分情况下,我们的h265比h264都要好得多. 
原始画质如何


原始的视频参数 
```c
 Duration: 00:04:44.67, start: 0.000000, bitrate: 2505 kb/s
    Stream #0:0: Video: h264 (High), yuv420p(tv, bt709), 1280x720 [SAR 1:1 DAR 16:9], 30 fps, 30 tbr
, 1k tbn, 60 tbc
```

使用x265编码后的视频参数
```c
  Duration: 00:04:44.67, start: 0.021333, bitrate: 119 kb/s
    Stream #0:0(und): Video: hevc (Main) (hev1 / 0x31766568), yuv420p(tv), 1280x720 [SAR 1:1 DAR 16:
9], 108 kb/s, 30 fps, 30 tbr, 15360 tbn, 30 tbc (default)
```


可以看到码率从原来的 2505kb/s 变成了现在的 119kb/s , 最终的结果就是视频体积从`90MB` 变成了`4.3MB` 体积变成了原来的$\frac{1}{20}$ . 

