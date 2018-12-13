from __future__ import absolute_import
import datetime
from lxml import objectify, etree


def make_custom_class_lookup():
    lookup = etree.ElementNamespaceClassLookup(objectify.ObjectifyElementClassLookup())
    ns_lookup = lookup.get_namespace(None)
    # add any custom class here
    ns_lookup['WebApp'] = WebApp
    ns_lookup['WebAppAuthRecord'] = WebAppAuthRecord
    ns_lookup['ServiceResponse'] = ServiceResponse
    return lookup


class WebAppAuthRecord(objectify.ObjectifiedElement):
    @property
    def id(self):
        return int(self.find('id'))

    def __str__(self):
        key_fields = ['id', 'name', 'url', 'owner', 'tags']
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % (item.tag,item.text) for item in self.getchildren() if item.tag in key_fields and item.text))

    __repr__ =  __str__


class WebApp(objectify.ObjectifiedElement):
    @property
    def id(self):
        return int(self.find('id'))

    def __str__(self):
        key_fields = ['id', 'name', 'url', 'owner', 'tags']
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % (item.tag,item.text) for item in self.getchildren() if item.tag in key_fields and item.text))

    __repr__ =  __str__


class ServiceResponse(objectify.ObjectifiedElement):
    @property
    def hasMoreRecords(self):
        return bool(self.find('hasMoreRecords'))  # catch missing field



class Host(object):
    def __init__(self, dns, id, ip, last_scan, netbios, os, tracking_method):
        self.dns = str(dns)
        self.id = int(id)
        self.ip = str(ip)
        try:
            last_scan = str(last_scan).replace('T', ' ').replace('Z', '').split(' ')
            date = last_scan[0].split('-')
            time = last_scan[1].split(':')
            self.last_scan = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]),
                                               int(time[2]))
        except IndexError:
            self.last_scan = 'never'
        self.netbios = str(netbios)
        self.os = str(os)
        self.tracking_method = str(tracking_method)

    def __repr__(self):
        return f"ip: {self.ip}, qualys_id: {self.id}, dns: {self.dns}"


class AssetGroup(object):
    def __init__(self, business_impact, id, last_update, scanips, scandns, scanner_appliances, title):
        self.business_impact = str(business_impact)
        self.id = int(id)
        self.last_update = str(last_update)
        self.scanips = scanips
        self.scandns = scandns
        self.scanner_appliances = scanner_appliances
        self.title = str(title)

    def addAsset(self, conn, ip):
        call = '/api/2.0/fo/asset/group/'
        parameters = {'action': 'edit', 'id': self.id, 'add_ips': ip}
        conn.request(call, parameters)
        self.scanips.append(ip)

    def setAssets(self, conn, ips):
        call = '/api/2.0/fo/asset/group/'
        parameters = {'action': 'edit', 'id': self.id, 'set_ips': ips}
        conn.request(call, parameters)

    def __repr__(self):
        return f"qualys_id: {self.id}, title: {self.title}"


class ReportTemplate(object):
    def __init__(self, isGlobal, id, last_update, template_type, title, type, user):
        self.isGlobal = int(isGlobal)
        self.id = int(id)
        self.last_update = str(last_update).replace('T', ' ').replace('Z', '').split(' ')
        self.template_type = template_type
        self.title = title
        self.type = type
        self.user = user.LOGIN

    def __repr__(self):
        return f"qualys_id: {self.id}, title: {self.title}"


class Report(object):
    def __init__(self, expiration_datetime, id, launch_datetime, output_format, size, status, type, user_login,
                 title=''):
        self.expiration_datetime = str(expiration_datetime).replace('T', ' ').replace('Z', '').split(' ')
        self.id = int(id)
        self.launch_datetime = str(launch_datetime).replace('T', ' ').replace('Z', '').split(' ')
        self.output_format = output_format
        self.size = size
        self.status = status.STATE
        self.type = type
        self.user_login = user_login
        self.title = title

    def __repr__(self):
        return f"qualys_id: {self.id}, title: {self.title}"

    def download(self, conn):
        call = '/api/2.0/fo/report'
        parameters = {'action': 'fetch', 'id': self.id}
        if self.status == 'Finished':
            return conn.request(call, parameters)


class Scan(object):
    def __init__(self, assetgroups, duration, launch_datetime, option_profile, processed, ref, status, target, title,
                 type, user_login):
        self.assetgroups = assetgroups
        self.duration = str(duration)
        launch_datetime = str(launch_datetime).replace('T', ' ').replace('Z', '').split(' ')
        date = launch_datetime[0].split('-')
        time = launch_datetime[1].split(':')
        self.launch_datetime = datetime.datetime(int(date[0]),
                                                 int(date[1]),
                                                 int(date[2]),
                                                 int(time[0]),
                                                 int(time[1]),
                                                 int(time[2]))
        self.option_profile = str(option_profile)
        self.processed = int(processed)
        self.ref = str(ref)
        self.status = str(status.STATE)
        self.target = str(target).split(', ')
        self.title = str(title)
        self.type = str(type)
        self.user_login = str(user_login)

    def __repr__(self):
        return f"qualys_ref: {self.ref}, title: {self.title}, option_profile: {self.option_profile}"

    def cancel(self, conn):
        cancelled_statuses = ['Cancelled', 'Finished', 'Error']
        if any(self.status in s for s in cancelled_statuses):
            raise ValueError("Scan cannot be cancelled because its status is " + self.status)
        else:
            call = '/api/2.0/fo/scan/'
            parameters = {'action': 'cancel', 'scan_ref': self.ref}
            conn.request(call, parameters)

            parameters = {'action': 'list', 'scan_ref': self.ref, 'show_status': 1}
            self.status = objectify.fromstring(
                conn.request(call, parameters).encode('utf-8')).RESPONSE.SCAN_LIST.SCAN.STATUS.STATE

    def pause(self, conn):
        if self.status != "Running":
            raise ValueError("Scan cannot be paused because its status is " + self.status)
        else:
            call = '/api/2.0/fo/scan/'
            parameters = {'action': 'pause', 'scan_ref': self.ref}
            conn.request(call, parameters)

            parameters = {'action': 'list', 'scan_ref': self.ref, 'show_status': 1}
            self.status = objectify.fromstring(
                conn.request(call, parameters).encode('utf-8')).RESPONSE.SCAN_LIST.SCAN.STATUS.STATE

    def resume(self, conn):
        if self.status != "Paused":
            raise ValueError("Scan cannot be resumed because its status is " + self.status)
        else:
            call = '/api/2.0/fo/scan/'
            parameters = {'action': 'resume', 'scan_ref': self.ref}
            conn.request(call, parameters)

            parameters = {'action': 'list', 'scan_ref': self.ref, 'show_status': 1}
            self.status = objectify.fromstring(
                conn.request(call, parameters).encode('utf-8')).RESPONSE.SCAN_LIST.SCAN.STATUS.STATE
