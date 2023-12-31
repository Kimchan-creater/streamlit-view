import streamlit as st

st.write("# 백석고 실체")
st.write("### 계단 빌런")
st.write("최근 백석고에 커플이 생김에 따라 계단에서 만나는 일명 '계단족'이 출몰하고 있다. 이들은 복도에서 대놓고 다니는 것이 부끄럽기 때문에 계단에 몰래 숨어서 다닌다. 그러나 사람이 지나갈 때에도 남들의 시선을 신경쓰지 않는다는 다소 모순적인 태도를 보이고 있다. 일부 학생들은 '커플들 보고 있으니 배아프다.' 혹은 '저것들 알고도 저러는 거다.'와 같은 반응들을 보이고 있다.")
st.write("### 백석고의 그녀")
st.write("한 학생의 백석고 귀신, 일명 '도리귀신'의 목격담이다.")
st.write("그때는.. 비오는 날이었어요. 핸드폰을 놓고 온 것을 수업 시작 즈음에 알아서 쌤한테 말씀드리고 급식실의 뒷문으로 몰래 들어갔어요. 핸드폰을 챙기고 다시 나오려고 하고 있었죠. 왜, 급식실 지하공간 빨간불빛 아시죠? 그쪽에서 물이 한방울 한방울 떨어지는 소리와 함께 이상한 말소리가 들리고 있었어요. 비가 샌다는 것도 이상해서 핸드폰 후레쉬를 켜고 지하로 내려가려고 했죠. 그 계단 끝에 두 개로 나뉜 문이 있는데 한쪽 문이 열려있고 빛이 새어나오고 있는 거예요. 그리고 안에서 '밖에 누구야? 혹시 뭐 찾으러 왔니?' 라는 말이 들렸죠. 그 순간 번개가 번쩍이며 안에 한 손에 칼을 든 고등학생 여자애를 보았죠. 그리고 말을 하더군요. '나를 꺼내주러 온거야? 나랑 놀아주려고? 나 심심했어 일로와 재밌게 놀자.. 근데 너는 혼자네... 재미없게..' 다시한번 번개를 친 순간 그 학생은 내 앞으로 왔어요. 그리고 손에 있던 식칼을 나에게 들이밀었죠. 순간 머리가 하얘졌어요. 순식간에 정신을 잃었죠. 그리고 다시 깨어났을 때는 사이렌이 울리고 있었어요. 선생님들께서는 계단에서 순식간에 무언가를 보고 정신을 잃었다고 말씀하셨죠. 담임쌤에게 무언가를 보지 못했냐고 여쭤봤더니 건물에 들어온 사람은 영양사쌤과 담임쌤 그리고 저밖에 없었다고 했고 그곳은 잠겨있다고 했죠. 제가 본것은 뭐였을까요. 그보다, 안쪽 빛으로 희미하게 보였던 형체가... 사람머리와 머리카락 이었죠...")

import streamlit as st

st.write("### 백석고의 우월함")

st.write("빅데이터를 바탕으로 조사한 내용으로, '백석고' 자체의 데이터량이 많지 않아 정확하지 않을 수 있다.")
st.write("사람들은 백석고를 부정적으로 바라볼까?")
st.write("백석고는 일산 일반고들 중 내신이 어렵기로 유명하다. 사람들은 다른 학교들과 비교했을 때 백석고를 얼마나 부정적으로 바라볼까? 백석고와 정발고, 백신고, 저동고를 부정적으로 바라본 웹 정보들을 바탕으로 조합한 결과이다(2023.6월 ~ 2023.7월 두 달 간).")
st.write("결론 : 모든 학교는 비슷하게 부정적인 평을 받는다. 백석고를 싫어하지 말자.")

import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

import pandas as pd
df = pd.DataFrame({
  '백석고': [22,42,25,56,30],
  '정발고': [25,0,36,60,0],
  '백신고': [0,22,20,0,100],
  '저동고': [36,13,33,80,0]
})

st.line_chart(data=df)

st.write("백석고는 학구열이 강할까?")
st.write("백석고는 상대적으로 공부를 잘 하는 학생들이 모여있다고 해도 과언이 아니다. 그만큼 학구열도 높을까? 부모님들 연령대가 백석고에 얼마나 관심을 가지고 있는지를 바탕으로 조사한 결과 검색 연령 비율을 고려했을 때 백석고=27.7%, 정발고=20.7%, 백신고=12.4%, 저동고=15.1%")
st.write("결론 : 부모님들이 상당히 많은 관심을 갖는다. 상대적으로 학구열이 높다고 볼 수도 있겠다.")
st.write("추가적으로, 위의 모든 학교는 공통적으로 여성이 더 많이 관심을 가졌다. 어머니께서는 우리를 많이 사랑하신다.")
