from nltk.tokenize import sent_tokenize, word_tokenize

#EXAMPLE_TEXT = "tôi tên là gì mà sao lại thế này. Anh ấy là người, mà tôi yêu. Đât nước của tôi đẹp! xinh. Tôi tên là gì? gia đình tôi có 3 người : bố mẹ,ông bà,tôi  "
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today?The weather is great, and Python is awesome.The sky is pinkish-blue.You shouldn't eat cardboard."
# tokenize the sentences
print(sent_tokenize(EXAMPLE_TEXT))
#tokenize the words
print(word_tokenize(EXAMPLE_TEXT))