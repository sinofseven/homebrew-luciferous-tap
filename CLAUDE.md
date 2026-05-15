# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## リポジトリの概要

`homebrew-luciferous-tap` は Homebrew のカスタム tap リポジトリです。Homebrew formula（`Formula/*.rb`）を管理し、ユーザーが `brew tap sinofseven/luciferous-tap` でインストールできるようにします。

Python プロジェクト（`pyproject.toml`）は tap のメンテナンス用スクリプト・ツールのためのものです。

## Python 環境

- Python バージョン: 3.14（`.python-version` で指定）
- パッケージマネージャー: `uv`
- PyPI レジストリ: `https://pypi.flatt.tech/simple/`（カスタムレジストリ）

```bash
# 依存関係のインストール
uv sync

# スクリプトの実行
uv run <script>
```

## Homebrew Formula

Formula は `Formula/*.rb` に Ruby で記述します。新しい formula を追加した後は以下でテストします。

```bash
# formula の構文チェック
brew audit --strict Formula/<name>.rb

# formula のインストールテスト
brew install --build-from-source Formula/<name>.rb

# テストの実行
brew test Formula/<name>.rb
```

## Renovate

`renovate.json` で依存関係の自動更新が設定されています。PyPI パッケージは `pypi.flatt.tech` レジストリを参照します。

## 開発ワークフロー（kanban-kit）

このリポジトリでの開発は Claude Code plugin `kanban-kit` を使用します。

- タスクの追加: `/add-kanban`
- タスクの実行: `/kanban`（args 未指定の場合、未完了タスクのうち番号が最大のものを選択）

詳細は `/kanban` スキルの `references/kanban-workflow.md` を参照。

### ディレクトリ・ファイル構成

```
kanban/
  {xxxx}_{title}/
    {xxxx}_{title}.md   # タスクファイル（ユーザーが作成）
    log.md              # 作業ログ（Claude が記録）
```

- `xxxx`: 4桁の0パディング連番（例: `0001`）
- タイムスタンプは JST ISO 8601 形式（`TZ=Asia/Tokyo date +"%Y-%m-%dT%H:%M:%S+09:00"`）

### タスクファイルの構造

ユーザーが以下の構造で作成する。`## 目的` は必須。

```markdown
# タイトル
## 目的
（なぜこの作業が必要か — 背景・動機・ゴール）

## 要望
（具体的に何をどうしてほしいか）
```

実装完了後、Claude が `## プラン` と `## 完了サマリー` を追記する。

### ログ記録の原則

- ログはプランモード承認後すぐに作成し、作業中も段階的に追記する（完了後まとめて書かない）
- 調査内容・判断経緯・会話内容を省略・圧縮せず完全に記録する
- 未完了タスク = `## 完了サマリー` を含まないタスクファイル
