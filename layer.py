#-*- coding: utf-8 -*-
from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from eduardo.eduardo import Ed

class EdLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over
        ed = Ed(u'Robô Ed')
        print 'onMessage'
        
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
        message = messageProtocolEntity.getBody()
        
        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            ed.say(messageProtocolEntity.getBody()),
            to = messageProtocolEntity.getFrom())
        #wait a few seconds
        self.toLower(receipt)
        self.toLower(outgoingMessageProtocolEntity)
        #self.toLower(message.ack(true))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)

    @ProtocolEntityCallback("ack")
    def onAck(self, entity):
        #formattedDate = datetime.datetime.fromtimestamp(self.sentCache[entity.getId()][0]).strftime('%d-%m-%Y %H:%M')
        #print("%s [%s]:%s"%(self.username, formattedDate, self.sentCache[entity.getId()][1]))
        if entity.getClass() == "message":
            print entity.getId()
            #self.notifyInputThread()

    @ProtocolEntityCallback("success")
    def onSuccess(self, entity):
        self.connected = True
        print "Logged in!"
        #self.notifyInputThread()

    @ProtocolEntityCallback("failure")
    def onFailure(self, entity):
        self.connected = False
        print "Login Failed, reason: %s" % entity.getReason()
