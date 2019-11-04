#!/usr/bin/env python

#
# Generated Thu Dec  6 09:27:46 2018 by generateDS.py version 2.30.8.
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'webapp.py')
#   ('-s', 'webappsubs.py')
#
# Command line arguments:
#   webapp.xsd
#
# Command line:
#   generateDS -o "webapp.py" -s "webappsubs.py" webapp.xsd
#
# Current working directory (os.getcwd()):
#   gen
#

import sys
from lxml import etree as etree_

import qualysapi.gen.webapp as supermod


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
        super(ServiceRequestSub, self).__init__(filters, preferences, data, **kwargs_)


supermod.ServiceRequest.subclass = ServiceRequestSub


# end class ServiceRequestSub


class ServiceRequestFiltersSub(supermod.ServiceRequestFilters):
    def __init__(self, Criteria=None, **kwargs_):
        super(ServiceRequestFiltersSub, self).__init__(Criteria, **kwargs_)


supermod.ServiceRequestFilters.subclass = ServiceRequestFiltersSub


# end class ServiceRequestFiltersSub


class CriteriaSub(supermod.Criteria):
    def __init__(self, field=None, name=None, operator=None, valueOf_=None, **kwargs_):
        super(CriteriaSub, self).__init__(field, name, operator, valueOf_, **kwargs_)


supermod.Criteria.subclass = CriteriaSub


# end class CriteriaSub


class ServiceRequestPreferencesSub(supermod.ServiceRequestPreferences):
    def __init__(self, startFromId=None, startFromOffset=None, limitResults=None, **kwargs_):
        super(ServiceRequestPreferencesSub, self).__init__(startFromId, startFromOffset, limitResults, **kwargs_)


supermod.ServiceRequestPreferences.subclass = ServiceRequestPreferencesSub


# end class ServiceRequestPreferencesSub


class ServiceRequestDataSub(supermod.ServiceRequestData):
    def __init__(self, WebApp=None, **kwargs_):
        super(ServiceRequestDataSub, self).__init__(WebApp, **kwargs_)


supermod.ServiceRequestData.subclass = ServiceRequestDataSub


# end class ServiceRequestDataSub


class ServiceResponseSub(supermod.ServiceResponse):
    def __init__(self, responseCode=None, responseErrorDetails=None, count=None, hasMoreRecords=None, lastId=None,
                 data=None, **kwargs_):
        super(ServiceResponseSub, self).__init__(responseCode, responseErrorDetails, count, hasMoreRecords, lastId,
                                                 data, **kwargs_)


supermod.ServiceResponse.subclass = ServiceResponseSub


# end class ServiceResponseSub


class ResponseErrorObjectSub(supermod.ResponseErrorObject):
    def __init__(self, errorMessage=None, errorResolution=None, internalErrorCodeId=None, **kwargs_):
        super(ResponseErrorObjectSub, self).__init__(errorMessage, errorResolution, internalErrorCodeId, **kwargs_)


supermod.ResponseErrorObject.subclass = ResponseErrorObjectSub


# end class ResponseErrorObjectSub


class ServiceResponseDataSub(supermod.ServiceResponseData):
    def __init__(self, WebApp=None, **kwargs_):
        super(ServiceResponseDataSub, self).__init__(WebApp, **kwargs_)


supermod.ServiceResponseData.subclass = ServiceResponseDataSub


# end class ServiceResponseDataSub


