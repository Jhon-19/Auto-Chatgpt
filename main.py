import pyautogui as ag
import pyperclip as clip
import json

from constant import WEBNLG_EXAMPLE
from utils import DATA_PATH, DATASET_LIST, DATASET_PROMPT_DICT

COPY_ICON_PATH = './images/copy-icon.png'
SUBMIT_ICON_PATH = './images/submit-icon.png'
WATING_ICON_PATH = './images/waiting-icon.png'
LOADING_ICON_PATH = './images/loading-icon.png'

### Need to change
SHOT = 5
DATASET = DATASET_LIST[2]
RESULTS_PATH = f'./results/{SHOT}-shot/{DATASET}'
###

def printAllWindows():
    windows = ag.getAllWindows()
    for window in windows:
        print(window.title)


def checkChatGPT():
    currentWindow = ag.getActiveWindow()
    isChatGPT = False
    if currentWindow.title.find('Google Chrome') != -1:
        isChatGPT = True
    return isChatGPT


def locateCopyIcon():
    patience = 0

    copy_location = None
    while copy_location is None:
        ag.moveTo(600, 600)
        ag.sleep(0.5)
        ag.scroll(-500)
        ag.sleep(0.5)

        if patience >= 10 and patience <= 12:
            ag.click(600, 600)

        if patience >= 3*60:
            ag.press('f5')
            ag.sleep(20)

        try:
            copy_location = ag.locateOnScreen(COPY_ICON_PATH, confidence=0.8)
        except:
            patience += 1
            pass

    if copy_location:
        x, y = ag.center(copy_location)
        return x, y


def locateSubmitIcon():
    submit_icon = None
    while submit_icon is None:
        ag.sleep(1)
        try:
            submit_icon = ag.locateOnScreen(SUBMIT_ICON_PATH, confidence=0.8)
        except:
            pass

    if submit_icon:
        x, y = ag.center(submit_icon)
        return x, y


def judgeWaiting():
    try:
        waiting_icon = ag.locateOnScreen(WATING_ICON_PATH, confidence=0.8)
    except:
        waiting_icon = None

    try:
        loading_icon = ag.locateOnScreen(LOADING_ICON_PATH, confidence=0.9)
    except:
        loading_icon = None

    is_waiting = False
    if waiting_icon or loading_icon:
        is_waiting = True

    return is_waiting


def locateInput(submit_location):
    submit_x, submit_y = submit_location
    return submit_x - 200, submit_y


def define_first_prompt(shot=1):
    first_prompt = 'Extract triples from the text in the format (head, relation, tail).'
    if shot == 0:
        first_prompt = f'''
        Extract triples from the text in the format (head, relation, tail).
        The relation is in the list {DATASET_PROMPT_DICT[DATASET][0]}
        '''
    elif shot == 1:
        first_prompt = f'''
        Extract triples from the text in the format (head, relation, tail).
        The relation is in the list {DATASET_PROMPT_DICT[DATASET][0]}
        Here is an example:
        {WEBNLG_EXAMPLE}
        '''
    elif shot == 5:
        first_prompt = f'''
        Extract triples from the text in the format (head, relation, tail).
        The relation is in the list {DATASET_PROMPT_DICT[DATASET][0]}
        Here are examples:
        {DATASET_PROMPT_DICT[DATASET][1]}
        '''

    return first_prompt


def generate_data_path(dataset):
    return f'{DATA_PATH}/{dataset}/test_triples.json'


def obtain_prompt_list(dataset):
    prompt_list = []
    initial_prompt = define_first_prompt(shot=SHOT)
    data_path = generate_data_path(dataset)

    with open(data_path, 'r', encoding='utf-8-sig') as f:
        datas = json.loads(f.read())

    # print(len(datas))
    data_length = len(datas)
    if data_length > 1000:
        datas_sample = []
        for index in range(0, data_length, 6):
            datas_sample.append(datas[index])
        datas = datas_sample
        print(len(datas))

    for index, data in enumerate(datas):
        if index % 100 == 0:
            prompt_list.append(initial_prompt)
        prompt_list.append(data['text'])

    return prompt_list


def start_task(prompt_list, index=0):
    index = index
    prompt_length = len(prompt_list)

    while True:
        if checkChatGPT():
            ag.sleep(20)
            if not judgeWaiting():
                submit_location = locateSubmitIcon()
                input_location = locateInput(submit_location)

                ag.click(*input_location)
                ag.sleep(0.5)
                typeText(prompt_list[index])

                ag.click(*submit_location)
                ag.sleep(20)

                while judgeWaiting():
                    ag.sleep(5)

                copy_location = locateCopyIcon()
                ag.click(*copy_location)
                ag.sleep(1)

                result = clip.paste()

                result_json = {
                    'text': prompt_list[index],
                    'result': result
                }

                save_result(index, result_json)

                index += 1
                if index >= prompt_length:
                    break
        else:
            ag.sleep(5)


def save_result(index, result):
    result_path = f'{RESULTS_PATH}/{index}.json'
    with open(result_path, 'w') as f:
        f.write(json.dumps(result))
    print(f'text-{index} finished!')


def typeText(text):
    clip.copy(text)
    ag.sleep(0.5)
    ag.hotkey('ctrl', 'v')
    ag.sleep(0.5)


if __name__ == '__main__':
    prompt_list = obtain_prompt_list(dataset=DATASET)
    # print(len(prompt_list))
    # print(prompt_list[10])
    start_task(prompt_list, index=836)

    # printAllWindows()
# print(locateCopyIcon())
# print(locateSubmitIcon())
