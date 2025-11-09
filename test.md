---

# 1. **한국어 감성분류 구현 (LSTM) - TensorFlow**

NLP(자연어 처리, Natural Language Processing)는 스팸 처리, 뉴스 분류, 텍스트 요약, 문장 생성, 기계 번역, 챗봇, 감성 분류등 다양한 분야에 활용되고 있습니다. 

일단 먼저 자연어를 처리하는 방법을 살펴본 후 LSTM을 이용하여 감성 분류 모델을 직접 구현해 보도록 하죠.

## 1.1 **자연어 처리 방법**

텍스트 데이터는 구조화되어 있지도 않고 데이터의 길이가 일정하지 않습니다. 

한글을 입력 데이터로 활용하기 위해서는 

1️⃣ 문장을 특정한 기준으로 잘라내야 합니다. 

이렇게 잘라낸 조각을 우리는 token이라고 부르죠. 영어는 이 token을 만드는 과정이 비교적 간단합니다. 띄어쓰기를 기준으로 잘라내면 되기 때문이죠. 하지만 한글은 조사(~가, ~을, ~처럼 같은)가 붙어 있어서 잘라내는 작업에 어려움이 있습니다. ( 형태소 분석을 해야 합니다. )

token을 잘라내는 역할을 하는 것을 tokenizer라고 하는데 이 tokenizer가 불용어(stopword) 처리를 통해 조사와 같은 불필요한 단어를 제거하는 기능을 수행합니다.

2️⃣ Vocabulary(단어사전, 어휘사전)를 생성해야 합니다. 

한글과 숫자를 1:1 매칭하는 방식으로 Vocabulary(단어사전, 어휘사전)를 만들어야 합니다. 이 단어사전은 모든 단어(token)를 숫자로 매핑한 사전을 의미합니다.

3️⃣ 한글을 숫자로 변환합니다.

4️⃣ 문장의 길이가 다를 경우 deep learning 모델에 입력으로 넣기 위해서는 길이를 동일하게 맞춰야 합니다.

간단하게 정리하면 문장 텍스트 데이터를 deep learning 모델에 입력으로 넣기 위해서 다음과 같은 작업이 필요합니다.

1️⃣ 토큰화 → tokenizer를 이용하여 문장을 띄어쓰기로 구분하고 불용어 처리

2️⃣ 단어 사전 작성 → 단어와 숫자를 매핑

3️⃣ 문자 인코딩 → 단어 사전을 바탕으로 token들을 숫자로 변경

4️⃣ padding → 인코딩된 문장 길이를 동일하게 변경

아래의 그림은 두 개의 문장을 인코딩과 패딩을 통해 동일한 길이의 데이터로 만드는 것에 대한 예시입니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f0d9b0b-32dc-4378-a446-13826f4b2e66/b894205f-9edd-4c9d-868d-f65d72e0b256/Untitled.png)

단어사전을 만들 때 단어의 순서가 아니라 일반적으로 단어의 빈도를 이용해 높은 빈도를 가지는 단어가 앞 번호를 가지도록 만듭니다.

tensorflow keras에서 제공하는 Tokenizer는 띄어쓰기를 기준으로 단어 사전을 생성하고 단어를 쉽게 encoding할 수 있도록 도와줍니다. 위의 그림에 있는 문장을 이용하여 코드를 작성하고 수행시켜 보도록 하겠습니다.

```python
%reset -f

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    '영실이는 나를 정말 정말 좋아해',
    '영실이는 영화를 좋아해'
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

print('단어 인덱스 : ', tokenizer.word_index)
# tokenizer.word_index : 등장 빈도수를 기준으로 가장 많이 나온 단어부터 
# 낮은 정수 인덱스를 부여한 딕셔너리 => Vocabulary 
# 단어 인덱스 :  {'영실이는': 1, '정말': 2, '좋아해': 3, '나를': 4, '영화를': 5}

# texts_to_sequences() 함수는 입력된 문장을 단어 index를 사용해
# 숫자 vector로 변환

word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)
# [[1, 4, 2, 2, 3], [1, 5, 3]]
```

