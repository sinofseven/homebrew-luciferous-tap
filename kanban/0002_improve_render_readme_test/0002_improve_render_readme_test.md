# render_readme() テストコードの改善

## 目的
テストの期待値が見にくいため、fixtureとparametrizeのindirectを使って、見やすくしたい

## 要望
render_readme()のテストコードを fixture `load_text()`を使って改善してください

## プラン

1. **期待値ファイルの作成**: 各テストケース（7つ）の期待値を外部ファイル（`tests/unit/fixtures/load_text/`配下）に分離
2. **parametrize の修正**: `indirect=["load_text"]` を追加して fixture と parametrize を連携
3. **テストメソッドの簡潔化**: `expected_output` パラメータを `load_text` に置き換え、テストコードを大幅削減

## 完了サマリー

**完了日時**: 2026-05-15T21:15:00+09:00

✅ 実装完了。以下の内容を実施：

- **期待値ファイル作成**: `tests/unit/fixtures/load_text/` 配下に 7つのファイルを作成
  - `only_tap_name.txt`
  - `multiple_casks_no_formulas.txt`
  - `multiple_formulas_no_casks.txt`
  - `mixed_casks_and_formulas.txt`
  - `display_name_override.txt`
  - `long_descriptions.txt`
  - `special_chars_in_tap_name.txt`

- **テストコード改善**: `tests/unit/utils/jinja2/test_render_readme.py` を修正
  - `indirect=["load_text"]` を追加
  - parametrize 値を「期待値文字列」から「ファイル名」に変更
  - テストメソッドシグネチャを更新（`expected_output` → `load_text`）
  - ファイルサイズ: 387行 → 143行（**63%削減**）

- **テスト実行**: `make test-unit` で全31テスト PASS ✅

**メリット**:
- テストコードの可読性が大幅に向上
- 期待値の管理が容易に（外部ファイル）
- fixture と parametrize の indirect パターンを実装
- 他のテストでも再利用可能な実装パターンを確立
