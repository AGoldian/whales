import heapq
import math
import numpy as np
import pandas
import streamlit as st
from PIL import Image


@st.cache(suppress_st_warning=True)
def load_data():
    return Image.open('./resources/defaultPhoto.jpg'), Image.open('./resources/defaultMask.png')


def use_network(photo, mask):
    return [1.3, 5.1, 2.2, 0.7, 1.1]


def find_top(predict_list, top_size):
    ls = [(i, predict_list[i]) for i in range(len(predict_list))]
    return heapq.nlargest(top_size, ls, key=lambda item: item[1])


# top_ls - list of tuples
def convert_to_prob(top_ls):
    if len(top_ls) == 0:
        return []

    probs = [math.exp(elem[1]) for elem in top_ls]
    sigma = sum(probs)

    return [(top_ls[i][0], probs[i] / sigma) for i in range(len(probs))]


def main():
    st.title("Цифровой прорыв. Команда \"Юзеры\"")
    file_photo = st.file_uploader("Загрузите фото кита:", type=['jpg'])
    file_mask = st.file_uploader("Загрузите маску:", type=['png'])

    top_size = st.number_input('Размер ТОПа:', min_value=1, max_value=50, value=5)

    # load default image
    if file_photo is not None and file_mask is not None:
        photo = Image.open(file_photo)
        mask = Image.open(file_mask)
    else:
        photo, mask = load_data()

    mask = mask.resize(photo.size)

    # show images
    col1, col2 = st.columns(2)
    with col1:
        st.text("Фото кита:")
        st.image(photo)
    with col2:
        st.text("Маска:")
        # multiply img with mask with pil

        photo_with_mask = Image.composite(photo, Image.new("RGB", photo.size, (255, 255, 255)), mask)
        st.image(photo_with_mask)

    photo_arr, mask_arr = np.array(photo), np.array(mask)

    predict_list = use_network(photo_arr, mask_arr)

    # find top 5 with indexes
    top_ls = find_top(predict_list, top_size)

    # convert to probability
    top_ls = convert_to_prob(top_ls)
    st.table(pandas.DataFrame(top_ls, columns=['Тип', 'Уверенность']))


if __name__ == '__main__':
    main()
