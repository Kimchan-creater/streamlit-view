import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io
import webbrowser
# Optional method to add title and icon to current page


import streamlit as st
import plotly.express as px
view=[31.7,150,30]
st.write('# 고민 상담소')
st.write('### 학생들이 가장 많이하는 고민')
st.write('요즘 학생들은 학업,직업, 혹은 자신의 외모에 대한 고민을 가지고 있습니다. 이러한 이유는 고등학교를 졸업한 후 대부분의 학생들은 대학을 가는 것이 필수적 관문이라 생각하기 때문입니다. 또한 학생 때에는 이성에 대한 관심이 높아지기 때문에 외모에 대한 관심 또한 높아집니다. 학생들의 고민에 대한 지수는 아래와 같습니다.')
st.write('## 학생들의 고민')

import streamlit as st
import matplotlib.pyplot as plt

labels = 'study', 'career', 'appearance', 'others'
sizes = [32, 27, 10, 31]
explode = (0.05, 0, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

st.pyplot(fig1)



st.write("출처 : 2022 통계청(파이 차트는 직접 제작함)")


import streamlit as st
st.write("위 그래프로 보았을 때 대부분의 학생들은 학업에 대한 고민이 높다는 것을 알 수 있습니다. 이는 수능에 대한 걱정이나 미래에 대한 막연한 불안 때문입니다. 그래서 이 사이트에서는 학업 관련 문제와 고민을 나눌 수 있는 공간을 만들었습니다. 저희는 여러분들이 이 사이트를 방문함으로써 학업에 대한 고민을 잘 이해하고 해결책을 찾을 수 있도록 도와드리고자 합니다. 여러분의 고민을 주저하지 말고 공유해주세요. 여러분들에게 제시받은 고민들은 위클래스에 있는 전문 상담사에게 전송됩니다!")


import streamlit as st

def main() :
        message = st.text_area('나누고 싶은 고민을 써주세요.', height=5)

if __name__ == "__main__" :
    main()

import streamlit as st
def main() :
    
    

    
    name = st.text_input('학번과 이름을 입력하세요.')

    if name != '' :
        st.write(name + '님 마지막으로 전송 버튼을 눌러주세요!')

    
if __name__ == "__main__" :
    main()



st.write("이 페이지는 미완성입니다. coming soon")