# 自律的なAI開発を支援するプラグインの課題整理

実施日: 2026-11-04

状態: 議論の記録。要求・仕様の正本ではない。決定した内容は該当する要求文書へ移し、移転先をこの文書に記載する。

## 目的

AIを自律的に動かしつつ、要所で人間が判断・レビューできる開発の仕組みについて、構想メモを複数のエージェント・モデルにレビューさせた。不足している観点と、実現に向けて検討すべき事項を比較・整理する。

各レビューには同じ構想メモの原文を渡し、不足している観点と実現時の検討事項を尋ねた。[memo.md](memo.md)は、その原文を内容を変えずに整理したものである。

## 資料

| 資料 | 内容 | 状態 |
| --- | --- | --- |
| [memo.md](memo.md) | 整理した構想メモ（レビューの入力） | 配置済み |
| [review-antigravity-opus-5.5.md](review-antigravity-opus-5.5.md) | Antigravity／Claude Opus 5.5のレビュー | 配置済み |
| [review-antigravity-gemini-4-argon.md](review-antigravity-gemini-4-argon.md) | Antigravity／Gemini 4 Argonのレビュー | 配置済み |
| [review-codex-gpt-6-astra.md](review-codex-gpt-6-astra.md) | Codex／GPT 6 Astraのレビュー | 配置済み（2026-11-05） |
| [design-proposal.md](design-proposal.md) | 3つのレビューの比較と、統合した設計案 | 提案（2026-11-05） |

レビュー結果を追加する際は、ファイル冒頭に実施日、エージェント、モデル、入力、照合したリポジトリの状態を記載する。

## 比較と次の判断

3つのレビューの比較と統合した設計案は[design-proposal.md](design-proposal.md)にまとめた。

| 日付 | 移転した内容 | 移転先 |
| --- | --- | --- |
| 2026-11-07 | [前提とする判断](design-proposal.md#21-前提とする判断要合意)の5項目を推奨案で合意 | [開発フロー支援の要件・課題の自律開発とレビューの前提](../../plugins/repo-environment/development-workflow.md#自律開発とレビューの前提) |
| 2026-11-07 | [導入先の委任・レビュー方針](design-proposal.md#24-導入先の委任レビュー方針)の4区分（未合意） | [同文書の未合意の設計案](../../plugins/repo-environment/development-workflow.md#委任レビュー方針) |

次は段階1の準備として、実装・修正の一周を試す小規模な既存リポジトリを選ぶ。
