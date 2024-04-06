from survey import AnonymousSurvey

# 定义一个问题并进行调查
question = "您首先学会说什么语言？"
language_survey = AnonymousSurvey(question)

# 显示问题并存储问题的答案
language_survey.show_question()
print("输入 q 即可退出\n")
while True:
    response = input("语言: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# 显示调查结果
print("\n感谢参与调查!")
language_survey.show_results()
