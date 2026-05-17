# JWT トークンのデコードと検証

## 目的
正規の起動かを検証したい

## 要望
3つ目のステップとして、jwt-tokenをjwtコマンでJSONデコードしたファイル `decoded_jwt.json` を生成し、値の検証をするステップを書いてください

## 仕様
### 処理フロー

1. jwtコマンドで `jwt-token` をJSONファイルとしてデコードし、 `decoded_jwt.json` として保存
2. 以下の値に対して検証を行う
   - `payload.event_name`: 値が `release` であるかどうか

## プラン

`.github/workflows/create_formula_by_published_release.yml` の Step 2（Verify jwt）の後に新ステップを挿入する。

- `jwt` コマンドは `sinofseven/action-verify-jwt` アクション内でインストール済みのため追加不要
- `jwt decode --json "$JWT_TOKEN"` で JSON 形式にデコードして `decoded_jwt.json` として保存
- `jq` で `payload.event_name` を取り出し、`release` でなければエラーで終了

## 完了サマリー

完了日時: 2026-05-17T22:33:46+09:00

`.github/workflows/create_formula_by_published_release.yml` に Step 3「Decode and validate jwt」を追加した。

追加内容:
- `jwt decode --json` で `decoded_jwt.json` を生成
- `payload.event_name` が `release` かどうかを `jq` で検証し、不一致の場合はワークフローを失敗させる
- JWT_TOKEN を環境変数経由で渡してシェルインジェクションを防止