# create_formula_by_published_release.yml に自動コミット・プッシュステップを追加

## 目的
コミットとPushしてFormulaやREADMEを更新したい

## 要望
create_formula_by_published_release.ymlにステップを追加し、変更があればコミットしPushしてください

## プラン
- ワークフローファイルに `permissions: contents: write` を追加して git push 権限を付与
- "Commit and push changes" という新しいステップをワークフロー最後に追加
- git config、add、diff、commit、push の処理を実装
- コミットメッセージは `feat: Add {formula_name} formula` の既存フォーマットに準拠
- `git diff --quiet --cached` で変更がない場合は自動スキップ

## 完了サマリー

**完了日時**: 2026-05-17T20:35:00+09:00

### 実装内容

`create_formula_by_published_release.yml` ワークフローに以下の変更を加えました：

1. **permissions セクション追加** (Line 3-4)
   ```yaml
   permissions:
     contents: write
   ```
   `GITHUB_TOKEN` に push 権限を付与

2. **"Commit and push changes" ステップ追加** (Line 79-85)
   - git ユーザー設定（`github-actions[bot]`）
   - 生成ファイル（Formula/, README.md, tap_info.json）のステージング
   - 変更有無確認後、自動コミット・プッシュ
   - コミットメッセージ: `feat: Add {inputs.name} formula`

### 実装の特徴

- **冪等性**: `git diff --quiet --cached` で変更がない場合はスキップ（不要なコミット作成を防止）
- **既存フォーマット準拠**: `feat:` type でコミット履歴と一貫性保持
- **入力値活用**: `inputs.name` をメッセージに埋め込み、追加された Formula 名を明確化
- **条件付き実行**: `if: success()` で前ステップ成功時のみ実行

### 動作フロー

GitHub Release が発行されて `create_formula_by_published_release.yml` ワークフローが実行されると：

1. Formula、README、tap_info.json が生成される
2. 変更がある場合、自動的にコミット作成
3. リモートブランチへプッシュ
4. リポジトリに Formula 更新が反映

### ファイル変更

- `.github/workflows/create_formula_by_published_release.yml`: +5 行（permissions セクション、新ステップ）