만약 단어 사전에 없는 새로운 단어가 등장하면 새로운 단어는 encoding할 때 무시됩니다. 다음 코드를 보시죠.

```python
%reset -f

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    '영실이는 나를 정말 정말 좋아해',
    '영실이는 영화를 좋아해'
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
print(tokenizer.word_index)
# {'영실이는': 1, '정말': 2, '좋아해': 3, '나를': 4, '영화를': 5}

new_sentences = ['영실이는 경록이와 나를 좋아해']
new_word_encoding = tokenizer.texts_to_sequences(new_sentences)
print(new_word_encoding)
# [[1, 4, 3]]   4개의 token이 도출되지만 encoding된 결과는 3개이다.
```

사전에 없는 단어가 등장하면 어떻게 할까? 위의 예처럼 그냥 없애버리면 되나? 사전에 존재하지 않는 단어를 OOV(out of vocabulary) token이라고 합니다. keras Tokenizer는 이 OOV token을 처리하기 위해 파라미터를 설정할 수 있습니다.

```python
%reset -f

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    '영실이는 나를 정말 정말 좋아해',
    '영실이는 영화를 좋아해'
]

tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)

print('단어 인덱스 : ', tokenizer.word_index)
# 단어 인덱스 :  {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}

new_sentences = ['영실이는 경록이와 나를 좋아해']
new_word_encoding = tokenizer.texts_to_sequences(new_sentences)
print(new_word_encoding)
# [[2, 1, 5, 4]]
```

텍스트 데이터셋에 빈도수가 작은 단어가 많이 존재하는 경우에는 이들 단어를 제외하는게 일반적입니다. 즉, 문장을 token으로 인코딩할 때 빈도수가 많은 순서대로 최대 사전 개수를 정하고 빈도수가 적은 단어를 제외시킵니다. 최대 사전 개수는 num_words 파라미터로 설정할 수 있습니다. 아래의 코드를 보시죠.

한가지 주의해야 할 점은 num_words=3이라고 하면 index < num_words인 단어만 사용됩니다. 즉, index 1과 2만 사용됩니다. ( Keras의 Tokenizer는 일반적으로 index 1부터 단어 인덱싱을 시작합니다. )

```python
%reset -f

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    '영실이는 나를 정말 정말 좋아해',
    '영실이는 영화를 좋아해'
]

tokenizer = Tokenizer(num_words=3, 
                      oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)

print('단어 인덱스 : ', tokenizer.word_index)
# 단어 인덱스 :  {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}

new_sentences = ['영실이는 경록이와 나를 좋아해']
new_word_encoding = tokenizer.texts_to_sequences(new_sentences)
print(new_word_encoding)
# [[2, 1, 1, 1]]
```

순환신경망에 데이터를 입력으로 넣기 위해서는 문장의 길이를 동일하게 맞춰야 합니다. 이를 padding이라고 부릅니다. 

keras의 pad_sequences 함수를 이용하면 이 작업을 쉽게 할 수 있습니다.

```python
%reset -f

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    '영실이는 나를 정말 정말 좋아해',
    '영실이는 영화를 좋아해'
]

tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)

print('단어 인덱스 : ', tokenizer.word_index)
# 단어 인덱스 :  {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}

word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)
# [[2, 5, 3, 3, 4], [2, 6, 4]]

padded = pad_sequences(word_encoding, 
                       maxlen=4)
print(padded)
# [[5 3 3 4]
#  [0 2 6 4]]
```

자연어 처리를 위해서는 Embedding과정이 반드시 필요합니다. Word2Vec과 같은 기법을 이용할 수 있지만 우리는 tensorflow keras를 이용하니 keras에서 제공하는 Embedding layer를 사용하도록 하겠습니다.

## 1.2 **한국어 감성분석 구현 - 데이터 로딩**

기본적인 내용은 배웠으니 이제 실제로 구현을 해 보죠.

먼저 필요한 module을 불러옵니다.