class WebAppSub(supermod.WebApp):
    def __init__(self, id=None, name=None, url=None, os=None, owner=None, scope='ALL', subDomain=None, domains=None,
                 uris=None, attributes=None, defaultProfile=None, defaultScanner=None, defaultScannerTags=None,
                 scannerLocked=False, progressiveScanning=None, redundancyLinks=None, maxRedundancyLinks=None,
                 urlBlacklist=None, urlWhitelist=None, postDataBlacklist=None, logoutRegexList=None, authRecords=None,
                 dnsOverrides=None, useRobots='IGNORE', useSitemap=False, headers=None, malwareMonitoring=None,
                 malwareNotification=None, malwareTaskId=None, malwareScheduling=None, tags=None, comments=None,
                 isScheduled=None, lastScan=None, createdBy=None, createdDate=None, updatedBy=None, updatedDate=None,
                 screenshot=None, proxy=None, config=None, crawlingScripts=None, **kwargs_):
        if isinstance(name, str):
            name = CdataSub(valueOf_=name)
        if isinstance(url, str):
            url = UrlSub(valueOf_=url)
        super(WebAppSub, self).__init__(id, name, url, os, owner, scope, subDomain, domains, uris, attributes,
                                        defaultProfile, defaultScanner, defaultScannerTags, scannerLocked,
                                        progressiveScanning, redundancyLinks, maxRedundancyLinks, urlBlacklist,
                                        urlWhitelist, postDataBlacklist, logoutRegexList, authRecords, dnsOverrides,
                                        useRobots, useSitemap, headers, malwareMonitoring, malwareNotification,
                                        malwareTaskId, malwareScheduling, tags, comments, isScheduled, lastScan,
                                        createdBy, createdDate, updatedBy, updatedDate, screenshot, proxy, config,
                                        crawlingScripts, **kwargs_)

    def __str__(self):
        key_fields = ['id', 'name', 'url', 'owner', 'tags']
        return '%s(%s)' % (
        type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items() if item[0] in key_fields and item[1]))


supermod.WebApp.subclass = WebAppSub


# end class WebAppSub


class CdataSub(supermod.Cdata):
    def __init__(self, valueOf_=None, extensiontype_=None, **kwargs_):
        super(CdataSub, self).__init__(valueOf_, extensiontype_, **kwargs_)

    def __str__(self):
        return self.valueOf_


supermod.Cdata.subclass = CdataSub


# end class CdataSub


class UrlListSub(supermod.UrlList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(UrlListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)


supermod.UrlList.subclass = UrlListSub


# end class UrlListSub


class UrlSub(supermod.Url):
    def __init__(self, valueOf_=None, **kwargs_):
        super(UrlSub, self).__init__(valueOf_, **kwargs_)

    def __str__(self):
        return self.valueOf_


supermod.Url.subclass = UrlSub


# end class UrlSub


class UserSub(supermod.User):
    def __init__(self, id=None, username=None, firstName=None, lastName=None, **kwargs_):
        super(UserSub, self).__init__(id, username, firstName, lastName, **kwargs_)

    def __str__(self):
        key_fields = ['id', 'username', "firstName", "lastName"]
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items() if item[0] in key_fields and item[1]))

supermod.User.subclass = UserSub
# end class UserSub


class HttpProxySub(supermod.HttpProxy):
    def __init__(self, id=None, name=None, url=None, **kwargs_):
        super(HttpProxySub, self).__init__(id, name, url, **kwargs_)


supermod.HttpProxy.subclass = HttpProxySub


# end class HttpProxySub


class WebAppConfigSub(supermod.WebAppConfig):
    def __init__(self, cancelScansAfterNHours=None, cancelScansAt=None, defaultAuthRecord=None, **kwargs_):
        super(WebAppConfigSub, self).__init__(cancelScansAfterNHours, cancelScansAt, defaultAuthRecord, **kwargs_)


supermod.WebAppConfig.subclass = WebAppConfigSub


# end class WebAppConfigSub


