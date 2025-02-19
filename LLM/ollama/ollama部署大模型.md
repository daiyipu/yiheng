# ollama 部署大模型
## windows部署方法
1. 加速下载：https://gh.api.99988866 xyz/
2. 下载地址：https://github.com/ollama
推荐用google下载
3. 下载完windows直接安全就行：ollama run deepseek-r1
4. 其他ollama的命令
ollama serve # 启动ollama
ollama create # 从模型文件创建模型
ollama show  # 显示模型信息
ollama run  # 运行模型，会先自动下载模型
ollama pull  # 从注册仓库中拉取模型
ollama push  # 将模型推送到注册仓库
ollama list  # 列出已下载模型
ollama ps  # 列出正在运行的模型
ollama cp  # 复制模型
ollama rm  # 删除模型

## 远程linux部署
curl -fsSL https://ollama.com/install.sh -o ollama_install.sh