```python
%reset -f

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import tensorflow as tf
import warnings
warnings.filterwarnings(action='ignore')
```

사용할 데이터 셋은 네이버 영화 리뷰 데이터를 이용하도록 하겠습니다. 다음의 코드로 파일을 받을 수 있습니다.

```python
# Naver sentiment movie corpus V1.0 

# ratings_train.txt는 train 파일이고
# ratings_test.txt는 test 파일입니다. 

train_file = tf.keras.utils.get_file(
    cache_dir='.',  # 상대경로설정 가능
    fname='ratings_train.txt',                        
    origin='https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',
    extract=True
)

train_path = os.path.join('./datasets', 
                          'ratings_train.txt')

train_df = pd.read_csv(train_path, sep='\t')
display(train_df.head(), train_df.shape)  
# (150000, 3)

test_file = tf.keras.utils.get_file(
    cache_dir='.',  
    fname='ratings_test.txt',                                     
    origin='https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt',
    extract=True
)

test_path = os.path.join('./datasets', 
                         'ratings_test.txt')
test_df = pd.read_csv(test_path, sep='\t')
display(test_df.head(), test_df.shape)  
# (50000, 3)
```

아래의 링크를 이용하면 text파일을 다운받으실 수 있습니다.

[ratings_train.txt](attachment:fa9edb49-9352-4b10-a6c3-01cd990bb665:ratings_train.txt)

[ratings_test.txt](attachment:ab59350b-772c-4061-9be3-31592bf285f7:ratings_test.txt)

DataFrame의 내용을 간단히 살펴보면 다음과 같습니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f0d9b0b-32dc-4378-a446-13826f4b2e66/41d0f45a-7031-4dd7-ab1a-a1e2c1d2747f/Untitled.png)

총 200,000개의 데이터가 있으며 train 데이터가 150,000개 test 데이터가 50,000개로 구성되어 있습니다. 

- 모든 Review의 길이는 140자 이내이며,
- 실제 영화 리뷰 점수는 1점에서 10점으로 이루어져 있습니다.
- 이 중 9점~10점을 긍정적인 Review, 1점~4점을 부정적 Review로 분류한 데이터 입니다. (참고로 5점~8점의 데이터는 포함하지 않았습니다.)

## 1.3 **한국어 감성분석 구현 - EDA(탐색적 데이터분석)**

간단한 EDA(탐색적 데이터분석)를 해 보죠. 전체 데이터를 파악하고 전처리가 필요한 부분을 찾아봐야 합니다. 여기서는 데이터 크기 및 샘플 확인, 레이블 비율, 결측치등을 확인해 보겠습니다.

```python
train_df = pd.read_csv(train_path, sep='\t')
display(train_df.head(), train_df.shape)  # (150000, 3)

# 감성분석을 위한 텍스트분류 모델에서 필요한 값은 document와 label입니다. 
# 총 150,000개의 데이터가 존재합니다. 

# label에 들어 있는 긍정과 부정의 비율을 확인해야 합니다. 참고로 데이터의 불균형이
# 발생하면 훈련이 정상적으로 이루어지기 어렵습니다. 

cnt = train_df['label'].value_counts()
print(cnt)

# 0    75173
# 1    74827
# Name: label, dtype: int64

# 0(부정)의 개수가 75,173개 1(긍정)의 개수가 74,82개로 비슷한 비율로
# 데이터가 구성되어 있음을 확인할 수 있습니다. 

# 결측치 확인

print(train_df.isnull().sum())

# id          0
# document    5
# label       0
# dtype: int64

# Review글이 없는 데이터가 5개가 존재합니다. 의미가 없는 데이터이기 때문에
# 결측치가 있는 데이터는 추후에 삭제해야 합니다.
```

## 1.4 **한국어 감성분석 구현 - 형태소 분석**

