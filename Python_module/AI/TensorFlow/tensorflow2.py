from keras.datasets import imdb
from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences

# 参数设置
vocab_size = 10000
max_length = 250
embedding_dim = 16
batch_size = 64
epochs = 5

# 加载并预处理数据
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=vocab_size)
train_data = pad_sequences(train_data, maxlen=max_length)
test_data = pad_sequences(test_data, maxlen=max_length)

# 构建模型
model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 训练模型
model.fit(train_data, train_labels, batch_size=batch_size, epochs=epochs, validation_split=0.2)

# 评估模型
test_loss, test_acc = model.evaluate(test_data, test_labels)
print('准确性:', test_acc)

# 获取词索引并创建反向词索引字典
word_index = imdb.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])


def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])


def predict_sentiment(review_text):
    encoded_review = [word_index.get(word, 2) for word in review_text.split()]
    encoded_review = pad_sequences([encoded_review], maxlen=max_length)
    prediction = model.predict(encoded_review)
    sentiment = 'positive' if prediction >= 0.5 else 'negative'
    return sentiment


# 预测并打印文本和情感
num_reviews = 10
for i in range(num_reviews):
    review_text = decode_review(test_data[i])
    true_sentiment = 'positive' if test_labels[i] == 1 else 'negative'
    predicted_sentiment = predict_sentiment(review_text)
    print(f"回顾 {i + 1}:")
    print("文本:", review_text)
    print("真实的情感:", true_sentiment)
    print("预测情绪:", predicted_sentiment)
    print("\n")
