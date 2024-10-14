# 迷路に対して幅優先探索を行うプログラム．
# 入力形式は，
#
# 行の長さ 列の長さ
#        ↑空白あり
# の後，一行ずつ迷路の情報を1マスごとに空白を挟んで入力
# 道は"."，通れない場所は"#"
# ただし，スタートとゴールについては"s"，"g"と入力してください．
#
# ex.
# 5 4
# . . s . .
# . . # # #
# . . . # g
# . # . . .
#
# 出力：8

from collections import deque

# 迷路本体
me = []
# 行の長さ
wi = []

width, height = input().split()
width = int(width)
height = int(height)

start = (0, 0)
goal = (0, 0)

# 移動方向管理
movex = [0, -1, 0, 1]
movey = [1, 0, -1, 0]

# 迷路の読み込み
for i in range(height):
    tmp = input().split()
    for j in range(width):
        if tmp[j] == '#':
            wi.append('#')
            continue
        elif tmp[j] == 's':
            start = (i, j)
            wi.append(0)
            continue
        elif tmp[j] == 'g':
            goal = (i, j)

        wi.append('.')
    me.append(wi)
    wi = []

for i in range(len(me)):
    print(me[i])
#オープンリスト
q = deque()
q.append(start)

# オープンリストが空になるまでループ
# あまりにも大きい迷路だと時間がかかりすぎると思うので，ループカウンタを設けて上限回数を設定したほうがいいかもしれない
while q:
    y, x = q.popleft()
    for i in range(4):
        nx = x + movex[i]
        ny = y + movey[i]
        if 0 <= ny < height and 0 <= nx < width and me[ny][nx] != '#':
            if me[ny][nx] == '.':
                me[ny][nx] = me[y][x] + 1
                q.append((ny, nx))

# ゴールの値が"."のままだったら，到達できていないため失敗
if me[goal[0]][goal[1]] == '.':
    print("Fail")
else:
    print(me[goal[0]][goal[1]])