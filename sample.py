import time
import csv
import os
import re
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import constants


def main(userid, password, waittime, combbox, file_name):
    """scraping main"""
    try:
        isAll = False
        # コンボボックスの判定
        if combbox == constants.COMBBOX[0]:
            isAll = True

        # WEBブラウザの起動
        if os.name == 'nt':
            # OSがWindows
            driverPath = './webdriver/win/chromedriver.exe'
        elif os.name == 'posix':
            # OSがUnix系
            driverPath = './webdriver/mac/chromedriver'
        driver = webdriver.Chrome(executable_path=driverPath)

        # サロンボードに遷移
        driver.get(constants.LOGIN_URL)

        # ログイン
        login(driver, userid, password)

        # ログインの成否判定
        time.sleep(1)
        if driver.title == 'SALON BOARD : ログイン エラー':
            raise Exception

        if waittime:
            # 10秒停止 ※画像認証が実行される可能性あり
            time.sleep(10)

        # CSVファイル作成
        writer = createCsv(isAll, file_name)

        # サロンボードをスクレイピング
        scrapingSalonBord(driver, writer, isAll)
    except Exception as e:
        print(e)
        messagebox.showerror(
            'エラー',
            'エラーが発生しました。ユーザーID/パスワードが正しいかご確認ください。'
        )
        raise Exception
    finally:
        # WEBブラウザを閉じる
        driver.quit()


def createCsv(isAll, file_name):
    """CSVファイルの作成"""
    csv_header = ''
    if isAll:
        csv_header = constants.CSV_HEADER_ALL
    else:
        csv_header = constants.CSV_HEADER_PARTIALLY

    result_dir = './result'
    os.makedirs(result_dir, exist_ok=True)
    f = open(file_name + '.csv', 'w', encoding='utf-8', errors='ignore')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(csv_header)
    return writer


def login(driver, userid, password):
    """サロンボードにログイン"""
    # userIdとpasswordを入力
    loginID = driver.find_element(By.NAME, 'userId')
    loginPass = driver.find_element(By.NAME, 'password')
    loginID.send_keys(userid)
    loginPass.send_keys(password)

    # ログインボタンをクリック
    driver.find_element(By.XPATH, constants.LOGIN_XPATH).click()


def scrapingSalonBord(driver, writer, isAll):
    """サロンボードをスクレイピング"""
    # 顧客情報に移動
    driver.get(constants.CUSTOMERLIST_URL)
    time.sleep(1)

    # 検索するをクリック
    driver.find_element(By.XPATH, constants.SERTCH_XPATH).click()
    time.sleep(1)

    # 顧客情報のページ分ループ
    while True:
        try:
            # 顧客情報テーブルを取得
            tableElem = driver.find_element(By.XPATH, constants.TABLE_XPATH)
            trElem = tableElem.find_elements(By.TAG_NAME, 'tr')

            # 顧客情報テーブルの件数分ループ
            for i in range(1, len(trElem)):
                # ユーザー詳細を取得してCSVに出力
                writeCsv(driver, tableElem, i, writer, isAll)

            # 顧客情報の「次へ」をクリック
            driver.find_element(
                By.CSS_SELECTOR, constants.NEXTBUTTON_SELECTOR).click()
            time.sleep(1)

        except Exception:
            break


def writeCsv(driver, tableElem, i, writer, isAll):
    """ユーザー詳細を取得してCSVに出力"""
    csvlist = []

    # ユーザー詳細ページに移動
    xpathStr = f'/html/body/div[3]/div/table/tbody/tr[{i}]/td[1]/a'
    driver.find_element(By.XPATH, xpathStr).click()
    time.sleep(1)

    # ユーザー詳細
    csvlist = getUserDetails(driver, csvlist, isAll)

    # CSVファイルへ書き込み
    writer.writerow(csvlist)

    # 顧客情報一覧へ戻る
    driver.find_element(By.XPATH, constants.BACK_XPATH).click()


def getUserDetails(driver, csvlist, isAll):
    """XPATHからユーザー詳細を取得"""
    if isAll:
        getInfo(driver, csvlist, constants.USER_DETAILS['氏名 (漢字)'])
        getInfo(driver, csvlist, constants.USER_DETAILS['氏名 (カナ)'])
        getInfo(driver, csvlist, constants.USER_DETAILS['電話番号1'])
        getInfo(driver, csvlist, constants.USER_DETAILS['電話番号2'])
        getInfo(driver, csvlist, constants.USER_DETAILS['E-MAIL (PC)'])
        getInfo(driver, csvlist, constants.USER_DETAILS['E-MAIL (携帯)'])
        getInfo(driver, csvlist, constants.USER_DETAILS['お客様番号'])
        getAddress(driver, csvlist, constants.USER_DETAILS['住所'])
        getInfo(driver, csvlist, constants.USER_DETAILS['はがき送付許諾'])
        getInfo(driver, csvlist, constants.USER_DETAILS['誕生日'])
        getInfo(driver, csvlist, constants.USER_DETAILS['性別'])
        getInfo(driver, csvlist, constants.USER_DETAILS['血液型'])
        getInfo(driver, csvlist, constants.USER_DETAILS['職業'])
        getInfo(driver, csvlist, constants.USER_DETAILS['要注意チェック'])
        getInfo(driver, csvlist, constants.USER_DETAILS['お客様メモ'])
        getInfo(driver, csvlist, constants.USER_DETAILS['その他1'])
        getInfo(driver, csvlist, constants.USER_DETAILS['その他2'])
        getInfo(driver, csvlist, constants.USER_DETAILS['その他3'])
        getInfo(driver, csvlist, constants.USER_DETAILS['初回来店日'])
        getInfo(driver, csvlist, constants.USER_DETAILS['来店きっかけ'])
        getInfo(driver, csvlist, constants.USER_DETAILS['来店回数'])
    else:
        getInfo(driver, csvlist, constants.USER_DETAILS['氏名 (漢字)'])
        getInfo(driver, csvlist, constants.USER_DETAILS['電話番号1'])
        getAddress(driver, csvlist, constants.USER_DETAILS['住所'])

    return csvlist


def getInfo(driver, csvlist, xpath):
    """顧客情報の取得"""
    value = driver.find_element(By.XPATH, xpath).text
    # 改行コードを半角スペースに置換
    value = value.replace('\n', ' ')
    csvlist.append(value)


def getAddress(driver, csvlist, addressXpath):
    """住所の取得"""
    postCode = '-'
    address = '-'
    strAddress = ''
    value = []

    # 住所を取得
    value = driver.find_element(By.XPATH, addressXpath).text.splitlines()

    if re.match('[0-9]{3}-?[0-9]{4}', value[0]):
        # 郵便番号が有り
        postCode = value[0]
        for i in range(1, len(value)):
            strAddress += value[i]
        address = strAddress
    else:
        # 郵便番号が無し
        for i in range(0, len(value)):
            strAddress += value[i]
        address = strAddress

    csvlist.append(postCode)
    csvlist.append(address)


# if __name__ == '__main__':
#    main
