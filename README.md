# mypkg

## プログラムの内容
ロボットシステム学の講義で使用された上田教授が作成したプログラムを改変したものです。
10Hzの間隔で数字をカウントするプログラムで、カウントの数によって数字の増え方が変化します。

## 環境
- Ubuntu 20.04.1LTS
- ROS(Noetic)

## 使い方
- 準備として以下のコマンドの実行をお願いします。
```
$cd ~/catkin_ws/src
$git clone https://github.com/keita8723/mypkg.git
$cd ..
$catkin_make
$cd src/mypkg/scripts
```
- ここからは複数のウインドを開いての実行となります。  
1つ目のウインドで以下のコマンドの実行をします。
```
$roscore
```  

２つ目のウインドで以下のコマンドの実行をする。
```
$cd ~/catkin_ws/src/mypkg/scripts
$rosrun mypkg count.py
```  

3つ目のウインドで以下のコマンドの実行をする。
```
$cd ~/catkin_ws/src/mypkg/scripts
$rosrun mypkg twice.py
```  

4つ目のウインドで以下のコマンドの実行をする。
```
$cd ~/catkin_ws/src/mypkg/scripts
$rostopic echo /twice
```  


