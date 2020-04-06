import pygame, sys, random, time, keyboard
from pygame.locals import *  # 从pygame模块导入常用的函数和常量

# 定义颜色变量
black_colour = pygame.Color(0, 0, 0)
white_colour = pygame.Color(255, 255, 255)
red_colour = pygame.Color(255, 0, 0)
grey_colour = pygame.Color(150, 150, 150)
green_colour = pygame.Color(0, 255, 0)

# 绘制得分
def ds(gamesurface, score):
    
    score_font = pygame.font.SysFont('arial', 30)

    score_text = score_font.render('score: ' + str(score), True, grey_colour)

    text_rect = score_text.get_rect()

    text_rect.topleft = [10, 10]

    gamesurface.blit(score_text, text_rect)
    pygame.display.update()

# 定义游戏结束函数
def GameOver(gamesurface, score, highest_score):
    # 设置提示字体的格式
    GameOver_font = pygame.font.SysFont('arial', 30)
    Score_font = pygame.font.SysFont('arial', 28)
    h_font = pygame.font.SysFont('arial', 28)
    Z_font = pygame.font.SysFont('arial', 24)
    Q_font = pygame.font.SysFont('arial', 24)


    # 设置提示字体的颜色
    GameOver_colour = GameOver_font.render('Game Over', True, grey_colour)
    Score_colour = Score_font.render('Score: '+str(score), True, grey_colour)
    h_colour = h_font.render('Your best score: ' + str(highest_score), True, grey_colour)

    Z_colour = Z_font.render('Input  \'R\'  to  restart ~', True, (255,255,0))
    Q_colour = Q_font.render('Input  \'Q\'  to  quit !', True, red_colour)
    # 设置提示位置
    GameOver_location = GameOver_colour.get_rect()
    GameOver_location.midtop = (300, 10)

    Score_location = Score_colour.get_rect()
    Score_location.midtop = (280, 50)

    h_location = Score_colour.get_rect()
    h_location.midtop = (280, 90)

    Z_location = Score_colour.get_rect()
    Z_location.midtop = (280, 150)

    Q_location = Score_colour.get_rect()
    Q_location.midtop = (290, 210)

    # 绑定以上设置到句柄
    gamesurface.blit(GameOver_colour, GameOver_location)
    gamesurface.blit(Score_colour, Score_location)
    gamesurface.blit(Z_colour, Z_location)
    gamesurface.blit(Q_colour, Q_location)
    gamesurface.blit(h_colour, h_location)
    # 提示运行信息
    pygame.display.flip()
    while True:
        if keyboard.read_key() == 'r' or keyboard.read_key() == 'R':
            break
        elif keyboard.read_key() == 'q' or keyboard.read_key() == 'Q':
            # 退出游戏
            pygame.quit()
            # 退出程序
            sys.exit()


    # 休眠5秒
    #time.sleep(5)

    # 退出游戏
    #pygame.quit()
    # 退出程序
    #sys.exit()

# 暂时没用button
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

# 记录最高分
def h_score(score, highest_score):
    if highest_score < score:
        highest_score = score

    return highest_score