한국어 형태소 분석기는 여러가지가 개발되어 있습니다. 대표적으로 Komoran, Okt, Mecab, Kiwi등이 있습니다. 영어는 띄어쓰기가 잘 되어 있는 편이지만 한글은 띄어쓰기, 맞춤법이 잘못됬을 경우 분리에 어려움이 많습니다. 또한 정확한 형태소 분석을 위해서는 전처리 과정이 필요할 수 있습니다.

실무나 연구에서 가장 많이 사용되는 형태소 분석기 3가지를 꼽자면 다음과 같습니다.

1. Mecab (메캅) - 가장 널리 사용됨
    - C++ 기반이라서 속도가 빠르고, 정확도 높고, 실무에 최적화되어 있습니다.
    - 설치가 다소 복잡한 단점이 있습니다.
2. Okt (Open Korean Text Processor) - 트위터에서 개발
    - 초보자가 사용하기 쉽고 설치가 간편합니다.
    - 속도가 느리고 정확도가 Mecab보다 낮습니다.
    - 내부적으로 JVM을 사용하기 때문에 Java를 설치해야 합니다.
3. Kiwi – 각광받는 신형 분석기
    - 최신 딥러닝 기반
    - 띄어쓰기 오류에 강함
    - 설치에 별도 라이브러리 필요합니다.

Mecab을 설치해서 사용하도록 하겠습니다. 

Colab에서 설치하는 방법과 WSL 환경에서 설치하는 방법에 대해서 알아보죠.

✅ Colab에서 Mecab 설치

```python
# 1. 필요한 패키지 설치
!apt-get update -qq
!apt-get install -y git curl build-essential

# 2. Mecab-ko 설치 스크립트 복제
!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
%cd Mecab-ko-for-Google-Colab

# 3. 설치 스크립트 실행(시간이 조금 걸립니다. 2-3분)
!bash install_mecab-ko_on_colab_light_220429.sh
%cd ..

# 4. Python 패키지 설치
!pip install konlpy
!pip install mecab-python3

# 5. Runtime 재시작!!
```

✅ Ubuntu (WSL2) 환경에서 Mecab 설치를 진행해보죠.

- 필요한 패키지 설치
    
    ```python
    sudo apt update
    sudo apt install -y make curl git build-essential autoconf automake libtool
    ```
    
- Mecab 본체 설치
    
    ```python
    sudo apt install -y mecab libmecab-dev mecab-ipadic-utf8
    ```
    
- Mecab 한국어 사전 설치 (mecab-ko-dic)
    
    ```python
    cd /tmp
    
    # mecab-ko-dic 다운로드
    wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
    tar zxfv mecab-ko-dic-2.1.1-20180720.tar.gz
    cd mecab-ko-dic-2.1.1-20180720
    
    # 설치 경로 확인
    mecab-config --dicdir
    # 보통 /usr/lib/x86_64-linux-gnu/mecab/dic 또는 /usr/local/lib/mecab/dic
    
    # 사전 컴파일 및 설치
    ./autogen.sh
    ./configure
    make
    sudo make install
    ```
    
- 설정파일 수정 - Mecab이 한국어 사전을 사용하도록 설정
    
    ```python
    # mecab 설정 파일 위치 확인
    mecab-config --sysconfdir
    
    # 설정 파일 수정 (경로는 시스템에 따라 다를 수 있음)
    sudo vi /etc/mecabrc
    # 또는
    sudo vi /usr/local/etc/mecabrc
    
    파일 내용을 다음과 같이 수정:
    dicdir = /usr/local/lib/mecab/dic/mecab-ko-dic
    ```
    
- 설치확인
    
    ```python
    # Mecab 버전 확인
    mecab --version
    # mecab of 0.996/ko-0.9.2
    
    # 한국어 테스트
    echo "이것은 소리없는 아우성!" | mecab
    
    # 이것    NP,*,T,이것,*,*,*,*
    # 은      JX,*,T,은,*,*,*,*
    # 소리    NNG,*,F,소리,*,*,*,*
    # 없      VA,*,T,없,*,*,*,*
    # 는      ETM,*,T,는,*,*,*,*
    # 아우성  NNG,*,T,아우성,*,*,*,*
    # !       SF,*,*,*,*,*,*,*
    # EOS
    ```
    
