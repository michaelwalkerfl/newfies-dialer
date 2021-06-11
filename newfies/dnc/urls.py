#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2015 Star2Billing S.L.
#
# The primary maintainer of this project is
# Arezqui Belaid <info@star2billing.com>
#

from django.conf.urls import url


urlpatterns = ['dnc.views',
                # DNC urls
                url(r'^module/dnc_list/$', 'dnc_list'),
                url(r'^module/dnc_list/add/$', 'dnc_add'),
                url(r'^module/dnc_list/contact_count/$', 'get_dnc_contact_count'),
                url(r'^module/dnc_list/del/(.+)/$', 'dnc_del'),
                url(r'^module/dnc_list/(.+)/$', 'dnc_change'),
                # DNC Contacts urls
                url(r'^module/dnc_contact/$', 'dnc_contact_list'),
                url(r'^module/dnc_contact/add/$', 'dnc_contact_add'),
                url(r'^module/dnc_contact_import/$', 'dnc_contact_import'),
                url(r'^module/dnc_contact/export/$', 'dnc_contact_export'),
                url(r'^module/dnc_contact/export_view/$', 'dnc_contact_export_view'),
                url(r'^module/dnc_contact/del/(.+)/$', 'dnc_contact_del'),
                url(r'^module/dnc_contact/(.+)/$', 'dnc_contact_change'),
            ]
