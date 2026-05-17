# create_formula_by_published_release.yml のコミットメッセージ改善

## 目的
コミットメッセージをわかりやすくしたい。

## 要望
create_formula_by_published_release.yml の最終ステップのコミットメッセージを feat 形式ではなく、どの Formula のなんというバージョンなのかを明記してほしい。

どの Formula なのかは `inputs.name` を、version は JWT をデコードしたデータから取得してください。

## プラン
`.github/workflows/create_formula_by_published_release.yml` の Commit and push changes ステップを修正：
1. `jq` で JWT デコード後の JSON ファイルから `payload.ref` を抽出してバージョンを取得
2. コミットメッセージ形式を `"feat: Add {バイナリ名} formula"` から `"{バイナリ名} formula ({バージョン})"` に変更
3. 例：`foo formula (v1.0.0)`

## 完了サマリー
**完了日時**: 2026-05-17T22:59:53+09:00

ワークフローファイル `.github/workflows/create_formula_by_published_release.yml` の行79-89 を修正。
- `jq -r '.payload.ref | split("/")[-1]'` で JWT から version を抽出
- `git commit -m "${{ inputs.name }} formula ($VERSION)"` でコミットメッセージを生成
- 結果：`foo formula (v1.0.0)` という形式で、Formula 名とバージョンを明記するコミットメッセージが生成される

詳細は `log.md` を参照。
