#!/usr/bin/env python
import sys
import logging

import qualysapi

if __name__ == '__main__':

    # Set the MAXIMUM level of log messages displayed @ runtime. 
    logging.basicConfig(level=logging.DEBUG)
    
    # Call helper that creates a connection w/ HTTP-Basic to QualysGuard v1 API
    api = qualysapi.connect('qualys.ini')

    # Logging must be set after instanciation of connector class.
    logger = logging.getLogger('qualysapi.connector')
    logger.setLevel(logging.DEBUG)

    # Log to sys.out.
    logger_console = logging.StreamHandler()
    logger_console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    logging.getLogger(__name__).addHandler(logger)


    # Formulate a request to the QualysGuard WAS V2 API
    #  docs @
    #  https://www.qualys.com/docs/qualys-waf-api-user-guide.pdf
    #
    # get your portal version
    # https://qualysapi.qualys.com/qps/rest/portal/version
    # ret = api.request('/qps/rest/portal/version')
    # for modulename, version in api.get_portal_version():
    #     print("%s: %s" %(modulename, version))

    # print(api.was.get_webapp_count())

    if False:
        webapp_list = api.was.webapp.search_webapp()
        for webapp in webapp_list:
            print(webapp)
            if webapp.crawlingScripts:
                app = api.was.webapp.get_webapp_details(webapp.id)
                print(f"SCRIPT FOUND IN {app.name}")

        print(api.was.webapp.get_webapp_details(webapp_list[-1].id))

        result = api.was.webapp.create_webapp("Test Web App", "https://nothere.example.com")
        print(result)

        result = api.was.webapp.update_webapp("Test Web App", "https://nothere.example.com")
        print(result)

        response = api.was.webapp.delete_webapp(id=result.id)
        print(response)

        response = api.was.webapp.get_selenium_script(24348536, 5200)
        print(response)

        # # should fail
        # response = api.was.webapp.delete_webapp(id='12098s')
        # print(response)

        # print(webapp_list[0].id)
        # response = api.was.webapp.get_selenium_script(webapp_list[0].id)

    if False:
        # import qualysapi
        # import qualysapi.core as qcore
        # qcore.pull_xsd()

        # print(api.was.get_auth_record_count())

        auth_records = api.was.authrecord.search_auth_record()
        for record in auth_records:
            print(record)

        # record = api.was.authrecord.get_auth_record_details(auth_records[-1].id)
        # print(record)
        #
        # result = api.was.authrecord.create_auth_record("name")
        # auth_record_id = result.id
        # print(result)
        #
        # result = api.was.authrecord.update_auth_record(id=auth_record_id, name="New name")
        # print(result)
        #
        # response = api.was.authrecord.delete_auth_record(id=auth_record_id)
        # print(response)


    # try objectify again
    response = b'<?xml version="1.0" encoding="UTF-8"?>\n<ServiceResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://qualysapi.qualys.com/qps/xsd/3.0/was/webappauthrecord.xsd">\n  <responseCode>SUCCESS</responseCode>\n  <count>9</count>\n  <hasMoreRecords>false</hasMoreRecords>\n  <data>\n    <WebAppAuthRecord>\n      <id>23391</id>\n      <name><![CDATA[ESL MyPortal Auth Record]]></name>\n      <owner>\n        <id>2230539</id>\n        <username>pente_bb</username>\n        <firstName><![CDATA[Bill]]></firstName>\n        <lastName><![CDATA[Boehm]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2013-07-05T15:08:59Z</createdDate>\n      <updatedDate>2018-11-19T14:33:09Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>347700</id>\n      <name><![CDATA[GEPARA SSO]]></name>\n      <owner>\n        <id>8414617</id>\n        <username>pente_er</username>\n        <firstName><![CDATA[Eric]]></firstName>\n        <lastName><![CDATA[Rubin]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2016-11-03T18:10:21Z</createdDate>\n      <updatedDate>2016-11-03T18:44:30Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>379034</id>\n      <name><![CDATA[GEPARA SSO - 1/10/2017]]></name>\n      <owner>\n        <id>8414617</id>\n        <username>pente_er</username>\n        <firstName><![CDATA[Eric]]></firstName>\n        <lastName><![CDATA[Rubin]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2017-01-10T14:39:21Z</createdDate>\n      <updatedDate>2018-12-01T21:02:04Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>621720</id>\n      <name><![CDATA[GXS PCI Admin Portal]]></name>\n      <owner>\n        <id>24346435</id>\n        <username>pente_sk</username>\n        <firstName><![CDATA[Scott]]></firstName>\n        <lastName><![CDATA[Karr]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2018-01-04T13:44:18Z</createdDate>\n      <updatedDate>2018-12-07T23:33:14Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>688892</id>\n      <name><![CDATA[TAFE]]></name>\n      <owner>\n        <id>24346435</id>\n        <username>pente_sk</username>\n        <firstName><![CDATA[Scott]]></firstName>\n        <lastName><![CDATA[Karr]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2018-04-26T13:55:33Z</createdDate>\n      <updatedDate>2018-11-26T17:36:22Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>695921</id>\n      <name><![CDATA[TAFE3_Admin]]></name>\n      <owner>\n        <id>24346435</id>\n        <username>pente_sk</username>\n        <firstName><![CDATA[Scott]]></firstName>\n        <lastName><![CDATA[Karr]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2018-05-08T14:42:23Z</createdDate>\n      <updatedDate>2018-11-26T15:57:37Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>730296</id>\n      <name><![CDATA[GEPARA SSO - 7/18/2018]]></name>\n      <owner>\n        <id>95448209</id>\n        <username>pente_cs</username>\n        <firstName><![CDATA[Chris]]></firstName>\n        <lastName><![CDATA[Sowley]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2018-07-18T16:26:03Z</createdDate>\n      <updatedDate>2018-11-19T16:49:41Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>732693</id>\n      <name><![CDATA[Bradesco]]></name>\n      <owner>\n        <id>127164079</id>\n        <username>pente_rw</username>\n        <firstName><![CDATA[Roshad]]></firstName>\n        <lastName><![CDATA[West]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2018-07-23T17:15:42Z</createdDate>\n      <updatedDate>2018-09-12T13:55:12Z</updatedDate>\n    </WebAppAuthRecord>\n    <WebAppAuthRecord>\n      <id>758707</id>\n      <name><![CDATA[ECD Alstom ACOMIS]]></name>\n      <owner>\n        <id>95448209</id>\n        <username>pente_cs</username>\n        <firstName><![CDATA[Chris]]></firstName>\n        <lastName><![CDATA[Sowley]]></lastName>\n      </owner>\n      <tags>\n        <count>0</count>\n      </tags>\n      <createdDate>2018-09-14T19:31:13Z</createdDate>\n      <updatedDate>2018-09-14T21:11:57Z</updatedDate>\n    </WebAppAuthRecord>\n  </data>\n</ServiceResponse>'
    from lxml import objectify, etree
    from qualysapi import api_objects

    if False:
        # normal objectify
        objtree = objectify.fromstring(response)
        print(objtree)
        print(objtree.count)
        print(objtree.data.WebAppAuthRecord[0].id)
        print(list(objtree.data.WebAppAuthRecord))


    class MyLookup(etree.CustomElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            print(f"MyLookup {name} {node_type}")
            if name == 'WebAppAuthRecord':
                return api_objects.WebAppAuthRecord  # be a bit more selective here ...
            #return etree.ElementBase

    if False:
        # Custom class chooser works as xmlparser
        parser = etree.XMLParser()
        parser.set_element_class_lookup(MyLookup())
        objtree = etree.fromstring(response, parser)
        print(objtree)
        print(objtree[2])
        print(objtree[3].getchildren())
        print(objtree[3][0].try_me())
        print(objtree[3][0].getchildren()[0].text)  # data.webauthrecord.id

    if False:
        # use a default namespace solution
        parser = etree.XMLParser()
        lookup = etree.ElementNamespaceClassLookup()
        parser.set_element_class_lookup(lookup)
        ns_lookup = lookup.get_namespace(None)
        ns_lookup['WebAppAuthRecord'] = api_objects.WebAppAuthRecord
        objtree = etree.fromstring(response, parser)
        print(objtree)
        print(objtree[2])
        print(objtree[3].getchildren())
        print(objtree[3][0].try_me())
        print(objtree[3][0].getchildren()[0].text)  # data.webauthrecord.id

    class MyLookupObjectify(objectify.ObjectifyElementClassLookup):
        def lookup(self, node_type, document, namespace, name):
            print(f"MyLookupObjectify {name}")
            if name == 'WebAppAuthRecord':
                return api_objects.WebAppAuthRecord  # be a bit more selective here ...

    if False:
        # non standard objectify - not custom class
        parser = objectify.makeparser(remove_blank_text=True)
        objtree = objectify.fromstring(response, parser)
        print(objtree)
        print(objtree.count)
        print(objtree.data.WebAppAuthRecord[0].id)
        print(list(objtree.data.WebAppAuthRecord))

    if False:
        # custom class objectify - not working
        parser = objectify.makeparser(remove_blank_text=True)
        lookup = MyLookup() # that doesnt work break objectify
        # lookup = objectify.ObjectifyElementClassLookup() # objectify still works
        # lookup = MyLookupObjectify()  # objectify works, but not custom class
        parser.set_element_class_lookup(lookup)
        objtree = objectify.fromstring(response, parser)
        print(objtree)
        print(objtree.count)
        print(objtree.data.WebAppAuthRecord[0].id)
        print(list(objtree.data.WebAppAuthRecord))

    if True:
        # custom class objectify simple version with namespace
        parser = objectify.makeparser(remove_blank_text=True)
        lookup = etree.ElementNamespaceClassLookup(objectify.ObjectifyElementClassLookup())
        ns_lookup = lookup.get_namespace(None)
        ns_lookup['WebAppAuthRecord'] = api_objects.WebAppAuthRecord
        parser.set_element_class_lookup(lookup)
        objtree = objectify.fromstring(response, parser)
        print(objtree)
        print(objtree.count)
        print(objtree.data.WebAppAuthRecord[0].id)
        print(list(objtree.data.WebAppAuthRecord))

    #parser = objectify.makeparser(remove_blank_text=True)
    #parser.set_element_class_lookup(MyLookupObjectify())
    # lookup = etree.ElementNamespaceClassLookup( MyLookupObjectify() )
    # parser.set_element_class_lookup(lookup)
    #objtree = objectify.fromstring(response)

    print("")
    exit(0)

    class MyLookup2(etree.PythonElementClassLookup):
        def lookup(self, document, element):
            print(f"lookup2: {element}")
            if element.tag == 'WebAppAuthRecord':
                return api_objects.WebAppAuthRecord

    # parsing_type = objectify.PyType('WebAppAuthRecord', api_objects.WebAppAuthRecord.check_type,
    #                                 api_objects.WebAppAuthRecord)
    # parsing_type.register()
    #parser = objectify.makeparser(remove_blank_text=True)

    # fallback = etree.ElementDefaultClassLookup()
    # lookup3 = etree.ElementNamespaceClassLookup(MyLookup() )
    # lookup2 = MyLookup2()
    # lookup = MyLookup()
    # parser.set_element_class_lookup(lookup)
    # objectify.set_default_parser(parser)
    objtree = etree.fromstring(response, parser)
    print(objtree)
    print(f"auth record 1 {objtree.data.WebAppAuthRecord}")
    print(list(objtree.data.WebAppAuthRecord))

    # list web applications
    # ret = qgs.request('/qps/rest/2.0/fo/report')

#     print(ret)