# 定义主函数
def main():
    highest_score = 0
    while(1):
        # 初始化pygame，为使用硬件做准备
        pygame.init()
        pygame.time.Clock()
        ftpsClock = pygame.time.Clock()
        # 创建一个窗口
        gamesurface = pygame.display.set_mode((640, 480))
        # 设置窗口的标题
        pygame.display.set_caption('tanchishe snake')

        gamesurface.fill([0, 0, 0])  # 用白色填充窗口

        myimage = pygame.image.load('start.png')  # 把变量myimage赋给导入的图片
        exp = pygame.image.load('sss.png')
        gamesurface.blit(myimage, [270, 30])  # 在100,100的地方画出这个图片（100和100为左部和上部）
        gamesurface.blit(exp, [50, 150])


        pygame.display.flip()
        wait = 1
        while wait:
            for event in pygame.event.get():  # 获得事件
                if event.type == pygame.MOUSEBUTTONDOWN and 270 <= event.pos[0] <= 371 and 30 <= event.pos[1] <= 132:  # 判断鼠标位置以及是否摁了下去。
                    # 做需要做的事情，如开始游戏。
                    wait = 0
        # 初始化变量
        # 初始化贪吃蛇的起始位置
        snakeposition = [100, 100]
        # 初始化贪吃蛇的长度
        snakelength = [[100, 100], [80, 100], [60, 100]]
        # 初始化目标方块的位置
        square_purpose = [300, 300]
        square_purpose_g = [150, 150]

        # 初始化一个数来判断目标方块是否存在
        square_position = 1
        square_position_g = 0

        # 初始化方向，用来使贪吃蛇移动
        derection = "right"
        change_derection = derection

        # 初始速度
        speed = 6

        # 初始分数
        score = 0
        # 初始是否存活
        live = 1

        # 控制绿色果果的出现
        times = 0
        # 进行游戏主循环
        while live:
            # 检测按键等pygame事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    # 接收到退出事件后，退出程序
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    # 判断键盘事件,用w,s,a,d来表示上下左右
                    if event.key == K_RIGHT or event.key == ord('d'):
                        change_derection = "right"
                    if event.key == K_LEFT or event.key == ord('a'):
                        change_derection = "left"
                    if event.key == K_UP or event.key == ord('w'):
                        change_derection = "up"
                    if event.key == K_DOWN or event.key == ord('s'):
                        change_derection = "down"
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
            # 判断移动的方向是否相反
            if change_derection == 'left' and not derection == 'right':
                derection = change_derection
            if change_derection == 'right' and not derection == 'left':
                derection = change_derection
            if change_derection == 'up' and not derection == 'down':
                derection = change_derection
            if change_derection == 'down' and not derection == 'up':
                derection = change_derection
            # 根据方向，改变坐标
            if derection == 'left':
                snakeposition[0] -= 20
            if derection == 'right':
                snakeposition[0] += 20
            if derection == 'up':
                snakeposition[1] -= 20
            if derection == 'down':
                snakeposition[1] += 20
            # 增加蛇的长度
            snakelength.insert(0, list(snakeposition))

            # 判断是否吃掉目标方块
            if snakeposition[0] == square_purpose[0] and snakeposition[1] == square_purpose[1]:
                square_position = 0
                speed = speed + 1
                score = score + 1
                times = times + 1

            elif square_position_g == 1 and snakeposition[0] == square_purpose_g[0] and snakeposition[1] == square_purpose_g[1]:
                snakelength.pop()
                square_position_g = 0
                square_position = 0
                speed = speed - 3
                times = times + 1


            else:
                snakelength.pop()


            # 重新生成目标方块
            if square_position == 0:
                # 随机生成x,y,扩大二十倍，在窗口范围内
                x = random.randrange(1, 32)
                y = random.randrange(1, 24)
                square_purpose = [int(x * 20), int(y * 20)]
                square_position = 1

            if square_position_g == 0 and times != 0 and times % 5 == 0:
                x1 = random.randrange(1, 32)
                y1 = random.randrange(1, 24)
                square_purpose_g = [int(x1 * 20), int(y1 * 20)]
                square_position_g = 1

            # 绘制pygame显示层
            gamesurface.fill(black_colour)
            for position in snakelength:
                pygame.draw.rect(gamesurface, white_colour, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(gamesurface, red_colour, Rect(square_purpose[0], square_purpose[1], 20, 20))

                if times != 0 and times % 5 == 0:
                    pygame.draw.rect(gamesurface, green_colour, Rect(square_purpose_g[0], square_purpose_g[1], 20, 20))


            # 刷新pygame显示层
            pygame.display.flip()
            # 判断是否死亡
            if snakeposition[0] < 0 or snakeposition[0] > 620:
                highest_score = h_score(score, highest_score)
                pygame.display.update()
                GameOver(gamesurface, score, highest_score)
                live = 0
            if snakeposition[1] < 0 or snakeposition[1] > 460:
                highest_score = h_score(score, highest_score)
                pygame.display.update()
                GameOver(gamesurface, score, highest_score)
                live = 0
            for snakebody in snakelength[1:]:
                if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                    highest_score = h_score(score, highest_score)
                    pygame.display.update()
                    GameOver(gamesurface, score, highest_score)
                    live = 0

            # 游戏过程中显示分数
            ds(gamesurface, score)

            # 控制游戏速度
            ftpsClock.tick(speed)


if __name__ == "__main__":
    main()







