from ldap3 import Server, Connection, ALL

LDAP_URL = 'ldap.forumsys.com'
USER = 'tesla'
PASSWORD = 'password'

class ATFLdap():
    def get_LDAP_user(self):
        try:
            server = Server(LDAP_URL, get_info=ALL)
            connection = Connection(server,
                                    'uid={username},dc=example,dc=com'.format(
                                        username=USER),
                                    PASSWORD, auto_bind=True)

            connection.search('dc=example,dc=com', '({attr}={login})'.format(
                attr='uid', login=USER), attributes=['cn'])

            if len(connection.response) == 0:
                return None

            print('connection.response', connection.response[0])
            return connection.response[0]
        except:
            return None

if __name__ == "__main__":
    ldap1 = ATFLdap()
    ldap1.get_LDAP_user()