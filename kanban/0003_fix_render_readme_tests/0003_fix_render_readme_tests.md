# render_readme() テストの修正

## 目的
テンプレートとレンダー方法を別途動かして修正した。今の関数出力を正として、テストを修正して欲しい

## 要望
render_readme()のテンプレートとレンダー方法を変更したのでテストを修正して

## プラン

### 実装方針
テンプレートのブロック構造（{% if %} ... {% endif %}）において、render_readme.py の `trim_blocks=True, lstrip_blocks=True` により、if ブロック内の空行が削除されるようになった。タスクの目的に基づき、fixture ファイルを修正して現在の実装出力に合わせる。

### 修正対象（5 ファイル）
1. `tests/unit/fixtures/load_text/only_tap_name.txt` — 4 つの空行を削除
2. `tests/unit/fixtures/load_text/multiple_casks_no_formulas.txt` — 2 つの空行を削除
3. `tests/unit/fixtures/load_text/multiple_formulas_no_casks.txt` — 2 つの空行を削除
4. `tests/unit/fixtures/load_text/long_descriptions.txt` — 2 つの空行を削除
5. `tests/unit/fixtures/load_text/special_chars_in_tap_name.txt` — 2 つの空行を削除

## 完了サマリー

**実施日時**: 2026-05-15T21:39:30+09:00

### 実施内容
5 つの fixture ファイルから、render_readme() の新しい実装により削除された空行を除去した。

### テスト結果
```
uv run pytest -vv tests/unit/utils/jinja2/test_render_readme.py
============================== 7 passed in 0.20s ===============================
```

すべてのテストケース（7 件）が PASSED。

### 修正内容の詳細
- **only_tap_name.txt**: Installation と Updating の間の 4 つの空行を削除（cask/formula セクションがない場合）
- **multiple_casks_no_formulas.txt**: cask ループ後と Updating セクション前の 2 つの空行を削除（formula セクションがない場合）
- **multiple_formulas_no_casks.txt**: Installation と Available Formulas セクション前の 2 つの空行を削除（cask セクションがない場合）
- **long_descriptions.txt**: cask ループ後と Updating セクション前の 2 つの空行を削除
- **special_chars_in_tap_name.txt**: cask ループ後と Updating セクション前の 2 つの空行を削除
