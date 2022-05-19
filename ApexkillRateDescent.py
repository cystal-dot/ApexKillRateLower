import pyautogui as pag
import time
import pydirectinput as direct

# 特定の画像が表示されているか確認する関数
def checkImageInScreen(img_path):
    icon_region = pag.locateOnScreen(img_path, confidence=0.8)
    if icon_region is not None:
        return True
    else:
        return False

# 特定の画像の座標をreturnする関数
def getImagePosition(img_path):
    icon_region = pag.locateOnScreen(img_path, confidence=0.8)
    if icon_region is not None:
        x,y = pag.center(icon_region)
        return x,y
    else:
        return None

# 特定の画像を押下する関数
def clickImage(img_path):
    pag.moveTo(getImagePosition(img_path))
    time.sleep(1)
    pag.click(getImagePosition(img_path))


def main():
    #windowを移動させる
    pag.click(700,900)
    time.sleep(1)
    # ロビーにいることを確認
    InRobby = checkImageInScreen('apexpicture/RobbyReady.png')
    if InRobby == True:
        # 準備完了を押下
        clickImage('apexpicture/RobbyReady.png')
    else:
        print('Robby is not ready')

    # マッチングを確認
    for i in range(180):
        GetMatching = checkImageInScreen('apexpicture/wraithCharacter.png')
        time.sleep(0.5)
        if GetMatching == True:
            print('GetMatching')
            break
        else:
            print('Not GetMatching: ' + str(i)+ 'times')

    # チャンピオン部隊の表示を確認
    for i in range(120):
        InChampion = checkImageInScreen('apexpicture/championSquad.png')
        time.sleep(0.5)
        if InChampion == True:
            print('Find Champion!')     
            # スクリーンショットを撮る
            latestImg = pag.screenshot('apexpicture/latestChampion.png')
            break
        else:
            print('Not Find Champion: ' + str(i)+ 'times')

    # 最新のチャンピオン画像を表示
#    latestImg.show()
    # マッチから退出を押下
    # エスケープを押下 
    time.sleep(0.2)
    direct.keyDown('esc')
    direct.keyUp('esc')
    print('clicked esc')
    time.sleep(0.2)
    # マッチから退出を押下
    clickImage('apexpicture/escapefrommatch.png')
    time.sleep(0.4)
    # はいを押下
    clickImage('apexpicture/yes.png')


    for i in range(60):
        if checkImageInScreen('apexpicture/goNext.png') == True:
            # 結果画面
            time.sleep(0.5)
            direct.keyDown('space')
            direct.keyUp('space')
            time.sleep(0.5)
            direct.keyDown('space')
            direct.keyUp('space')
            time.sleep(0.5)
            direct.keyDown('space')
            direct.keyUp('space')
            break

if __name__ == '__main__':
    for i in range(0,7):
        print('Round: ' + str(i))
        time.sleep(0.5)
        main()
        print('finished: ' + str(i))

