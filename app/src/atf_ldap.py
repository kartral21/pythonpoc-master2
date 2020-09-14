from ldap3 import Server, Connection, ALL

LDAP_URL = '127.0.0.1'
USER = 'admin'
PASSWORD = 'atfldap'

class ATFLdap():

    def __init__(self):
        server = Server(LDAP_URL, get_info=ALL)
        connection = Connection(server,'cn={username},dc=example,dc=com'.format(username=USER),
                                PASSWORD, auto_bind=True)
        self.conn = connection

    def add_LDAP_group(self):
        try:
            attr = {'objectClass': ['top', 'posixGroup'], 'gidNumber': '100'}
            response = self.conn.add('cn=atfldap,dc=example,dc=com', attributes=attr)
            return "Group Added Successfully"
        except Exception as e:
            return e

    def add_LDAP_user(self):
        try:
            ldap_attr = {"cn":"email user","sn":"EMU"}
            user_dn = "cn=emailuser,cn=atfldap,dc=example,dc=com"
            response = self.conn.add(dn=user_dn,object_class='inetOrgPerson', attributes=ldap_attr)
            return "User Added Successfully"
        except Exception as e:
            return e

    def update_LDAP_user(self):
        try:
            response = self.conn.modify_dn('cn=emailuser,cn=atfldap,dc=example,dc=com', 'cn=outlookuser')
            return "User Updated Successfully"
        except Exception as e:
            return e

    def delete_LDAP_user(self):
        try:
            response = self.conn.delete('cn=outlookuser,cn=atfldap,dc=example,dc=com')
            return "Deleted Successfully"
        except Exception as e:
            return e

    def get_LDAP_user(self):
        try:
            self.conn.search('cn=atfldap,dc=example,dc=com', '({attr}={name})'.format(
                    attr='cn', name='outlookuser'), attributes=['cn','sn'])
            if len(self.conn.response) != 0:
                return self.conn.response[0]
            else:
                return "No Data Found!"
        except Exception as e:
            return e

if __name__ == "__main__":
    ldap1 = ATFLdap()
    ldap1.add_LDAP_group()
    ldap1.add_LDAP_user()
    ldap1.update_LDAP_user()
    ldap1.get_LDAP_user()
    # ldap1.delete_LDAP_user()