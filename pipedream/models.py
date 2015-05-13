from django.db import models

# Create your models here.


class InterfaceKind(models.Model):
    name = models.CharField(max_length=200)


class Interface(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    kind = models.ForeignKey(InterfaceKind)


class MessageType(models.Model):
    name = models.CharField(max_length=7)  # for example: ADT^A01, ORU^R01


class SegmentType(models.Model):
    name = models.CharField(max_length=3)  # for example:  PID, PV1, OBR


class Message(models.Model):
    queue_id = models.IntegerField()  # non-unique message ID.  This is only unique when paired with a specific interface
    type = models.ForeignKey(MessageType)
    control = models.CharField(max_length=200)  # MSH-10
    interface = models.ForeignKey(Interface)


class Segment(models.Model):
    type = models.ForeignKey(SegmentType)
    message = models.ForeignKey(Message)
    content = models.TextField()


class Error(models.Model):
    interface = models.ForeignKey(Interface)
    message = models.ForeignKey(Message)
    segment = models.ForeignKey(Segment)
    text = models.CharField(max_length=200)
    code = models.IntegerField()
    badval = models.CharField(max_length=200)
    item = models.CharField(max_length=200)



