r"""
Streamlit UIを使ったコードです。
・pip install streamlit
実行は「ターミナル」で下記を打ち込みます
python -m streamlit run "C:\Users\7Java15\Desktop\Kotobaate\Kotobaate5.py"
そうすると最初は青文字でEmail：と聞いてきます。無視してリターンを押せば実行。
その後は出てきません。

・CTRL+Cでストップ
"""


import random
import streamlit as st

kotoba_a = ["あんぱん","あいどる","いのしし","うめぼし","ういるす","えだまめ","えびちり","おにぎり","おれんじ"]
kotoba_k = ["かいがら","かいしゃ","きつつき","きみどり","くさかり","くしかつ","くつした","けいたい","けんだま","こうもり"]
kotoba_s = ["さいだー","さかむけ","しまうま","しりとり","すいっち","すいえい","せいかつ","せんせい","せんたく","そうじき","そうめん",]
kotoba_t = ["たけうま","たこやき","ちゃいむ","ちりとり","つなひき","つりざお","てあらい","てぶくろ","とびばこ","とんかつ"]

kotoba = kotoba_a+kotoba_k+kotoba_s+kotoba_t

game_over = False

st.title("ことばあてゲーム～！")

#セッション保持するときの定型文
if "answer" not in st.session_state:
    st.session_state["answer"] = random.choice(kotoba)

if "typed" not in st.session_state:
    st.session_state.typed = ""

if "hint_list" not in st.session_state:
    st.session_state.hint_list = []

st.text_input("４文字ことばを入力してください（やめるの入力で終了）", key="temp_input")

current_input = st.session_state.typed + st.session_state.temp_input
st.markdown("### 現在の入力")
st.text(current_input)


if st.session_state.hint_list:
    st.markdown("## ヒント")
    for hint in st.session_state.hint_list:
        st.write(hint)
def do_ok():
    check_word = st.session_state.typed + st.session_state.temp_input
    if not check_word:
        return
    if check_word == st.session_state.answer:
        st.success("せいかい！")
        st.session_state.answer = random.choice(kotoba)
        st.session_state.typed = ""
        st.session_state.hint_list = []
    elif check_word == "やめる":
        st.write("ゲームを終了しました")
        st.session_state.typed = ""
    else:
        for i in range(min(len(st.session_state.answer),len(check_word))):
            if check_word[i] ==  st.session_state.answer[i]:
                hint = (f"{i+1}文字目が正解 ({st.session_state.answer[i]})")
                if hint not in st.session_state.hint_list:
                    st.session_state.hint_list.append(hint)
                st.write("もう一度チャレンジしよう")
                st.session_state.typed = ""

def do_quit():
    st.write("ゲームを終了しました")
    st.session_state.typed = ""
    st.session_state.hint_list = []

col_ok, col_yameru = st.columns([1,3])
with col_ok:
    st.button("OK" , on_click= do_ok)
with col_yameru:
    st.button("やめる", on_click=do_quit)
#     if st.button("OK"):
#         check_word = st.session_state.typed + st.session_state.temp_input

#         if check_word:
#                 if check_word == st.session_state.answer:
#                     st.success("せいかい！")
#                     st.session_state.answer = random.choice(kotoba)
#                     st.session_state.typed = ""
#                     st.session_state.hint_list = []
                    

#                 else:
                    # for i in range(min(len(st.session_state.answer),len(check_word))):
                    #     if check_word[i] ==  st.session_state.answer[i]:
                    #         hint = (f"{i+1}文字目が正解 ({st.session_state.answer[i]})")
                            # if hint not in st.session_state.hint_list:
                            #     st.session_state.hint_list.append(hint)
#                     st.write("もう一度挑戦しよう")
#                     st.session_state.typed = ""

# with col_yameru:
#     if st.button("やめる"):
#         check_word = st.session_state.typed + st.session_state.temp_input
#         if check_word == "やめる":
#             st.write("ゲームを終了しました")


def is_hiragana(text):
    return all(('あ' <= ch <= 'ん' ) or ch == 'ー' for ch in text)
gojuon_columns = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "　", "ゆ", "　", "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "　", "　", "　", "を"],
    ["　", "　", "　", "　", "ん"]
]

gojuon_columns_sonota = [
    ["が","ぎ","ぐ","げ","ご"],
    ["ざ","じ","ず","ぜ","ぞ"],
    ["だ","ぢ","づ","で","ど"],
    ["ば","び","ぶ","べ","ぼ"],
    ["ぱ","ぴ","ぷ","ぺ","ぽ"],
    ["ゃ","　","ゅ","　","ょ"],
    ["っ","　","　","　","ー"],
]

# 右から左に並べるために reverse
gojuon_columns_reversed = list(reversed(gojuon_columns))


st.markdown("### あいうえおリスト")

cols = st.columns(len(gojuon_columns_reversed))  # 11列

for col_idx, col_chars in enumerate(gojuon_columns_reversed):
    with cols[col_idx]:
        for row_idx, char in enumerate(col_chars):
            if char.strip() and st.button(char, key=f"btn_{char}_{col_idx}_{row_idx}"):
                st.session_state.typed += char

st.markdown("### その他ボタン")
gojuon_columns_sonota_reversed = list(reversed(gojuon_columns_sonota))
cols2 = st.columns(len(gojuon_columns_sonota_reversed))

for col2_idx, col2_chars in enumerate(gojuon_columns_sonota_reversed):
    with cols2[col2_idx]:
        for row_idx, char in enumerate(col2_chars):
            if char.strip() and st.button(char, key=f"btn_{char}_sonota_{col2_idx}_{row_idx}"):
                st.session_state.typed += char
