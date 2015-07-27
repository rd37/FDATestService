'''
Created on Jul 21, 2015

@author: ronaldjosephdesmarais
'''
from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess, FilePasswordDB
from twisted.internet import reactor

p = Portal(FTPRealm('./', userHome='/home' ), [AllowAnonymousAccess(), FilePasswordDB("FTPService/key.dat")])
f = FTPFactory(p)
try:
    reactor.listenTCP(21, f)
    reactor.run()
except Exception as e:
    print "Error %s"%e
