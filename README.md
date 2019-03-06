# macOSでscrapy

pythonのインストール

```shell
$ brew install python
リンクのエラーが出るので、以下を実行する
$ sudo mkdir /usr/local/Frameworks
$ sudo chown $(whoami):admin /usr/local/Frameworks
$ brew link python　
```

- [Homebrewで入れたPythonでのlinkエラー問題 - Qiita](https://qiita.com/Jung0/items/d4012814e6fb1b694208)

pipのインストール
- https://pip.pypa.io/en/stable/installing/
　上記 URL から get-pip.py をダウンロードしターミナルから実行する。
　カレントユーザーの権限で使用できるよう --user オプション付きでインストールする。

`$ python get-pip.py --user`

実行が完了すると $HOME/Library/Python にインストールされる。pip コマンドが利用できるようパスを通す。

bashなら

`$ echo 'export PATH="$HOME/Library/Python/2.7/bin:$PATH"' >> ~/.bash_profile`

zshなら

`$ echo 'export PATH="$HOME/Library/Python/2.7/bin:$PATH"' >> ~/.zshrc`

`$ pip install scrapy --user`

`--user`がないと、権限のエラーが出るので、常につけること。

- [pip install nfcpyでPermission denied発生したときの対処法](https://engrowth.me/tech/pip_installerror/)

# Spiderの実行

`$ scrapy crawl hatena`
