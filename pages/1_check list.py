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

    # 宿題リストの表示
    for homework_item in homework_list:
        st.checkbox(homework_item.strip(), key=homework_item.strip())
except FileNotFoundError:
    # ファイルが見つからない場合のエラーハンドリング
    st.error("リストのファイルが見つかりません。")