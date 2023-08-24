# file that contains functions that allow the bot to bypass bot detection
from imports import *

# waits a random amount of time between x and x+y seconds
def timeR(x, y = 1):
    return (time.sleep(x + (float(randint(0, 100)) / 100) * y))


def move_mouse(browser, element = None):
    points = [
        [-6, 2],
        [-3, -2],
        [0, 0],
        [0, 2],
        [2, 3],
        [4, 0],
        [6, 3],
        [8, 5],
        [8, 8],
        [6, 8],
        [5, 9],
        [7, 2],
    ]
    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]

    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)

    x_tup = si.splrep(t, x, k=3)
    y_tup = si.splrep(t, y, k=3)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = si.splev(ipl_t, x_list)
    y_i = si.splev(ipl_t, y_list)

    if element is None:
        element = browser.find_element(By.TAG_NAME, 'body')
    
    action = ActionChains(browser)
    if(randint(0, 1) == 0):
        action.move_to_element(element)
    action.perform()

    for mouse_x, mouse_y in zip(x_i, y_i):
        try:
            action.move_by_offset(mouse_x,mouse_y)
            action.perform()
        except:
            pass
        time.sleep(0.1)
        #print(mouse_x, mouse_y)

def slice_sentence(sentence):
    #splits a sentence into a list of words, but puts random cuts
    #in the sentence to make it look more human
    words = sentence.split(' ')
    new_words = []
    for word in words:
        if randint(0, 1) == 0:
            new_words.append(word + " ")
        else:
            length = randint(0, len(word))
            new_words.append(word[:length])
            new_words.append(word[length:] + " ")

    return new_words