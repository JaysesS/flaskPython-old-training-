# flaskPython

  Start: python3 server.py -port 8080
  
  getMessage, sendMessage, findMessages
  
  /SendMessage example: 
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Message>
        <Header>
            <To>example</To>
            <From>example</From>
            <Timestamp>27.04.2017 12:22:30</Timestamp>
        </Header>
        <Title>example</Title>
        <Body>
          example
        </Body>
    </Message>
    
  /findMessages example:
    
     {
        "filter" : {
            "to" : "Vlad",
            "from": "Kto-to",
            "date" : "27.04.2017"
            "title" : "hey"
        }
    }
    
    
