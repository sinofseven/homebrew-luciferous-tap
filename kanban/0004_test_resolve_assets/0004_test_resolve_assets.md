# resolve_assets() のテスト実装

## 目的
動作を安定させたい

## 要望
resolve_assets()に対してテストを書いてください。テストでは `https://api.github.com/repos/sinofseven/oidc-jwks-converter/releases/tags/v0.1.0` を使用してください。

## プラン

- `tests/unit/utils/usecases/test_resolve_assets.py` を新規作成
- モックなしで実際の GitHub API にリクエストを投げる
- `sinofseven/oidc-jwks-converter` の `v0.1.0` を入力として、macOS / Linux ARM64 / Linux AMD64 の各アセット情報をアサーション

## 完了サマリー

- **完了日時**: 2026-05-17T02:48:53+09:00
- `tests/unit/utils/usecases/test_resolve_assets.py` を新規作成
- 実際の GitHub API へリクエストを投げて期待値と比較するテスト 1 件を実装
- 全テスト（39 件）PASS を確認
