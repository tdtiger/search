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

start = (0, 0)
goal = (0, 0)

# 移動方向管理
movex = [0, -1, 0, 1]
movey = [1, 0, -1, 0]

# 迷路の列数，行数を読み込み
print("迷路の列数，行数を入力してください．")
print("入力形式 : 列数 (空白) 行数")
width, height = input().split()
width = int(width)
height = int(height)

# 迷路の読み込み
print("迷路の情報を入力してください．")
print("入力形式 : 道 -> .  壁 -> #")
print()
for i in range(height):
    print(f"{i + 1}行目")
    tmp = input().split()
    for j in range(width):
        if tmp[j] == 's':
            start = (i, j)
        elif tmp[j] == 'g':
            goal = (i, j)

        wi.append(tmp[j])
    # 行の情報を保存
    me.append(wi)

    # 行の情報を初期化
    wi = []

# 迷路を確認
print()
print("入力された迷路")
for i in range(height):
    for j in range(width):
        if me[i][j] == '#':
            print("# ", end = "")
        elif (i, j) == start:
            print("s ", end = "")
        elif (i, j) == goal:
            print("g ", end = "")
        else:
            print(". ", end = "")
    print()
print()

#オープンリスト
q = deque()
q.append(start)

me[start[0]][start[1]] = 0
me[goal[0]][goal[1]] = '.'

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
    print(f"最短手数:{me[goal[0]][goal[1]]}")

# 迷路を確認
# そのマスまで移動するのにかかる手数が表示
print()
print("探索後の迷路")
for i in range(height):
    for j in range(width):
        if me[i][j] == '#':
            print("# ", end = "")
        else:
            print(me[i][j], end = " ")
    print()