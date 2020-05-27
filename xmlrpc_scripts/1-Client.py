#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpc.client
import csv

db = 'copassa_testing'
host = 'http://3.23.176.152:9003'
user = 'admin'
password = 'qazwsxedc123'

sock_common = xmlrpc.client.ServerProxy('{0}/xmlrpc/common'.format(host))
uid = sock_common.login(db, user, password)
sock = xmlrpc.client.ServerProxy('{0}/xmlrpc/object'.format(host))

if not uid:
    print("Credenciales incorrectas")
    exit()

CUSTOMERS = 'res_partner.csv'
Customers = csv.DictReader(open(CUSTOMERS, "r"), delimiter=",")

print("Iniciando Proceso (Clientes)...")

c = 1

for row in Customers:

    print("Finaliza Proceso (Clientes)...")
    c += 1

    vals = {
        'company_type': 'person',
        'type': 'contact',
        'customer_rank': True,
        'name': row['NameCustomer'].strip(),
        'birthdate_date': row[
            'BirthDate'].strip() if row['BirthDate'] else False,
        'phone': row['Phone'].strip(),
        'mobile': row['Phone'].strip(),
        'email': row['Email'].strip(),
        'note_primary': row['Note 1'].strip(),
        'note_extra': row['Note 2'].strip(),
        'policy_number': row['Policy Number'].strip(),
        'company': row['Company'].strip(),
        'plan': row['Plan'].strip(),
        'effective_date': row['Effective Date'].strip(),
        'p_date': row['P. Type'].strip(),
    }
    print(vals)
    sock.execute_kw(
        db, uid, password, 'res.partner', 'create', [vals])
