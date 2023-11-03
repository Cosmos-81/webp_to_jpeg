from PIL import Image
import os
import sys
import glob

def main():
    
    # 初回ログファイル生成
    log_path = os.path.join(os.path.dirname(sys.argv[0]),"log.txt")  # ログファイルのパス生成
    open(log_path, 'w',encoding='UTF-8',newline='').close            # ログファイル.txtを生成
    flog = open(log_path, 'a',encoding='UTF-8',newline='')           # 追記形式で開く

    # .webpのリスト
    s_key = generat_glob_key()                                       # 配下検索用のglobキー生成
    webp_list = glob.glob(s_key,recursive=True)                      # globで一致する.webpリストを取得

    # .webpがない場合
    if len(webp_list) == 0:
        str_logline = 'E:.webpがありません'
        w_log(flog,str_logline)
        return

    # リストを処理
    for img_file in webp_list:

        fdir = os.path.dirname(img_file)                             # イメージファイルのディレクトリ
        fname = os.path.basename(img_file).replace(".webp",".jpg")   # イメージファイルの変換後拡張子
        save_path = os.path.join(fdir,fname)                         # イメージファイルの変換後保存パス

        if not(os.path.exists(save_path)):                           # 既に変換済みファイルがあるか
            
            str_logline = '変換中,' + img_file                      
            w_log(flog,str_logline)                                 

            img = Image.open(img_file).convert("RGB")                # 変換処理
            img.save(save_path,"jpeg")                               # 変換した画像(.jpg)を保存
            
            str_logline = '変換済,' + save_path
            w_log(flog,str_logline)

        else:
            str_logline = 'E:重複した変換処理,' + img_file
            w_log(flog,str_logline)

    flog.close() # ログファイルを閉じる

# デバッグ出力・ログファイル書出
def w_log(log_f,line):
    log_f.write(line + '\r\n')
    print('AYASE > ' + line)

# glob検索キーを生成
def generat_glob_key():
    current_dir = os.path.dirname(sys.argv[0])
    glob_key = current_dir + "/**/*.webp"
    return glob_key

if __name__ == '__main__':
    main()