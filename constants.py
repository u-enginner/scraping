# CSV_HEADER
CSV_HEADER_ALL = [
    '氏名 (漢字)',
    '氏名 (カナ)',
    '電話番号1',
    '電話番号2',
    'E-MAIL (PC)',
    'E-MAIL (携帯)',
    'お客様番号',
    '郵便番号',
    '住所',
    'はがき送付許諾',
    '誕生日',
    '性別',
    '血液型',
    '職業',
    '要注意チェック',
    'お客様メモ',
    'その他1',
    'その他2',
    'その他3',
    '初回来店日',
    '来店きっかけ',
    '来店回数'
]
CSV_HEADER_PARTIALLY = [
    '氏名',
    '電話番号',
    '郵便番号',
    '住所'
]

# XPATH
LOGIN_XPATH = '//*[@id="idPasswordInputForm"]/div/div[2]/a'  # ログインボタン
SERTCH_XPATH = '//*[@id="search"]'  # 顧客情報検索ボタン
TABLE_XPATH = '/html/body/div[3]/div/table'  # 顧客情報テーブル
BACK_XPATH = '//*[@id="customerDetail"]/p/a'
USER_DETAILS = {
    '氏名 (漢字)': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[1]/td',
    '氏名 (カナ)': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[2]/td',
    '電話番号1': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[3]/td',
    '電話番号2': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[4]/td',
    'E-MAIL (PC)': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[5]/td',
    'E-MAIL (携帯)': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[6]/td',
    'お客様番号': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[7]/td',
    '住所': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[8]/td',
    'はがき送付許諾': '//*[@id="customerDetail"]/div[5]/table[1]/tbody/tr[9]/td',
    '誕生日': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[1]/td',
    '性別': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[2]/td',
    '血液型': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[3]/td',
    '職業': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[4]/td',
    '要注意チェック': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[5]/td',
    'お客様メモ': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[6]/td',
    'その他1': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[7]/td',
    'その他2': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[8]/td',
    'その他3': '//*[@id="customerDetail"]/div[5]/table[2]/tbody/tr[9]/td',
    '初回来店日': '//*[@id="customerDetail"]/div[7]/table[1]/tbody/tr/td',
    '来店きっかけ': '//*[@id="customerDetail"]/div[7]/table[2]/tbody/tr[1]/td',
    '来店回数': '//*[@id="customerDetail"]/div[7]/table[2]/tbody/tr[2]/td'
}

# CSS_SELECTOR
NEXTBUTTON_SELECTOR = 'body > div.contents > div > div.pb10.dbbS > div > div.columnBlock02 > div > p.next > a'

# URL
LOGIN_URL = 'https://salonboard.com/login/'  # サロンボードログイン
CUSTOMERLIST_URL = 'https://salonboard.com/KLP/customer/customerSearch/'  # 顧客情報

# UI
COMBBOX = ['顧客情報全データ取得', '氏名, 電話番号, 郵便番号, 住所']
