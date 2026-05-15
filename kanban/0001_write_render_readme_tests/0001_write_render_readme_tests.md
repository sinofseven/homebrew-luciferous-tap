# render_readme() のテスト実装

## 目的
README.mdの生成を安定させたい。

## 要望
render_readme()のテストを書いてください

仕様:
- `@pytest.mark.parametrize()`を使ってください
- テストケースに渡す値がstrのとき `TextWrapper`でラップしてください

## プラン

`render_readme()` 関数のテストを `@pytest.mark.parametrize()` を使用して実装する。

### テスト設計
- テストファイル: `tests/unit/utils/jinja2/test_render_readme.py`
- テストクラス: `TestRenderReadme`
- 7 つのテストケースを parametrize で定義
- パラメータ: `option` (render_readme() に `**option` で渡す辞書), `expected_output` (期待される出力)
- TextWrapper は `expected_output`（複数行のマークダウンテキスト）にのみ使用

### テストケース
1. only_tap_name - tap 名のみ、casks/formulas 空
2. multiple_casks_no_formulas - 複数 casks、formulas 空
3. multiple_formulas_no_casks - 複数 formulas、casks 空
4. mixed_casks_and_formulas - casks と formulas が混在
5. display_name_override - display_name が設定されている場合
6. long_descriptions - 長い説明文
7. special_chars_in_tap_name - tap 名に特殊文字

## 完了サマリー

完了日時: 2026-05-15T20:51:00+09:00

`render_readme()` 関数の包括的なテスト実装が完了しました。7 つのテストケースがすべてパスしています。

実装ファイル:
- `tests/unit/utils/jinja2/test_render_readme.py`

テスト結果:
- render_readme テスト: 7/7 PASSED
- 全テスト: 31/31 PASSED
