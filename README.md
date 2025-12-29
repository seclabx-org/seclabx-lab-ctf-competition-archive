# CTF 比赛复现规范

📁 目录命名  
- 比赛目录：`比赛名+年份`（例：LilCTF2025）  
- 题目目录：`类型-名称`（例：web-one-job / misc-png-master / blockchain-treasure）

> 题目目录名称届时会作为镜像名称，要方便分类

📄 比赛目录必须包含：  
`README.md`（写清：比赛来源 + 原仓库链接 + 可公开 WP 链接），`最好是每道题能够追溯到公开的wp`

⚠️ 注意  
- 只收录公开题  
- 尊重原作者要求，如需声明来源或其他要求请写在 README 中

例如：

```
LilCTF2025
├── README.md # 比赛级 README（来源说明、原仓库、WP 总览）
├── web-one-job
│ ├── 题目描述.md # 题目描述（md 格式，可直接复制到平台，静态附件题需要附上flag）
│ ├── 附件/xxx.php # 静态附件题需要
│ ├── src/ # 源码 / 部署
│ └── ...
├── misc-png-master
│ ├── 题目描述.md
│ └── ...
└── blockchain-treasure
├── 题目描述.md
└── ...
```

