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
        webapp_list = api.was.search_webapp()
        for webapp in webapp_list:
            print(webapp)
            if webapp.crawlingScripts:
                app = api.was.get_webapp_details(webapp.id)
                print(f"SCRIPT FOUND IN {app.name}")

        print(api.was.get_webapp_details(webapp_list[-1].id))

        result = api.was.create_webapp("Test Web App", "https://nothere.example.com")
        print(result)

        result = api.was.update_webapp("Test Web App", "https://nothere.example.com")
        print(result)

        response = api.was.delete_webapp(id=result.id)
        print(response)

        response = api.was.get_selenium_script(24348536, 5200)
        print(response)

        # # should fail
        # response = api.was.delete_webapp(id='12098s')
        # print(response)

        # print(webapp_list[0].id)
        # response = api.was.get_selenium_script(webapp_list[0].id)

    if True:
        print(api.was.get_auth_record_count())
        auth_records = api.was.search_auth_record()
        for record in auth_records:
            print(record)

        print(api.was.get_auth_record_details(auth_records[-1].id))

        # result = api.was.create_auth_record("name", "data")
        # print(result)

        # result = api.was.update_auth_record()
        # print(result)

        #response = api.was.delete_auth_record()
        # print(response)



    # list web applications
    # ret = qgs.request('/qps/rest/2.0/fo/report')

#     print(ret)
