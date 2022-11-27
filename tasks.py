import time
text = {
    1: '',
    2: "Вы ввели неправильное значение!\nПопробуйте ещё раз"
}
def pretty_input(prompt=''):
    while True:
        try:
            val = int(pretty_input)
            for i in text[1]:
                time.sleep(0.081)
                print(i, end='', flush=True)
            break
        except (Exception):
            for i in text[2]:
                time.sleep(0.081)
                print(i, end='', flush=True)