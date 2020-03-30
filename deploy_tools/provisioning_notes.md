 

ssh username: wp_y7p8kv
             @blueocianic.club
pw: jCHbSXI54Txz
かなあ。それかuntitle.pngをみること

ssh -T wp_y7p8kv@blueocianic.club

でログインできる

log-in notice of important sites and pcs AND use-password
pwdvapikey
portfolio app

accuracy over recall
have to know why abcd ranks on ipoww
warehouse bank IMPORTANT

gmail以外でgoogleにログインしなくていいようにしたい

tryagain without the farthest,threshold and modifier

kasikin stockaggr havefun nextroom wp 22soul
highpc highvr highscr


Desktopのputtyのショートカットをクリック（c:/bin)
ss


[server]$ ./config --prefix=/home/wp_y7p8kv/openssl --openssldir=/home/wp_y7p8kv/openssl no-ssl2

gitつかいかた（ギット）
$ cd 対象フォルダ
$ git init
ファイル内をgitで管理可能にする

$ git add .
先ほどと同じように、ドラッグしましょう

$ git commit -m "[変更点などを記述]"
任意でメッセージを記入可能


elspeth@server:$ export SITENAME=superlists-staging.ottg.eu　# you should replace the URL in the next line with the URL for your own repo

elspeth@server:$ git clone https://github.com/hjwp/book-example.git ~/sites/$SITENAME
または
$ git remote add origin [アップロード先]（？？？）

BASHつかいかた
↑キー以外にCtrl-Rでhistoryからインクリメンタル検索できますが、インクリメンタル検索の次候補が出したければさらにCtrl-Rを押していくと過去のコマンド履歴に戻っていくことができます。
また、カーソルキーが前節のようにバグって表示されてしまう環境の場合、↑キーは Ctrl-P（Previous）、↓キーはCtrl-N（Next）で代用できます。同様に→キーはCtrl-F（Forward）、←キーはCtrl-B（Back）で代替できます。

完全にnonempty dirを消す
rm -rf dir-name
rm -rf /path/to/dir/name

Puttyほか4をダウンロードして、exeファイルを
C:\bin\putty.exeにmoveしました。

Name servers

To use Lightsail to manage DNS records for your domain, you will have to configure your domain provider to use the following name servers:

    ns-1538.awsdns-00.co.uk
    ns-76.awsdns-09.com
    ns-535.awsdns-02.net
    ns-1482.awsdns-57.org

ubuntu@ip-172-26-10-182
Public IP
54.188.57.170

User name
ubuntu


Ubuntu-1asdfghjkl
512 MB RAM, 1 vCPU, 20 GB SSD

oeawFebe

Account ID:

425976745706

This ID is shared by your AWS and Lightsail accounts

oregon (us-west-2)
default download

puttyでhostnameに54.188.57.170
SSH→authにoregon-2のpem
connectionでkeepaliveに50
session a1とa2
login as: ubuntu

（2つ目の接続は、~/Users/keypairname2をauthにいれればOKのようだ)

8000のポートを開いた(security firewall)


COPY=COMMAND(1つめ）

cd ~/sites/blueocianic.de && ./virtualenv/bin/python3.7 manage.py runserver 0.0.0.0:8000

COPY=COMMAND(2つめ）

cd ~/sites/blueocianic.de && source ./virtualenv/bin/activate && STAGING_SERVER=staging.blueocianic.de:8000 ./manage.py test functional_tests --failfast

cd ~/sites/blueocianic.de && source ./virtualenv/bin/activate && STAGING_SERVER=54.188.57.170:8000 ./manage.py test functional_tests --failfast

export PATH=$PATH:＜追加したいパス＞

そこで、.bash_profileを使います。

.bash_profileは、bashのログイン時に自動的に読み込まれる設定ファイルです。
設定ファイルと言っても、ログイン時に実行してほしいコマンドを記述しておくだけのものですが

この.bash_profileに、さきほどのコマンドを記載しておけば、毎ログイン時に自動的にPATHを設定しなおしてくれます。
テキストエディタ等で、~/.bash_profileに前述した一文を追加したら完了です。

NSrecord
ns-307.awsdns-38.com. 
ns-808.awsdns-37.net. 
ns-1589.awsdns-06.co.uk. 
ns-1029.awsdns-00.org.

Djangoであれば python manage.py runserver というコマンドでサーバーを起動できます。 なぜこのサーバーを使わずにgunicornを使うのでしょうか？

理由は簡単に言うと、動作が速いからです。


================================
## Required packages:
*nginx
*Python 3.7
*virtualenv+pip
*Git
eg, on Ubuntu16.04:

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install nginx git python37 python3.7-venv

##Nginx Virtual Host config
*see nginx.template.conf
*replace DOMAIN with, e.g., staging.my-domain.com
##Systemd service
*see gunicorn-systemd.template.service
*replace DOMAIN with, e.g., staging.my-domain.com

##Folder structure:

Asume we have auser account at /home/username
/home/username
|--DOMAIN1
| |-.env
| |-db.sqlite3
| |-manage.py etc
| |-static
| |-virtualenv
|
|--DOMAIN2
  |-.env
  |-db.sqlite3
  |-etc


