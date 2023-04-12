import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# ページのタイトル設定
st.set_page_config(
    page_title="bar",
)

# csv読み込み
df0 = pd.read_csv('test.csv', index_col=0)

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = -1
    st.session_state.df0 = df0

# 各種メニューの非表示設定
hide_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_style, unsafe_allow_html=True)

# 最初のページ
def main_page():
    st.markdown(
        "<h2 style='text-align: center;'>棒グラフ表示</h2>",
        unsafe_allow_html=True,
    )

    shop_list=st.session_state.df0.columns.values
    Day_list=st.session_state.df0.index.values
    shop_list_selector=st.sidebar.selectbox( "ショップ選択",shop_list)

    top=st.session_state.df0.sort_values(shop_list_selector,ascending=False)[:5][shop_list_selector]

    fig1, ax1 = plt.subplots()

    ax1.bar(top.index.values,top)
    ax1.set_title(shop_list_selector+"店上位5位売り上げ")
    ax1.set_xlabel("売上年月日")
    ax1.set_ylabel("総売上")

    st.pyplot(fig1)

# ページ判定
if st.session_state.page_id == -1:
    main_page()


#x軸とy軸のラベル表示
#上の度数分布表でy軸が整数になるようにする
#上の度数分布表の元データを書き換えて、正規分布のような形のヒストグラムになるようにする