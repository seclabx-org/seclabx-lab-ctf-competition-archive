# 贡献指南

本指南用于规范赛事与题目的收录流程，便于协作与审核。

## 协作流程

- 在 Issues 使用“赛事收录任务”模板创建任务
- Fork 仓库并创建分支：`feat/<赛事>-<题目>`（例如：`feat/LilCTF-web-ez-bottle`或者`feat/issue-23`）
- 每个 Issue 对应一个 PR，一个 Issue 可包含同一赛事/同一年份的多道题
- PR 目标分支必须为 `develop`
- 等待 Review 与 CI/CD 检查通过

## 协作者操作步骤（从认领到 PR）

1) 认领 Issue
- 在对应 Issue 下评论：`/claim`

2) Fork 并拉取仓库
```bash
git clone <你的fork地址>
cd <仓库目录>
git remote add upstream <原仓库地址>
git fetch upstream
git checkout develop
git pull upstream develop
```

3) 创建分支并开发
```bash
git checkout -b feat/<赛事>-<题目>
```

4) 添加题目内容并提交
```bash
git add .
git commit -m "add: <赛事>-<题目>"
```

5) 推送到自己的 Fork
```bash
git push origin feat/<赛事>-<题目>
```

6) 发起 PR
- 目标分支：`develop`
- 关联对应 Issue

## 维护者操作步骤（审核与合并）

1) 分配/确认 Issue 认领
- Issue 中确认认领人并保持追踪

2) Review PR
- 检查目录结构与必备文件
- 确认命名规范与来源说明
- 等待 CI 通过

3) 触发手动构建（如需）
- Actions → `build-challenge-images` → `Run workflow`

4) 合并到 `develop`
- PR 通过后合并

5) 上线发布（如需）
- Actions 手动触发 `latest-<题目tag>` 构建

## 目录与命名规范

```
目录结构：赛事名/年份/题目类型-题目名
赛事名：保留官方大小写，空格用短横线
年份：4 位
题目类型：web | pwn | reverse | crypto | misc | forensics
题目名：小写 + 短横线 + 无空格/中文
示例：
LilCTF/2025/web-ez-sql
GeekGame/2024/reverse-baby-crack
XCTF/2023/pwn-heap-baby
```

## 题目内容要求

- 题目目录内包含 `README.md`（复现步骤/关键说明）
- 赛事目录（`赛事/年份/`）内包含 `SOURCE.md`（官方来源或公开链接）
- 保留原始 LICENSE 或授权说明
- 严禁提交用于商业用途的内容

## 题目结构与 flag 说明

- 所有题目必须包含 `README.md`
- 有 `challenge.yaml` 的题目按其赛事规范执行（例如 flag 类型与 container 配置）
- 是否构建镜像以 `Dockerfile` 为准：有则构建，无则跳过
- `Dockerfile` 可放在题目根目录或 `build/` 下
- README 需注明 flag 注入方式（示例：环境变量、flag 文件、数据库预置）

## 冲突与索引更新

- 为减少冲突，PR 不修改索引文件（`INDEX.yaml`/`INDEX.md`）
- 索引由维护者统一更新
- 维护者可用 `python scripts/generate_index_md.py` 生成 `INDEX.md`（需先 `pip install pyyaml`）
- 维护者可用 `python scripts/generate_index_yaml.py` 扫描目录生成 `INDEX.yaml`（会校验 `赛事/年份/SOURCE.md`）

## 编码与格式

- 所有文本文件使用 UTF-8（无 BOM）
- 命名规则统一为英文与短横线
- 不提交系统垃圾文件（已在 `.gitignore` 统一过滤）

## 镜像命名规范

- 镜像仓库：`crpi-7st94yd1uskrhjrz.cn-chengdu.personal.cr.aliyuncs.com/seclabx/ctf`
- 题目镜像 tag：`赛事-年份-类型-题目`（全小写，短横线）
- 题目 tag 示例：`lilctf-2025-web-ez-bottle`
- PR 测试 tag：`pr-<PR号>-<题目tag>`
- 集成测试 tag：`dev-<题目tag>`（手动触发）
- 生产发布 tag：`latest-<题目tag>`
- 完整镜像示例：`crpi-7st94yd1uskrhjrz.cn-chengdu.personal.cr.aliyuncs.com/seclabx/ctf:latest-lilctf-2025-web-ez-bottle`

## 模板使用

- PR 必须使用 PR 模板：`.github/PULL_REQUEST_TEMPLATE.md`
- Issue 必须使用赛事收录模板：`.github/ISSUE_TEMPLATE/competition.md`

## CI/CD 触发方式

- PR 到 `develop`：自动构建并推送 `pr-<PR号>-<题目tag>`
- 手动触发：构建并推送 `dev-<题目tag>` 或 `latest-<题目tag>`
- PR 构建支持多个题目；手动构建仅支持单个题目

## 手动触发步骤（GitHub Actions）

- 进入仓库 → Actions → 选择 `build-challenge-images`
- 点击 `Run workflow`
- 填写参数：
  - `challenge_path`：题目路径（如 `LilCTF/2025/web-ez-bottle`）
  - `tag_prefix`：`dev` 或 `latest`
  - `force_rebuild`：需要覆盖时勾选
