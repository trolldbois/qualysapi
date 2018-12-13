from __future__ import absolute_import

from io import StringIO
from lxml import objectify, etree

from qualysapi.core import QualysModule


class WASModuleWebAppAPI(object):
    GET_WEBAPP_COUNT = ('/qps/rest/3.0/count/was/webapp', ['POST', 'GET'])
    SEARCH_WEBAPP = ('/qps/rest/3.0/search/was/webapp', ['POST'])
    GET_WEBAPP_DETAILS = ('/qps/rest/3.0/get/was/webapp/{id}', ['GET'])
    CREATE_WEBAPP = ('/qps/rest/3.0/create/was/webapp', ['POST'])
    UPDATE_WEBAPP = ('/qps/rest/3.0/update/was/webapp/{id}', ['POST'])
    DELETE_WEBAPP_BY_ID = ('/qps/rest/3.0/delete/was/webapp/{id}', ['POST'])
    DELETE_WEBAPP_BY_FILTERS = ('/qps/rest/3.0/delete/was/webapp/{filters}', ['POST'])
    PURGE_WEBAPP_BY_ID = ('/qps/rest/3.0/purge/was/webapp/{id}', ['POST'])
    PURGE_WEBAPP_BY_FILTERS = ('/qps/rest/3.0/purge/was/webapp/{filters}', ['POST'])
    GET_SELENIUM_SCRIPT = ('/qps/rest/3.0/downloadSeleniumScript/was/webapp', ['POST'])


class WASModuleAuthRecordAPI(object):
    GET_AUTH_RECORD_COUNT = ('/qps/rest/3.0/count/was/webappauthrecord', ['POST', 'GET'])
    SEARCH_AUTH_RECORD = ('/qps/rest/3.0/search/was/webappauthrecord', ['POST'])
    GET_AUTH_RECORD_DETAILS = ('/qps/rest/3.0/get/was/webappauthrecord/{id}', ['GET'])
    CREATE_AUTH_RECORD = ('/qps/rest/3.0/create/was/webappauthrecord', ['POST'])
    UPDATE_AUTH_RECORD = ('/qps/rest/3.0/update/was/webappauthrecord/{id}', ['POST'])
    DELETE_AUTH_RECORD_BY_ID = ('/qps/rest/3.0/delete/was/webappauthrecord/{id}', ['POST'])
    DELETE_AUTH_RECORD_BY_FILTERS = ('/qps/rest/3.0/delete/was/webappauthrecord/', ['POST'])


class WASModuleWebApp(QualysModule):

    def _make_webapp_data(self, name, url):
        # use objectify
        request_data = objectify.Element("ServiceRequest")
        request_data.data = objectify.Element("ServiceRequestData")
        request_data.data.WebApp = objectify.Element("WebApp")
        request_data.data.WebApp.name = name
        request_data.data.WebApp.url = url
        objectify.deannotate(request_data)
        etree.cleanup_namespaces(request_data)
        obj_xml = etree.tostring(request_data,
                                 pretty_print=True,
                                 xml_declaration=True)
        return obj_xml

    def get_webapp_count(self):
        result = self.request(WASModuleWebAppAPI.GET_WEBAPP_COUNT)
        return result.count

    def search_webapp(self):
        result = self.request(WASModuleWebAppAPI.SEARCH_WEBAPP)
        return list(result.data.WebApp)

    def get_webapp_details(self, webapp_id):
        result = self.request(WASModuleWebAppAPI.GET_WEBAPP_DETAILS, id=webapp_id)
        return result.data.WebApp[0]

    def create_webapp(self, name, url):
        data = self._make_webapp_data(name, url)
        result = self.request(WASModuleWebAppAPI.CREATE_WEBAPP, data=data)
        return result.data.WebApp[0]

    def update_webapp(self, id, name, url):
        # partial
        data = self._parsing_module.WebAppSub(id=id, name=name, url=url)
        result = self.request(WASModuleWebAppAPI.UPDATE_WEBAPP, data=data)
        return result.data.WebApp[0]

    def delete_webapp(self, id=None, filters=None):
        if id:
            #  INVALID_REQUEST if ID doesn't exist
            #  INVALID_URL if id is not an int
            result = self.request(WASModuleWebAppAPI.DELETE_WEBAPP_BY_ID, id=id)
            return result.data.WebApp[0]  # returns self deleted webapp
        elif filters:
            # partial
            result = self.request(WASModuleWebAppAPI.DELETE_WEBAPP_BY_FILTERS, filters=filters)
            return list(result.data.WebApp)

    def get_selenium_script(self, webapp_id, crawling_script_id):
        id_criteria = objectify.E.Criteria(str(webapp_id), field="id", operator="EQUALS")
        id_script = objectify.E.Criteria(str(crawling_script_id), field="crawlingScripts.id", operator="EQUALS")
        request_data = self._make_request_filter_data([id_criteria, id_script])
        result = self.request(WASModuleWebAppAPI.GET_SELENIUM_SCRIPT, data=request_data)
        return result


class WASModuleAuthRecord(QualysModule):
    def _get_parsing_module(self):
        return qualysapi.gen.webappauthrecordsubs

    def _make_auth_record_data(self, id=None, name=None):
        out = StringIO()
        record = self._parsing_module.WebAppAuthRecordSub(id=id, name=name)
        request_data = self._parsing_module.ServiceRequestSub()
        request_data.data = self._parsing_module.ServiceRequestDataSub()
        request_data.data.WebAppAuthRecord = record
        request_data.export(out, 0)
        return out.getvalue()

    def get_auth_record_count(self):
        result = self.request(WASModuleAuthRecordAPI.GET_AUTH_RECORD_COUNT)
        return result.count

    def search_auth_record(self):
        result = self.request(WASModuleAuthRecordAPI.SEARCH_AUTH_RECORD)
        return list(result.data.WebAppAuthRecord)

    def get_auth_record_details(self, webapp_id):
        result = self.request(WASModuleAuthRecordAPI.GET_AUTH_RECORD_DETAILS, id=webapp_id)
        return result.data.WebAppAuthRecord[0]

    def create_auth_record(self, name):
        data = self._make_auth_record_data(name=name)
        result = self.request(WASModuleAuthRecordAPI.CREATE_AUTH_RECORD, data=data)
        return result.data.WebAppAuthRecord[0]

    def update_auth_record(self, id, name):
        # partial
        data = self._parsing_module.WebAppAuthRecordSub(id=id, name=name)
        result = self.request(WASModuleAuthRecordAPI.UPDATE_AUTH_RECORD, data=data)
        return result.data.WebAppAuthRecord[0]

    def delete_auth_record(self, id=None, filters=None):
        if id:
            #  INVALID_REQUEST if ID doesn't exist
            #  INVALID_URL if id is not an int
            result = self.request(WASModuleAuthRecordAPI.DELETE_AUTH_RECORD_BY_ID, id=id)
            return result.data.WebAppAuthRecord[0]  # returns self deleted webapp
        elif filters:
            # partial
            result = self.request(WASModuleAuthRecordAPI.DELETE_AUTH_RECORD_BY_FILTERS, filters=filters)
            return list(result.data.WebAppAuthRecord)



class WASModule(object):
    def __init__(self, connector):
        self.connector = connector
        self.webapp = WASModuleWebApp(connector)
        self.authrecord = WASModuleAuthRecord(connector)