- Python에서 사용
    
    ```python
    pip install mecab-python3
    pip install konlpy
    ```
    

설치가 잘 되었는지 다음 코드로 확인해보죠.

```python
from konlpy.tag import Okt, Mecab

# okt = Okt()
mecab = Mecab()
# mecab = MeCab(dicpath='/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic')

text = '이것은 소리없는 아우성. 저 푸른 해원을 향하여 흔드는 영원한 노스탤지어의 손수건'

# morphs() : 텍스트에서 형태소를 반환합니다. 
# pos() : 텍스트에서 품사 정보를 부착하여 반환합니다.

# print(okt.morphs(text))
# ['이', '것', '은', '소리', '없는', '아우성', '.', '저', '푸른', '해원', '을', '향', '하여', 
#  '흔드는', '영원한', '노스탤지어', '의', '손수건']

# print(okt.pos(text))
# [('이', 'Determiner'), ('것', 'Noun'), ('은', 'Josa'), ('소리', 'Noun'), ('없는', 'Adjective'), 
#  ('아우성', 'Noun'), ('.', 'Punctuation'), ('저', 'Noun'), ('푸른', 'Noun'), ('해원', 'Noun'), 
#  ('을', 'Josa'), ('향', 'Noun'), ('하여', 'Verb'), ('흔드는', 'Verb'), ('영원한', 'Adjective'), 
#  ('노스탤지어', 'Noun'), ('의', 'Josa'), ('손수건', 'Noun')]

print(mecab.morphs(text))
# ['이것', '은', '소리', '없', '는', '아우성', '.', '저', '푸른', '해원', '을', '향하', '여', 
#  '흔드', '는', '영원', '한', '노스탤지어', '의', '손수건']
print(mecab.pos(text))
# [('이것', 'NP'), ('은', 'JX'), ('소리', 'NNG'), ('없', 'VA'), ('는', 'ETM'), ('아우성', 'NNG'), 
#  ('.', 'SF'), ('저', 'NP'), ('푸른', 'VA+ETM'), ('해원', 'NNG'), ('을', 'JKO'), ('향하', 'VV'), 
#  ('여', 'EC'), ('흔드', 'VV'), ('는', 'ETM'), ('영원', 'NNG'), ('한', 'XSA+ETM'), ('노스탤지어', 'NNG'), 
#  ('의', 'JKG'), ('손수건', 'NNG')]
```

위의 결과처럼 어떠한 형태소 분석기를 사용하느냐에 따라 결과가 달라집니다. 

당연히 형태소 분리의 결과가 모델 성능에 큰 영향을 주게 됩니다. 따라서 띄어쓰기와 맞춤법에 맞는 문장으로 이루어진다면 좋은 성능을 기대할 수 있습니다. 한가지 추가적으로 용량이 큰 텍스트를 사용할 경우 성능외에 속도 역시 중요한 요소가 됩니다.

Mecab은 windows 환경에서 지원되지 않지만 Colab환경이나 WSL2 Ubuntu 환경에서 사용할 수 있기 때문에 Mecab을 사용하면 빠른 속도로 조금 더 나은 성능을 기대할 수 있습니다. 

## 1.5 **한국어 감성분석 구현 - 데이터 전처리**

데이터를 확인해 보면 알겠지만 몇가지 데이터 전처리를 진행해야 합니다.

1. 우리의 Review 텍스트 데이터에는 특수문자, 숫자등이 포함되어 있습니다. 정규식을 활용해 영어, 한글, 띄어쓰기만 남기고 나머지 특수문자를 제거해야 합니다.
2. 결측치를 제거해야 합니다. (5개)
3. stopword(불용어)를 제거해야 합니다.
    
    불용어란 자연어처리(NLP)에서 의미 분석에 큰 영향을 주지 않는 단어를 말합니다. 즉, 의미보다는 문법적으로 자주 쓰이는 단어로, 분석 시 제외할 수 있는 단어들을 말합니다.
    
