#!/usr/bin/env python

#
# Generated Mon Dec 10 15:26:32 2018 by generateDS.py version 2.30.8.
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'webappauthrecord.py')
#   ('-s', 'webappauthrecordsubs.py')
#   ('--super', 'qualysapi.gen.webappauthrecord')
#
# Command line arguments:
#   webappauthrecord.xsd
#
# Command line:
#   generateDS -o "webappauthrecord.py" -s "webappauthrecordsubs.py" --super="qualysapi.gen.webappauthrecord" webappauthrecord.xsd
#
# Current working directory (os.getcwd()):
#   gen
#

import sys
from lxml import etree as etree_

import qualysapi.gen.webappauthrecord as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class ServiceRequestSub(supermod.ServiceRequest):
    def __init__(self, filters=None, preferences=None, data=None, **kwargs_):
        super(ServiceRequestSub, self).__init__(filters, preferences, data,  **kwargs_)
supermod.ServiceRequest.subclass = ServiceRequestSub
# end class ServiceRequestSub


class ServiceRequestFiltersSub(supermod.ServiceRequestFilters):
    def __init__(self, Criteria=None, **kwargs_):
        super(ServiceRequestFiltersSub, self).__init__(Criteria,  **kwargs_)
supermod.ServiceRequestFilters.subclass = ServiceRequestFiltersSub
# end class ServiceRequestFiltersSub


class CriteriaSub(supermod.Criteria):
    def __init__(self, field=None, operator=None, valueOf_=None, **kwargs_):
        super(CriteriaSub, self).__init__(field, operator, valueOf_,  **kwargs_)
supermod.Criteria.subclass = CriteriaSub
# end class CriteriaSub


class ServiceRequestPreferencesSub(supermod.ServiceRequestPreferences):
    def __init__(self, startFromId=None, startFromOffset=None, limitResults=None, **kwargs_):
        super(ServiceRequestPreferencesSub, self).__init__(startFromId, startFromOffset, limitResults,  **kwargs_)
supermod.ServiceRequestPreferences.subclass = ServiceRequestPreferencesSub
# end class ServiceRequestPreferencesSub


class ServiceRequestDataSub(supermod.ServiceRequestData):
    def __init__(self, WebAppAuthRecord=None, **kwargs_):
        super(ServiceRequestDataSub, self).__init__(WebAppAuthRecord,  **kwargs_)
supermod.ServiceRequestData.subclass = ServiceRequestDataSub
# end class ServiceRequestDataSub


class ServiceResponseSub(supermod.ServiceResponse):
    def __init__(self, responseCode=None, responseErrorDetails=None, count=None, hasMoreRecords=None, lastId=None, data=None, **kwargs_):
        super(ServiceResponseSub, self).__init__(responseCode, responseErrorDetails, count, hasMoreRecords, lastId, data,  **kwargs_)
supermod.ServiceResponse.subclass = ServiceResponseSub
# end class ServiceResponseSub


class ResponseErrorObjectSub(supermod.ResponseErrorObject):
    def __init__(self, errorMessage=None, errorResolution=None, internalErrorCodeId=None, **kwargs_):
        super(ResponseErrorObjectSub, self).__init__(errorMessage, errorResolution, internalErrorCodeId,  **kwargs_)
supermod.ResponseErrorObject.subclass = ResponseErrorObjectSub
# end class ResponseErrorObjectSub


class ServiceResponseDataSub(supermod.ServiceResponseData):
    def __init__(self, WebAppAuthRecord=None, **kwargs_):
        super(ServiceResponseDataSub, self).__init__(WebAppAuthRecord,  **kwargs_)
supermod.ServiceResponseData.subclass = ServiceResponseDataSub
# end class ServiceResponseDataSub


class WebAppAuthRecordSub(supermod.WebAppAuthRecord):
    def __init__(self, id=None, name=None, owner=None, formRecord=None, serverRecord=None, tags=None, comments=None, createdDate=None, createdBy=None, updatedDate=None, updatedBy=None, **kwargs_):
        if isinstance(name, str):
            name = CdataSub(valueOf_=name)
        super(WebAppAuthRecordSub, self).__init__(id, name, owner, formRecord, serverRecord, tags, comments, createdDate, createdBy, updatedDate, updatedBy,  **kwargs_)
    def __str__(self):
        key_fields = ['id', 'name', 'owner', 'tags']
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items() if item[0] in key_fields and item[1]))
supermod.WebAppAuthRecord.subclass = WebAppAuthRecordSub
# end class WebAppAuthRecordSub


class WebAppAuthFormRecordSub(supermod.WebAppAuthFormRecord):
    def __init__(self, type_=None, sslOnly=None, seleniumScript=None, fields=None, **kwargs_):
        super(WebAppAuthFormRecordSub, self).__init__(type_, sslOnly, seleniumScript, fields,  **kwargs_)
