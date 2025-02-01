import streamlit as st

# 入力フォームとボタンをグループ化する
with st.form(key='my_form'):
    new_content = st.text_input("書き込む内容を入力してください: ")
    submit_button = st.form_submit_button("書き込み")

if submit_button:
    # ユーザーがボタンを押したら、ここのコードが実行されます
    with open('homework_list.txt', 'a', encoding='utf-8') as file:
        file.write(new_content + '\n')
    st.info("書き込みされました。")

# 宿題リストを読み込む関数
def load_homework_list(file_name="homework_list.txt"):
    with open(file_name, 'r', encoding="utf-8") as file:
        homework_list = file.readlines()
    return homework_list    

# エラーがあった場合のための try-except ブロックを用意する
try:
    # ファイルを読み込む
    homework_list = load_homework_list("homework_list.txt")
    st.write("リストを読み込みました。")

    # チェックボックスの状態を保存するリスト
    checked_items = []

    # 宿題リストの表示
    for homework_item in homework_list:
        checked = st.checkbox(homework_item.strip(), key=homework_item.strip())
        if checked:
            checked_items.append(homework_item.strip())  # チェックされたアイテムを追加

    # チェックされたアイテムを削除するボタン
    if st.button("削除"):
        # 新しいリストを作成
        updated_list = [item for item in homework_list if item.strip() not in checked_items]

        # 更新されたリストをファイルに書き込む
        with open('homework_list.txt', 'w', encoding='utf-8') as file:
            file.writelines(updated_list)

        st.success("チェックされたアイテムが削除されました。もう一度チェックマークを押してください。")

except FileNotFoundError:
    # ファイルが見つからない場合のエラーハンドリング
    st.error("リストのファイルが見つかりません。")