class DomainListSub(supermod.DomainList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(DomainListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)


supermod.DomainList.subclass = DomainListSub


# end class DomainListSub


class DomainSub(supermod.Domain):
    def __init__(self, valueOf_=None, **kwargs_):
        super(DomainSub, self).__init__(valueOf_, **kwargs_)


supermod.Domain.subclass = DomainSub


# end class DomainSub


class AttributeListSub(supermod.AttributeList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(AttributeListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)


supermod.AttributeList.subclass = AttributeListSub


# end class AttributeListSub


class AttributeSub(supermod.Attribute):
    def __init__(self, name=None, value=None, **kwargs_):
        super(AttributeSub, self).__init__(name, value, **kwargs_)


supermod.Attribute.subclass = AttributeSub


# end class AttributeSub


class WasScanOptionProfileSub(supermod.WasScanOptionProfile):
    def __init__(self, id=None, name=None, **kwargs_):
        super(WasScanOptionProfileSub, self).__init__(id, name, **kwargs_)


supermod.WasScanOptionProfile.subclass = WasScanOptionProfileSub


# end class WasScanOptionProfileSub


class ScannerApplianceSub(supermod.ScannerAppliance):
    def __init__(self, type_=None, friendlyName=None, **kwargs_):
        super(ScannerApplianceSub, self).__init__(type_, friendlyName, **kwargs_)


supermod.ScannerAppliance.subclass = ScannerApplianceSub


# end class ScannerApplianceSub


class UrlEntryListSub(supermod.UrlEntryList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(UrlEntryListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)


supermod.UrlEntryList.subclass = UrlEntryListSub


# end class UrlEntryListSub


class UrlEntrySub(supermod.UrlEntry):
    def __init__(self, regex=False, valueOf_=None, **kwargs_):
        super(UrlEntrySub, self).__init__(regex, valueOf_, **kwargs_)


supermod.UrlEntry.subclass = UrlEntrySub


# end class UrlEntrySub


class WebAppAuthRecordListSub(supermod.WebAppAuthRecordList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, **kwargs_):
        super(WebAppAuthRecordListSub, self).__init__(count, list, set, add, remove, **kwargs_)


supermod.WebAppAuthRecordList.subclass = WebAppAuthRecordListSub


# end class WebAppAuthRecordListSub


class WebAppAuthRecordSub(supermod.WebAppAuthRecord):
    def __init__(self, id=None, name=None, **kwargs_):
        super(WebAppAuthRecordSub, self).__init__(id, name, **kwargs_)


supermod.WebAppAuthRecord.subclass = WebAppAuthRecordSub


# end class WebAppAuthRecordSub


class DnsOverrideListSub(supermod.DnsOverrideList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, **kwargs_):
        super(DnsOverrideListSub, self).__init__(count, list, set, add, remove, **kwargs_)


supermod.DnsOverrideList.subclass = DnsOverrideListSub


# end class DnsOverrideListSub


class DnsOverrideSub(supermod.DnsOverride):
    def __init__(self, id=None, name=None, **kwargs_):
        super(DnsOverrideSub, self).__init__(id, name, **kwargs_)


supermod.DnsOverride.subclass = DnsOverrideSub


# end class DnsOverrideSub


class WebAppHeaderListSub(supermod.WebAppHeaderList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(WebAppHeaderListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)


supermod.WebAppHeaderList.subclass = WebAppHeaderListSub


# end class WebAppHeaderListSub


class WebAppHeaderSub(supermod.WebAppHeader):
    def __init__(self, valueOf_=None, **kwargs_):
        super(WebAppHeaderSub, self).__init__(valueOf_, **kwargs_)


supermod.WebAppHeader.subclass = WebAppHeaderSub


# end class WebAppHeaderSub


class TagListSub(supermod.TagList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(TagListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)
    def __str__(self):
        if self.list:
            return ','.join(self.list)
        return "[]"

supermod.TagList.subclass = TagListSub


# end class TagListSub


class TagSub(supermod.Tag):
    def __init__(self, id=None, name=None, **kwargs_):
        super(TagSub, self).__init__(id, name, **kwargs_)
    def __str__(self):
        return self.name

supermod.Tag.subclass = TagSub


# end class TagSub


class CommentListSub(supermod.CommentList):
    def __init__(self, count=None, list=None, set=None, add=None, **kwargs_):
        super(CommentListSub, self).__init__(count, list, set, add, **kwargs_)


supermod.CommentList.subclass = CommentListSub


# end class CommentListSub


class CommentSub(supermod.Comment):
    def __init__(self, contents=None, author=None, createdDate=None, **kwargs_):
        super(CommentSub, self).__init__(contents, author, createdDate, **kwargs_)


supermod.Comment.subclass = CommentSub


# end class CommentSub


class WasScanSub(supermod.WasScan):
    def __init__(self, id=None, name=None, **kwargs_):
        super(WasScanSub, self).__init__(id, name, **kwargs_)


supermod.WasScan.subclass = WasScanSub


# end class WasScanSub


class TimeZoneSub(supermod.TimeZone):
    def __init__(self, code=None, offset=None, **kwargs_):
        super(TimeZoneSub, self).__init__(code, offset, **kwargs_)


supermod.TimeZone.subclass = TimeZoneSub


# end class TimeZoneSub


class SchedulePlanificationSub(supermod.SchedulePlanification):
    def __init__(self, startDate=None, timeZone=None, occurrenceType=None, occurrence=None, cancelAfterNHours=None,
                 cancelTime=None, **kwargs_):
        super(SchedulePlanificationSub, self).__init__(startDate, timeZone, occurrenceType, occurrence,
                                                       cancelAfterNHours, cancelTime, **kwargs_)


supermod.SchedulePlanification.subclass = SchedulePlanificationSub


# end class SchedulePlanificationSub


class HourlyOccurrenceSub(supermod.HourlyOccurrence):
    def __init__(self, everyNHours=None, occurrenceCount=None, **kwargs_):
        super(HourlyOccurrenceSub, self).__init__(everyNHours, occurrenceCount, **kwargs_)


supermod.HourlyOccurrence.subclass = HourlyOccurrenceSub


# end class HourlyOccurrenceSub


class DailyOccurrenceSub(supermod.DailyOccurrence):
    def __init__(self, everyNDays=None, occurrenceCount=None, **kwargs_):
        super(DailyOccurrenceSub, self).__init__(everyNDays, occurrenceCount, **kwargs_)


supermod.DailyOccurrence.subclass = DailyOccurrenceSub


# end class DailyOccurrenceSub


class WeeklyOccurrenceSub(supermod.WeeklyOccurrence):
    def __init__(self, everyNWeeks=None, onDays=None, occurrenceCount=None, **kwargs_):
        super(WeeklyOccurrenceSub, self).__init__(everyNWeeks, onDays, occurrenceCount, **kwargs_)


supermod.WeeklyOccurrence.subclass = WeeklyOccurrenceSub


# end class WeeklyOccurrenceSub


class MonthlyOccurrenceSub(supermod.MonthlyOccurrence):
    def __init__(self, monthlyType=None, occurrenceCount=None, **kwargs_):
        super(MonthlyOccurrenceSub, self).__init__(monthlyType, occurrenceCount, **kwargs_)


supermod.MonthlyOccurrence.subclass = MonthlyOccurrenceSub


# end class MonthlyOccurrenceSub


class CrawlingScriptListSub(supermod.CrawlingScriptList):
    def __init__(self, count=None, list=None, set=None, add=None, remove=None, update=None, **kwargs_):
        super(CrawlingScriptListSub, self).__init__(count, list, set, add, remove, update, **kwargs_)


supermod.CrawlingScriptList.subclass = CrawlingScriptListSub


# end class CrawlingScriptListSub


class SeleniumScriptSub(supermod.SeleniumScript):
    def __init__(self, id=None, name=None, data=None, regex=None, requiresAuthentication=None, startingUrl=None,
                 startingUrlRegex=None, **kwargs_):
        super(SeleniumScriptSub, self).__init__(id, name, data, regex, requiresAuthentication, startingUrl,
                                                startingUrlRegex, **kwargs_)


supermod.SeleniumScript.subclass = SeleniumScriptSub


# end class SeleniumScriptSub


class listTypeSub(supermod.listType):
    def __init__(self, Url=None, **kwargs_):
        super(listTypeSub, self).__init__(Url, **kwargs_)


supermod.listType.subclass = listTypeSub


# end class listTypeSub


class setTypeSub(supermod.setType):
    def __init__(self, Url=None, **kwargs_):
        super(setTypeSub, self).__init__(Url, **kwargs_)


supermod.setType.subclass = setTypeSub


# end class setTypeSub


class addTypeSub(supermod.addType):
    def __init__(self, Url=None, **kwargs_):
        super(addTypeSub, self).__init__(Url, **kwargs_)


supermod.addType.subclass = addTypeSub


# end class addTypeSub


class removeTypeSub(supermod.removeType):
    def __init__(self, Url=None, **kwargs_):
        super(removeTypeSub, self).__init__(Url, **kwargs_)


supermod.removeType.subclass = removeTypeSub


# end class removeTypeSub


class updateTypeSub(supermod.updateType):
    def __init__(self, Url=None, **kwargs_):
        super(updateTypeSub, self).__init__(Url, **kwargs_)


supermod.updateType.subclass = updateTypeSub


# end class updateTypeSub


class listType1Sub(supermod.listType1):
    def __init__(self, Domain=None, **kwargs_):
        super(listType1Sub, self).__init__(Domain, **kwargs_)


supermod.listType1.subclass = listType1Sub


# end class listType1Sub


class setType2Sub(supermod.setType2):
    def __init__(self, Domain=None, **kwargs_):
        super(setType2Sub, self).__init__(Domain, **kwargs_)


supermod.setType2.subclass = setType2Sub


# end class setType2Sub


class addType3Sub(supermod.addType3):
    def __init__(self, Domain=None, **kwargs_):
        super(addType3Sub, self).__init__(Domain, **kwargs_)


supermod.addType3.subclass = addType3Sub


# end class addType3Sub


class removeType4Sub(supermod.removeType4):
    def __init__(self, Domain=None, **kwargs_):
        super(removeType4Sub, self).__init__(Domain, **kwargs_)


supermod.removeType4.subclass = removeType4Sub


# end class removeType4Sub


class updateType5Sub(supermod.updateType5):
    def __init__(self, Domain=None, **kwargs_):
        super(updateType5Sub, self).__init__(Domain, **kwargs_)


supermod.updateType5.subclass = updateType5Sub


# end class updateType5Sub


class listType6Sub(supermod.listType6):
    def __init__(self, Attribute=None, **kwargs_):
        super(listType6Sub, self).__init__(Attribute, **kwargs_)


supermod.listType6.subclass = listType6Sub


# end class listType6Sub


class setType7Sub(supermod.setType7):
    def __init__(self, Attribute=None, **kwargs_):
        super(setType7Sub, self).__init__(Attribute, **kwargs_)


supermod.setType7.subclass = setType7Sub


# end class setType7Sub


class addType8Sub(supermod.addType8):
    def __init__(self, Attribute=None, **kwargs_):
        super(addType8Sub, self).__init__(Attribute, **kwargs_)


supermod.addType8.subclass = addType8Sub


# end class addType8Sub


class removeType9Sub(supermod.removeType9):
    def __init__(self, Attribute=None, **kwargs_):
        super(removeType9Sub, self).__init__(Attribute, **kwargs_)


supermod.removeType9.subclass = removeType9Sub


# end class removeType9Sub


class updateType10Sub(supermod.updateType10):
    def __init__(self, Attribute=None, **kwargs_):
        super(updateType10Sub, self).__init__(Attribute, **kwargs_)


supermod.updateType10.subclass = updateType10Sub


# end class updateType10Sub


class listType11Sub(supermod.listType11):
    def __init__(self, UrlEntry=None, **kwargs_):
        super(listType11Sub, self).__init__(UrlEntry, **kwargs_)


supermod.listType11.subclass = listType11Sub


# end class listType11Sub


class setType12Sub(supermod.setType12):
    def __init__(self, UrlEntry=None, **kwargs_):
        super(setType12Sub, self).__init__(UrlEntry, **kwargs_)


supermod.setType12.subclass = setType12Sub


# end class setType12Sub


class addType13Sub(supermod.addType13):
    def __init__(self, UrlEntry=None, **kwargs_):
        super(addType13Sub, self).__init__(UrlEntry, **kwargs_)


supermod.addType13.subclass = addType13Sub


# end class addType13Sub


class removeType14Sub(supermod.removeType14):
    def __init__(self, UrlEntry=None, **kwargs_):
        super(removeType14Sub, self).__init__(UrlEntry, **kwargs_)


supermod.removeType14.subclass = removeType14Sub


# end class removeType14Sub


class updateType15Sub(supermod.updateType15):
    def __init__(self, UrlEntry=None, **kwargs_):
        super(updateType15Sub, self).__init__(UrlEntry, **kwargs_)


supermod.updateType15.subclass = updateType15Sub


# end class updateType15Sub


class listType16Sub(supermod.listType16):
    def __init__(self, WebAppAuthRecord=None, **kwargs_):
        super(listType16Sub, self).__init__(WebAppAuthRecord, **kwargs_)


supermod.listType16.subclass = listType16Sub


# end class listType16Sub


class setType17Sub(supermod.setType17):
    def __init__(self, WebAppAuthRecord=None, **kwargs_):
        super(setType17Sub, self).__init__(WebAppAuthRecord, **kwargs_)


supermod.setType17.subclass = setType17Sub


# end class setType17Sub


class addType18Sub(supermod.addType18):
    def __init__(self, WebAppAuthRecord=None, **kwargs_):
        super(addType18Sub, self).__init__(WebAppAuthRecord, **kwargs_)


supermod.addType18.subclass = addType18Sub


# end class addType18Sub


class removeType19Sub(supermod.removeType19):
    def __init__(self, WebAppAuthRecord=None, **kwargs_):
        super(removeType19Sub, self).__init__(WebAppAuthRecord, **kwargs_)


supermod.removeType19.subclass = removeType19Sub


# end class removeType19Sub


class listType20Sub(supermod.listType20):
    def __init__(self, DnsOverride=None, **kwargs_):
        super(listType20Sub, self).__init__(DnsOverride, **kwargs_)


supermod.listType20.subclass = listType20Sub


# end class listType20Sub


class setType21Sub(supermod.setType21):
    def __init__(self, DnsOverride=None, **kwargs_):
        super(setType21Sub, self).__init__(DnsOverride, **kwargs_)


supermod.setType21.subclass = setType21Sub


# end class setType21Sub


class addType22Sub(supermod.addType22):
    def __init__(self, DnsOverride=None, **kwargs_):
        super(addType22Sub, self).__init__(DnsOverride, **kwargs_)


supermod.addType22.subclass = addType22Sub


# end class addType22Sub


class removeType23Sub(supermod.removeType23):
    def __init__(self, DnsOverride=None, **kwargs_):
        super(removeType23Sub, self).__init__(DnsOverride, **kwargs_)


supermod.removeType23.subclass = removeType23Sub


# end class removeType23Sub


class listType24Sub(supermod.listType24):
    def __init__(self, WebAppHeader=None, **kwargs_):
        super(listType24Sub, self).__init__(WebAppHeader, **kwargs_)


supermod.listType24.subclass = listType24Sub


# end class listType24Sub


class setType25Sub(supermod.setType25):
    def __init__(self, WebAppHeader=None, **kwargs_):
        super(setType25Sub, self).__init__(WebAppHeader, **kwargs_)


supermod.setType25.subclass = setType25Sub


# end class setType25Sub


class addType26Sub(supermod.addType26):
    def __init__(self, WebAppHeader=None, **kwargs_):
        super(addType26Sub, self).__init__(WebAppHeader, **kwargs_)


supermod.addType26.subclass = addType26Sub


# end class addType26Sub


class removeType27Sub(supermod.removeType27):
    def __init__(self, WebAppHeader=None, **kwargs_):
        super(removeType27Sub, self).__init__(WebAppHeader, **kwargs_)


supermod.removeType27.subclass = removeType27Sub


# end class removeType27Sub


class updateType28Sub(supermod.updateType28):
    def __init__(self, WebAppHeader=None, **kwargs_):
        super(updateType28Sub, self).__init__(WebAppHeader, **kwargs_)


supermod.updateType28.subclass = updateType28Sub


# end class updateType28Sub


class listType29Sub(supermod.listType29):
    def __init__(self, Tag=None, **kwargs_):
        super(listType29Sub, self).__init__(Tag, **kwargs_)


supermod.listType29.subclass = listType29Sub


# end class listType29Sub


class setType30Sub(supermod.setType30):
    def __init__(self, Tag=None, **kwargs_):
        super(setType30Sub, self).__init__(Tag, **kwargs_)


supermod.setType30.subclass = setType30Sub


# end class setType30Sub


class addType31Sub(supermod.addType31):
    def __init__(self, Tag=None, **kwargs_):
        super(addType31Sub, self).__init__(Tag, **kwargs_)


supermod.addType31.subclass = addType31Sub


# end class addType31Sub


class removeType32Sub(supermod.removeType32):
    def __init__(self, Tag=None, **kwargs_):
        super(removeType32Sub, self).__init__(Tag, **kwargs_)


supermod.removeType32.subclass = removeType32Sub


# end class removeType32Sub


class updateType33Sub(supermod.updateType33):
    def __init__(self, Tag=None, **kwargs_):
        super(updateType33Sub, self).__init__(Tag, **kwargs_)


supermod.updateType33.subclass = updateType33Sub


# end class updateType33Sub


class listType34Sub(supermod.listType34):
    def __init__(self, Comment=None, **kwargs_):
        super(listType34Sub, self).__init__(Comment, **kwargs_)


supermod.listType34.subclass = listType34Sub


# end class listType34Sub


class setType35Sub(supermod.setType35):
    def __init__(self, Comment=None, **kwargs_):
        super(setType35Sub, self).__init__(Comment, **kwargs_)


supermod.setType35.subclass = setType35Sub


# end class setType35Sub


class addType36Sub(supermod.addType36):
    def __init__(self, Comment=None, **kwargs_):
        super(addType36Sub, self).__init__(Comment, **kwargs_)


supermod.addType36.subclass = addType36Sub


# end class addType36Sub


class occurrenceType37Sub(supermod.occurrenceType37):
    def __init__(self, hourlyOccurrence=None, dailyOccurrence=None, weeklyOccurrence=None, monthlyOccurrence=None,
                 **kwargs_):
        super(occurrenceType37Sub, self).__init__(hourlyOccurrence, dailyOccurrence, weeklyOccurrence,
                                                  monthlyOccurrence, **kwargs_)


supermod.occurrenceType37.subclass = occurrenceType37Sub


# end class occurrenceType37Sub


class onDaysTypeSub(supermod.onDaysType):
    def __init__(self, WeekDay=None, **kwargs_):
        super(onDaysTypeSub, self).__init__(WeekDay, **kwargs_)


supermod.onDaysType.subclass = onDaysTypeSub


# end class onDaysTypeSub


class monthlyTypeTypeSub(supermod.monthlyTypeType):
    def __init__(self, occurDayNbInMonth=None, occurDayOrderInMonth=None, **kwargs_):
        super(monthlyTypeTypeSub, self).__init__(occurDayNbInMonth, occurDayOrderInMonth, **kwargs_)


supermod.monthlyTypeType.subclass = monthlyTypeTypeSub


# end class monthlyTypeTypeSub


class occurDayNbInMonthTypeSub(supermod.occurDayNbInMonthType):
    def __init__(self, dayNb=None, everyNMonths=None, **kwargs_):
        super(occurDayNbInMonthTypeSub, self).__init__(dayNb, everyNMonths, **kwargs_)


supermod.occurDayNbInMonthType.subclass = occurDayNbInMonthTypeSub


# end class occurDayNbInMonthTypeSub


class occurDayOrderInMonthTypeSub(supermod.occurDayOrderInMonthType):
    def __init__(self, dayOrder=None, dayOfMonth=None, everyNMonths=None, **kwargs_):
        super(occurDayOrderInMonthTypeSub, self).__init__(dayOrder, dayOfMonth, everyNMonths, **kwargs_)


supermod.occurDayOrderInMonthType.subclass = occurDayOrderInMonthTypeSub


# end class occurDayOrderInMonthTypeSub


class listType38Sub(supermod.listType38):
    def __init__(self, SeleniumScript=None, **kwargs_):
        super(listType38Sub, self).__init__(SeleniumScript, **kwargs_)


supermod.listType38.subclass = listType38Sub


# end class listType38Sub


class setType39Sub(supermod.setType39):
    def __init__(self, SeleniumScript=None, **kwargs_):
        super(setType39Sub, self).__init__(SeleniumScript, **kwargs_)


supermod.setType39.subclass = setType39Sub


# end class setType39Sub


class addType40Sub(supermod.addType40):
    def __init__(self, SeleniumScript=None, **kwargs_):
        super(addType40Sub, self).__init__(SeleniumScript, **kwargs_)


supermod.addType40.subclass = addType40Sub


# end class addType40Sub


class removeType41Sub(supermod.removeType41):
    def __init__(self, SeleniumScript=None, **kwargs_):
        super(removeType41Sub, self).__init__(SeleniumScript, **kwargs_)


supermod.removeType41.subclass = removeType41Sub


# end class removeType41Sub


class updateType42Sub(supermod.updateType42):
    def __init__(self, SeleniumScript=None, **kwargs_):
        super(updateType42Sub, self).__init__(SeleniumScript, **kwargs_)


supermod.updateType42.subclass = updateType42Sub


# end class updateType42Sub


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
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
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
    # import pdb; pdb.set_trace()
    main()
