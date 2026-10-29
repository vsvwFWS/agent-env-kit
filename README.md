# agent-env-kit

AI開発ワークフローを改善するためのプラグインを開発・管理するリポジトリです。他の開発リポジトリで、必要な拡張を選んで利用できる形を目指します。

機能別の拡張と、同じ目的に対する別案の比較実験を扱います。最初の製品として、導入先の状況を調べ、ユーザーと相談しながら開発環境を整えるセットアップ・メンテナンス拡張を試作しています。

## 現在の状態

最初のプラグインに、setup／maintenanceのskillsと導入・検証手順を用意しました。初期の検証対象はCodexデスクトップアプリで、リポジトリ単位の導入を想定しています。実動検証は未完了です。[検証記録](tests/repo-environment/validation.md)で、確認済みの範囲と残作業を確認できます。

## プラグイン一覧

| プラグイン | 目的 | 状態 | 要求・仕様 |
| --- | --- | --- | --- |
| [Repo Environment](plugins/repo-environment/README.md) | 指示・検証・採用拡張・関連リポジトリ参照の整備と見直し | 試作版・デスクトップ実動未検証 | [開発依頼書](PROJECT_BRIEF.md) |

新しい拡張や継続比較する別案を追加したら、この一覧に用途、状態、参照先を記載します。

## 文書の入口

- 利用を検討する方：[プラグインのREADME](plugins/repo-environment/README.md)で導入・利用方法と制約、[開発依頼書](PROJECT_BRIEF.md)で要求を確認できます。
- 開発する方：[構成・運用方針](docs/repository.md)で配置、文書の正本、実験・検証の進め方を確認してください。
- 作業するエージェント：[AGENTS.md](AGENTS.md)に、このリポジトリでの判断規則と検証の入口があります。

## 開発時の検証

Python 3.10以降で、配布フォルダ単体の構造とローカルリンクを確認できます。外部ライブラリは不要です。

```sh
python3 tests/repo-environment/check_package.py
git diff --check
```

デスクトップでの実動確認は[受け入れ確認の手順](tests/repo-environment/README.md)に従います。

Pythonファイルの編集後は、[Pythonの整形・lint手順](docs/repository.md#pythonの整形lint)に従ってRuffを実行します。
