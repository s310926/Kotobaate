import random

kotoba_a = ["あんぱん","あいどる","いのしし","うめぼし","ういるす","えだまめ","えびちり","おにぎり","おれんじ"]
kotoba_k = ["かいがら","かいしゃ","きつつき","きみどり","くさかり","くしかつ","くつした","けいたい","けんだま","こうもり"]
kotoba_s = ["さいだー","さかむけ","しまうま","しりとり","すいっち","すいえい","せいかつ","せんせい","せんたく","そうじき","そうめん",]
kotoba_t = ["たけうま","たこやき","ちゃいむ","ちりとり","つなひき","つりざお","てあらい","てぶくろ","とびばこ","とんかつ"]

kotoba = kotoba_a+kotoba_k+kotoba_s+kotoba_t

answer = random.choice(kotoba)
print(answer)

# input_answer = input("言葉を入力してください>>")

while True: #正解するまでループ
    input_answer = input("言葉を入力してください>>")
    if input_answer == answer:
        print("正解")
        break
    else :
        for i in range(len(answer)):
            if i < len(input_answer) and input_answer[i] == answer[i]:
                print(f"{i+1}文字目が正解 ({answer[i]})")
        print("もう一度挑戦しよう")

