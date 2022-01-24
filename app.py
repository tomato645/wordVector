import streamlit as st
import gensim
form PIL import Image



def do(word, count):
  word,"の類語を考えています🧐"
  
  image = Image.open('test.png')
  st.image(image, caption='Sunrise by the mountains')

  try:
    model = gensim.models.keyedvectors.load_word2vec_format("model.vec")
    answer = model.most_similar(positive = word)
  except:
    st.error('学習されていない単語です')
    st.stop()

  st.balloons()

  # 答えをforで任意の順位まで出力する
  for i in range (count):
    str(i+1),"位は",str(answer[i]),"です。"

# 言葉が適切か確認する。
def check(self):
  if self == "":
    # テキストボックスが空
    "入力してください。"
    return False
  else:
    # テキストボックスに入力された
    self,"が入力されました..."
    return True

def main():
  word = st.text_input("何か言葉を入力してください。", value="リンゴ")

  count = st.slider(label="出力の値を設定", min_value=1, max_value=10, value=5, step=1)
  st.write(str(count),"位まで出力します。")

  # ボタンを押されたら
  if st.button("実行する"):
    if check(word) == True:
      st.write("実行します")
      do(word, count)
    else:
      st.write("無効な言葉です")

if __name__ == "__main__":
  main()
