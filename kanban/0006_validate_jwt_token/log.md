# タスク 0006: JWT トークンのデコードと検証ステップ追加

## ヘッダー

- 開始時刻: 2026-05-17T22:33:09+09:00
- 完了時刻: 2026-05-17T22:33:46+09:00

---

## タスク概要

3つ目のステップとして、jwt-tokenをjwtコマンドでJSONデコードしたファイル `decoded_jwt.json` を生成し、値の検証をするステップを書いてください

仕様:
1. jwtコマンドで `jwt-token` をJSONファイルとしてデコードし、 `decoded_jwt.json` として保存
2. 以下の値に対して検証を行う
   - `payload.event_name`: 値が `release` であるかどうか

---

## 調査結果

### `.github/workflows/create_formula_by_published_release.yml`

ファイルの全体構成（48行）:

```yaml
name: create_formula_by_published_release.yml

on:
  workflow_dispatch:
    inputs:
      name: (required) binary filename
      display_name: (optional) display name
      description: (required) description
      license_name: (required) license name
      command_test: (required) test command for formula
      jwt_token: (required) JWT token string

jobs:
  create_formula:
    runs-on: ubuntu-24.04
    environment: ${{ inputs.name }}
    steps:
      - name: Checkout
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6

      - name: Verify jwt
        uses: sinofseven/action-verify-jwt@v1.1.0
        with:
          token: ${{ inputs.jwt_token }}
          jwks-url: "https://token.actions.githubusercontent.com/.well-known/jwks"
          audience: ${{ secrets.JWT_AUDIENCE }}

      - name: Setup uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

- `sinofseven/action-verify-jwt@v1.1.0` アクションが JWT の署名検証と `jwt` コマンドのインストールを行う
- 新ステップは Step 2（Verify jwt）と Step 3（Setup uv）の間に挿入する
- `jq` は ubuntu-24.04 にデフォルトで搭載済み

### Python 実装との関係

- `src/utils/models/decoded_jwt_info.py`: JWT デコード結果のデータモデル（`DecodedJwtInfo`）
- `src/utils/usecases/parse_decoded_jwt_info.py`: `decoded_jwt.json` を読み込んで `DecodedJwtInfo` を生成
- `src/handlers/create_formula_by_published_release/create_formula_by_published_release.py`: メインハンドラー

Python コードは `decoded_jwt.json` を読み込む前提で実装済みのため、ワークフロー側でこのファイルを生成する必要がある。

---

## 実装プラン

`.github/workflows/create_formula_by_published_release.yml` の Step 2（Verify jwt）の後に以下の新ステップを挿入:

```yaml
- name: Decode and validate jwt
  env:
    JWT_TOKEN: ${{ inputs.jwt_token }}
  run: |
    jwt decode --json "$JWT_TOKEN" > decoded_jwt.json
    event_name=$(jq -r '.payload.event_name' decoded_jwt.json)
    if [ "$event_name" != "release" ]; then
      echo "::error::payload.event_name が release ではありません (値: $event_name)"
      exit 1
    fi
```

ポイント:
- `jwt` コマンドは Step 2（`sinofseven/action-verify-jwt`）でインストール済みのため追加不要
- `jwt decode --json` で JSON 形式で出力して `decoded_jwt.json` に保存
- `jq -r '.payload.event_name'` で payload.event_name の値を抽出して検証
- JWT_TOKEN は環境変数経由で渡す（シェルインジェクション防止）

---

## プランニング経緯

- 最初のプランでは `npm install -g jwt-cli` を含めていた
- ユーザーから「jwtコマンドはStep2でインストールしているので必要ありません」とのフィードバック
- インストールステップを削除して修正プランを提示し、承認を得た

---

## 会話内容

1. ユーザーが `/kanban 0006` を実行
2. タスクファイルを読み込み、プランモードに入った
3. `.github/workflows/create_formula_by_published_release.yml` を調査
4. 最初のプランで `npm install -g jwt-cli` を含めて提示
5. ユーザーから「Step 2 でインストール済み」とのフィードバック
6. プランを修正（インストールステップ削除）して再提示、承認を得た

---

## 編集したファイル

- [x] `.github/workflows/create_formula_by_published_release.yml` — Step 3「Decode and validate jwt」を追加
- [x] `kanban/0006_validate_jwt_token/0006_validate_jwt_token.md` — プランと完了サマリーを追記

---

## 実行したコマンド

（実装中に追記）

---

## 判断・意思決定

（実装中に追記）

---

## エラー・問題

（実装中に追記）
