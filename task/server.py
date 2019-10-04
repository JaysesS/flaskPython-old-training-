# python3
# flask

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-port',  '--port', nargs="?", help='Server port')

argv = parser.parse_args()

if argv.port is not None:

    from flask import Flask, request, Response
    from xml.etree.ElementTree import fromstring, Element, SubElement, tostring
    import json
    app = Flask(__name__)

    # Основной массив сообщений
    MESSAGES = []

    @app.route("/", methods=['GET'])
    def index():
        return 'Vladislav Olshanskiy // softelele2@mail.ru'

    # sendMessage
    @app.route("/sendMessage", methods=['POST'])
    def sendMessage():
        try:
            r = request.data.decode('UTF-8')
            # Преобразование xml в список
            # И добавление в главный лист MESSAGES
            parseXml(fromstring(r))
            return ''
        except:
            return 'Verify your request'
    
    # getMessage
    @app.route("/getMessage", methods=['GET'])
    def getMessage():
        if len(MESSAGES) > 0:
            # Преобразование (если такое есть) последнего сообщения xml
            # и формируем ответ
            ans = createXmlGetMessage(MESSAGES[-1])
            return Response(ans, mimetype= 'application/xml')
        else:
            return "No messages"

    # Запрос findMessage
    # Теги to, from, date, title
    # {
    #     "filter" : {
    #         "to" : "Vlad",
    #         "from": "Kto-to",
    #         "date" : "27.04.2017"
    #         "title" : "hey"
    #     }
    # }
    @app.route("/findMessages", methods=['POST', 'GET'])
    def findMessages():
        try:
            r = request.json
            # Поиск сообщений, переменная resSearch принимает список
            # с результатами совпадений по каждому сообщению
            # Пример: {0: 0, 1: 3, 2: 0, 3: 0, 4: 0, 5: 4}
            # В данном примере видно, что найдено в первом сообщении
            # 3 совпадения, в пятом 4, а в остальных по нулям.
            resSearch = findMsgs(r)
            if resSearchIsNotEmpty(resSearch):
                # Если есть результат поиска, то формируем ответ.
                ans = createXmlFindMessages(resSearch)
                return Response(ans, mimetype= 'application/xml')
            else:
                return 'No search result'
        except:
            return 'Verify your request'

    # Метод проверяющий на НЕ пустоту результатов поиска
    def resSearchIsNotEmpty(found):

        check = 0
        for i in range(len(found)):
            if found[i] == 0:
                check+=1
        
        if check == len(found):
            return False
        else:
            return True

    # Метод разбирающий проходящий json 
    # и формирование списка совпадений
    def findMsgs(r):

        try:
            From = r['filter']['from']
        except KeyError:
            From = None
        
        try:
            To = r['filter']['to']
        except KeyError:
            To = None

        try:
            Date = r['filter']['date']
        except KeyError:
            Date = None

        try:
            Title = r['filter']['title']
        except KeyError:
            Title = None

        # Создание списка совпадений
        found = {i : 0 for i in range(len(MESSAGES))}

        # Заполнение списка совпадений
        for i in range(len(MESSAGES)):
            if From is not None and MESSAGES[i]['Message']['Header']['From'] == From:
                found[i] += 1
            if To is not None and MESSAGES[i]['Message']['Header']['To'] == To:
                found[i] += 1
            if Date is not None and Date in MESSAGES[i]['Message']['Header']['Timestamp']:
                found[i] += 1
            if Title is not None and MESSAGES[i]['Message']['Title'] == Title:
                found[i] += 1

        return found
    
    # Метод создающий xml для ответа на запрос findMessage
    def createXmlFindMessages(found):

        xml = Element('Messages')

        for i in range(len(found)):
            if found[i] > 0:
                
                Message = MESSAGES[i]

                mess = SubElement(xml, 'Message')

                Header = SubElement(mess, 'Header')
                To = SubElement(Header, 'To')
                To.text = Message["Message"]["Header"]["To"]
                From = SubElement(Header, 'From')
                From.text = Message["Message"]["Header"]["From"]
                Timestamp = SubElement(Header, 'Timestamp')
                Timestamp.text = Message["Message"]["Header"]["Timestamp"]

                Title = SubElement(mess, 'Title')
                Title.text = Message["Message"]["Title"]

                Body = SubElement(mess, 'Body')
                Body.text = Message["Message"]["Body"]
        
        return tostring(xml, encoding='utf8')
    
    # Метод создающий xml для ответа на запрос getMessage
    # и очистка последлего сообщение в очереде (листе MESSAGES)
    def createXmlGetMessage(lastMessage):

        xml = Element('Message')

        Header = SubElement(xml, 'Header')
        To = SubElement(Header, 'To')
        To.text = lastMessage["Message"]["Header"]["To"]
        From = SubElement(Header, 'From')
        From.text = lastMessage["Message"]["Header"]["From"]
        Timestamp = SubElement(Header, 'Timestamp')
        Timestamp.text = lastMessage["Message"]["Header"]["Timestamp"]

        Title = SubElement(xml, 'Title')
        Title.text = lastMessage["Message"]["Title"]

        Body = SubElement(xml, 'Body')
        Body.text = lastMessage["Message"]["Body"]
        
        MESSAGES.pop()

        return tostring(xml, encoding='utf8')

    # Разбор приходящего сообщения через запрос sendMessage
    # и добавление в лист MESSAGES
    def parseXml(newMessage):

        message = {"Message": {"Header" : {"To": "", "From" : "", "Timestamp" : ""}, "Title" : "", "Body" : ""}}
        message["Message"]["Header"]["To"] = newMessage[0][0].text
        message["Message"]["Header"]["From"] = newMessage[0][1].text
        message["Message"]["Header"]["Timestamp"] = newMessage[0][2].text
        message["Message"]["Title"] = newMessage[1].text
        message["Message"]["Body"] = str(newMessage[2].text).strip()
        MESSAGES.append(message)

    if __name__ == "__main__":
        app.run(debug=False, host='localhost', port=argv.port)
else:
    parser.print_help()