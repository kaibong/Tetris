import sys,pygame,random,time
all_block=[
[[0,0],[0,1],[0,2],[0,3],],
[[0,0],[0,1],[1,0],[1,1],],
[[0,0],[1,0],[0,1],[0,2],],
[[0,0],[0,1],[0,-1],[0,-2],],
[[0,0],[0,1],[1,1],[1,2],],
[[0,0],[0,-1],[1,-1],[1,-2],],
[[0,0],[0,1],[0,-1],[1,0],],
]
backgroud=[[0 for column in range(0,10)]for row in range(0,22)]
backgroud[0]=[1 for column in range(0,10)]
select_block=list(random.choice(all_block))
block_initial_position=[21,5]
times=0
score=[0]
gameover=[]
press=False

pygame.init()
screen=pygame.display.set_mode((250,500))
def block_move_down():
    y_drop=block_initial_position[0]
    x_move=block_initial_position[1]
    y_drop-=1
    for row,column in select_block:
        row+=y_drop
        column+=x_move
        if backgroud[row][column]:
            break
    else:
        block_initial_position.clear()
        block_initial_position.extend([y_drop,x_move])
        return
    y_drop,x_move=block_initial_position
    for row,column in select_block:
        backgroud[y_drop+row][x_move+column]=1
    complete_row=[]
    for row in range(1,21):
        if 0 not in backgroud[row]:
            complete_row.append(row)
    complete_row.sort(reverse=True)
    for row in complete_row:
        backgroud.pop(row)
        backgroud.append([0 for column in range(0,10)])
    score[0]+=len(complete_row)
    pygame.display.set_caption('your score:'+str(score[0]))
    select_block.clear()
    select_block.extend(list(random.choice(all_block)))
    block_initial_position.clear()
    block_initial_position.extend([20,5])
    y_drop,x_move=block_initial_position
    for row,column in select_block:
        row+=y_drop
        column+=x_move
        if backgroud[row][column]==1:
            gameover.append(1)
def new_draw():
    y_drop,x_move=block_initial_position
    for row,column in select_block:
        row+=y_drop
        column+=x_move
        pygame.draw.rect(screen,(255,165,0),(column*25,500-row*25,23,23))
    for row in range(0,20):
        for column in range(0,10):
            bottom_block=backgroud[row][column]
            if bottom_block:
                pygame.draw.rect(screen,(0,0,255),(column*25,500-row*25,23,23))
def move_left_right(n):
    y_drop,x_move=block_initial_position
    x_move+=n
    for row,column in select_block:
        row+=y_drop
        column+=x_move
        if column<0 or column>9 or backgroud[row][column]:
            break
    else:
        block_initial_position.clear()
        block_initial_position.extend([y_drop,x_move])
def rotate():
    y_drop,x_move=block_initial_position
    rotating_position=[(-column,row)for row,column in select_block]
    for row,column in rotating_position:
        row+=y_drop
        column+=x_move
        if column<0 or column>9 or backgroud[row][column]:
            break
    else:
        select_block.clear()
        select_block.extend(rotating_position)


while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            move_left_right(-1)
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            move_left_right(1)
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            rotate()
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            press=True
        elif event.type==pygame.KEYUP and event.key==pygame.K_DOWN:
            press=False
    times+=1
    if times>=50:
        block_move_down()
        times=0
    else:
        times+=0.5
    if press:
        times+=10
    if gameover:
        sys.exit()
    new_draw()
    pygame.time.Clock().tick(200)
    pygame.display.flip()
    