4. 단어사전을 만들고 문자를 숫자로 변경하는 token화를 진행해야 합니다.
5. 동일한 문장 길이로 정리해야 합니다. (padding)

위의 내용을 코드로 표현하면 다음과 같습니다. 다음의 코드는 Colab에서 GPU를 사용해서 실행시켜야 합니다. CPU로 작업하면 시간이 너무 오래 걸립니다. Colab에서 GPU로 작업해도 약 9분이 소요됩니다.

```python
%reset -f

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import tensorflow as tf
import warnings

warnings.filterwarnings(action='ignore')

# Naver sentiment movie corpus V1.0 

train_file = tf.keras.utils.get_file(
    cache_dir='.',  
    fname='ratings_train.txt', 
    origin='https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',
    extract=True
)

train_path = os.path.join('./datasets', 
                          'ratings_train.txt')

train_df = pd.read_csv(train_path, sep='\t')
display(train_df.head(), train_df.shape)  # (150000, 3)

# 1. 정규식을 활용해 영어, 한글, 띄어쓰기만 남기고 나머지 특수문자를 제거
train_df['document'] = train_df['document'].str.replace(r'[^A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ ]', 
                                                        '', 
                                                        regex=True)
display(train_df.head())  

# 2. 결측지 제거 (5개)
train_df = train_df.dropna()
print(train_df.shape) # (149995, 3) 
```

```python
# 3. 불용어(stopword)제거
# 불용어는 관사, 전치사, 조사, 접속사등 의미가 없는 단어를 의미합니다. 
# 한글에는 정말 많은 불용어가 존재하는데 이 중 일부만 처리하도록 합니다. 
# 불용어를 처리하는 함수를 정의한 후 이용합니다. 

from konlpy.tag import Okt, Mecab
from tqdm import tqdm

# from tqdm.notebook import tqdm
tqdm.pandas()  # tqdm을 pandas에 등록

mecab = Mecab()
# okt = Okt()

def word_tokenization(text):
    # stop_words = ['는', '을', '를', '이', '가', '의', '던', '고', '하', '다', 
    #               '은', '에', '들', '지', '게', '도']
    
    stop_words = [
    # 조사
    '은', '는', '이', '가', '을', '를', '에', '에서', '에게', '한테', '으로', '로',
    '과', '와', '도', '만', '이나', '보다', '처럼', '까지', '부터', '라도', '마저',

    # 접속사
    '그리고', '그러나', '하지만', '그래서', '그러면', '그런데', '따라서', '혹은', '또는',

    # 의존명사/형식적 명사
    '수', '것', '거', '때', '중', '등', '뿐', '대로', '만큼', '따위',

    # 대명사/지시어
    '나', '너', '우리', '저희', '그', '이', '저', '그것', '이것', '저것', '자기',

    # 일반 동사/보조용언
    '되다', '하다', '있다', '없다', '이다', '아니다', '받다', '주다', '되어다', '같다', '되었다',

    # 감탄사/불필요 표현
    '아', '야', '어', '우와', '헐', '음', '응', '네', '예', '자', '좀', '요', '그냥', '또', '그래',

    # 빈도 높은 불필요 어휘
    '정말', '진짜', '너무', '매우', '아주', '항상', '더', '더욱', '계속', '이미', '이제',

    # 불용 보조 용언/어미 어절
    '것이다', '것이', '때문이다', '있습니다', '없습니다', '하는', '해서', '하였다', '했다', '하고', '하며', '하면서',

    # 기타 (프로젝트 목적 따라 제거 가능)
    '하지만', '그러나', '혹시', '그러면', '그럼', '혹은', '만약', '만일', '또는'
    ]

    return [word for word in mecab.morphs(text) if word not in stop_words]

data_train = train_df['document'].progress_apply(word_tokenization)
print(data_train.head())
# 0                                     [빙, 짜증, 네요, 목소리]
# 1    [흠, 포스터, 보고, 초딩, 영화, 줄, 오버, 연기, 조차, 가볍, 지, 않, 구나]
# 2                                  [재, 밓었다그래서보는것을추천한다]
# 3                [교도소, 이야기, 구먼, 솔직히, 재미, 없, 다, 평점, 조정]
# ...
```

