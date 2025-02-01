import streamlit as st
# パスワードを設定
correct_password = "passnyan"
Nothing = ""

# ユーザーからの入力を受け取る
user_input = st.text_input("パスワードを入力してください:")

# 入力した文字がパスワードと同じかチェック
if user_input == correct_password:
    st.write("https://dot-labo-st-assistant-demo.streamlit.app/")  # 一致したら「OK」と表示
elif user_input == Nothing:
    st.write("・・・")
else:
    st.write("違います")  # 一致しなかったら「違います」と表示