supermod.WebAppAuthFormRecord.subclass = WebAppAuthFormRecordSub
# end class WebAppAuthFormRecordSub


class WebAppAuthFormRecordFieldListSub(supermod.WebAppAuthFormRecordFieldList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(WebAppAuthFormRecordFieldListSub, self).__init__(count, list, set, add, remove, update,  **kwargs_)
supermod.WebAppAuthFormRecordFieldList.subclass = WebAppAuthFormRecordFieldListSub
# end class WebAppAuthFormRecordFieldListSub


class WebAppAuthFormRecordFieldSub(supermod.WebAppAuthFormRecordField):
    def __init__(self, id=None, name=None, secured=None, value=None, **kwargs_):
        super(WebAppAuthFormRecordFieldSub, self).__init__(id, name, secured, value,  **kwargs_)
supermod.WebAppAuthFormRecordField.subclass = WebAppAuthFormRecordFieldSub
# end class WebAppAuthFormRecordFieldSub


class SeleniumScriptSub(supermod.SeleniumScript):
    def __init__(self, name=None, data=None, regex=None, **kwargs_):
        super(SeleniumScriptSub, self).__init__(name, data, regex,  **kwargs_)
supermod.SeleniumScript.subclass = SeleniumScriptSub
# end class SeleniumScriptSub


class WebAppAuthServerRecordSub(supermod.WebAppAuthServerRecord):
    def __init__(self, sslOnly=None, certificate=None, fields=None, **kwargs_):
        super(WebAppAuthServerRecordSub, self).__init__(sslOnly, certificate, fields,  **kwargs_)
supermod.WebAppAuthServerRecord.subclass = WebAppAuthServerRecordSub
# end class WebAppAuthServerRecordSub


class WebAppAuthServerRecordFieldListSub(supermod.WebAppAuthServerRecordFieldList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(WebAppAuthServerRecordFieldListSub, self).__init__(count, list, set, add, remove, update,  **kwargs_)
supermod.WebAppAuthServerRecordFieldList.subclass = WebAppAuthServerRecordFieldListSub
# end class WebAppAuthServerRecordFieldListSub


class WebAppAuthServerRecordFieldSub(supermod.WebAppAuthServerRecordField):
    def __init__(self, id=None, type_=None, domain=None, username=None, password=None, **kwargs_):
        super(WebAppAuthServerRecordFieldSub, self).__init__(id, type_, domain, username, password,  **kwargs_)
supermod.WebAppAuthServerRecordField.subclass = WebAppAuthServerRecordFieldSub
# end class WebAppAuthServerRecordFieldSub


class CertificateSub(supermod.Certificate):
    def __init__(self, name=None, contents=None, passphrase=None, **kwargs_):
        super(CertificateSub, self).__init__(name, contents, passphrase,  **kwargs_)
supermod.Certificate.subclass = CertificateSub
# end class CertificateSub


class TagListSub(supermod.TagList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, **kwargs_):
        super(TagListSub, self).__init__(count, list, set, add, remove,  **kwargs_)
    def __str__(self):
        if self.list:
            return ','.join(self.list)
        return "[]"
supermod.TagList.subclass = TagListSub
# end class TagListSub


class TagSub(supermod.Tag):
    def __init__(self, id=None, name=None, **kwargs_):
        super(TagSub, self).__init__(id, name,  **kwargs_)
    def __str__(self):
        return self.name
supermod.Tag.subclass = TagSub
# end class TagSub


class CommentListSub(supermod.CommentList):
    def __init__(self, count=None, list=None, set=None, add=None, **kwargs_):
        super(CommentListSub, self).__init__(count, list, set, add,  **kwargs_)
supermod.CommentList.subclass = CommentListSub
# end class CommentListSub


class CommentSub(supermod.Comment):
    def __init__(self, contents=None, author=None, createdDate=None, **kwargs_):
        super(CommentSub, self).__init__(contents, author, createdDate,  **kwargs_)
supermod.Comment.subclass = CommentSub
# end class CommentSub


class CdataSub(supermod.Cdata):
    def __init__(self, valueOf_=None, **kwargs_):
        super(CdataSub, self).__init__(valueOf_,  **kwargs_)
    def __str__(self):
        return self.valueOf_
supermod.Cdata.subclass = CdataSub
# end class CdataSub


class UserSub(supermod.User):
    def __init__(self, id=None, username=None, firstName=None, lastName=None, **kwargs_):
        super(UserSub, self).__init__(id, username, firstName, lastName,  **kwargs_)

    def __str__(self):
        key_fields = ['id', 'username', "firstName", "lastName"]
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items() if item[0] in key_fields and item[1]))

supermod.User.subclass = UserSub
# end class UserSub


class listTypeSub(supermod.listType):
    def __init__(self, WebAppAuthFormRecordField=None, **kwargs_):
        super(listTypeSub, self).__init__(WebAppAuthFormRecordField,  **kwargs_)