```python
# 4. 단어사전을 만들고 문자를 숫자로 변경하는 token화를 진행

from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(data_train)
print('총 단어 개수 : ', len(tokenizer.word_index))
# 총 단어 개수 :  52185

# print(tokenizer.word_index)

# print(tokenizer.word_counts)

# print(tokenizer.word_counts.values())

# 단어빈도가 5회 이상인 단어가 몇개인지 확인
def get_voca_size(threshold):
    cnt = 0
    for x in tokenizer.word_counts.values():
        if x > threshold:
            cnt = cnt + 1
    return cnt

voca_size = get_voca_size(5)
print('vocabulary size : ', voca_size)
# vocabulary size :  13727

# 단어 사전을 생성합니다.

oov_token = '<OOV>'  # 사전에 없는 단어
voca_size = 15000  # 5 이상의 빈도를 가지는 단어는 총 19,338개 이지만 15000개로 설정

tokenizer = Tokenizer(oov_token=oov_token, 
                      num_words=voca_size)
tokenizer.fit_on_texts(data_train)

# print(tokenizer.word_index)

print('vocabulary size : ', len(tokenizer.word_counts))
# vocabulary size :  52185

# 이제 각 문장을 숫자 벡터로 변환하여 encoding
data_train_seq = tokenizer.texts_to_sequences(data_train)
print(data_train_seq[:2])
# [[20, 893, 26, 196, 22, 672], 
#  [939, 458, 305, 603, 2, 95, 1533, 37, 764, 926, 9, 30, 341]]

# 5. 동일한 문장 길이로 정리해야 합니다.
# 이 작업을 하기 위해 문장 최대 길이를 구해보죠.
max_length = max(len(x) for x in data_train_seq)
print('문장 최대 길이 : ', max_length)
# 문장 최대 길이 :  75

# 문장의 길이를 동일하게 맞추기 위해 pad_sequences 함수를 이용합니다. 
# 이때, 최대길이보다 짧은 문장은 문장 앞에 0을 붙여서 길이를 맞춥니다. 

from tensorflow.keras.preprocessing.sequence import pad_sequences

x_data_train = pad_sequences(data_train_seq,
                             truncating='post',
                             padding='pre',
                             maxlen=max_length)

y_data_train = np.asarray(train_df['label'])

print('샘플 형태 : ', x_data_train[:1])
# [[  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
#     0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
#     0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
#     0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  20 893  26
#   196  22 672]]
```

## 1.6 **한국어 감성분석 구현 - 모델 구현**

Embedding은 tensorflow keras가 제공하는 Embedding layer를 이용해 구현합니다. 정수 인덱스에서 고밀도 vector로 매핑되어 단어 간의 유사성을 함께 인코딩하게 됩니다.

코드는 다음과 같습니다.

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Bidirectional 
from tensorflow.keras.layers import LSTM, Embedding
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.callbacks import TensorBoard

model = Sequential()

# Embedding 파라미터
# input_dim : 단어 사전의 크기
# output_dim : 출력 vector의 차원
# input_length : 입력 길이

model.add(Embedding(input_dim=voca_size+1,
                    output_dim=128,
                    input_length=max_length))

model.add(Bidirectional(LSTM(units=16,
                             activation='tanh')))

model.add(Dense(units=1,
                activation='sigmoid'))

