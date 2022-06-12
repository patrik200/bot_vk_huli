# pip install vk_api качаем хуйню
# подключаем хуйню
# нужно запустить код и не выключать (нужен конечно же интернет)
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
#прописываем токен блять (ссылка на бота https://vk.com/public213872207)

main_token = '446d243249d47a1bfce25de517f658c1cedf58dc210b47ac50004c77c5666a560308926b728424f85bada'
# прописывем лонг пул (обязательно, связь с вк)
vk_session = vk_api.VkApi(token = main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


#функции для отправки фото (начало на 19 строке)


def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )


def main():
    vk_session = vk_api.VkApi(token = main_token)
    vk = vk_session.get_api()
    upload = VkUpload(vk)

    send_photo(vk, PEER_ID, *upload_photo(upload, '1.jpg'))



#функции для отправки фото (конец на 43 строчке)


def sender(id, text): #функции для отправки сообщения
  vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})



for event in longpoll.listen(): #чекаем сообщения боту
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower() #переводим в нижний регистр сообщения для простого распознования и ифов
            id = event.user_id #id-шник пользователя, ОБЯЗАТЕЛЬНО НАХУЙ
            for msg_for in msg.split(): #разбиваем строку на массив
                if msg_for == "пидр":
                    sender(id, 'пошёл нахуй чмо ебаное') #функции для отправки текстового сообщения
                    PEER_ID = id
                    if __name__ == '__main__':
                        main() #функции для отправки картинки

