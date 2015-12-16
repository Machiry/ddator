__author__ = 'machiry'
"""
Almost all of this code is copied from Yanick Fratantinio (@reyammer)
"""
import xml.dom.minidom
from logger import DDLogger


def _get_package_name(manifest):
    package_name = ''
    if len(manifest.getElementsByTagName('manifest')) > 0:
        m = manifest.getElementsByTagName('manifest')[0]
        package_name = str(m.getAttribute('package'))
    return package_name


def _get_main_activity(manifest, package_name):
    activities = _get_activities(manifest, package_name)
    for activity, intents in activities.items():
        is_main = False
        for intent in intents:
            if str(intent[0]) == 'android.intent.action.MAIN':
                is_main = True
        if is_main:
            return activity

    # There are cases where an apk does not have a main activity
    return None


def _get_exported_flags(manifest, package_name):
    exported_flags = {}

    components_xml = (manifest.getElementsByTagName('activity') +
                      manifest.getElementsByTagName('service') +
                      manifest.getElementsByTagName('receiver'))

    for component_xml in components_xml:
        name = str(component_xml.getAttribute('android:name'))

        if name.startswith('.'):
            name = package_name + name

        exported = str(component_xml.getAttribute('android:exported'))

        if not exported: exported = 'unset'

        exported_flags[name] = exported

    return exported_flags


def _get_activities(manifest, package_name):
    activities = {}
    activities_xml = manifest.getElementsByTagName('activity')
    for activity_xml in activities_xml:
        name = str(activity_xml.getAttribute('android:name'))

        if name.startswith('.'):
            name = package_name + name
        activities[name] = []
        intent_filters_xml = activity_xml.getElementsByTagName('intent-filter')
        for intent_filter_xml in intent_filters_xml:
            try:
                priority = int(intent_filter_xml.getAttribute('android:priority'))
            except:
                priority = 0
            try:
                action_xml = intent_filter_xml.getElementsByTagName('action')[0]
                action = action_xml.getAttribute('android:name')
            except IndexError:
                action = ''
            try:
                category_xml = intent_filter_xml.getElementsByTagName('category')[0]
                category = category_xml.getAttribute('android:name')
            except IndexError:
                category = ''
            if action or category:
                activities[name].append((action, category, priority))

    return activities


def _get_services(manifest, package_name):
    services = {}
    services_xml = manifest.getElementsByTagName('service')
    for service_xml in services_xml:
        name = str(service_xml.getAttribute('android:name'))
        if name.startswith('.'):
            name = package_name + name
        services[name] = []
        intent_filters_xml = service_xml.getElementsByTagName('intent-filter')
        for intent_filter_xml in intent_filters_xml:
            try:
                priority = int(intent_filter_xml.getAttribute('android:priority'))
            except:
                priority = 0
            try:
                action_xml = intent_filter_xml.getElementsByTagName('action')[0]
                action = action_xml.getAttribute('android:name')
            except IndexError:
                action = ''
                pass
            try:
                category_xml = intent_filter_xml.getElementsByTagName('category')[0]
                category = category_xml.getAttribute('android:name')
            except IndexError:
                category = ''
            if action or category:
                services[name].append((action, category, priority))
    return services


def _get_receivers(manifest, package_name):
    receivers = {}
    receivers_xml = manifest.getElementsByTagName('receiver')
    for receiver_xml in receivers_xml:
        name = str(receiver_xml.getAttribute('android:name'))
        if name.startswith('.'):
            name = package_name + name
        receivers[name] = []
        intent_filters_xml = receiver_xml.getElementsByTagName('intent-filter')
        for intent_filter_xml in intent_filters_xml:
            try:
                priority = int(intent_filter_xml.getAttribute('android:priority'))
            except:
                priority = 0
            try:
                action_xml = intent_filter_xml.getElementsByTagName('action')[0]
                action = action_xml.getAttribute('android:name')
            except IndexError:
                action = ''
                pass
            try:
                category_xml = intent_filter_xml.getElementsByTagName('category')[0]
                category = category_xml.getAttribute('android:name')
            except IndexError:
                category = ''
            if action or category:
                receivers[name].append((action, category, priority))
    return receivers


def _get_providers(manifest, package_name):
    providers = []
    providers_xml = manifest.getElementsByTagName('provider')
    for provider_xml in providers_xml:
        name = str(provider_xml.getAttribute('android:name'))
        if name.startswith('.'):
            name = package_name + name
        providers.append(name)
    return providers


def _get_sdk_versions(manifest):
    min_sdk_v = -1
    target_sdk_v = -1
    max_sdk_v = -1

    if len(manifest.getElementsByTagName('uses-sdk')) > 0:
        sdk_version_xml = manifest.getElementsByTagName('uses-sdk')[0]
        min_sdk_v = str(sdk_version_xml.getAttribute('android:minSdkVersion'))
        target_sdk_v = str(sdk_version_xml.getAttribute('android:targetSdkVersion'))
        max_sdk_v = str(sdk_version_xml.getAttribute('android:maxSdkVersion'))

    return min_sdk_v, target_sdk_v, max_sdk_v


def _get_libraries_used(manifest):
    libs = []
    xml_libs = manifest.getElementsByTagName('uses-library')
    for xml_l in xml_libs:
        l = str(xml_l.getAttribute('android:name'))
        libs.append(l)
    return libs


def _get_required_permissions(manifest):
    permissions = []
    xml_permissions = manifest.getElementsByTagName('uses-permission')
    for xml_p in xml_permissions:
        p = str(xml_p.getAttribute('android:name'))
        permissions.append(p)
    return permissions


def parse_apk_manifest(manifest_fp):

    manifest_xml = open(manifest_fp, 'r').read()
    manifest_info = {}
    try:
        manifest = xml.dom.minidom.parseString(manifest_xml)
        package_name = _get_package_name(manifest)
        manifest_info['package_name'] = package_name
        manifest_info['sdk_versions'] = _get_sdk_versions(manifest)
        manifest_info['main_activity'] = _get_main_activity(manifest, package_name)
        manifest_info['activities'] = _get_activities(manifest, package_name)
        manifest_info['services'] = _get_services(manifest, package_name)
        manifest_info['broadcast_receivers'] = _get_receivers(manifest, package_name)
        manifest_info['providers'] = _get_providers(manifest, package_name)
        manifest_info['used_libraries'] = _get_libraries_used(manifest)
        manifest_info['required_permissions'] = _get_required_permissions(manifest)
        # XXX hack
        manifest_info['exported_flags'] = _get_exported_flags(manifest, package_name)
    except Exception as e:
        DDLogger.write_failure_message("Failed to Parse the provided AndroidManifest.xml:" + str(manifest_fp))

    return manifest_info