model.compile(optimizer=Adam(learning_rate=1e-3),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Checkpoint
checkpoint_cb = ModelCheckpoint(filepath='./best_model.weights.h5',
                                save_weights_only=True,
                                save_best_only=True,
                                monitor='val_loss',
                                verbose=1)

# Early Stopping
earlystopping_cb = EarlyStopping(monitor='val_loss',
                                 restore_best_weights=True,
                                 patience=4,
                                 verbose=1)

# TensorBoard
log_dir = './logs/' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
tensorboard_cb = TensorBoard(log_dir=log_dir,
                             histogram_freq=1)

# 학습
model.fit(x_data_train,
          y_data_train,
          epochs=100,
          batch_size=64,
          validation_split=0.2,
          callbacks=[checkpoint_cb, earlystopping_cb, tensorboard_cb],
          verbose=1)
```

결과를 보면 training set의 accuracy는 약 88%이고 validation set의 accuracy는 84%입니다. 

## 1.7 **한국어 감성분석 구현 - 평가**

모델의 구현이 다 되었으니 이제 test data set을 이용해서 우리 모델을 평가해보겠습니다. test data를 loading하는 것부터 전처리를 거쳐 평가하는 것까지 다음의 코드로 표현될 수 있습니다.

```python
test_file = tf.keras.utils.get_file(
    cache_dir='.',  
    fname='ratings_test.txt', 
    origin='https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt',
    extract=True
)

test_path = os.path.join('./datasets', 
                         'ratings_test.txt')
test_df = pd.read_csv(test_path, sep='\t')

# 1. 정규식을 활용해 영어, 한글, 띄어쓰기만 남기고 나머지 특수문자를 제거
test_df['document'] = test_df['document'].str.replace('[^A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ ]', '')

# 2. 결측지 제거 (5개)
test_df = test_df.dropna()

# 3. 불용어(stopword)제거
data_test = test_df['document'].progress_apply(word_tokenization)

# 4. 각 문장을 숫자 벡터로 변환하여 encoding
data_test_seq = tokenizer.texts_to_sequences(data_test)

# 5. 동일한 문장 길이로 정리해야 합니다.
x_data_test = pad_sequences(data_test_seq,
                            truncating='post',
                            padding='pre',
                            maxlen=max_length)

y_data_test = np.asarray(test_df['label'])

# evaluation
print(model.evaluate(x_data_test, y_data_test))

# 1563/1563 [==============================] - 6s 4ms/step - loss: 0.3694 - accuracy: 0.8386
# [0.34369906783103943, 0.8498910069465637]
```

정확도가 약 84%정도 나오는 군요. 어느 정도는 학습이 된 것을 확인할 수 있습니다.

## 1.8 **한국어 감성분석 구현 - 실제 Review 데이터 작성 후 Test**

그럼 몇가지 Review를 직접 입력해서 감성분류가 잘 되는지 결과를 살펴보죠.

```python
review_sentences = ['내가 만들어도 이것보단 잘 만들겠다.',
                    '너무너무 재미있었습니다. 감사합니다.',
                    '아..내 돈... 돈 아까워 죽을거 같아요',
                    '아나..이것도 영화라고 만들었냐. 무슨 스토리가 산으로 가냐',
                    '감동과 재미가 같이 있는 영화입니다. 훌륭합니다.',
                    '너무너무 재미없다.. 잠와 죽는줄.',
                    '너무너무 재미있다.. 잠이 확깨네.']

df = pd.DataFrame({'document': review_sentences})

# 정규식을 활용해 영어, 한글, 띄어쓰기만 남기고 나머지 특수문자를 제거
df['document'] = df['document'].str.replace(r'[^A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ ]', 
                                            '', 
                                            regex=True)

# 불용어(stopword)제거
data_predict = df['document'].progress_apply(word_tokenization)

# 4. 각 문장을 숫자 벡터로 변환하여 encoding
data_predict_seq = tokenizer.texts_to_sequences(data_predict)

# 5. 동일한 문장 길이로 정리해야 합니다.
x_data_predict = pad_sequences(data_predict_seq,
                               truncating='post',
                               padding='pre',
                               maxlen=max_length)

# predict
print(model.predict(x_data_predict))

# [[0.03753586]
#  [0.99050903]
#  [0.00718504]
#  [0.00777603]
#  [0.9874061 ]
#  [0.03121529]
#  [0.68418586]]
```

End.
