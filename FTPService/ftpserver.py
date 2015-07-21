'''
Created on Jul 21, 2015

@author: ronaldjosephdesmarais
'''
from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess, FilePasswordDB
from twisted.internet import reactor

p = Portal(FTPRealm('.', userHome='/Users' ), [AllowAnonymousAccess(), FilePasswordDB("key.dat")])
f = FTPFactory(p)
reactor.listenTCP(2221, f)
reactor.run()