supermod.listType.subclass = listTypeSub
# end class listTypeSub


class setTypeSub(supermod.setType):
    def __init__(self, WebAppAuthFormRecordField=None, **kwargs_):
        super(setTypeSub, self).__init__(WebAppAuthFormRecordField,  **kwargs_)
supermod.setType.subclass = setTypeSub
# end class setTypeSub


class addTypeSub(supermod.addType):
    def __init__(self, WebAppAuthFormRecordField=None, **kwargs_):
        super(addTypeSub, self).__init__(WebAppAuthFormRecordField,  **kwargs_)
supermod.addType.subclass = addTypeSub
# end class addTypeSub


class removeTypeSub(supermod.removeType):
    def __init__(self, WebAppAuthFormRecordField=None, **kwargs_):
        super(removeTypeSub, self).__init__(WebAppAuthFormRecordField,  **kwargs_)
supermod.removeType.subclass = removeTypeSub
# end class removeTypeSub


class updateTypeSub(supermod.updateType):
    def __init__(self, WebAppAuthFormRecordField=None, **kwargs_):
        super(updateTypeSub, self).__init__(WebAppAuthFormRecordField,  **kwargs_)
supermod.updateType.subclass = updateTypeSub
# end class updateTypeSub


class listType1Sub(supermod.listType1):
    def __init__(self, WebAppAuthServerRecordField=None, **kwargs_):
        super(listType1Sub, self).__init__(WebAppAuthServerRecordField,  **kwargs_)
supermod.listType1.subclass = listType1Sub
# end class listType1Sub


class setType2Sub(supermod.setType2):
    def __init__(self, WebAppAuthServerRecordField=None, **kwargs_):
        super(setType2Sub, self).__init__(WebAppAuthServerRecordField,  **kwargs_)
supermod.setType2.subclass = setType2Sub
# end class setType2Sub


class addType3Sub(supermod.addType3):
    def __init__(self, WebAppAuthServerRecordField=None, **kwargs_):
        super(addType3Sub, self).__init__(WebAppAuthServerRecordField,  **kwargs_)
supermod.addType3.subclass = addType3Sub
# end class addType3Sub


class removeType4Sub(supermod.removeType4):
    def __init__(self, WebAppAuthServerRecordField=None, **kwargs_):
        super(removeType4Sub, self).__init__(WebAppAuthServerRecordField,  **kwargs_)
supermod.removeType4.subclass = removeType4Sub
# end class removeType4Sub


class updateType5Sub(supermod.updateType5):
    def __init__(self, WebAppAuthServerRecordField=None, **kwargs_):
        super(updateType5Sub, self).__init__(WebAppAuthServerRecordField,  **kwargs_)
supermod.updateType5.subclass = updateType5Sub
# end class updateType5Sub


class listType7Sub(supermod.listType7):
    def __init__(self, Tag=None, **kwargs_):
        super(listType7Sub, self).__init__(Tag,  **kwargs_)
supermod.listType7.subclass = listType7Sub
# end class listType7Sub


class setType8Sub(supermod.setType8):
    def __init__(self, Tag=None, **kwargs_):
        super(setType8Sub, self).__init__(Tag,  **kwargs_)
supermod.setType8.subclass = setType8Sub
# end class setType8Sub


class addType9Sub(supermod.addType9):
    def __init__(self, Tag=None, **kwargs_):
        super(addType9Sub, self).__init__(Tag,  **kwargs_)
supermod.addType9.subclass = addType9Sub
# end class addType9Sub


class removeType10Sub(supermod.removeType10):
    def __init__(self, Tag=None, **kwargs_):
        super(removeType10Sub, self).__init__(Tag,  **kwargs_)
supermod.removeType10.subclass = removeType10Sub
# end class removeType10Sub


class listType11Sub(supermod.listType11):
    def __init__(self, Comment=None, **kwargs_):
        super(listType11Sub, self).__init__(Comment,  **kwargs_)
supermod.listType11.subclass = listType11Sub
# end class listType11Sub


class setType12Sub(supermod.setType12):
    def __init__(self, Comment=None, **kwargs_):
        super(setType12Sub, self).__init__(Comment,  **kwargs_)
supermod.setType12.subclass = setType12Sub
# end class setType12Sub


class addType13Sub(supermod.addType13):
    def __init__(self, Comment=None, **kwargs_):
        super(addType13Sub, self).__init__(Comment,  **kwargs_)
supermod.addType13.subclass = addType13Sub
# end class addType13Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ServiceRequest'
        rootClass = supermod.ServiceRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ServiceRequest'
        rootClass = supermod.ServiceRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ServiceRequest'
        rootClass = supermod.ServiceRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ServiceRequest'
        rootClass = supermod.ServiceRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from qualysapi.gen.webappauthrecord import *\n\n')
        sys.stdout.write('import qualysapi.gen.webappauthrecord as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
