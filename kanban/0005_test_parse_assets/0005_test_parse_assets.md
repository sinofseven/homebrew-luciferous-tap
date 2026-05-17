# parse_assets()のテスト実装

## 目的
重要な関数なので安定化させたい

## 要望
parse_assets()のテストコードを書いてください。`TARGETS_*` の変数を使ってテストを書いて欲しい

## プラン
1. 既存テストファイル `/tests/unit/utils/usecases/test_resolve_assets.py` に `TestParseAsset` クラスを追加
2. `parse_asset()` の6つのテストケースを `@pytest.mark.parametrize` で実装
   - 単一ターゲット/複数ターゲットのマッチング
   - マッチなし、空リストのエッジケース
   - 複数アセット中での優先順位確認
3. 各テストケースで `TARGETS_MACOS`, `TARGETS_LINUX_ARM64`, `TARGETS_LINUX_AMD64` を使用
4. 全テストスイートの実行確認

## 完了サマリー

**完了日時**: 2026-05-17T14:40:00+09:00

### 実装結果
`parse_asset()` 関数に対するユニットテスト `TestParseAsset` クラスを実装。6つのテストケースで以下をカバー：
- 単一ターゲットでの正常なマッチング
- 複数ターゲット（TARGETS_LINUX_ARM64など）での柔軟なマッチング
- エッジケース（マッチなし、空リスト）
- 複数アセット中での最初のマッチが優先されるルール検証

### テスト実行確認
- `TestParseAsset`: 6/6 テストケース PASSED ✓
- 全テストスイート: 45/45 テスト PASSED ✓（既存テストへの影響なし）
